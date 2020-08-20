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
        done = False
        empty = []
        for key in self.rooms:
            empty.append(key)
        for i in empty:
            if "?" not in self.rooms[i].values():
                done = True
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
        
        visited = list()

        while q.size() > 0:
           
            removed_path = q.dequeue() 

            last_room = removed_path[len(removed_path) - 1]

            if last_room not in visited:
                
                if "?" in self.rooms[last_room].values():
                    
                    return visited  
                exits = self.get_exits() 
                neighbor_list = []
                for exitt in exits:
                    neighbor_list.append(self.rooms[last_room][exitt])
                    visited.append(exitt)
           
                exit_paths = []

                for i in range(len(exits)):
                 

                    exit_paths.append(removed_path.copy()) 
                    exit_paths[i].append(neighbor_list[i]) 

                for exits in exit_paths:
                    q.enqueue(exits)
