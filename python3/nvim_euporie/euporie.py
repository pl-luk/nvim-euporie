import vim
import euporie
from importlib.metadata import entry_points


class Euporie():

    def run(self):
       entry_points().select(name='notebook')[0].load() 
