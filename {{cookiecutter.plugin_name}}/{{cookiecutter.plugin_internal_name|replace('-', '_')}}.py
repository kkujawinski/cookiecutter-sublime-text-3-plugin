# -*- coding: utf-8 -*-
"""Load and Unload all {{cookiecutter.plugin_name}} modules.

This module exports __all__ modules, which Sublime Text needs to know about.
The list of __all__ exported symbols is defined in modules/__init__.py.
"""

try:
    from .modules import *
except ValueError:
    from modules import *
except ImportError:
    # Failed to import at least one module. The current solution
    import sublime
    sublime.message_dialog(
        "{{cookiecutter.plugin_name}} failed to reload properly.\n"
        "Please restart Sublime Text to fix this!")
