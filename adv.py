from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
back_path=[]

# This is the list of opposite direction
def opposite(exist):
    if exist == "n":
        return "s"
    if exist == "s":
        return "n"
    if exit == "w":
        return "e"
    if exist == "e":
        return "w"
    else:
        return "error"

# Keep track of the rooms visited
rooms={}

# Begin journey
rooms[player.current_room.id]=player.current_room.get_exits()
print(rooms)

# checking if we have travel all rooms using dft 
while len(rooms)< (len(room_graph)):

    # check if  the is in now has not been visited
    if player.current_room.id not in rooms:
        # add the room id with it exist to the roooms
        rooms[player.current_room.id]=player.current_room.get_exits()

        last_room= back_path[-1]
        # Remove the last room
        rooms[player.current_room.id].remove(last_room)

    # if  the player reach a dead end we do bfs to find the shortest path
    if len(rooms[player.current_room.id]) <1:
        # last direction
        back=back_path.pop()
        # go back one step
        player.travel(back)
        # this is a move so add it to the traversed path
        traversal_path.append(back)
    # if we have unchecked rooms
    else:
        # pick an exist which is the last exist 
        exit = rooms[player.current_room.id].pop()
        # it is a move so we  add the move to the traversal path
        traversal_path.append(exit)
        # we add the opposite direction to our back_path
        back_path.append(opposite(exit))
        # we no go to the next room through the exist we found
        player.travel(exit)



    





# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
