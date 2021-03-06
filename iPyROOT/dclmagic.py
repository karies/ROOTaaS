import IPython.core.magic as ipym
import utils

@ipym.magics_class
class DeclareMagics(ipym.Magics):
    @ipym.cell_magic
    def dcl(self, line, cell=None):
        """Inject into root."""
        retval = 0
        if cell:
            retval = utils.declareCppCode(cell)
        return retval

def load_ipython_extension(ipython):
    ipython.register_magics(DeclareMagics)
