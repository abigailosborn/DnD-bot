import random 

#Roll all of the dice, wooo
class dice_rolls:
    #roll d4
    def d_four():
        return random.randint(1, 4)
    #roll d6
    def d_six():
        return random.randint(1, 6)
    #roll d8
    def d_eight():
        return random.randint(1, 8)
    #roll d10
    def d_ten():
        return random.randint(1, 10)
    #roll d12
    def d_twelve():
        return random.randint(1, 12)
    #roll d20
    def d_twenty():
        return random.randint(1, 20)
    #roll d100
    def d_hundred():
        return random.randint(1, 100)

class character:

    def gen_names():
        first_name = random.choice(open(".names.txt").readlines())
        last_name = random.choice(open(".names.txt").readlines())
        name = first_name.strip() + " " + last_name.strip()
        return name
    
    def gen_stats():
        stat = random.randint(3, 18)
        return stat
    
    def gen_class():
        dnd_class = random.choice(open(".classes.txt").readlines())
        return dnd_class.strip()
    
    def gen_race():
        race = random.choice(open(".races.txt").readlines())
        return race.strip()
