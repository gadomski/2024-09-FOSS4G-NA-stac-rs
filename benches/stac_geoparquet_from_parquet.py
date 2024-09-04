#!/usr/bin/env python

import json
from pathlib import Path

import pyarrow
import pyarrow.parquet
import stac_geoparquet.arrow

benches = Path(__file__).parent


table = pyarrow.parquet.read_table(
    benches / "1000-sentinel-2-items-stac-geoparquet.parquet"
)
items = list(stac_geoparquet.arrow.stac_table_to_items(table))
with open("/tmp/out.json", "w") as f:
    json.dump({"type": "FeatureCollection", "features": items}, f)
