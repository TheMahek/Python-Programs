class Cat:
    def speak(self):
        return "Meow!"
    
class Cow :
    def speak(self):
        return "Moo!"
    
def animal_speak(animal):
    print(animal.speak())

cat = Cat()
cow = Cow()

animal_speak(cat)
animal_speak(cow)