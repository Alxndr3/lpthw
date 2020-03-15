class Wheel(object):

	def raios(self):
		print("A bicycle wheel has spokes")

	def tires(self):
		print("There are tires on the wheel")
class Bike(Wheel):

	def tires(self):
		print("A bicycle has tires")
	
	def brake(self):
		print("A bicycle has brakes")

roda = Wheel()
bici = Bike()

roda.raios()
bici.raios()

roda.tires()
bici.tires()

bici.brake()

