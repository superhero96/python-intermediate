class dog:
    #class attributies
    num_of_legs = 4

    def __init__(self, name, color, breed):
        self.name = name
        self.color = color  
        self.breed = breed



class parrot:
    #class attributies
    num_of_legs = 2

    def __init__(self, name, color, beak_color):
        self.name = name
        self.color = color 
        self.beak_color = beak_color 




#creating instances of a dog class
tommy = dog('tommy' , 'black' , 'labordor')
rudlof = dog('rudlof', 'white', 'german Sheperd')
print(f'tommy has {tommy.num_of_legs} legs it is{tommy.color} in color and its breed is {tommy.breed}')
print(f'tommy has {rudlof.num_of_legs} legs it is{rudlof.color} in color and its breed is {rudlof.breed}')
#creatinginstances of a parrot class
charlie = parrot('charlie', 'green', 'red')
print(f'charlie has {charlie.num_of_legs} legs it is{charlie.color} in color and its beak_color is {charlie.beak_color}')