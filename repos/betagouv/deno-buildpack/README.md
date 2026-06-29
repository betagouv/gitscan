# Deno Buildpack for Scalingo

A custom Heroku-compatible buildpack that installs [Deno](https://deno.land) runtime.

## Usage

### Single Buildpack

```bash
scalingo env-set BUILDPACK_URL=https://github.com/YOUR_ORG/deno-buildpack
```

### Multi-Buildpack (recommended for this project)

Create a `.buildpacks` file in your project root:

```
https://github.com/Scalingo/nodejs-buildpack
https://github.com/YOUR_ORG/deno-buildpack
https://github.com/Scalingo/go-buildpack
```

**Order matters!** Node.js first (for `npx`), then Deno, then Go.

## Configuration

### Specify Deno Version

Option 1: Environment variable
```bash
scalingo env-set DENO_VERSION=2.1.4
```

Option 2: `.deno-version` file in project root
```
2.1.4
```

Default version: `2.1.4`

## Detection

The buildpack activates when it finds any of:
- `deno.json`
- `deno.jsonc`
- `deno.lock`
- `.deno-version`
- Any `.ts` file in root

## What Gets Installed

At **build time**:
- Deno binary downloaded to cache
- Binary copied to `/app/.deno/bin/`
- Dependencies cached (if `deno.lock` exists)

At **runtime**:
- `deno` command available in PATH
- `DENO_DIR` set to `/app/.deno/cache`

## Runtime Availability (Multi-Buildpack)

With the multi-buildpack setup above, at runtime you'll have:

| Command | Provided By |
|---------|-------------|
| `node`, `npm`, `npx` | nodejs-buildpack |
| `deno` | deno-buildpack (this) |
| Your Go binary | go-buildpack |

All three are in PATH because each buildpack adds a `.profile.d/*.sh` script.

## Verification

After deployment, verify Deno is available:

```bash
scalingo run deno --version
# deno 2.1.4
```

## Local Testing

```bash
# Simulate buildpack execution
mkdir -p /tmp/{build,cache,env}
cp -r your-app/* /tmp/build/
./bin/detect /tmp/build && ./bin/compile /tmp/build /tmp/cache /tmp/env
```

## License

MIT
