class Parent(object):

	def impicit(self):
		print("PARENT implicit()")

class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.impicit()
son.impicit()
