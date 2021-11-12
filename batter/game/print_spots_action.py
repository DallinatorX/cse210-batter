from game.action import Action

class Print_Spots(Action):
    
    def execute(self, cast):
        for group in cast.values():
            for temp in group:
                print (temp.get_position())
