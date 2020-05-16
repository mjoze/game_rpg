from characters import Player
from places.city import church


p1 = Player.Player()
place1 = church.Church()
p1.get_injured(4)
p1.walk(place1)
place1.pray(p1)
print(place1)
print(p1)

