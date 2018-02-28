import sublime
import sublime_plugin


class {{cookiecutter.plugin_internal_name | replace('_', ' ') | title | replace(' ', '')}}DoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        s = sublime.load_settings("{{cookiecutter.plugin_name}}.sublime-settings")
        first_name = s.get('first_name', 'Noname')
        self.view.insert(edit, 0, "Hi %s!" % first_name)
