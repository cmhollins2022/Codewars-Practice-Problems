# First way...
# def are_you_playing_banjo(name: str):
#     if name.capitalize()[0] == "R":
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"
    
def are_you_playing_banjo(name: str):
    if name[0] == "r" or name[0] == "R":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
      
# Alternatively... 
def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"
