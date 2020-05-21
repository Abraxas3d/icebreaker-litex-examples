# This file is Copyright (c) 2020 Piotr Esden-Tempski <piotr@esden.net>
# License: BSD

from migen import *

from litex.soc.interconnect.csr import *
from litex.soc.integration.doc import AutoDoc, ModuleDoc


class Segments(Module, AutoCSR, AutoDoc):
    """iCEBreaker seven_segment_PMOD1A control.

    With this module you can control the two-digit 
    seven-segment display from 1 bit squared. 

    Attributes:
        segment_pin: the pins
        segment_name: the name of the pin; which segment lit.
        AI: do we need a way to handle the cathode trick? yes.
    """
    def __init__(self, segment_pin, segment_name=[]):
        # Documentation
        self.intro = ModuleDoc("""iCEBreaker seven_segment_PMOD1A
        control.
        """)

        # HDL Implementation
        self._out = CSRStorage(len(segment_pin), fields=[
            CSRField(fld[0], description=fld[1]) for fld in segment_name
        ])
        self.comb += segment_pin.eq(self._out.storage)
