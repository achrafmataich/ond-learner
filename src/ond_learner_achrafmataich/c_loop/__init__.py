from ctypes import CDLL, c_char_p, c_int
import os

handler_path = os.path.join(os.path.dirname(__file__), "ctypes", "c_loop.so")
print(handler_path)
handler = CDLL(handler_path)

loopy = handler.loopy

loopy.argtypes = [c_int]
loopy.restype = c_char_p

class Looper:
    """
    Looper is a class that handles c loops
    """
    def __init__(self, num_iter: int) -> None:
        self.num_iter = num_iter
        
    def do_loop(self) -> None:
        """
        do a loop in c
        """
        res = loopy(self.num_iter)
        print(res)