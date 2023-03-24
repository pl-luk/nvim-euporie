import vim
import subprocess

class Euporie():

    def run(self):
        b = vim.current.buffer
        b[:] = None
        
        with open("bytes", "rb") as f:
            b.append(f.read())
