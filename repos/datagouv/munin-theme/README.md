# Etalab munin theme

This repository contains the Etalab munin theme

## Installation

Clone this repository somewhere in on the munin server host:

```shell
git clone https://github.com/etalab/munin-theme.git /path/to/theme
```

Then edit your `munin.conf` to use it:

```inifile
tmpldir /path/to/theme/templates
staticdir /path/to/theme/static
```

Restart the munin server (or run munin-cron) to apply these changes.
