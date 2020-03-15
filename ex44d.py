class Parent(object):

	def override(self):
		print("PARENT overrinde")

	def implicit(self):
		print("PARENT implicit")

	def altered(self):
		print("PARENT altered()")

class Child(Parent):

	def override(self):
		print("CHILD override")

	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit() # from Parent class run implicit function.
son.implicit() # class Child has-no an implicit function, it inherits that funtion from Parent class.

dad.override() # from Paren class run override function.
son.override() # as class Child has-a override function as well as class Parent, it runs its own version.

dad.altered() # from Parent class run altered function.
son.altered() # altered function's class Child overrides Parent's one because it has-a function with same name, then super() function runs Parent classes's version of altered function, after altered funtion from class Child is finished.

