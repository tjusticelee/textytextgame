import engine
import map
import character

user_character = character.Character()
new_map = map.Map('tavern')
new_game = engine.Engine(new_map, user_character)
new_game.play(user_character)
