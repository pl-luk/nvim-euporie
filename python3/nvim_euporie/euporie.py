import vim
import subprocess

class Euporie():

    def run(self):
        b = vim.current.buffer
        b[:] = None
        
        with open("/src/nvim-euporie/python3/nvim_euporie/bytes", "rb") as f:
            b.append(f.read())
