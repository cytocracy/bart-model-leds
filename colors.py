

colors = {}

colors["black"] = "\033[30m"
colors["red"] = "\033[31m"
colors["green"] = "\033[32m"
colors["orange"] = "\033[33m"
colors["blue"] = "\033[34m"
colors["purple"] = "\033[35m"
colors["cyan"] = "\033[36m"
colors["white"] = "\033[37m"
colors["darkgrey"] = "\033[90m"
colors["lightred"] = "\033[91m"
colors["lightgreen"] = "\033[92m"
colors["yellow"] = "\033[93m"
colors["lightblue"] = "\033[94m"
colors["pink"] = "\033[95m"
colors["lightcyan"] = "\033[96m"
    
def get_color(color):
    return colors[color]
