class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

spider = ["The itsy bitsy spider went up the water spout!",
          "Down came the rain and washed the spider out!"]

kid_song = Song(spider)

kid_song.lyrics = spider

kid_song.sing_me_a_song()