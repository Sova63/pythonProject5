class Cat():
	def __init__(self, name):
		self.name = name
		self._state = "Sad"
		self._hangry = True
		self._calory = 0
	def Feed(self,food):
		self._calory += food
		if self._calory>500:
			self._hangry = False
	def Pogladit(self):
		if self.GetState() =="Sad":
			pass
		elif self.GetState() == "Norma":
			print("Мур")
		elif self.GetState() == "Happy":
			print("Мур Мур")
	def GetState(self):
		if self._calory > 500:
			self._state = "Happy"
		elif self._calory <= 500 and self._calory >=250:
			self._state = "Normal"
		elif self._calory < 250:
			self._state = "Sad"
		return self._state