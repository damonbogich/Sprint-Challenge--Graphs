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
    def get_neighbors(self, room):
        """
        Get all neighbors (edges) of a vertex.
        Returns the directions that can be traveled
        from current room
        """
        #TODO: this function
        # return self.rooms[room_id]

    def get_exits(self):
        """
        returns a list of directions to exit
        """
        return self.player.current_room.get_exits()
    def dft(self, path):
        #experimental:
        #set player's current room to variable
        stack = Stack()
        current_room = self.player.current_room.id
        stack.push(current_room)

        #add current room to graph: {{current_room: {n: "?", s: "?"}}}
        #only adds directions that can be traveled in 
        self.add_room(current_room)
        print('herehhe', self.rooms)
        visited = list()
        while stack.size() > 0:
            current_room = stack.pop()
            if current_room not in visited:
                visited.append(current_room)
            #unexplored_directions is a list of exit directions that have not yet been traveled
                unexplored_directions = [k for k,v in self.rooms[current_room].items() if v == '?']
                #now we want to pick a random unexplored direction from unexplored_directions
                if len(unexplored_directions) > 0:
                    random_direction = random.choice(unexplored_directions)
                    #now we want to travel that direction
                    self.player.travel(random_direction)
                    # and log random_direction in steps traveled -- add to traversal path
                    path.append(random_direction)
                    #also need to update our graph
                    self.add_edge(current_room, random_direction, self.player.current_room.id)
                    # self.rooms[current_room][random_direction] = self.player.current_room.id
                    print('diciin', self.rooms)
                    stack.push(self.player.current_room.id)
                #elif check current room's available directions and walk that way if there is a '?' value
                    #if no '?' value then just walk a random way until room with '?' is found
                else:
                    #going to check all of the current room's direction values
                    #look at them in the graph self.rooms[value]
                        #if one of them has a '?' as a value, we will move to that one and put it on stack
                    for direction in self.bfs(self.player.current_room.id, path):
                        self.player.travel(direction)
                        path.append(direction)
                    print('path',path)
                    print(self.player.current_room.id)
                    stack.push(self.player.current_room.id)
                        
                    


    
    def bfs(self, starting_room, path):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #starting room is current room player is in
        #path is the list that I neeed directions in 

        #instantiate queue
        q = Queue()
        #put current room into queue in list format
        q.enqueue([starting_room])
        #maybe add directions in list?
        visited = list()

        while q.size() > 0:
            #list of rooms
            removed_path = q.dequeue() 
            #last room in list
            last_room = removed_path[len(removed_path) - 1]

            if last_room not in visited:
                #if last room not in visited, we need to figure out the directions that were taken,
                #to travel this path
                if "?" in self.rooms[last_room].values():
                    print(visited)
                    return visited  #should as a list of rooms where last one has "?" val

                

                #if no "?" found:
                    #want to add path to all other rooms 
                exits = self.get_exits() #exits: ['s']
                # want to get the room to 's' and add it to removed 
                # neighbor = self.rooms[last_room][exits[0]] #1
                neighbor_list = []
                for exitt in exits:
                    neighbor_list.append(self.rooms[last_room][exitt])
                    visited.append(exitt)
                #going to need to change line above so that it will find all neighboring rooms
                #and their paths

                

                #create a list to store the path to all neighbors of current vertex
                exit_paths = []

                for i in range(len(exits)):
                    #need to find another way to put this in list
                    #can't do it with a string
                    # neighbor_list = list(neighbor) #['1']

                    exit_paths.append(removed_path.copy()) #[['1']]
                    exit_paths[i].append(neighbor_list[i]) #[['2', '1']]
                    print('exit paths', exit_paths)

                for exits in exit_paths:
                    q.enqueue(exits)




        #find shortest path to unexplored room -- room with a '?' for an exit

        # Instead of searching for a target vertex, you are searching for an exit with a '?' as the value. If an exit has been explored, you can put it in your BFS queue like normal.

        # BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.

        # If all paths have been explored, you're done!


            pass














###Lines 111 - 139 is the previous working DFT
#  beg # def dft(self, path):
    #     #set player's current room to variable
    #     stack = Stack()
    #     current_room = self.player.current_room.id
    #     stack.push(current_room)

    #     #add current room to graph: {{current_room: {n: "?", s: "?"}}}
    #     #only adds directions that can be traveled in 
    #     self.add_room(current_room)
    #     print('herehhe', self.rooms)
    #     visited = list()
    #     while stack.size() > 0:
    #         current_room = stack.pop()
    #         if current_room not in visited:
    #             visited.append(current_room)
    #         #unexplored_directions is a list of exit directions that have not yet been traveled
    #             unexplored_directions = [k for k,v in self.rooms[current_room].items() if v == '?']
    #             #now we want to pick a random unexplored direction from unexplored_directions
    #             if len(unexplored_directions) > 0:
    #                 random_direction = random.choice(unexplored_directions)
    #                 #now we want to travel that direction
    #                 self.player.travel(random_direction)
    #                 # and log random_direction in steps traveled -- add to traversal path
    #                 path.append(random_direction)
    #                 #also need to update our graph
    #                 self.add_edge(current_room, random_direction, self.player.current_room.id)
    #                 # self.rooms[current_room][random_direction] = self.player.current_room.id
    #                 print('diciin', self.rooms)
    #     end         stack.push(self.player.current_room.id)
                #right now graph goes all the way down one direction, then while there it has no unexplored directions left to go to

                #You can find the path to the shortest unexplored room by using a breadth-first search for a room with a '?' for an exit. If you use the bfs code from the homework, you will need to make a few modifications.

                    #Instead of searching for a target vertex, you are searching for an exit with a '?' as the value. If an exit has been explored, you can put it in your BFS queue like normal.

                    # BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.

                #first we need to search for a room that still has a '?' for an exit value

      
        
    
        





# def bfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.
#         """
#         #create an empty queue and enqueue the path to the starting vertex
#         q = Queue() #empty q

#         q.enqueue([starting_vertex]) #[['1']]
#         #create set to store visited
#         visited = set() #{}
#         #while queue is not empty:
#         while q.size() > 0:
#             #dequeue the first path
#             removed_path = q.dequeue() #['1']
#             #grab last vertex value from the path
#             last_vert = removed_path[len(removed_path) - 1] #'1'

#             #if the vertex has not been visited:
#             if last_vert not in visited:
#                 #if it is the destination_index:
#                 if last_vert == destination_vertex:
#                     #return the path
#                     return removed_path
#                 #mark it as visited
#                 visited.add(last_vert) ### visited = {'1'}

#                 #then add a path to its neighbors to the back of the queue
#                 neighbors = self.get_neighbors(last_vert) #returns set of neighbors = {'2','3'}
#                 print(neighbors)

#                 #create a list to store the path to all neighbors of current vertex
#                 neighbor_paths = []
#                 #loop through and make a list with path to all neighbors
#                 for i in range(len(neighbors)):
#                     neighbor_list = list(neighbors) #['2', '3']

#                     neighbor_paths.append(removed_path.copy()) #[['1'], ['1']]
#                     neighbor_paths[i].append(neighbor_list[i]) 
#                     print('neighbor paths', neighbor_paths)

#                 for path in neighbor_paths:
#                     q.enqueue(path)



#                 #make a copy of the path
                
#                 #append the neighbor to the back of the path
#                 #enqueue out new path
            
#         return None




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

    # def opposite_direction(self, direction, opposite_list):
    #     if direction == 'n':
    #         opposite_list.append('s')
    #         opposite_list.reverse()
    #     elif direction == 's':
    #         opposite_list.append('n')
    #         opposite_list.reverse()
    #     elif direction == 'e':
    #         opposite_list.append('w')
    #         opposite_list.reverse()
    #     elif direction == 'w':
    #         opposite_list.append('e')
    #         opposite_list.reverse()