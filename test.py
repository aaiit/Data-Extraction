import json
import jsonpickle
from json import JSONEncoder

class Employee(object):
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address
    def save(self):
    	return jsonpickle.encode(self, unpicklable=False)
    def load(self,s):
    	print(jsonpickle.decode(s))
    	self = jsonpickle.decode(s)
class Address(object):
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin

address = Address("Alpharetta", "7258 Spring Street", "30004")
employee = Employee("John", 9000, address)

r = employee.save()

Z=Employee("++", "7258 ll ll", "5555")
Z.load(r)
print(Z.save())
