class ConstructedElement:

    def __init__(self):
        """
        properties
            in_use: bool
            length: int
            starting_position: int
            text: str
        methods
            set_text(text:str)
            treset()
        """
        self.in_use: bool = False
        self.length: int = 0
        self.starting_position: int = -1
        self.text: str = ""
        return
    
    def set_text(self, text):
        """
        sets in use to True, saves text and text length to respective properties
        """
        self.in_use = True
        self.length = len(text)
        self.text = text
        return
    
    def reset(self):
        """
        reset element when not required for current use case
        """
        self.in_use = False
        self.length = 0
        self.starting_position = -1
        self.text = ""
        return