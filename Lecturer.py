from Person import Person
class Lecturer(Person):
  def __init__(self, name, age, mail, startDate):
    super().__init__(name, age, mail)
    self.startDate = startDate
    