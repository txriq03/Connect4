from classes.MainMenu import MenuOption
import sys
menuScreen: str = """
_________                                     __     _____  
\_   ___ \  ____   ____   ____   ____   _____/  |_  /  |  | 
/    \  \/ /  _ \ /    \ /    \_/ __ \_/ ___\   __\/   |  |_  
\     \___(  <_> )   |  \   |  \  ___/\  \___|  | /    ^   /
 \______  /\____/|___|  /___|  /\___  >\___  >__| \____   | 
        \/            \/     \/     \/     \/          |__| by Tariq Brown
        
1 - VsPlayer
2 - VsComputer
3 - Leaderboard
4 - Quit
"""

def loadMenu():
    print(menuScreen)

    while True:
        option = input("> ")
        choice = MenuOption.parse(option);

        if type(choice) == MenuOption:
            branchToFeature(choice)
        else:
            print("Please select a valid option.", file=sys.stderr)
            

def branchToFeature(opt: MenuOption):
    match opt:
        case MenuOption.VsComputer:
            print("VsComputer selected")
        case MenuOption.VsPlayer:
            print("VsPlayer selected")

        case MenuOption.Leaderboard:
            print("Leaderboard selected.")

        case MenuOption.Quit:
            print("Thank you for playing!")
            sys.exit()