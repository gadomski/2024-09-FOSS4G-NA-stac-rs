# Repeatable "benchmarks"

Let's not take these too seriously, but we do want to offer some sort of comparison between **stac-rs** and other tools.

## Results

### Server

| Test | stac-rs | stac-fastapi | Speedup |
| -- | -- | -- | -- |
| fetch one page | 48.3 ms ± 3.2 ms | 62.0 ms ± 2.2 ms| 22% |
| search all | 4.460 s ± 0.061 s | 5.894 s ± 0.045 s | 24% |

### stac-geoparquet

| Test | stac-rs | stac-geoparquet | Speedup |
| -- | -- | -- | -- |
| to parquet | 1.281 s ± 0.024 s | 1.869 s ± 0.25 s | 30% |
| from parquet | | 3.352 s ± 0.066 s | |

## Usage

Install the dependencies:

- **stac-cli**: `cargo install stac-cli`
- **stac-fastapi-pgstac**: `uv pip install stac-fastapi-pgstac uvicorn`
- **hyperfine**: `brew install hyperfine`

You'll also need to have a **pgstac** database, we use the one from the [stac-rs docker-compose](https://github.com/stac-utils/stac-rs/blob/main/pgstac/docker-compose.yml).
Then, use `hyperfine`, probably with a `--warmup`.

## Data

[1000-sentinel-2-items.json](./1000-sentinel-2-items.json) was created with the following command:

```shell
stac search https://planetarycomputer.microsoft.com/api/stac/v1 -c sentinel-2-l2a --intersects "$(cat benches/colorado.json)" --max-items 1000 --sortby="-properties.datetime" benches/1000-sentinel-2-items.json
```

Then, those data were loaded to a **pgstac** database:

```shell
stac serve --pgstac postgresql://username:password@localhost:5432/postgis benches/1000-sentinel-2-items.json
```

TODO: make a direct load command
