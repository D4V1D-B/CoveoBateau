from json.encoder import INFINITY
from turtle import position
from game_message import Map, Tick, Action, Spawn, Sail, Dock, Anchor, directions
from python.test.game_message import Position
from queue import PriorityQueue

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
    for x in range(-1,1):
        for y in range(-1,1):
            if x is 0 and y is 0:
                continue
            liste.append((pos[0]-x, pos[0]-y))

    print('liste de neibor: ',liste)
    return liste



def getBoatposition():
    return [Tick.currentLocation.row, Tick.currentLocation.column]
    
def getPosNearestPort():
    liste = Tick.map.ports
    valeur = []
    for x in liste:
        print(x)
        valeur.append(h(getBoatposition, x))
        print("distance la plus proche",valeur)
        print("le port le plus proche ********",sorted(valeur[0]))

    
    return sorted(valeur[0])

def reconstruct_path(current, cameFrom):
    boat_pos = getBoatposition
    total_path = current
    for current in cameFrom:
        current = cameFrom[current]
        total_path.append(current)
    return total_path

def A_star(start, end, h):
    count = 0
    openSet = PriorityQueue()
    openSet.put((0, count, start))

    cameFrom = {}

    gScore = {Map: float("inf")}
    gScore[start] = 0

    fScore = {Map: float("inf")}
    fScore[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not openSet.empty():
        current = openSet.get()[2]
        open_set_hash.remove(current)

        if current ==  end:
            return reconstruct_path(cameFrom, current) # return path

        for  neighbor in current.neighbors:
            tentative_gScore = gScore[current] + 1

            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    openSet.put((fScore[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
    return False