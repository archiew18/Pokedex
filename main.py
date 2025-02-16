class Pokemon:
  def __init__(self,entry,name,types,description,is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught == True

  def speak(self):
    print(self.name + self.name)
  
  def display_details(self):
    print('Entry number: ' + self.entry + '\n' + 'Name: ' + self.name + '\n' + 'Type: ' + self.types + '\n' + 'Description: ' + self.description)
    if self.is_caught == True:
      print(self.name + ' has already been caught!')
    else:
      print(self.name + ' hasnt been caught')

pikachu = Pokemon(25, 'Pikachu', 'Electric', 'When it is angered, it immediately discharges the energy stored in the pouches in its cheeks.', True)

pikachu.speak()
pikachu.display_details()
