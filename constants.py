
# num leds
num_leds = 60
red_line = 0
orange_line = 1
green_line = 2
blue_line = 3
yellow_line = 4


red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
orange = (255, 165, 0)

def get_color(color):
    if color == 'red':
        return red
    elif color == 'blue':
        return blue
    elif color == 'yellow':
        return yellow
    elif color == 'green':
        return green
    elif color == 'orange':
        return orange

stations_north = {}
stations_south = {}
stations_north['12TH'] = 0
stations_north['16TH'] = 1
stations_north['19TH'] = 2
stations_north['24TH'] = 3
stations_north['ANTC'] = 4
stations_north['ASHB'] = 5
stations_north['BALB'] = 6
stations_north['BAYF'] = 7
stations_north['BERY'] = 8
stations_north['CAST'] = 9
stations_north['CIVC'] = 10
stations_north['COLS'] = 11
stations_north['COLM'] = 12
stations_north['CONC'] = 13
stations_north['DALY'] = 14
stations_north['DBRK'] = 15
stations_north['DUBL'] = 16
stations_north['DELN'] = 17
stations_north['PLZA'] = 18
stations_north['EMBR'] = 19
stations_north['FRMT'] = 20
stations_north['FTVL'] = 21
stations_north['GLEN'] = 22
stations_north['HAYW'] = 23
stations_north['LAFY'] = 24
stations_north['LAKE'] = 25
stations_north['MCAR'] = 26
stations_north['MLBR'] = 27
stations_north['MLPT'] = 28
stations_north['MONT'] = 29
stations_north['NBRK'] = 30
stations_north['NCON'] = 31
stations_north['OAKL'] = 32
stations_north['ORIN'] = 33
stations_north['PITT'] = 34
stations_north['PCTR'] = 35
stations_north['PHIL'] = 36
stations_north['POWL'] = 37
stations_north['RICH'] = 38
stations_north['ROCK'] = 39
stations_north['SBRN'] = 40
stations_north['SFIA'] = 41
stations_north['SANL'] = 42
stations_north['SHAY'] = 43
stations_north['SSAN'] = 44
stations_north['UCTY'] = 45
stations_north['WCRK'] = 46
stations_north['WARM'] = 47
stations_north['WDUB'] = 48
stations_north['WOAK'] = 49

stations_south['16TH'] = 50
stations_south['19TH'] = 51
stations_south['24TH'] = 52
stations_south['ANTC'] = 53
stations_south['ASHB'] = 54
stations_south['BALB'] = 55
stations_south['BAYF'] = 56
stations_south['BERY'] = 57
stations_south['CAST'] = 58
stations_south['CIVC'] = 59
stations_south['COLS'] = 60
stations_south['COLM'] = 61
stations_south['CONC'] = 62
stations_south['DALY'] = 63
stations_south['DBRK'] = 64
stations_south['DUBL'] = 65
stations_south['DELN'] = 66
stations_south['PLZA'] = 67
stations_south['EMBR'] = 68
stations_south['FRMT'] = 69
stations_south['FTVL'] = 70
stations_south['GLEN'] = 71
stations_south['HAYW'] = 72
stations_south['LAFY'] = 73
stations_south['LAKE'] = 74
stations_south['MCAR'] = 75
stations_south['MLBR'] = 76
stations_south['MLPT'] = 77
stations_south['MONT'] = 78
stations_south['NBRK'] = 79
stations_south['NCON'] = 80
stations_south['OAKL'] = 81
stations_south['ORIN'] = 82
stations_south['PITT'] = 83
stations_south['PCTR'] = 84
stations_south['PHIL'] = 85
stations_south['POWL'] = 86
stations_south['RICH'] = 87
stations_south['ROCK'] = 88
stations_south['SBRN'] = 89
stations_south['SFIA'] = 90
stations_south['SANL'] = 91
stations_south['SHAY'] = 92
stations_south['SSAN'] = 93
stations_south['UCTY'] = 94
stations_south['WCRK'] = 95
stations_south['WARM'] = 96
stations_south['WDUB'] = 97
stations_south['WOAK'] = 98
stations_south['12TH'] = 99


def get_station(key, direction):
    if direction == "North":
        return stations_north[key]
    else:
        return stations_south[key]
