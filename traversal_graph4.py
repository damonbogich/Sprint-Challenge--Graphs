from player import Player
from util import Stack, Queue

class Traversal_Graph():
    def __init__(self, player):
        """
        vertices are all of the seperate rooms.
        entries in this dictionary will be current_room: {directions: ?}
        0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
        """
        self.rooms = {}
        self.player = player
        self.stack = Stack()
        self.queue = Queue()
        self.opposite_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        
    def add_room(self, current_room):
        """
        Add a room to the graph.
        As you travel to a new room,
        add it to the graph with a dictionary
        containing alll of the directions you 
        can move in.  And the room in that direction
        """
        # current_room = self.player.current_room.id
        room_exits = self.get_exits()
        
        self.rooms[current_room] = {}
        for exxit in room_exits:
            self.rooms[current_room][exxit] = "?"
            
    def get_room_exits(self, room):
        return list(self.rooms[room].keys())

    def get_unexplored_directions(self, current_room):
        unexplored_directions = [k for k,v in self.rooms[current_room].items() if v == '?']
        return unexplored_directions

    def get_exits(self):
        """
        returns a list of directions to exit
        """
        return self.player.current_room.get_exits()
    def dft(self, path):
        
        stack = self.stack
        starting_room = self.player.current_room.id
        # stack.push(starting_room)
        self.add_room(starting_room)
        
        #figure out what direction to travel.
        unexplored_exits = self.get_room_exits(starting_room)
        #pick an exit from unexplored exits for player to travel
        travel_direction = unexplored_exits.pop()
        #send player to travel in that direction and add that direction to graph
        #travel:
        self.player.travel(travel_direction)
        path.append(travel_direction)
        #get player's new current room:
        current_room = self.player.current_room.id
        #add direction to graph:
        self.rooms[starting_room][travel_direction] = current_room
        #after traveling:
        #we want to add opposite travel direction to stack
        stack.push(self.opposite_directions[travel_direction])
   
        #We want to add new room to graph, and make sure it contains the room traveled from
        self.add_room(current_room)
        #good way to add room left to new room's object???
        self.rooms[current_room][self.opposite_directions[travel_direction]] = starting_room
        print('rooms graph', self.rooms)

        #start loopppping
        #check to see if current room has any directions it has not traveled in yet,
        #if it does, then we will travel in one of those directions and continue filling out graph
        #if it does not then we will start popping from the stack

        while stack.size() > 0:

            #all within while loop:
            current_room = self.player.current_room.id
            unexplored_directions_list = self.get_unexplored_directions(current_room)

            if len(unexplored_directions_list) > 0:
                print(unexplored_directions_list)
                explore_direction = unexplored_directions_list.pop()
                print(explore_direction)
                #want to move in that direction
                self.player.travel(explore_direction)
                path.append(explore_direction)
                new_room = self.player.current_room.id
                #add the direction explored to old room's object
                self.rooms[current_room][explore_direction] = new_room
                #add opposite of explored direction to stack 
                self.stack.push(self.opposite_directions[explore_direction])

                #add room we get to into graph, with room we came from included
                #check if new room is in graph
                if new_room not in self.rooms:
                    self.add_room(new_room)
                    
                self.rooms[new_room][self.opposite_directions[explore_direction]] = current_room
                print(self.rooms)
                
                print('stack', self.stack.stack)
            
            else: #if no unexplored directions from here!!!!!!!!
                # we want to move back using the directions in the stack until we find room with "?"
                # pop direction off of the stack, have player move there, then re loop 
                back_direction = stack.pop()
                print('back direction', back_direction)
                self.player.travel(back_direction)
                path.append(back_direction)
                #we're back to original rooms, but stack is empty so while loop doesn't run
                current_room = self.player.current_room.id
                unexplored_directions_list = self.get_unexplored_directions(current_room)
                if len(unexplored_directions_list) > 0:
                    #need to move that way and get something on stack
                    
                    travel_direction = unexplored_directions_list.pop()

                    self.player.travel(travel_direction)
            
                    #add travel direction to path
                    path.append(travel_direction)
                    #add opposite of travel direction to stack
                    stack.push(self.opposite_directions[travel_direction])

                    new_room = self.player.current_room.id
                   
                    #add new room to graph;
                    self.add_room(new_room)
                    #Adds new room to old room's object
                    self.rooms[current_room][travel_direction] = new_room
                    #add previous room to new room's object
                    self.rooms[new_room][self.opposite_directions[travel_direction]] = current_room
                    



            
 

        
        #travel in one of the directions and add that direction to the stack

        # while stack.size() > 0:

  
            
       
            # unexplored directions all that needs to do is populate that list with any room exit directions of a current room that still has a ? as a value and then instead of choosing a random one I would just pop one off the end

            # unexplored_directions = [k for k,v in self.rooms[current_room].items() if v == '?']