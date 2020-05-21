# This file is Copyright (c) 2020 Piotr Esden-Tempski <piotr@esden.net>
# License: BSD

from migen import *
from migen.genlib.cdc import MultiReg

from litex.soc.interconnect.csr import *
from litex.soc.integration.doc import AutoDoc, ModuleDoc


class Btns(Module, AutoCSR, AutoDoc):
    """iCEBreaker User Buttons control.

    With this module you can control the three User Buttons on the breakoff board.

    Attributes:
        btn_pin: Signals of the Button pin inputs.
        btn_name: Array of the Button names and descriptions. [["name1", "description1"], ["name2", "description2"]]
    """
    def __init__(self, btn_pin):
        # Documentation
        self.intro = ModuleDoc("""iCEBreaker Button control.
        The three momentary switches on the breakaway PMOD.
        """)

        # HDL Implementation
        self._in = CSRStatus(len(btn_pin))
        self.specials += MultiReg(btn_pin, self._in.status)
