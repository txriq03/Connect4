from enum import Enum
from typing import Optional

class MenuOption(Enum):
    VsComputer = 1
    VsPlayer = 2
    Leaderboard = 3
    Quit = 4

    @staticmethod
    def parse(opt: str) -> Optional['MenuOption']:
        match opt.lower():
            case "1":
                return MenuOption.VsComputer
            case "2":
                return MenuOption.VsPlayer
            case "3":
                return MenuOption.Leaderboard
            case "4" | "q":
                return MenuOption.Quit


