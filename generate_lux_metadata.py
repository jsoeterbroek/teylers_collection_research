#!/usr/bin/env python3
"""
Generate LUX/Linked.art JSON-LD metadata from Teylers analysis files.

Reads every file in analysis/*.md, parses the "Teylers Catalog Record"
table, and writes one JSON-LD file per object into lux_metadata/.
A combined all_objects.json is also written.

Usage:
    python generate_lux_metadata.py
"""

import json
import re
import sys
from typing import Dict, List, Optional, Tuple
from pathlib import Path

ANALYSIS_DIR = Path("analysis")
OUTPUT_DIR = Path("lux_metadata")

# Linked.art JSON-LD context
CONTEXT = "https://linked.art/ns/v1/linked-art.json"

# Getty AAT URIs used in this dataset
AAT = {
    "preferred_name":          "http://vocab.getty.edu/aat/300404670",
    "accession_number":        "http://vocab.getty.edu/aat/300312355",
    "sort_name":               "http://vocab.getty.edu/aat/300404672",
    "description":             "http://vocab.getty.edu/aat/300411780",
    "inscription":             "http://vocab.getty.edu/aat/300028702",
    "physical_description":    "http://vocab.getty.edu/aat/300435452",
    "dimensions_description":  "http://vocab.getty.edu/aat/300435430",
    "subject_heading":         "http://vocab.getty.edu/aat/300435416",
    "provenance_stmt":         "http://vocab.getty.edu/aat/300435438",
    "webpage":                 "http://vocab.getty.edu/aat/300264578",
    "iiif_manifest":           "http://iiif.io/api/presentation/3#Manifest",
    "publishing":              "http://vocab.getty.edu/aat/300054686",
    "height":                  "http://vocab.getty.edu/aat/300055644",
    "width":                   "http://vocab.getty.edu/aat/300055647",
    "weight":                  "http://vocab.getty.edu/aat/300056240",
    "diameter":                "http://vocab.getty.edu/aat/300055624",
    "centimeters":             "http://vocab.getty.edu/aat/300379098",
    "millimeters":             "http://vocab.getty.edu/aat/300379097",
    "grams":                   "http://vocab.getty.edu/aat/300379226",
}

# ---------------------------------------------------------------------------
# Object-type determination
# ---------------------------------------------------------------------------

# Prefix → broad category
PREFIX_TYPE = {
    "fk":   "instrument",   # Fysische/wetenschappelijke instrumenten
    "tmnk": "medal",        # Teylers Museum Numismatische Collectie
    "pp":   "medal",        # Penningen
    "m":    "mineral",      # Mineralen
    "f":    "fossil",       # Fossielen
    "kg":   "art",          # Kunst/drawings
    "ks":   "art",          # Kunst/schilderijen
    "kt":   "art",          # Kunst/tekeningen
    "a":    "art",
    "n":    "art",
    "o":    "art",
    "p":    "art",
    "t":    "art",
    "l":    "art",
    "u":    "art",
    "wbw":  "art",
    "rdw":  "art",
    "tvb":  "art",
}

# Field-value substrings that indicate a natural (found, not made) object
NATURAL_OBJECT_KEYWORDS = {
    "mineraal", "mineral", "fosiel", "fossil",
    "gesteente", "rock", "meteoriet", "meteorite",
}

BOOK_KEYWORDS = {"boek", "book", "manuscript", "brochure"}


def _obj_type_from_fields(fields: dict) -> str:
    """Determine broad object type from catalog record fields."""
    obj_name_field = (
        fields.get("Object name", "") or
        fields.get("Object Name", "") or
        fields.get("Object type", "") or
        fields.get("Type", "") or
        fields.get("type", "")
    ).lower()

    if any(k in obj_name_field for k in NATURAL_OBJECT_KEYWORDS):
        return "natural"
    if any(k in obj_name_field for k in BOOK_KEYWORDS):
        return "book"
    return ""


def determine_type(obj_id: str, fields: dict) -> str:
    """Return one of: instrument, medal, mineral, fossil, art, book, hmo."""
    from_fields = _obj_type_from_fields(fields)
    if from_fields:
        return from_fields

    # Identify prefix from object ID (e.g. "FK 0002" → "fk")
    clean = obj_id.lower().replace(" ", "").replace("-", "")
    for prefix, t in sorted(PREFIX_TYPE.items(), key=lambda x: -len(x[0])):
        if clean.startswith(prefix):
            if t in ("mineral", "fossil"):
                return t
            return t

    # Pure numeric IDs are books
    if re.match(r"^\d+$", obj_id.replace(" ", "")):
        return "book"

    return "hmo"


# ---------------------------------------------------------------------------
# Markdown parsing helpers
# ---------------------------------------------------------------------------

def parse_catalog_table(content: str) -> dict:
    """Return {field: value} from the 'Teylers Catalog Record' markdown table."""
    m = re.search(
        r"## Teylers Catalog Record\s*\n(.*?)(?=\n##|\Z)",
        content, re.DOTALL,
    )
    if not m:
        return {}

    result = {}
    for line in m.group(1).split("\n"):
        # Match pipe-delimited table rows, skip separator lines
        row = re.match(r"\|\s*(.+?)\s*\|\s*(.+?)\s*\|", line)
        if row:
            key = row.group(1).strip()
            val = row.group(2).strip()
            if key.lower() not in ("field", "---", "------", ""):
                # Strip backslash escapes (e.g. \| in values)
                val = val.replace("\\|", "|")
                result[key] = val
    return result


def get_source_url(content: str) -> Optional[str]:
    m = re.search(r"\*\*Source record:\*\*\s*<?([^\s>\n]+)>?", content)
    return m.group(1) if m else None


def get_object_description(content: str) -> Optional[str]:
    m = re.search(
        r"## Object Description\s*\n(.*?)(?=\n##|\Z)",
        content, re.DOTALL,
    )
    return m.group(1).strip() if m else None


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------

def parse_date_range(s: str) -> dict:
    """
    Extract begin/end years from a messy date string.
    Returns dict with optional keys: begin, end, label.
    """
    if not s or s.strip().lower() in ("not recorded", "(none listed)", "—", "-"):
        return {}

    s = s.strip()

    # Try to find up to two 4-digit years
    years = re.findall(r"\b(\d{4})\b", s)
    result = {"label": s}
    if years:
        result["begin"] = f"{years[0]}-01-01"
        result["end"]   = f"{years[-1]}-12-31"
    return result


def make_timespan(date_str: str) -> Optional[dict]:
    parsed = parse_date_range(date_str)
    if not parsed:
        return None
    ts: dict = {"type": "TimeSpan"}
    if "begin" in parsed:
        ts["begin_of_the_begin"] = parsed["begin"]
    if "end" in parsed:
        ts["end_of_the_end"] = parsed["end"]
    if "label" in parsed:
        ts["identified_by"] = [{"type": "Name", "content": parsed["label"]}]
    return ts


# ---------------------------------------------------------------------------
# Dimension helpers
# ---------------------------------------------------------------------------

def _dim_obj(value_str: str, dim_type_label: str, dim_type_aat: str,
              unit_label: str, unit_aat: str) -> dict:
    try:
        value = float(value_str.replace(",", "."))
    except ValueError:
        return {}
    return {
        "type": "Dimension",
        "value": value,
        "classified_as": [{"id": dim_type_aat, "_label": dim_type_label}],
        "unit": {"id": unit_aat, "_label": unit_label},
    }


def parse_dimensions(fields: dict) -> List[dict]:
    """
    Convert dimension fields to a list of LUX Dimension objects.
    Handles combined 'Dimensions' as well as separate Height/Width fields.
    """
    dims = []

    # Separate height / width fields (seen in art/paintings)
    h_str = fields.get("Height", fields.get("height", ""))
    w_str = fields.get("Width", fields.get("width", ""))

    def strip_unit(s: str) -> Tuple[str, str]:
        """Return (numeric_part, unit). Defaults to cm."""
        s = s.strip()
        for unit in ("mm", "cm", "m", "g", "kg"):
            if s.lower().endswith(unit):
                return s[:-len(unit)].strip(), unit
        return s, "cm"

    if h_str:
        num, unit = strip_unit(h_str)
        unit_aat = AAT["millimeters"] if unit == "mm" else AAT["centimeters"]
        d = _dim_obj(num, "height", AAT["height"], unit, unit_aat)
        if d:
            dims.append(d)

    if w_str:
        num, unit = strip_unit(w_str)
        unit_aat = AAT["millimeters"] if unit == "mm" else AAT["centimeters"]
        d = _dim_obj(num, "width", AAT["width"], unit, unit_aat)
        if d:
            dims.append(d)

    # Combined 'Dimensions' field — store as a description statement
    # (structured parsing of free-form strings like "727×127 mm; diameter: 36.6 mm"
    #  is too fragile; we preserve the text via referred_to_by instead)
    return dims


# ---------------------------------------------------------------------------
# LUX record builders
# ---------------------------------------------------------------------------

def _make_base(source_url: Optional[str], obj_id: str, title: str, entity_type: str) -> dict:
    return {
        "@context": CONTEXT,
        "id": source_url or f"urn:teylers:{obj_id.replace(' ', '_')}",
        "type": entity_type,
        "_label": title,
        "identified_by": [
            {
                "type": "Name",
                "content": title,
                "classified_as": [{"id": AAT["preferred_name"], "_label": "preferred name"}],
            },
            {
                "type": "Identifier",
                "content": obj_id,
                "classified_as": [{"id": AAT["accession_number"], "_label": "accession number"}],
                "assigned_by": [{
                    "type": "AttributeAssignment",
                    "carried_out_by": [{"type": "Group", "_label": "Teylers Museum"}],
                }],
            },
        ],
    }


def _add_webpage(record: dict, source_url: Optional[str]) -> None:
    if not source_url:
        return
    record.setdefault("subject_of", []).append({
        "type": "LinguisticObject",
        "digitally_carried_by": [{
            "type": "DigitalObject",
            "classified_as": [{"id": AAT["webpage"], "_label": "web page"}],
            "access_point": [{"id": source_url}],
            "format": "text/html",
            "identified_by": [{"type": "Name", "content": "Teylers Museum catalog page"}],
        }],
    })


def make_hmo(obj_id: str, fields: dict, source_url: Optional[str],
             description: Optional[str], obj_type: str) -> dict:
    """Build a HumanMadeObject record for instruments, medals, art, and generic HMOs."""
    title = (
        fields.get("Title") or fields.get("title") or obj_id
    )

    record = _make_base(source_url, obj_id, title, "HumanMadeObject")

    # ── Classification ──────────────────────────────────────────────────────
    obj_name = (
        fields.get("Object name") or fields.get("Object Name") or
        fields.get("Object type") or fields.get("Type") or ""
    )
    if obj_name:
        record["classified_as"] = [{"type": "Type", "_label": obj_name}]

    # ── Materials ────────────────────────────────────────────────────────────
    mat_str = fields.get("Material") or fields.get("materials") or ""
    if mat_str:
        mats = [m.strip() for m in re.split(r"[,;]", mat_str) if m.strip()]
        record["made_of"] = [{"type": "Material", "_label": m} for m in mats]

    # ── Dimensions ───────────────────────────────────────────────────────────
    dims = parse_dimensions(fields)
    if dims:
        record["dimension"] = dims

    # ── Production ───────────────────────────────────────────────────────────
    creator_str = (
        fields.get("Creator") or fields.get("Maker") or
        fields.get("maker") or ""
    )
    date_str = (
        fields.get("Production date") or fields.get("Production Date") or
        fields.get("Date") or fields.get("Production period") or ""
    )
    technique_str = fields.get("Technique") or fields.get("technique") or ""
    location_str  = fields.get("Location") or fields.get("Place") or ""

    is_natural = obj_type in ("mineral", "fossil")

    if is_natural:
        encounter: dict = {"type": "Encounter"}
        ts = make_timespan(date_str) if date_str else None
        if ts:
            encounter["timespan"] = ts
        coll_loc = fields.get("Collection location") or location_str
        if coll_loc:
            encounter["took_place_at"] = [{"type": "Place", "_label": coll_loc}]
        if ts or coll_loc:
            record["encountered_by"] = [encounter]
    else:
        production: dict = {"type": "Production"}
        if creator_str and creator_str.lower() not in ("", "(none listed)", "unknown"):
            production["carried_out_by"] = [{"type": "Actor", "_label": creator_str}]
        ts = make_timespan(date_str) if date_str else None
        if ts:
            production["timespan"] = ts
        if technique_str:
            production["technique"] = [{"type": "Type", "_label": technique_str}]
        if location_str:
            production["took_place_at"] = [{"type": "Place", "_label": location_str}]
        if production.keys() - {"type"}:
            record["produced_by"] = production

    # ── Statements (referred_to_by) ──────────────────────────────────────────
    referred: List[dict] = []

    # AI-written object description (English)
    if description:
        referred.append({
            "type": "LinguisticObject",
            "content": description,
            "classified_as": [{"id": AAT["description"], "_label": "description"}],
            "language": [{"type": "Language", "_label": "en"}],
            "identified_by": [{"type": "Name", "content": "AI research description"}],
        })

    # Catalog description field (Dutch)
    cat_desc = fields.get("Description") or fields.get("description") or ""
    if cat_desc and cat_desc.lower() not in ("not recorded", "(none listed)", ""):
        referred.append({
            "type": "LinguisticObject",
            "content": cat_desc,
            "classified_as": [{"id": AAT["description"], "_label": "description"}],
            "language": [{"type": "Language", "_label": "nl"}],
            "identified_by": [{"type": "Name", "content": "Teylers catalog description"}],
        })

    # Combined Dimensions field → text statement
    dim_str = (
        fields.get("Dimensions") or fields.get("Dimension") or
        fields.get("dimensions") or ""
    )
    if dim_str:
        referred.append({
            "type": "LinguisticObject",
            "content": dim_str,
            "classified_as": [{"id": AAT["dimensions_description"], "_label": "dimensions description"}],
        })

    # Inscriptions (any Field key containing "inscription")
    for key, val in fields.items():
        if "inscription" in key.lower() and val:
            stmt: dict = {
                "type": "LinguisticObject",
                "content": val,
                "classified_as": [{"id": AAT["inscription"], "_label": "inscription"}],
            }
            if "obv" in key.lower():
                stmt["identified_by"] = [{"type": "Name", "content": "obverse inscription"}]
            elif "rev" in key.lower():
                stmt["identified_by"] = [{"type": "Name", "content": "reverse inscription"}]
            referred.append(stmt)

    # Subject tags
    subj = (
        fields.get("Subject Tags") or fields.get("Subject tags") or
        fields.get("Subject") or fields.get("subjects") or ""
    )
    if subj:
        referred.append({
            "type": "LinguisticObject",
            "content": subj,
            "classified_as": [{"id": AAT["subject_heading"], "_label": "subject heading"}],
        })

    # Provenance statement
    prov = fields.get("Provenance") or fields.get("provenance") or ""
    if prov and prov.lower() not in ("not recorded", "(none listed)", ""):
        referred.append({
            "type": "LinguisticObject",
            "content": prov,
            "classified_as": [{"id": AAT["provenance_stmt"], "_label": "provenance statement"}],
        })

    # Acquisition date
    acq = fields.get("Acquisition") or fields.get("acquisition") or ""
    if acq:
        referred.append({
            "type": "LinguisticObject",
            "content": acq,
            "classified_as": [{"id": "http://vocab.getty.edu/aat/300055863", "_label": "acquisition"}],
            "identified_by": [{"type": "Name", "content": "acquisition date"}],
        })

    if referred:
        record["referred_to_by"] = referred

    # ── Set membership (collection) ───────────────────────────────────────────
    coll = fields.get("Collection") or fields.get("collection") or ""
    if coll:
        record["member_of"] = [{"type": "Set", "_label": coll}]

    # ── Current owner / copyright ─────────────────────────────────────────────
    cr = fields.get("Copyright") or fields.get("copyright") or ""
    if cr:
        record["current_owner"] = [{"type": "Group", "_label": cr}]

    # ── Digital reference ─────────────────────────────────────────────────────
    _add_webpage(record, source_url)

    # ── Art: link to VisualWork ───────────────────────────────────────────────
    if obj_type == "art":
        record["shows"] = [{
            "type": "VisualItem",
            "_label": title,
        }]

    return record


def make_textual_work(obj_id: str, fields: dict, source_url: Optional[str],
                       description: Optional[str]) -> dict:
    """Build a LinguisticObject record for books / textual works."""
    title = fields.get("Title") or fields.get("title") or obj_id

    # Books are physical objects carrying a text; we represent the work level.
    record = _make_base(source_url, obj_id, title, "LinguisticObject")

    # ── Creation ─────────────────────────────────────────────────────────────
    author = fields.get("Author") or fields.get("Creator") or fields.get("creator") or ""
    date_str = fields.get("Date") or fields.get("Production date") or ""
    if author and author.lower() not in ("", "(none listed)"):
        record["created_by"] = {
            "type": "Creation",
            "carried_out_by": [{"type": "Person", "_label": author}],
        }

    # ── Publication ───────────────────────────────────────────────────────────
    publisher = fields.get("Publisher") or fields.get("publisher") or ""
    pub_place  = fields.get("Publication place") or fields.get("Place") or ""
    if publisher or date_str:
        pub: dict = {
            "type": "Activity",
            "classified_as": [{"id": AAT["publishing"], "_label": "publishing"}],
        }
        if publisher:
            pub["carried_out_by"] = [{"type": "Group", "_label": publisher}]
        if pub_place:
            pub["took_place_at"] = [{"type": "Place", "_label": pub_place}]
        ts = make_timespan(date_str) if date_str else None
        if ts:
            pub["timespan"] = ts
        record["used_for"] = [pub]

    # ── Language ─────────────────────────────────────────────────────────────
    # Not reliably available in catalog; leave absent rather than guess.

    # ── About / Subject ───────────────────────────────────────────────────────
    subj = fields.get("Subject") or fields.get("subjects") or ""
    if subj:
        record["about"] = [{"type": "Type", "_label": subj}]

    related_people = fields.get("Related persons") or fields.get("Related persons") or ""

    # ── Statements ────────────────────────────────────────────────────────────
    referred: List[dict] = []

    if description:
        referred.append({
            "type": "LinguisticObject",
            "content": description,
            "classified_as": [{"id": AAT["description"], "_label": "description"}],
            "language": [{"type": "Language", "_label": "en"}],
            "identified_by": [{"type": "Name", "content": "AI research description"}],
        })

    fmt = fields.get("Format") or fields.get("format") or ""
    if fmt:
        referred.append({
            "type": "LinguisticObject",
            "content": fmt,
            "classified_as": [{"id": AAT["physical_description"], "_label": "physical description"}],
        })

    dim_str = fields.get("Dimensions") or fields.get("Dimension") or ""
    if dim_str:
        referred.append({
            "type": "LinguisticObject",
            "content": dim_str,
            "classified_as": [{"id": AAT["dimensions_description"], "_label": "dimensions description"}],
        })

    if related_people:
        referred.append({
            "type": "LinguisticObject",
            "content": related_people,
            "classified_as": [{"id": AAT["subject_heading"], "_label": "subject heading"}],
            "identified_by": [{"type": "Name", "content": "related persons"}],
        })

    if referred:
        record["referred_to_by"] = referred

    _add_webpage(record, source_url)
    return record


# ---------------------------------------------------------------------------
# Per-file processing
# ---------------------------------------------------------------------------

def process_file(filepath: Path) -> Tuple[dict, str]:
    content = filepath.read_text(encoding="utf-8")

    source_url  = get_source_url(content)
    fields      = parse_catalog_table(content)
    description = get_object_description(content)

    # Prefer the catalog's own "Object number" field if present
    actual_id = (
        fields.get("Object number") or
        fields.get("Object Number") or
        # Fall back to deriving from filename: teylers-fk-0002-analysis → FK 0002
        re.sub(r"^teylers-", "", re.sub(r"-analysis$", "", filepath.stem))
          .upper()
          .replace("-", " ")
    )

    obj_type = determine_type(actual_id, fields)

    if obj_type == "book":
        record = make_textual_work(actual_id, fields, source_url, description)
    else:
        record = make_hmo(actual_id, fields, source_url, description, obj_type)

    return record, actual_id


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    all_records: List[dict] = []
    errors: List[Tuple[str, str]] = []

    for filepath in sorted(ANALYSIS_DIR.glob("*.md")):
        try:
            record, obj_id = process_file(filepath)
            safe = obj_id.replace(" ", "_").replace("/", "_")
            out = OUTPUT_DIR / f"{safe}.json"
            out.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
            all_records.append(record)
            print(f"  ok  {obj_id}")
        except Exception as exc:
            errors.append((filepath.name, str(exc)))
            print(f"  ERR {filepath.name}: {exc}", file=sys.stderr)

    combined = OUTPUT_DIR / "all_objects.json"
    combined.write_text(
        json.dumps(all_records, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"\n{len(all_records)} records written to {OUTPUT_DIR}/")
    print(f"Combined file: {combined}")
    if errors:
        print(f"\n{len(errors)} error(s):")
        for name, msg in errors:
            print(f"  {name}: {msg}")


if __name__ == "__main__":
    main()
