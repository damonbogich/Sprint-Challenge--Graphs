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

    
    
    def dft(self, traversal_path, traversal_graph):
        #picks a random unexplored direction from the player's current room
         #returns list of directions that can be explored. pick random direction

        stack = Stack() #how can i use the stack????  Add rooms that we visit to it

        # visited = set() #do i need this? 

        #pick random direction from get exits

        #list of exits
        exits = self.current_room.get_exits()
        # #random exit from list of exits
        # random_exit_direction = random.choice(exits)    what is the point of randomizing???

        #push random direction onto stack --- I think this is wrong what goes on stack?????
        stack.push({self.current_room.id : exits})
        print(stack.stack)

        while stack.size() > 0:
            #pop room and exits off of stack
            room_and_directions = stack.pop() #dictionary {roomid: [possible directions]}
            directions = room_and_directions[self.current_room.id] #list of possible directions
            #remove first direction and move that way:
            first_direction = directions[0]

            #move that direction if room in that direction has not been visited
            #check traversal graph to see if the room from current room's direction is known
            # print('hereeee',traversal_graph[self.current_room.id][first_direction])
            if traversal_graph[self.current_room.id][first_direction] == '?':
                current_room = self.current_room.id
                self.travel(first_direction)
                #add direction traveled 
                #change ? to the room we arrive in 
                traversal_path.append(first_direction)
                traversal_graph[current_room][first_direction] = self.current_room.id
                print('traversal_graph', traversal_graph)
                # print('traversal graph', traversal_graph)
                # print('current_room', self.current_room.id)
                #need to add the new current room's direction to stack the same way as i did earlier
                
                new_exits = self.current_room.get_exits()
                stack.push({self.current_room.id : new_exits})
                # print('stack', stack.stack)
            
        return traversal_path

    # def bfs(self, traversal_graph, starting_vert, ending_vert):
    #     #You can find the path to the shortest unexplored room by using a breadth-first search for a room with a '?' for an exit. If you use the bfs code from the homework, you will need to make a few modifications.
    #     q = Queue()

    #     q.enqueue([starting_vertex])

    #     visited = set()

    #     while q.size() > 0:
    #         #dequeue the first path
    #         removed_path = q.dequeue() #['1']
    #         #grab last vertex value from the path
    #         last_vert = removed_path[len(removed_path) - 1] #'1'

    #         #if the vertex has not been visited:
    #         if last_vert not in visited:
    #             #if it is the destination_index:
    #             if last_vert == destination_vertex:
    #                 #return the path
    #                 return removed_path
    #             #mark it as visited
    #             visited.add(last_vert) ### visited = {'1'}

    #             #then add a path to its neighbors to the back of the queue
    #             neighbors = self.get_neighbors(last_vert) #returns set of neighbors = {'2','3'}
    #             print(neighbors)

    #             #create a list to store the path to all neighbors of current vertex
    #             neighbor_paths = []
    #             #loop through and make a list with path to all neighbors
    #             for i in range(len(neighbors)):
    #                 neighbor_list = list(neighbors) #['2', '3']

    #                 neighbor_paths.append(removed_path.copy()) #[['1'], ['1']]
    #                 neighbor_paths[i].append(neighbor_list[i]) 
    #                 print('neighbor paths', neighbor_paths)

    #             for path in neighbor_paths:
    #                 q.enqueue(path)



    #             #make a copy of the path
                
    #             #append the neighbor to the back of the path
    #             #enqueue out new path
            
    #     return None








            
    
        #travel and log that direction
            # self.travel(random_exit_direction)
            # traversal_path.append(random_exit_direction)
            # print('room', self.current_room.id)
            # print('path', traversal_path)

        # loops and keeps going that direction


        #TAKE ROOM AND ADD ALL NEIGHBORS TO STACK?
        #find neighbors like find exits here?


       













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



