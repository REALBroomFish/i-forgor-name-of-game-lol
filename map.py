rooms = {
    "Reception": {
        "Name": "Reception",
        "Description":
        """You are in a maze of twisty little passages, all alike.
        Next to you is the School of Computer Science and
        Informatics reception. The receptionist, Matt Strangis,
        seems to be playing an old school text-based adventure
        game on his computer. There are corridors leading to the
        south and east. The exit is to the west.""",
        "Exits": {"South": "Admins", "East": "Tutor", "West": "Parking"}},
    "Admins": {
        "Name": "MJ and Simon's room",
        "Description":
        """You are leaning agains the door of the systems managers'
        room. Inside you notice Matt "MJ" John and Simon Jones. They
        ignore you. To the north is the reception.""",
        "Exits": {"North": "Reception"}},
    "Tutor": {
        "Name": "your personal tutor's office",
        "Description":
        """You are in your personal tutor's office. He intently
        stares at his huge monitor, ignoring you completely.
        On the desk you notice a cup of coffee and an empty
        pack of biscuits. The reception is to the west.""",
        "Exits": {"West": "Reception"}},
    "Parking": {
        "Name": "the parking lot",
        "Description":
        """You are standing in the Queen's Buildings parking lot.
        You can go south to the COMSC reception, or east to the
        general office.""",
        "Exits": {"South": "Reception", "East": "Office"}},
    "Office": {
        "Name": "the general office",
        "Description":
        """You are standing next to the cashier's till at
        30-36 Newport Road. The cashier looks at you with hope
        in their eyes. If you go west you can return to the
        Queen's Buildings.""",
        "Exits": {"West": "Parking"}}
}






