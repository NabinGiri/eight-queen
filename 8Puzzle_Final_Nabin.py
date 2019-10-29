#!/usr/bin/env python
# coding: utf-8

# In[107]:


import random
BOARD_SIZE = 4

goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ," "]
state1 = [7, ' ', 14, 4, 10, 5, 1, 11, 3, 12, 2, 15, 13, 6, 9, 8]
state2 = [5, 10, 14, 4, 7, 1, ' ', 11, 3, 12, 2, 15, 13, 6, 9, 8]
state3 = [12, 7, 14, 4, 10, 5, 1, ' ', 9, 13, 6, 11, 3, 2, 8, 15]
state4 = [' ', 5, 4, 15, 3, 14, 7, 12, 1, 10, 6, 11, 13, 9, 8, 2] 
state5 = [9, 10, 1, 15, 14, 4, 7, ' ', 3, 11, 12, 2, 5, 6, 8, 13] 
state6 = [13, 12, 7, ' ', 9, 4, 10, 1, 15, 2, 3, 14, 5, 8, 6, 11] 
state7 = [14, 9, 10, 15, ' ', 6, 4, 7, 11, 12, 1, 8, 3, 5, 13, 2] 
state8 = [' ', 9, 10, 15, 14, 11, 4, 7, 12, 6, 1, 8, 3, 5, 13, 2] 
state9 = [10, 12, 14, 4, ' ', 7, 11, 8, 9, 15, 6, 1, 3, 5, 13, 2] 
state10 = [9, ' ', 14, 7, 5, 12, 4, 3, 6, 15, 2, 1, 13, 8, 10, 11] 


if BOARD_SIZE == 3:
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, " "]
    state1 = [1, 2, " ", 5, 6, 3, 4, 7, 8]
    state2 = [5, 2, 7, " ", 3, 4, 6, 1, 8]
    state3 = [5, 2, 7, 4, 6, 8, 3, ' ', 1]
    state4 = [2, 4, 7, 5, 8, ' ', 3, 6, 1]
    state5 = [5, ' ', 7, 4, 2, 8, 3, 6, 1]
    state6 = [5, 2, 7, 3, 4, 8, 6, ' ', 1]
    state7 = [3, 1, 5, 6, 2, ' ', 4, 7, 8]
    state8 = [5, 6, 2, 4, 1, 7, ' ', 3, 8]
    state9 = [2, 4, 7, 5, 8, ' ', 3, 6, 1]
    state10 = [2, 7, 8, 5, 4, 1, 3, ' ', 6]


def show_state(state):
    for i in range(len(state)):
        print(state[i], end=" ")
        if i % BOARD_SIZE == BOARD_SIZE - 1 :
            print()
    print()



def get_possible_actions(state):
    # return a list of actions. subset of ["Left","Right","Up","Down"]
    # get the position of blank.
    # First index of the black. Next row, col of the blank
    actions = []
    blank_index = state.index(" ")
    r = blank_index // BOARD_SIZE
    c = blank_index % BOARD_SIZE
    if r > 0:
        actions.append("Up")
    if r < BOARD_SIZE - 1 :
        actions.append("Down")
    if c > 0:
        actions.append("Left")
    if c < BOARD_SIZE - 1:
        actions.append("Right")
    return actions

def update_state(state,action):
    # change the given state after taking the action
    blank_index = state.index(" ")
    if action == "Left":
        switch_index = blank_index - 1
    elif action == "Right":
        switch_index = blank_index + 1
    elif action == "Down":
        switch_index = blank_index + BOARD_SIZE
    elif action == "Up":
        switch_index = blank_index - BOARD_SIZE
    state[blank_index], state[switch_index] = state[switch_index], state[blank_index]

def random_shuffle(state,move_cnt):
    for i in range(move_cnt):
        action = random.choice(get_possible_actions(state))
        print("state = ",state)
        update_state(state,action)
    
def random_search(state):
    # change the given state until you arrive at the goal state
    move_count = 0
    while state != goal_state:
        random_action = random.choice(get_possible_actions(state))
        update_state(state,random_action)
        move_count += 1
        if move_count % 200000 == 0:
            print("Loop Count\t", move_count)
            show_state(state)
            
        #print(random_action)
        #show_state(state)
    print("Finished in {} steps.".format(move_count))

def expand(state):
    # return children states from the given state
    # For example
    # expand([1,2,3,4,5,6," ",7,8]) # possibles actions are ["Up", "Right"]
    #   returns [ [1,2,3," ",5,6,4,7,8], [1,2,3,4,5,6,7," ",8] ]
    successors = []
    for action in get_possible_actions(state):
        new_state = state[:]
        update_state(new_state,action)
        successors.append(new_state)
    return successors

def show_solution(node):
    path = [node[1]]
    while node[2]:
        node = node[2]
        path.append(node[1])
    path.reverse()
    print("The solutions is...")
    if len(path) < 10:
        for s in path:
            show_state(s)
    print("Finished in {} steps".format(len(path)-1))
        
def show_solution2(node):   # for AStar
    path = [node[3]]
    while node[-1]:
        node = node[-1]
        path.append(node[3])
    path.reverse()
    print("The solutions is...")
    if len(path) < 10:
        for s in path:
            show_state(s)
    print("Finished in {} steps".format(len(path)-1))
        
def BFS(initial_state): # Breadth-First Search
    # node is (cost, state, parent)
    visited_states = set()
    root_node = (0,initial_state,None)
    frontier = [root_node]
    loop_cnt = 0
    num_generated_nodes = 0 
    while frontier != []:
        loop_cnt += 1
        node = frontier.pop(0)
        if node[1] == goal_state or loop_cnt % 250000 == 0: #keeping fixed loop count for 4X4 matrix board
            print("BFS\nLoop Count:\t",loop_cnt,"\nGenerated Nodes:",num_generated_nodes,"\nVisited Nodes:\t" ,len(visited_states)) #printing once the fixed loop count is reached.
            if node[1] == goal_state:
                show_solution(node)
                print(loop_cnt, num_generated_nodes, len(visited_states))
            return
        # expand the state. add the successor to the frontier
        successors = expand(node[1])
        for succ in successors:
            if tuple(succ) not in visited_states:
                visited_states.add(tuple(succ))
                new_node = (node[0]+1, succ, node)
                frontier.append(new_node)
            num_generated_nodes += 1

def DFS(initial_state): # Depth-First Search
    # node is (cost, state, parent)
    visited_states = set()
    root_node = (0,initial_state,None)
    frontier = [root_node]
    loop_cnt = 0
    num_generated_nodes = 0 
    while frontier != []:
        loop_cnt += 1
        node = frontier.pop(0)
        if node[1] == goal_state or loop_cnt % 250000 == 0: #keeping fixed loop count for 4X4 matrix board
            print("DFS\nLoop Count:\t",loop_cnt,"\nGenerated Nodes:",num_generated_nodes,"\nVisited Nodes:\t" ,len(visited_states)) #printing once the fixed loop count is reached.
            if node[1] == goal_state:
                show_solution(node)
                print(loop_cnt, num_generated_nodes, len(visited_states))
            return
        # expand the state. add the successor to the frontier
        successors = expand(node[1])
        for succ in successors:
            if tuple(succ) not in visited_states:
                visited_states.add(tuple(succ))
                new_node = (node[0]+1, succ, node)
                frontier.insert(0,new_node)
            num_generated_nodes += 1


def DFS_limited(initial_state, max_depth): # Depth-First Search

        #max_depth = 20
        visited_states = {}
        root_node = (0,initial_state,None) #cost is zero at first , our state is first so its initial, we donot have any parent now.
        frontier = [root_node]
        loop_cnt = 0
        num_generated_nodes = 0 
        while frontier != []:
            loop_cnt += 1
            node = frontier.pop(0)
            if node[1] == goal_state:
                show_solution(node)
                return True
            
            if max_depth == 0:
                return "Depth Cannot be zero"
                return True
            
            if node[0] < max_depth:
                successors = expand(node[1]) # expand the state. add the successor to the frontier 
                for succ in successors:
                    if tuple(succ) not in visited_states or node[0] < visited_states[tuple(succ)]:
                        visited_states.update({tuple(succ) : node [0]})
                        new_node = (node[0]+1, succ, node)
                        frontier.insert(0,new_node)
                    else:
                        return False
        print(loop_cnt, num_generated_nodes, len(visited_states))
        
    # similar to DFS but does not go deeper than max_depth

    # visited_states need to keep cost for each state.  
    # eg) visited_states = {} # set of (k,v) pairs. k is tuple(board), v is cost 
    # if a generated states is in the visited_states, but if it has smaller cost
    # then still add a node of the board while updating the cost in visited_states.
	
    # It is possible to fail to find solution. Return False when it fails, True when succeed.
   # pass # replace this line with your code

def DFS_iterative_deepening(initial_state):
    max_depth = 1
    result = False
    while(not result):
        result = DFS_limited(initial_state, max_depth)
        max_depth += 1
        
    # Call DFS_limited multiple times until it succeed.
    # Begin with max_depth = 1 and increase it by one 
    # Refer to the pseudo code in page 89 of the textbook.
    pass # replace this line with your code

def heuristic(state):
    count = 0;
    for i in range(len(state)):
##       if state[i] != " " and i!=state[i]-1:
        if state[i] != goal_state[i]:
           count += 1            
    return count

import time 
from heapq import *
def AStar(initial_state):
    # node is (g+h,h,time.perf_counter(),state, parent)
    visited_states = {}
    h = heuristic(initial_state)
    root_node = (0+h,h,time.perf_counter(),initial_state,None)
    frontier = [root_node]
    loop_cnt = 0
    num_generated_nodes = 0 
    while frontier != []:
        loop_cnt += 1
        node = heappop(frontier)
        if node[3] == goal_state or loop_cnt % 250000 == 0: #keeping fixed loop count for 4X4 matrix board
            print("AStar\nLoop Count:\t",loop_cnt,"\nGenerated Nodes:",num_generated_nodes,"\nVisited Nodes:\t" ,len(visited_states)) #printing once the fixed loop count is reached.
            if node[3] == goal_state:
                show_solution2(node)
                print(loop_cnt, num_generated_nodes, len(visited_states))
            return
        # expand the state. add the successor to the frontier
        successors = expand(node[3])
        for succ in successors:
            h = heuristic(succ)
            node_g = node[0]-node[1]
            g = node_g + 1
            if tuple(succ) not in visited_states or g+h < visited_states[tuple(succ)]:
                visited_states[tuple(succ)] = g + h
                new_node = (g+h,h, time.perf_counter(), succ, node)
##                frontier.append(new_node)
##                heapify(frontier)
                heappush(frontier,new_node)
            num_generated_nodes += 1

#print(heuristic([1,2,3,4,5," ",6,7,8]))
   
#print(expand([1,2,3,4," ", 5,6,7,8]))
#state1 = goal_state[:]
#random_shuffle(state7,550)
#show_state(state1)
#random_search(state10)
#BFS(state2)
#DFS(state2)
#AStar(state2)
#DFS_limited(state10,20)
DFS_iterative_deepening(state2)
#print(get_possible_actions(state1))
#update_state(state1,"Up")
#random_search(state3)
#show_state(state1)

#show_state(state1)


# In[ ]:





# In[ ]:




