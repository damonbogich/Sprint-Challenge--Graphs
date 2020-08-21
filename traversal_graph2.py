from util import Stack, Queue
import random

from player import Player

class Traversal_GraphT():
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
                visited.append(current_room)

                for direction in self.bfs(self.player.current_room.id, path):
                    self.player.travel(direction)
                    path.append(direction)
                
                stack.push(self.player.current_room.id)
                        
                    


    
    def bfs(self, starting_room, path):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
       
        q = Queue()
       
        q.enqueue([starting_room])
        
        path_back = list()

        visited = list()

        while q.size() > 0:
           
            removed_path = q.dequeue() 

            last_room = removed_path[len(removed_path) - 1]

            visited.append(last_room)

            
                
            if "?" in self.rooms[last_room].values():
                
                return path_back  
            
            # elif self.check_graph() == True:
            #     break
            # exits = self.get_exits() 
            exits = self.get_room_exits(last_room)
            viable_exits = []
            for exitt in exits:
                if self.rooms[last_room][exitt] not in visited:
                    viable_exits.append(exitt)


            neighbor_list = []
            real_neighbor_list = []
            for exitt in viable_exits:
                neighbor_list.append(self.rooms[last_room][exitt])
                # path_back.append(exitt) #<--- when this comes back 
            #checks if more than one neighbor
            if len(neighbor_list) > 1:
                #loops through neighbors
                for neighbor in neighbor_list:
                    #checks for neighbor with "?" value
                    if "?" in self.rooms[neighbor].values():
                        #new list to add the 
                        real_neighbor_list.append(neighbor)
                for key in self.rooms[last_room]:
                    if self.rooms[last_room][key] == real_neighbor_list[0]:
                        path_back.append(key)
                        viable_exits = list(key)
            else:
                real_neighbor_list = neighbor_list
                path_back.append(viable_exits[0])

            exit_paths = []

            for i in range(len(viable_exits)):
                

                exit_paths.append(removed_path.copy()) 
                exit_paths[i].append(real_neighbor_list[i]) 

            for exits in exit_paths:
                q.enqueue(exits)