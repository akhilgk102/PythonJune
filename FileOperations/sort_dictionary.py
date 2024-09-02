placements={"Django":35,"Flutter":40,"BigData":20,"Java":10}

def get_value(key):

    return placements.get(key)

srt=sorted(placements,key=get_value,reverse=True)

print(srt)