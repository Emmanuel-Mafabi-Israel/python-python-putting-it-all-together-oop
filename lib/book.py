# GLORY BE TO GOD,
# PYTHON PROGRAMMING - PYTHON - PUTTING IT ALL TOGETHER, OOP
# BY ISRAEL MAFABI EMMANUEL

class Book:
    def __init__(self, title:str = "", page_count:int = 0):
        self.title      = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, count):
        if not isinstance(count, int):
            print("page_count must be an integer")
        else:
            self._page_count = count

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title_text):
        if not isinstance(title_text, str):
            print("page title must be text ~ a string!")
        else:
            self._title = title_text

    def turn_page(self):
        try:
            print("Flipping the page...wow, you read so fast!!!")
        except TypeError as e:
            print(f"Error associated with page number: {e}")