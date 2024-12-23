
class Footbalist:

    def __init__(self, first_name, last_name, weight ,  height , number ):
        
        self.first_name = first_name

        self.last_name = last_name

        self.number = number

        self.height = height

        self.weight = weight


    def player_first_number(self):
        return('The player first name: '+ self.first_name)
    
   
class Goalkeeper(Footbalist):
    pass


class Defenders(Footbalist):
    pass


player1 = Footbalist('Mohammad ' , 'Maleki' , 98 , 190 , 1)

player2 = Goalkeeper('Amir ' , 'Kheyri' , 77 , 171 , 2)

player3 = Defenders('Mehdi ' , 'Zamani' , 75 , 170 , 3)

player4 = Defenders('Mohammad ' , 'Mahmodi' , 180 , 190 , 4)

print(player1.player_first_number())
