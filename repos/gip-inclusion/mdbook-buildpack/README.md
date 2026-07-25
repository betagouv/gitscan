# mdbook-buildpack

Scalingo buildpack for [mdBook](https://rust-lang.github.io/mdBook/) static site generation.

Detects projects with a `book.toml` at the root, builds the book, and outputs to `dist/`.

## Usage

This is a build-only buildpack: it compiles mdBook sources into static HTML in `dist/`. It must be paired with a serving buildpack.

### With oauth2-proxy (private docs)

`.buildpacks`:

```
https://github.com/betagouv/mdbook-buildpack.git
https://github.com/betagouv/oauth2-proxy-buildpack.git
```

`Procfile`:

```
web: bin/start_static_oauth2_proxy.sh
```

### With nginx (public docs)

`.buildpacks`:

```
https://github.com/betagouv/mdbook-buildpack.git
https://github.com/Scalingo/nginx-buildpack.git
```

`nginx.conf`:

```nginx
location / {
    root /app/dist;
    try_files $uri $uri/ /index.html;
}
```

## Configuration

| Environment variable | Default | Description |
|---|---|---|
| `MDBOOK_VERSION` | `0.5.2` | mdBook release version to use |
| `MDBOOK_CHECKSUM` | *(built-in)* | SHA-256 checksum of the mdBook tarball (must match `MDBOOK_VERSION`) |

## How it works

1. **Detect**: looks for `book.toml` in the project root
2. **Compile**: downloads the mdBook binary (cached between builds, verified with SHA-256), runs `mdbook build --dest-dir dist`
