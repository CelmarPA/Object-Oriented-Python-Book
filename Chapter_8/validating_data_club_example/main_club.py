# main_club.py

# Club example main program

from club import *

# Create a club with at most 5 members
o_programming_club: Club = Club("Programming", 5)

o_programming_club.add_member("Joe Schmoe")
o_programming_club.add_member("Cindy Lou Hoo")
o_programming_club.add_member("Dino Richmond")
o_programming_club.add_member("Susie Sweetness")
o_programming_club.add_member("Fred Farkle")
o_programming_club.report()

# Attempt to add additional member
o_programming_club.add_member('Iwanna Join')
