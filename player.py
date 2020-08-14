from util import Stack, Queue
class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
    def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")

    
    
    def dft(self):
        #picks a random unexplored direction from the player's current room
        
        print('exits', self.current_room.get_exits()) #returns list of directions that can be explored. pick random direction
        


        #travels and logs that direction, then loops





    # #lets try to write a function that could be used to pass the first test in player
    # def dft(self, path, traversal_graph):
    #     #will carry room_id and directions that have been traveled from that room?

    #     current_room_id = self.current_room.id

    #     current_room_exits = self.current_room.get_exits()
    #     print('room exits', current_room_exits) #returns list of possible directions to travel
    #     if traversal_graph[current_room_id]['n'] == '?':
            
    #         #travels north if possible
    #         self.travel('n')

    #         #fills in traversal graph value
    #         traversal_graph[current_room_id]['n'] = self.current_room.id
    #         print('traversalgraph', traversal_graph)
    #         print('after travel', self.current_room.id)
    #         path.append('n')



