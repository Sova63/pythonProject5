from Dog import Dog
from Cow import Cow
from Cat import Cat
from Fish import Fish
from Animal import Animal

def SpeakAnimal(animal:Animal):
	animal.Speak()
	if __name__=="__main__":
		cat = Cat()
		dog = Dog()
		cow = Cow()
		fish = Fish()
		animals = [cat,dog,cow,fish]
		for animal in animals:
			print(animal.__class__)
			SpeakAnimal(animal)
		for animal in animals:
			print(animal.__class__)
			SpeakAnimal(animal)



