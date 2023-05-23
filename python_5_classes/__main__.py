from menu import *
from character import *
# from vehicule import *
# from rules import *
# from track import *

menu_principal = MK_menu()

menu_principal.opening(menu_principal) 

user_character = character("", 0,0,0,0,0)
user_character.character_select()

print(user_character.name)