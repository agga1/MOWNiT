from classes.Text import Text

class Article:
    """
    Text with some metadata
    """
    def __init__(self, title: str, text: str, link: str = None):
        self.title = title
        self.text = Text(text)
        self.link = link  # absolute path to the full article in txt form

    def to_BOW_with_clean(self, dictionary):
        BOW = self.text.convert_to_BOW(dictionary)
        self.text = None
        return BOW

    def __repr__(self):
        return f"title: {self.title}"  # link:{self.link}
