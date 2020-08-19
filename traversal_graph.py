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


            # #update current room???
            # current_room = self.player.current_room.id
            # print(current_room)
        
        # then loop.

        #when you reach a dead-end (i.e. a room with no unexplored paths)
        #walk back to the nearest room that does contain an unexplored path.
            #will use a breadth first search to find nearest room that does
            #contain an unexplored path
        pass
    def bfs(self, starting_vertex, destination_vertex):
        pass





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