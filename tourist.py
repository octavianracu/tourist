class Tourist:
  def __init__(self,name,age):
    if len(self.name) < 3:
        self.name = name
    else:
       print("ValueError")
    if len(self.age) <= 1:
        self.age = age      
    else:
       print("ValueError")
  def  __str__(self):
    return f'{self.name} ({self.age}years)'     # e.g. "John Doe (31years)"  