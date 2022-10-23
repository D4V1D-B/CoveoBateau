from json.encoder import INFINITY
from turtle import position
from game_message import Map, Tick, Action, Spawn, Sail, Dock, Anchor, directions
from python.test.game_message import Position

class Bot:
    def __init__(self):
        #spawn dans une postion optimiser
        getListeNodeAutour
    
        
    def get_next_move(self, tick: Tick) -> Action:
        """
        Here is where the magic happens, for now the move is random. I bet you can do better ;)
        """
        if tick.currentLocation is None:
            return Spawn(tick.map.ports[0])
        
        return Sail(directions[tick.currentTick % len(directions)])


    #la carte est de 60 pixel par 60 pixel
def h(start, end):
    return ((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5

def getMapTopo():
    return Map.topology

def getListeNodeAutour():
    liste = []
    pos = getBoatposition()
    liste.append((pos[0]-1, pos[0]-1))
    liste.append((pos[0]-1, pos[0]))
    liste.append((pos[0]-1, pos[0]+1))
    liste.append((pos[0], pos[0]+1))
    liste.append((pos[0], pos[0]-1))
    liste.append((pos[0]+1, pos[0]+1))
    liste.append((pos[0]+1, pos[0]))
    liste.append((pos[0]+1, pos[0]-1))
    print(liste)
    return liste



def getBoatposition():
    return [Tick.currentLocation.row, Tick.currentLocation.column]
    
def reconstruct_path(getBoatposition, current):
    boat_pos = getBoatposition
    total_path = current
    for current in cameFrom:
        current = cameFrom[current]
        total_path += current
    return total_path

def A_star(start, goal, h):
    
    openSet = Tick.currentLocation
    
    cameFrom = 'idk' #EmptyMAp

    gScore = map with default value of INFINITY
    gScore(Tick.currentLocation)

    fScore := map with default value of Infinity
    fScore[start] := h(start)

    while openSet is not empty
        current := the node in openSet having the lowest fScore[] value
        if current ==  goal:
            return reconstruct_path(cameFrom, current)

        openSet.Remove(current)
        for each neighbor of current
           
            tentative_gScore = gScore[current] + d(current, neighbor)
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] := current
                gScore[neighbor] := tentative_gScore
                fScore[neighbor] := tentative_gScore + h(neighbor)
                if neighbor not in openSet
                    openSet.add(neighbor)
        openSet.isEmpty