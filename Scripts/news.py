
class News:
    def __init__(self, date, text, link, id):
        self.date = date
        self.text = text
        self.link = link
        self.id = id
    
    def getDate(self):
        return self.date

    def getText(self):
        return self.text
    
    def getLink(self):
        return self.link