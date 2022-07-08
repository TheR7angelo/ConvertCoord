from src.lib.palettes import *
from src.widgets import vb_wg
from src.widgets.LineEdit.Build import Build


##################
##     BASE     ##
##################
class Base:
    def __init__(self, *wgs):
        self.wgs = wgs

    def th(self):
        Build(
            *self.wgs,
        )
    def tr(self):
        Build(
            *self.wgs,

            bg=Rgb().tr(),
            fg=Rgb().th3()
        )
    def rgb_hex(self):
        Build(
            *self.wgs,

            align_horizontal=Align().center_horizontal(),

            bg=Rgb().tr(),
            bg_selection=Rgb().th3(),
            fg=Rgb().th3(),
            fg_selection=Rgb().th1(),
        )
