class Document(object):
    """description of class"""
    def __init__(self, filename=None):
        self.fileName = filename
        self.pages = []
        self.addPage()

    def addPage(self, title='New Page'):
        page = Page(title)
        self.pages.append(page)

    def __getitem__(self, index):
        return self.pages[index]

    def __setitem__(self, index, page):
        self.pages[index] = page

    def __delitem__(self, index):
        del self.pages[index]


class Page(object):
    def __init__(self, title):
        self.title = title
        self.text = ''