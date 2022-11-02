from game.casting.artifact import Artifact

class Gem(Artifact): #gem is a child class of artifact
  
    def __init__(self):    
        super().__init__()  #the shape of the artifact gem is created.
        self._text = "*"     # one point is added when the robot meets with a gem. 
