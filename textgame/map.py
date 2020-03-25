import scenes

class Map(object):
    #These are all of the different traversible scenes
    scenes = {
        'death': scenes.Death(),
        'tavern': scenes.Tavern(),
        'town_center': scenes.TownCenter(),
        'general_store': scenes.GeneralStore(),
        'trader_wagon': scenes.TraderWagon(),
        'road_out_of_town': scenes.RoadOutOfTown(),
        'gloomy_forest': scenes.GloomyForest(),



    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    #handles what next scene will be
    def change_scene(self, scene_name):
        new_scene = Map.scenes.get(scene_name)
        return new_scene

    #handles what the opening scene is
    def opening_scene(self):
        return self.change_scene(self.start_scene)
