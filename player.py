from util import Stack, Queue
import random

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

    
    
   
   
   
   
   
   
   
   
    # def dft(self, traversal_path, traversal_graph):
    #     stack = Stack() #how can i use the stack????  Add rooms that we visit to it

    #     #list of exits
    #     exits = self.current_room.get_exits()
    #     # #random exit from list of exits
    #     # random_exit_direction = random.choice(exits)    what is the point of randomizing???

    #     #push random direction onto stack --- I think this is wrong what goes on stack?????
    #     stack.push({self.current_room.id : exits})
    #     print(stack.stack)

    #     while stack.size() > 0:
    #         #pop room and exits off of stack
    #         room_and_directions = stack.pop() #dictionary {roomid: [possible directions]}
    #         directions = room_and_directions[self.current_room.id] #list of possible directions
    #         print('directions',directions)
    #         #remove first direction and move that way:
    #         first_direction = directions[0]
    #         # for i in directions:
    #         #     if traversal_graph[self.current_room.id][i] == '?':
    #         #         first_direction = directions[i]

            

    #         if traversal_graph[self.current_room.id][first_direction] == '?':
    #             current_room = self.current_room.id
    #             self.travel(first_direction)
    #             #add direction traveled 
    #             #change ? to the room we arrive in 
    #             traversal_path.append(first_direction)
    #             traversal_graph[current_room][first_direction] = self.current_room.id
    #             print('traversal_graph', traversal_graph)
    #             # print('traversal graph', traversal_graph)
    #             # print('current_room', self.current_room.id)
                
    #             new_exits = self.current_room.get_exits()
    #             stack.push({self.current_room.id : new_exits})
               
    #     return traversal_path


