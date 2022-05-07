class constants:
    # num leds
    num_leds = 60
    
    class colors:
        red = (255, 0, 0)
        blue = (0, 0, 255)
        yellow = (255, 255, 0)
        green = (0, 255, 0)
        orange = (255, 165, 0)

    class keys:
        stations_north = {}
        stations_south = {}
        stations_north['12TH'] = 0
        stations_north['16TH'] = 0
        stations_north['19TH'] = 0
        stations_north['24TH'] = 0
        stations_north['ANTC'] = 0
        stations_north['ASHB'] = 0
        stations_north['BALB'] = 0
        stations_north['BAYF'] = 0
        stations_north['BERY'] = 0
        stations_north['CAST'] = 0
        stations_north['CIVC'] = 0
        stations_north['COLS'] = 0
        stations_north['COLM'] = 0
        stations_north['CONC'] = 0
        stations_north['DALY'] = 0
        stations_north['DBRK'] = 0
        stations_north['DUBL'] = 0
        stations_north['DELN'] = 0
        stations_north['PLZA'] = 0
        stations_north['EMBR'] = 0
        stations_north['FRMT'] = 0
        stations_north['FTVL'] = 0
        stations_north['GLEN'] = 0
        stations_north['HAYW'] = 0
        stations_north['LAFY'] = 0
        stations_north['LAKE'] = 0
        stations_north['MCAR'] = 0
        stations_north['MLBR'] = 0
        stations_north['MLPT'] = 0
        stations_north['MONT'] = 0
        stations_north['NBRK'] = 0
        stations_north['NCON'] = 0
        stations_north['OAKL'] = 0
        stations_north['ORIN'] = 0
        stations_north['PITT'] = 0
        stations_north['PCTR'] = 0
        stations_north['PHIL'] = 0
        stations_north['POWL'] = 0
        stations_north['RICH'] = 0
        stations_north['ROCK'] = 0
        stations_north['SBRN'] = 0
        stations_north['SFIA'] = 0
        stations_north['SANL'] = 0
        stations_north['SHAY'] = 0
        stations_north['SSAN'] = 0
        stations_north['UCTY'] = 0
        stations_north['WCRK'] = 0
        stations_north['WARM'] = 0
        stations_north['WDUB'] = 0
        stations_north['WOAK'] = 0
        stations_north['12TH'] = 0
        
        stations_south['16TH'] = 0
        stations_south['19TH'] = 0
        stations_south['24TH'] = 0
        stations_south['ANTC'] = 0
        stations_south['ASHB'] = 0
        stations_south['BALB'] = 0
        stations_south['BAYF'] = 0
        stations_south['BERY'] = 0
        stations_south['CAST'] = 0
        stations_south['CIVC'] = 0
        stations_south['COLS'] = 0
        stations_south['COLM'] = 0
        stations_south['CONC'] = 0
        stations_south['DALY'] = 0
        stations_south['DBRK'] = 0
        stations_south['DUBL'] = 0
        stations_south['DELN'] = 0
        stations_south['PLZA'] = 0
        stations_south['EMBR'] = 0
        stations_south['FRMT'] = 0
        stations_south['FTVL'] = 0
        stations_south['GLEN'] = 0
        stations_south['HAYW'] = 0
        stations_south['LAFY'] = 0
        stations_south['LAKE'] = 0
        stations_south['MCAR'] = 0
        stations_south['MLBR'] = 0
        stations_south['MLPT'] = 0
        stations_south['MONT'] = 0
        stations_south['NBRK'] = 0
        stations_south['NCON'] = 0
        stations_south['OAKL'] = 0
        stations_south['ORIN'] = 0
        stations_south['PITT'] = 0
        stations_south['PCTR'] = 0
        stations_south['PHIL'] = 0
        stations_south['POWL'] = 0
        stations_south['RICH'] = 0
        stations_south['ROCK'] = 0
        stations_south['SBRN'] = 0
        stations_south['SFIA'] = 0
        stations_south['SANL'] = 0
        stations_south['SHAY'] = 0
        stations_south['SSAN'] = 0
        stations_south['UCTY'] = 0
        stations_south['WCRK'] = 0
        stations_south['WARM'] = 0
        stations_south['WDUB'] = 0
        stations_south['WOAK'] = 0
        
        def getStation(key, is_north):
            if is_north == True:
                return constants.keys.stations_north[key]
            else:
                return constants.keys.stations_south[key]
