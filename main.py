import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/utils")

from agent import AbstractSearchAgent
from plotting import Plotting
import generator as gn

class BFS_Agent(AbstractSearchAgent):
    def searching(self):
        
        """
        BFS search algorithm
        
        Returns:
        * path (list): The planned path from start to goal

        * visted (list): list of visited nodes
        """
        visited = []
        reachedToGoal = False
        self.OPEN.append(s_start)

        while(not (reachedToGoal)):
            current_state = self.OPEN[0]
            neighbors = self.get_neighbor(current_state)
            
            for i in neighbors:

                #checking if goal is in our neighbors or not
                if(i==s_goal):
                    self.PARENT[i] = current_state
                    reachedToGoal = True

                #Add unvisited neighbors to open list
                if(not (i in self.CLOSED) and not (i in self.OPEN)):
                    self.OPEN.append(i)
                    #if(not (i in self.PARENT)):
                    self.PARENT[i] = current_state
                    visited.append(i)

            if(reachedToGoal):
                break

            self.CLOSED.append(current_state)
            self.OPEN.remove(current_state)
        
        
        return self.extract_path(self.PARENT),visited




            
            
        

class DFS_Agent(AbstractSearchAgent):
    def searching(self):

        """
        DFS search algorithm
        
        Returns:
        * path (list): The planned path from start to goal

        * visted (list): list of visited nodes
        """

        visited = []
        reachedToGoal = False
        self.OPEN.append(s_start)

        while(not (reachedToGoal)):
            current_state = self.OPEN.pop()
            self.CLOSED.append(current_state)
            visited.append(current_state)

            neighbors = self.get_neighbor(current_state)
            for i in neighbors:
                if(i==s_goal):
                    self.PARENT[i] = current_state
                    reachedToGoal = True
             
                if(not (i in self.CLOSED) and not (i in self.OPEN)):
                    self.OPEN.append(i)
                    self.PARENT[i] = current_state

            if(reachedToGoal):
                print(self.PARENT)
                break

            


        return self.extract_path(self.PARENT),visited

            






            

        

class AStar_Agent(AbstractSearchAgent):
    def searching(self):
        """
        DFS search algorithm
        
        Returns:
        * path (list): The planned path from start to goal

        * visted (list): list of visited nodes
        """

        visited = []
        realCosts = dict()
        self.OPEN.append(s_start)
        realCosts[s_start] = 0
        minAnswerCost = 10000


        while(True):
            minCost = 10000
            #Choosing best option from open list
            for i in self.OPEN:
                #if((realCosts[i] + max(abs(s_goal[0]-i[0]),abs(s_goal[1]-i[1]))) < minCost):
                if((realCosts[i] + abs(s_goal[0]-i[0]) + abs(s_goal[1]-i[1])) < minCost):
                    #minCost = realCosts[i] + max(abs(s_goal[0]-i[0]),abs(s_goal[1]-i[1]))
                    minCost = (realCosts[i] + abs(s_goal[0]-i[0]) + abs(s_goal[1]-i[1]))
                    current_state = i
            
            if(minCost > minAnswerCost):
                break
                    
            
            visited.append(current_state)
                    
            if(current_state == s_goal and realCosts[current_state] < minAnswerCost):
                
                minAnswerCost = realCosts[current_state]
                    
            neighbors = self.get_neighbor(current_state)
            
            for j in neighbors:
                if(not (j in self.CLOSED) ):
                    if(j in self.OPEN and realCosts[j]>realCosts[current_state]+1):
                        self.PARENT[j] = current_state
                        if(abs(current_state[0]-j[0])+abs(current_state[1]-j[1])==1):
                            realCosts[j] = realCosts[current_state]+1.00
                        else:
                            realCosts[j] = realCosts[current_state]+1.4142
                    elif(not (j in self.OPEN)):
                        self.OPEN.append(j)
                    if(not (j in self.PARENT) or realCosts[j]>realCosts[current_state]+1):
                        self.PARENT[j] = current_state
                        if(abs(current_state[0]-j[0])+abs(current_state[1]-j[1])==1):
                            realCosts[j] = realCosts[current_state]+1.00
                        else:
                            realCosts[j] = realCosts[current_state]+1.4142
            
            self.OPEN.remove(current_state)
            self.CLOSED.append(current_state)

        print(realCosts[s_goal])
                        
        return self.extract_path(self.PARENT),visited
                    
                



if __name__ == "__main__":
    s_start = (5, 5) # Starting point
    s_goal = (45, 25) # Goal

    FPS = 60
    generate_mode = False # Turn to True to change the map
    map_name = 'default'

    if generate_mode:
        gn.main(map_name)
    
    else:
        agent = AStar_Agent(s_start, s_goal, map_name) # Choose the agent here
        path, visited = agent.searching()

        # Plotting the path
        plot = Plotting(s_start, s_goal, map_name, FPS)

        plot.animation(path, visited)