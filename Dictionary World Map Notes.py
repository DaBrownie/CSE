world_map = {
    'WESTHOUSE' : {
        'NAME' : "West of House",
        'DESCRIPTION' : "You are west of a white house",
        'PATHS' : {
            'NORTH' : "NORTHHOUSE",
            'SOUTH' : 'SOUTHHOUSE',
        }
    },
    'NORTHHOUSE' : {
        'NAME' : "North of House",
        'DESCRIPTION' : "Insert description here",
        'PATHS' : {
            'NORTH' : 'WESTHOUSE',
        }
    },
    'SOUTHHOUSE' : {
        'NAME' : "South of House",
        'DESCRIPTION' : "Insert description here",
        'PATHS' : {
            'NORTH' : 'WESTHOUSE',
        }
    }
}

current_node = world_map['WESTHOUSE']
pr