class Person:
  def __init__(self, first_name, last_name, age):
    self._first_name = first_name
    self._last_name = last_name 
    self._age = age
    self._gender = None

  def get_fullname(self):
    return f'{self._first_name} {self._last_name}'

  def set_gender(self, gender):
    self._gender = gender

  def __str__(self) -> str:
    return f'{self._first_name} {self._last_name}'

class Account:
  def __init__(self, person):
    if not isinstance(person, Person):
      raise TypeError('Not compatible')

    self._owner = person
    self._balance = 0

  def withdraw(self, amount):
    if not type(amount) == 'int':
      raise TypeError('invalid ty')
    if amount < self._balance:
      raise ValueError('Insufficient fund')

    self._balance = self._balance - amount

  def deposit(self, amount):
    self._balance = self._balance + amount

  def check_balance(self):
    return self._balance

  def holder(self):
    return self._owner.get_fullname()

  def set_holder(self, person):
    if isinstance(person, Person):
      self._owner = person
    else:
      raise TypeError('Not compatible')

  def __str__(self) -> str:
    return '\n Account owner: {}\n Account balance: {}'.format(self._owner, self._balance)

if __name__ == '__main__':
  person1 = Person('John', 'Doe', 23)
  person1.set_gender('male')
  chimasAcc = Account(person1)
  person2 = Person('Sam', 'Johnson', 21)
  person2.set_gender('female')
  chimasAcc.deposit(7890)
  effiongsAcc = Account(person2)
  chimasAcc.set_holder(person1)
  effiongsAcc.deposit(3450)
  effiongsAcc.set_holder(person2)

  mikesAccount = Account(person1)
  print(f'Initial balance:', mikesAccount.check_balance())
  mikesAccount.deposit(5000)

  print('Chimas account', chimasAcc)
  print('Effiongs acccount', effiongsAcc)
 
  print('Chimas Balance', chimasAcc.check_balance())
  print('Account name', effiongsAcc.holder())
  print(f'Current balance:', mikesAccount.check_balance())