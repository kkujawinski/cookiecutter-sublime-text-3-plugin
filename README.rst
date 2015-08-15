==================================
cookiecutter-sublime-text-3-plugin
==================================

Cookiecutter template for a Sublime Text 3 plugin.

* Free software: BSD license

Features
--------
* Example settings file configuration,
* Example sublime commands,
* Example main menu changes,
* Example key bindings


Usage
-----

Go to you Sublime Packages directory::

    cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages

Generate a Python package project::

    cookiecutter https://github.com/kkujawinski/cookiecutter-sublime-text-3-plugin.git

Then:

* Uncomment functionality in cofiguration files:

    * Default plugin settings in `*.sublime-settings`,
    * Plugin key binding in * `($platform).sublime-keymap`,
    * Plugin command in `Default.sublime-commands`,
    * Edit preferences command in `Default.sublime-commands`,
    * Edit preferences menu items in `Main.sublime-menu`,
    * Plugin command menu items in `Main.sublime-menu`,

* Update your license if don't want BSD,

* Init git repository, submit your project to packagecontrol.io, enjoy!
