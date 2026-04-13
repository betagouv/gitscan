# Renovate configuration

This repository contains common [renovate](https://docs.renovatebot.com/) bot configuration.

Renovate allow to create [presets](https://docs.renovatebot.com/config-presets/) and use them or 
extends them in another configuration.

## Usage

create a `renovate.json` file in at the root of your repository with this content:

```json
{
  "extends": [
    "github>numerique-gouv/renovate-configuration"
  ],
}
```

If you need to extend this preset, you can do it in your config file like explain
in the [preset](https://docs.renovatebot.com/config-presets/) documentation.
