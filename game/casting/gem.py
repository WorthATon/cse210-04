from game.casting.artifact import Artifact

class Gem(Artifact):
  
    def __init__(self):    
        super().__init__()
        self._text = "*"
