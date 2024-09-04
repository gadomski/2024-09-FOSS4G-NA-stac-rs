#!/usr/bin/env python

import json
from pathlib import Path

import stac_geoparquet.arrow

benches = Path(__file__).parent

with open(benches / "1000-sentinel-2-items.json") as f:
    data = json.load(f)

table = stac_geoparquet.arrow.parse_stac_items_to_arrow(data["features"])
stac_geoparquet.arrow.to_parquet(
    table, benches / "1000-sentinel-2-items-stac-geoparquet.parquet"
)
