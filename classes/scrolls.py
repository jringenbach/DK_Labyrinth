from classes.element import Element


class Scrolls(Element):
    """Scrolls inherit from Element.
    This is an element that will have an additionnal attribute : message"""

    def __init__(self, message):
        Element.__init__(self, "scroll", "P", "resources/img/sprites/scroll_30_30.png", False, False)
        self.message = message
        
