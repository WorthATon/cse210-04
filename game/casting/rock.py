from game.casting.artifact import Artifact
#rock deducts a point when it touches the artifact
class Rock(Artifact):
    def __init__(self):
        super().__init__()
        self._text = "O"
