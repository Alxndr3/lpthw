class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Haapy birthday to you",
	"I don't want to get sued",
	"So I'll stop right there"])

bull_on_parade = Song(["They rally aroung tha family",
	"With pockets full of shells"])

atirei_o_pau_no_gato = Song(["Atirei o pau no gato",
	"mas o gato não morreu",
	"Dona Chica adimirou-se-se"])

happy_bday.sing_me_a_song()

bull_on_parade.sing_me_a_song()

Song.sing_me_a_song(atirei_o_pau_no_gato)
