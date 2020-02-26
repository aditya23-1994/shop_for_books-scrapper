import re
from locators.book_locator import BookLocator

class BookParser:

    RATINGS = {
        'one': 1,
        'two': 2,
        'three':3,
        'four':4,
        'five':5
    }

    def __init__(self,parent):
        self.parent = parent
        self.pound = u"\xA3"

    def __repr__(self):
        return f'<Book {self.name}, {self.price} ({self.ratings} stars)>'
    @property
    def name(self):
        locator = BookLocator.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name
    
    @property
    def link(self):
        locator = BookLocator.LINK_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['href']
        return item_link

    @property
    def price(self):
        locator = BookLocator.PRICE_LOCATOR
        item_price = self.parent.select_one(locator)
        
        pattern = f'{self.pound}([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))
    
    @property
    def rating(self):
        locator = BookLocator.PRICE_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r!='star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0], -1) #NONE if not found

        return rating_number