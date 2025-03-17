Sier2 Blocks Config
===================

This package provides configuration options for Sier2 blocks.

Sier2 can be used in a variety of environments. However, these enviroments
may require different softwre configurations, For example, when using map tiles
on the Internet, a default tile provider can be used, but on a private network,
a caching tile provider may be preferred.

By placing configuration options in a separate package, blocks can be used in
different environments without having to make environment-specific changes to block code.
Instead, changes can be confined to an environment-specific copy of `sier2-blocks-config`.

Configurations are looked up using the Python entry points specification (see https://packaging.python.org/en/latest/specifications/entry-points/#entry-points). This is the same mechanism
that sier2 uses to find blocks. The entry point name is `sier2.config`. Packages that provide
the entry point implement a function that returns a config dictionary, and specify the
following section in `pyproject.toml`.

.. code-block:: text

    [project.entry-points."sier2.config"]
    export = "sier2_blocks_config:config"

A convenience function called `get_block_config()` is provided by `sier2`. This function
looks up the entry point, calls the config function, and returns the dictionary.

The returned dictionary can contain arbitrary keys and values.
One top-level string key **must** be present: `'config'` provides the name of
the environment that this package is intended for. This copy of the package
provides the name `'public'`; other copies may provide names such as
`'corporate'` or `'private'`. In this way, it easier to quickly determine which copy of
the package is installed, and make it easier to track a possible cause of
broken functionality.

If no config package is found, or more than one config package is found,
`get_block_config()` will produce a warning (using `warnings.warn()`),
and a default config will be returned, with the `'config'` key having the value `None`.
