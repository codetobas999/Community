---
title: "plugin disable"
description: "the plugin disable command description and usage"
keywords: "plugin, disable"
---

# plugin disable

```markdown
Usage:  docker plugin disable [OPTIONS] PLUGIN

Disable a plugin

Options:
  -f, --force   Force the disable of an active plugin
      --help    Print usage
```

## Description

Disables a plugin. The plugin must be installed before it can be disabled,
see [`docker plugin install`](plugin_install.md). Without the `-f` option,
a plugin that has references (e.g., volumes, networks) cannot be disabled.

## Examples

The following example shows that the `sample-volume-plugin` plugin is installed
and enabled:

```console
$ docker plugin ls

ID            NAME                                    DESCRIPTION                ENABLED
69553ca1d123  tiborvass/sample-volume-plugin:latest   A test plugin for Docker   true
```

To disable the plugin, use the following command:

```console
$ docker plugin disable tiborvass/sample-volume-plugin

tiborvass/sample-volume-plugin

$ docker plugin ls

ID            NAME                                    DESCRIPTION                ENABLED
69553ca1d123  tiborvass/sample-volume-plugin:latest   A test plugin for Docker   false
```

## Related commands

* [plugin create](plugin_create.md)
* [plugin enable](plugin_enable.md)
* [plugin inspect](plugin_inspect.md)
* [plugin install](plugin_install.md)
* [plugin ls](plugin_ls.md)
* [plugin push](plugin_push.md)
* [plugin rm](plugin_rm.md)
* [plugin set](plugin_set.md)
* [plugin upgrade](plugin_upgrade.md)
