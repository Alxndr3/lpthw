from textwrap import dedent
from time import sleep


class Engine(object):

	def __init__(self, room):
		self.room_go = room
		return LivingRoom.self.room_go() 


class LivingRoom(object):

	def sofa(self):
		print(dedent("""As you just got in the house sit on the couch
		and take 5.
		"""))
		for x in range(1, 6):
			print(f'{x} minutes')
			sleep(1)
		next_room =  input("Ok!, Now choose your next room: ").title().lower()
		return f'{next_room}()'


class Kitchen(object):

	def eat(self):
		pass
			

class Gym(object):

	def workout(self):
		pass

class Bedroom(object):

	def sleep(self):
		pass

class Bathroom(object):

	def shower(self):
		pass

class Home(object):

	def get_back(self):
		print(dedent("""Congrats, you're not going to die
		because obesety))



start = LivingRoom()
print(start.sofa())

