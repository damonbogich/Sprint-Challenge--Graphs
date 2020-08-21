from util import Stack, Queue
import random

from player import Player

class Traversal_Graph():
    def __init__(self, player):
        """
        vertices are all of the seperate rooms.
        entries in this dictionary will be current_room: {directions: ?}
        0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
        """
        self.rooms = {}
        self.player = player
        
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
    def add_edge(self, current_room, direction, new_room):
        """
        Add a directed edge to the graph.
        Edges are created when '?' value is
        changed to a room #
        """
        self.rooms[current_room][direction] = new_room
        #if room traveled to is not in graph
            #add it to graph
        if new_room not in self.rooms.keys():
            self.add_room(new_room)

        #fill in the room that was traveled from into this
        #room's dictionary
        if direction == 'n':
            self.rooms[new_room]['s'] = current_room
        elif direction == 's':
            self.rooms[new_room]['n'] = current_room
        elif direction == 'w':
            self.rooms[new_room]['e'] = current_room
        elif direction == 'e':
            self.rooms[new_room]['w'] = current_room
    def check_graph(self):
        """
        Get all neighbors (edges) of a vertex.
        Returns the directions that can be traveled
        from current room
        """
        done = True
        empty = []
        for key in self.rooms:
            empty.append(key)
        for i in empty:                         
            if "?" in self.rooms[i].values():
                print('room', self.player.current_room.id)
                print('check', self.rooms[i].values())
                done = False
        return done


    

    def get_exits(self):
        """
        returns a list of directions to exit
        """
        return self.player.current_room.get_exits()
    def dft(self, path):
        
        stack = Stack()
        current_room = self.player.current_room.id
        stack.push(current_room)
        visited = []
        self.add_room(current_room)


        while stack.size() > 0:
  
            current_room = stack.pop()
       
            
            unexplored_directions = [k for k,v in self.rooms[current_room].items() if v == '?']
            
            if len(unexplored_directions) > 0:
                random_direction = random.choice(unexplored_directions)
                
                self.player.travel(random_direction)
                
                path.append(random_direction)
        
                self.add_edge(current_room, random_direction, self.player.current_room.id)
            
  
                stack.push(self.player.current_room.id)
   
            elif self.check_graph() == True:
                break
        
            else:
                
                #returns path from current room to room with ?
                returned_path = self.bfs(current_room)
                #removes first room from returned path
                returned_path.pop(0)
                print('returned_path', returned_path)


                #create new list to store directions to desired room
                direction_path = []
            
                for i in range(len(returned_path)):
                    #takes keys from self.rooms at current room
                    for key in self.rooms[current_room]:
                        #check if current room has a direction that equals first
                        #item in path
                        print('key', key)
                        print('currentroom', self.rooms[current_room])
                        if self.rooms[current_room][key] == returned_path[i]:
                            #add that key to dictionary
                            direction_path.append(key)
                            #current room gets updated to wherever
                            #item in returned_path is being looked at
                            current_room = returned_path[i]
                       


                #add directions to path and add player's new 
                #current room to stack
                for direction in direction_path:
                    self.player.travel(direction)
                    path.append(direction)
                print('player room id',self.player.current_room.id )
                stack.push(self.player.current_room.id)



                
                
                
                    


    
    def bfs(self, starting_room):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #needs to result in directions to room with "?" as a value
       
        q = Queue()
        #enqueue the room that is a dead_end
        q.enqueue([starting_room])
        #list of visited rooms.... last room from path
        visited = list()


        while q.size() > 0:
            #first path from queue
            removed_path = q.dequeue() 
            #last room from path
            last_room = removed_path[len(removed_path) - 1]
            
            if last_room not in visited:
                #if last room has "?" value it is the destination
                if "?" in self.rooms[last_room].values():
                    #path of rooms
                    return removed_path
                #add current room to visited
                visited.append(last_room)

            #neighbors will be rooms that are near... find them by checking dictionary for values
            exits = self.get_room_exits(last_room)

            neighbors = []

            for exitt in exits:
                neighbors.append(self.rooms[last_room][exitt])
            
            #going to result in a list of paths to neighbors from starting room
            neighbor_paths = []

            for i in range(len(neighbors)):
                neighbor_list = list(neighbors)
                

                neighbor_paths.append(removed_path.copy()) 
                neighbor_paths[i].append(neighbor_list[i]) 

            for path in neighbor_paths:
                q.enqueue(path)
