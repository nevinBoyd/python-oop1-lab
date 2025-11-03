#!/usr/bin/env python3

class Book:
     # Initialize with title and page count
     def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
     
     #Ensure page_count is always an integer
     @property
     def page_count(self):
        return self._page_count

     @page_count.setter
     def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")   
    
     # Simulates turning a page
     def turn_page(self):
        print("Flipping the page...wow, you read fast!")       