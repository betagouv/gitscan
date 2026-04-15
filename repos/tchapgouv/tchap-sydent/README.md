# Tchap Sydent

[![Docker](https://github.com/tchapgouv/tchap-sydent/actions/workflows/docker.yml/badge.svg)](https://github.com/tchapgouv/tchap-sydent/actions/workflows/docker.yml)

This repo only hosts Github Action CI to build the docker image from the [main sydent repo branch dinsic](https://github.com/matrix-org/sydent/tree/dinsic).

## Pull this image

```
docker login ghcr.io --username <github_username> --password-stdin
docker pull ghcr.io/tchapgouv/tchap-sydent:latest
```

## Release

Docker image is build daily if new tag is detected on sydent repo on `dinsic` branch

Two images are created: `tchap-sydent:latest` and `tchap-sydent:tag_version`
