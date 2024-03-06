import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class Hronobloknot(Adw.Application):
    def __init__(self) -> None:
        super().__init__(application_id='com.example.Hronobloknot')

    def do_activate(self) -> None:
        builder = Gtk.Builder()
        builder.add_from_file('ui/hronobloknot.ui')

        self.window = builder.get_object("main_window")

        if not isinstance(self.window, Gtk.ApplicationWindow):
            raise Exception

        self.add_window(self.window)
        self.window.set_title('Hronobloknot')
        self.window.set_default_size(1100, 800)

        self.window.present()


if __name__ == '__main__':
    Hronobloknot().run(sys.argv)

