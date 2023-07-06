# The Ever-Changing Ankara: You are a fashion designer known for your unique and vibarnt Ankara designs.
# // Recently, you've discovered that some of your fabric patterns change their designs based on the 
# // temperature and mood of the WebGLVertexArrayObject. You want to craete a software application that 
# // can predict the changes in the fabric design given changing Ankara and how to predict the changes.
# class AnkaraFabric:
#     def __init__(self,pattern,temperature,mood):
#          self.pattern=pattern
#          self.temperature=temperature
#          self.mood=mood
# class WearerData:
#      def __init__(self,mood,temperature):
#           self.mood=mood
#           self.temperature=temperature
# class Design_Predict:
#      def predict_change_of_design(self,mood_of_wearer):
#           self.mood_of_wearer=mood_of_wearer

class AnkaraFabric:
     def __init__(self,mood,temperature):
          self.mood=mood
          self.temperature=temperature
     def predict_design(self,design):
          if self.temperature in range(5,25) and self.mood=="happy":
               return f"Pattern changes to {design}"
          elif self.temperature in range(30,40) and self.mood=="sad":
               return f"pattern changes to {design}"
          else:
               return f"pattern to none"
     # instances
     designs=AnkaraFabric("happy","floral","20")
     designs.predict_design("dotted")

     

# // The Great Migration Forecast:Every year , millions of wildebeest, zebras, and other animals participate 
# // in the Great Migration across the Serengeti-Mara ecosystem.As a conservationist, you want to develop 
# // a software system that models this migartion, predicting the movement of the herds based on weather
# // patterns, river levels, and predator locations. Consider what classes you will need to represent the 
# // animals, the environment, and the various factors that influence the migration.
# class Animal:
#      def __init__(self,name,species,location):
#           self.name=name
#           self.species=species
#           self.location=location
# class Environment:
#      def __init__(self,river_level,predator_locations,weather_patterns):
#           self.river_level=river_level
#           self.predator_locations=predator_locations
#           self.weather_patterns=weather_patterns
# class Migration:
#      def predict_migration(self,environment):
#           self.environment=environment

class Migration:
    def __init__(self,weather,river_level,preditor_location):
        self.weather=weather
        self.river_level = river_level
        self.preditor_location = preditor_location
    def predict_location(self):
        river_level_in_fts = 200
        curret_weather = "rainy"
        if self.weather == curret_weather and self.river_level > river_level_in_fts:
            return "The great migration will not occur"
        else:
            return "The great migration wil occur"
    def new_location(self,currrent_location):
        current_location="serengeti"
        return f"The migration will occur from ${self.preditor_location} to ${self.current_location}"
    
    # migration = Migration("rainy",300,"Maasai mara")
    # print(migration.predict_location())
    # print(migration.new_location("Serengeti"))
# // Nollywood Movie Planner:As a producer in the booming Nollywood movie industry, you are in charge of 
# // multiple film projects at once. Each movie has different cast members, shooting schedules, and budgets.
# // You want to write a program to help manage your film projects efficiently. The software should be able 
# // to handle the complexities of sceduling, budgeting and cordinating between different movie projects.  
class cast_members:
     def __init__(self,name,role,age):
          self.name=name
          self.role=role
          self.age=age
class movie_project:
     def __init__(self,project_name,cast_members,budget,shooting_schedule):
          self.project_name=project_name
          self.cast_members=cast_members
          self.budget=budget
          self.shooting_schedule=shooting_schedule
class Budget:
     def __init__(self,production_cost,marketing):
          self.production_cost=production_cost
          self.marketing=marketing
class Shooting_schedule:
     def __init__(self,dates,venues):
          self.dates=dates
          self.venues=venues
# // The Magical Baobab:In a small village, there is a Baobab tree believed to have magical properties. 
# // Every season, it bears different types of fruits, each with its own unique power. Yo have decided 
# // to create a software system that tracks the changes in the tree and predicts what type of fruit 
# // it will bear next season and what powers it will posses. The system shold also record the effect 
# // of each fruit when consumed. 
# class Baobab_tree:
#     def __init__(self):
#           self.season=[]
#     def every_season(self,season):
#          self.seasons.append(season)
#     def predict_next_season(self):

# class Season:
#     def __init__(self,fruits):
#           self.fruits=fruits
# class fruit:
#     def __init__(self,fruit_type):
#           self.fruit_type=fruit_type

empty_list =[]
class Possible_Fruit:
    def __init__(self,powers,effect,season,name):
        self.powers=powers
        self.effect=effect
        self.season=season
        self.name=name
    def __repr__(self):
         return f"{self.name} {self.effect} {self.powers} {self.season}"
fruits = Possible_Fruit(powers="changecolor",effect="gives energy",season="wet",name="big baobab")
empty_list.append(fruits)
print(fruits)
print(empty_list)
class Seasons:
    def __init__(self,seasons):
        self.seasons = seasons
    def __str__(self):
            return f"{self.seasons}"
    def predict_fruit(self):
        for item in empty_list:
            if self.seasons == item.season:
                print( f"{item.name} was produced in this {self.seasons} season")
s = Seasons(seasons="wet")
s.predict_fruit()









    

# // The Legendary African Drum Circles: You're part of a community that hosts one of the largest drum 
# // circles in Africa. There are different types of traditional drums used in the circle, each with its
# // unique sound and rythm. The Djembe, Talking Drum, and Bougaraubou are among the popular ones. These 
# // drums have common properties such as the material they're made from and their sizes, but they also 
# // have distinct characteristics. For instanceof, the Talking Drum can mimic the lines of human speech,
# // the Djembe i)s known for its wide range of tones, and the Bougaraubou is noted for its deep
# // rich bas tones.

# // You want to create a softtware model of the drum circle that encapsulates these different types 
# // of drums. You wish to include methods for each drum that represent the sound it makes, and also
# // group similar drums together. Think about craeting a base Drum class that contains properties 
# // and methods common to all drums common to all drums, and then create subclasses for each specific
# // type of drum (like Djembe, TalkingDrum, and Bougaraubou).


# // The subclasses should inherit from the base DRum class and also implement their unique characteristics
# // .This software model would help newcomers understand the characteristics of each drum and how 
# // they contribute to the overall rhythm of the drum circle.
class Drum:
    def __init__(self,material,size):
            self.material=material
            self.size=size

    def predict_sound(self):
        print(f"{self.sound}")

class Djembe(Drum):
     sound=("produces a wide range of sound")
class Talking_Drum(Drum):
     sound=("It mimics the line of human speech.")
class Bougarabou(Drum):
     sound=("produces deep,rich bass tones")
Drum1=Talking_Drum(material="skin",size="big")
Drum1.predict_sound()
Talking_Drum.mi



class Drum:
    def __init__(self, material, size):
        self.material = material
        self.size = size

    def play(self):
        print("*drum sound*")

class Djembe(Drum):
    def __init__(self, material, size):
        super().__init__(material, size)

    def make_sound(self):
        print("*deep, rich bass sound*")

class TalkingDrum(Drum):
    def __init__(self, material, size):
        super().__init__(material, size)

    def make_sound(self):
        print("*high-pitched sound that can mimic human speech*")

class Bougaraubou(Drum):
    def __init__(self, material, size):
        super().__init__(material, size)

    def make_sound(self):
        print("*high-pitched, piercing sound*")

# Create some drums
# djembe = Djembe("wood", 24")
# talking_drum = TalkingDrum("leather", 18")
# bougaraubou = Bougaraubou("hide", 12")

# Play the drums
djembe.play()
talking_drum.play()
bougaraubou.play()



# class Drum:
#     def __init__(self, material, size):
#         self.material = material
#         self.size = size
#     def make_sound(self):
#         print(f"{self.__class__.__name__} which is {self.size} and is made of {self.material} {self.sound}")
# class Djembe(Drum):
#     sound = "produces wide range of sound"
# class Talking_drum(Drum):
#     sound = "can mimic human lines"
# class Bougarabou(Drum):
#     sound = "produces deep, rich bass tone"
# drum1 = Djembe("wood", "medium")
# drum1.make_sound()
# drum2 = Talking_drum("leather", "large")
# drum2.make_sound()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
# drum3 = Bougarabou("plastic", "small")
# drum3.make_sound()

# Python program that takes a list of numbers as input and outputs the sum of all the even numbers 
# and the product of all the odd numbers using the if-else statement.


def sum_even_product_odd(numbers):
  even_sum = 0
  odd_product = 1
  for number in numbers:
    if number % 2 == 0:
      even_sum += number
    else:
      odd_product *= number
  return even_sum, odd_product


if __name__ == "__main__":
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  even_sum, odd_product = sum_even_product_odd(numbers)
  print("The sum of all the even numbers is", even_sum)
  print("The product of all the odd numbers is", odd_product)