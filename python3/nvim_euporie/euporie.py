import vim
import subprocess

class Euporie():

    def run(self):
        b = vim.current.buffer
        b[:] = None
        
        with open("/src/nvim-euporie/python3/nvim_euporie/bytes", "rb") as f:
           binary_buf = f.read()
           lines = binary_buf.split(b'\n')
           b[:] = lines
