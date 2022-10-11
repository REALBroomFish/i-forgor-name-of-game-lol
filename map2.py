def init():    
    places = []
    places.append({"Type" : "START", "Name": "Reception", "Connects_to": {"Parking": "West", "Tutor": "East", "MJ & Simon": "South"}, 
        "Desc": """You are in a maze of twisty little passages, all alike.
                Next to you is the School of Computer Science and
                Informatics reception. The receptionist, Matt Strangis,
                seems to be playing an old school text-based adventure
                game on his computer. There are corridors leading to the
                south and east. The exit is to the west."""})
   
    places.append({"Type" : "Connect", "Name": "Parking", "Connects_to": {"Reception": "South", "General Office": "East"}, 
        "Desc": """You are standing in the Queen's Buildings parking lot.
                You can go south to the COMSC reception, or east to the
                general office."""})
   
    places.append({"Type" : "Connect", "Name": "General Office", "Connects_to": {"Parking": "West"}, 
        "Desc": """You are standing next to the cashier's till at
                30-36 Newport Road. The cashier looks at you with hope
                in their eyes. If you go west you can return to the
                Queen's Buildings."""})
   
    places.append({"Type" : "Connect", "Name": "MJ & Simon", "Connects_to": {"Reception": "North"}, 
        "Desc": """You are leaning agains the door of the systems managers'
                room. Inside you notice Matt "MJ" John and Simon Jones. They
                ignore you. To the north is the reception."""})
   
    places.append({"Type" : "Connect", "Name": "Tutor", "Connects_to": {"Reception": "West"}, 
        "Desc": """You are in your personal tutor's office. He intently
                stares at his huge monitor, ignoring you completely.
                On the desk you notice a cup of coffee and an empty
                pack of biscuits. The reception is to the west."""})


def dont_init():
    # runs through every item in the "places" array
    start_found = False
    start_pos = (5,5)
    for pos in range(0, len(places)-1):
        #initialises start item
        if places[pos]["Type"] == "START" and not start_found:
            places[pos]["Position"] == start_pos
            x, y = start_pos
            start_found = True
        elif places[pos]["Type"] == "START" and start_found:
            print("Multiple starts found... closing game.")
            quit()
    if not start_found:
        print("ERROR: START not found. please fix... closing game...")
        quit()
        
    for pos in range(0, len(places)-1):
        # checks every connection per item
        for connection in places[pos]["Connects_to"]:
            #lil bit of clarification, this line underneath gets the name of the PLACE/connection between the current position and one of the connections, say reception and parking (would return parking)
            place = places[pos]["Connects_to"][connection]
            print(place)
            # then checks against the 4 cardinal points and increments the original coordinates based on that.#
            print(connection)
            if places[pos]["Connects_to"][connection] == "North":
                y += 1
            elif places[pos]["Connects_to"][connection] == "East":
                x += 1
            elif places[pos]["Connects_to"][connection] == "South":
                y -= 1
            elif places[pos]["Connects_to"][connection] == "West":
                x -= 1
            print("(" + str(x) + ", " + str(y) + ")")
            MAP_NAME = places[pos]["Map_Name"][connection]
            # then places the item at the position in question
            map[x][y] = MAP_NAME

    for row in map:
        print(str(row))