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

            #checking if goal is in our neighbors or not
            for i in neighbors:
                if(i==s_goal):
                    self.PARENT[i] = current_state
                    reachedToGoal = True
            if(reachedToGoal):
                break
            
            #Add unvisited neighbors to open list
            
            for j in neighbors:
                if(not (j in self.CLOSED) and not (j in self.OPEN)):
                    self.OPEN.append(j)
                    #if(not (j in self.PARENT)):
                    self.PARENT[j] = current_state
                    visited.append(j)

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

        """visited = []
        reachedToGoal = False
        stack = []
        self.OPEN.append(s_start)


        while(reachedToGoal):"""
            

        

class AStar_Agent(AbstractSearchAgent):
    def searching(self):
        """
        DFS search algorithm
        
        Returns:
        * path (list): The planned path from start to goal

        * visted (list): list of visited nodes
        """

        # TODO

if __name__ == "__main__":
    s_start = (5, 5) # Starting point
    s_goal = (45, 25) # Goal

    FPS = 60
    generate_mode = False # Turn to True to change the map
    map_name = 'default'

    if generate_mode:
        gn.main(map_name)
    
    else:
        agent = BFS_Agent(s_start, s_goal, map_name) # Choose the agent here
        path, visited = agent.searching()

        # Plotting the path
        plot = Plotting(s_start, s_goal, map_name, FPS)

        plot.animation(path, visited)