class item(object):
  def __init__(self, name, sellable=false, sell_price=0):
    self.name = name
    self.is_sellable = sellable
    self.sell_price = sell_price
