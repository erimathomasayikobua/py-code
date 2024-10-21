class person:
	def __init__(self, name, age, gender,):
	    self.name = name
	    self.age = age
	    self.gender = gender

	def  display_info(self):
		return f"Name: {self.name} Age: {self.age} Gender: {self.gender}"

class student(person):
	def __init__(self, name, age, gender,RegNo):
	    super().__init__(name, age, gender)
	    self.RegNo = RegNo

	def display_info(self):
	    return super().display_info() + f", RegNo {self.RegNo}"

class Staff(person):
	def __init__(self, name, age, gender,workPermit):
		super().__init__(name, age, gender)
		self.workPermit = workPermit

	def display_info(self):
	    return super().display_info() + f", workPermit {self.workPermit}"	

person1 = person("Agnes", 20, "female")
person2 = person("Henry", 24, "Male")
student1 = student("Abooki", 23,"Male", "M23B13/065")
student2 = student("Atwooki", 19, "Male", "S24B23/034")
staff1 = Staff("Brian", 15, "Male", "1973676")

print(person1.display_info())
print(person2.display_info())
print(student1.display_info())
print(student2.display_info())
print(staff1.display_info())