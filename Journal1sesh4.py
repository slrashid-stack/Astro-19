class favanimal1:
	def __init__(self, arms, fins, eyes, furry, tail):
		self.arms = arms
		self.fins = fins
		self.eyes = eyes
		self.furry = furry
		self.tail = tail
	def describe(self):
		print("Description")
		print(f"Arm length: {self.arms}")
		print(f"fin length: {self.fins}")
		print(f"eye number: {self.eyes}")
		print(f"furry?: {self.furry}")
		print(f"tail?: {self.tail}")

favanimal = favanimal1(2.55, 4.67, 2, True, False)
favanimal.describe()