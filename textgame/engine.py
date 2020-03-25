import scenes

#Engine for the game - makes the game "go"
class Engine(object):

    def __init__(self, scene_map, character):
        self.scene_map = scene_map
        self.character = character

    def play(self, character):
        """This method starts the game, and continues running it until game_over is met."""
        #enter opening scene - tavern
        current_scene = self.scene_map.opening_scene()
        game_over = self.scene_map.change_scene('death')

        #If you haven't died, go to user specified scene
        while current_scene != game_over:
            new_scene_name = current_scene.enter(character)
            current_scene = self.scene_map.change_scene(new_scene_name)
