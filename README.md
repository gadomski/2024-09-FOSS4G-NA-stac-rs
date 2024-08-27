# _stac-rs: high-performance, reliable STAC tooling with Rust_

This is my FOSS4G-NA 2024 talk.

## Abstract

stac-rs is a Rust implementation of the SpatioTemporal Asset Catalog (STAC) specification.
Our high-performance STAC tools include a STAC API server with duck-db and postgres backends, and our applications leverage latest developments in geoparquet and geoarrow.

## Description

The SpatioTemporal Asset Catalog (STAC) community specification is a key component of the growing cloud-native geospatial ecosystem.
Well built, spec-specific tooling is a key part of the community-supported software landscape, as it helps developers and data consumers alike work efficiently with the data they need without needing to deeply understand the spec or implement the tooling themselves.
We present [**stac-rs**](https://github.com/stac-utils/stac-rs), a Rust implementation of the STAC spec, as part of the cloud-native geospatial software landscape.

**stac-rs** includes:

- A STAC API server with **duck-db** and **pgstac** backends
- A command-line interface (CLI) for querying STAC APIs and static STAC catalogs
- Several Rust libraries for building your own applications

In this talk, we walk through the components of **stac-rs**, describe some of the advantages and disadvantages of a Rust implementation of the STAC spec, and provide some performance benchmarks against other widely used tooling (e.g. **stac-fastapi** and **stac-server**).

## Acknowledgements

These slides are built on [reveal.js](https://revealjs.com/).
