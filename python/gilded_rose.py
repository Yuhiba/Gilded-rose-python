# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    self.decrease_quality_except_sulfuras(item)
            else:
                if item.quality < 50:
                    self.increase_quality(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                           if item.quality < 50:
                                self.increase_quality(item)
                        if item.sell_in < 6:
                            if item.quality < 50:
                                self.increase_quality(item)
            self.decrease_sell_in_except_hand(item)
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            self.decrease_quality_except_sulfuras(item)
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        self.increase_quality(item)

    def decrease_quality_except_sulfuras(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            self.decrease_quality(item)

    def decrease_sell_in_except_hand(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

    def increase_quality(self, item):
        item.quality += 1

    def decrease_quality(self, item):
        item.quality -= 1



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
