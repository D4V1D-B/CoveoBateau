from game_message import Map, Tick, Action, Spawn, Sail, Dock, Anchor, directions
from python.test.game_message import Position

class Bot:
    def __init__(self):
        #spawn dans une postion optimiser
        print("Initializing your super mega duper bot")
        
    def get_next_move(self, tick: Tick) -> Action:
        """
        Here is where the magic happens, for now the move is random. I bet you can do better ;)
        """
        if tick.currentLocation is None:
            return Spawn(tick.map.ports[0])
        
        return Sail(directions[tick.currentTick % len(directions)])


    #la carte est de 60 pixel par 60 pixel
    def getPosition(self):
        return (Position.row, Position.column)
    
    def pathFinding(self,start, goal, h):
        return None

    def euclidienne(self):
        liste = Map.ports
        print(liste)

        return (x, y)
