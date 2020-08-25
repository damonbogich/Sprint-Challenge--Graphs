from room import Room
from player import Player
from world import World
# from traversal_graph import Traversal_Graph
# from traversal_graph2 import Traversal_GraphT
# from traversal_graph3 import Traversal_Graph
from traversal_graph4 import Traversal_Graph

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
# print('roooooom', room_graph)
# print('roijn', room_graph[0][1]['n'])



#making a traversal graph out of room graph
# get_rid_of_coordinates = {}

# for key, value in room_graph.items():
#     get_rid_of_coordinates[key] = value[1]
# print('convert', get_rid_of_coordinates)

# traversal_graph = {key: {k: '?' for k in dct} for key, dct in get_rid_of_coordinates.items()}
# print('traversal graph', traversal_graph)
# print('traverrrr', traversal_graph[0]['n'] == '?')



world.load_graph(room_graph) #creates room graph


# Print an ASCII map
world.print_rooms() #creates rooms and lines between them

player = Player(world.starting_room) #player instantiated starting in room 0
# print('curr', player.current_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

traversal_graph = Traversal_Graph(player)

traversal_graph.dft(traversal_path)

# traversal_graph2 = Traversal_GraphT(player)

# traversal_graph2.dft(traversal_path)



#player.currentroom is room object where player is player.current_room.id is room number
# player.current_room.get_exits() list with all possible directions player can move




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
