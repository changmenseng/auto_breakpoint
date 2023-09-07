import sys
import pdb
import bdb
import os

class MimicTb:
    def __init__(self, tb):
        self.tb_frame = tb.tb_frame
        self.tb_lasti = tb.tb_lasti
        self.tb_lineno = tb.tb_lineno
        self.tb_next = None
        
def is_user_code(fname):
    for path in sys.path:
        if (path in fname) and (path != '') and (path != os.getcwd()):
            return False
    return True

def handle(etype, value, tb):
    if etype != KeyboardInterrupt and etype != bdb.BdbQuit:
        while tb:
            if is_user_code(tb.tb_frame.f_code.co_filename):
                user_tb = tb
            tb = tb.tb_next
        mimic_user_tb = MimicTb(user_tb)
        pdb.post_mortem(t=mimic_user_tb)

try:
    # ipython interpreter
    ip = get_ipython()
    def handler(self, etype, value, tb, tb_offset=None):
        ip.excepthook(etype, value, tb)
        handle(etype, value, tb)

    ip.set_custom_exc((Exception,), handler)

except NameError:
    # normal python interpreter
    old_excepthook = sys.excepthook
    def excepthook(etype, value, tb):
        old_excepthook(etype, value, tb)
        handle(etype, value, tb)

    sys.excepthook = excepthook
