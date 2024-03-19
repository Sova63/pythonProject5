from Cat1 import Cat
if __name__ == "__main__":
	cat = Cat("Василий")
	print(cat.GetState())
	cat.Pogladit()
	cat.Feed(260)
	print(cat.GetState())
	cat.Pogladit()
	cat.Feed(260)
	cat.Pogladit()
	print(cat.GetState())
