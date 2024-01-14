class Money:
  _currencies = ("MDL","USD","EUR","RUB","RON")
  def __init__(self, amount, currency):
    if amount > 0 or currency is Money._currencies: 
        self.amount = amount
        self.currency = currency
    else:
        print("ERROR")
  def  __str__(self):
    for i in Money._currencies:
        return f"{self.amount}{Money._currencies[i]}"      # e.g. "100.00MDL"