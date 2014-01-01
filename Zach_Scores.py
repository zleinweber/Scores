from os import system

class Scores_App(object):

	def __init__(self):
		self.HName = raw_input('Home Team Name?> ')
		self.VName = raw_input('Visitor Team Name?> ')
		self.Stats = ['Points', 'Points Allowed', 'Games Played']
		self.Home = {
			'Points': 0,
			'Points Allowed': 0,
			'Games Played': 0}
		self.Visitor = { 
			'Points': 0, 
			'Points Allowed': 0, 
			'Games Played': 0}
		self.stat_choose()
		print self.Home

	def stat_populate(self, statvar):
		curstat = statvar
		print 'Home Team %s?' % curstat
		try:
			self.Home[curstat] = int(raw_input('> '))
		except ValueError:
			print 'Type a Number!'
			self.stat_populate(curstat)

	def stat_choose(self):
		n = 0
		for item in self.Stats:
			self.stat_populate(self.Stats[n])
			n+= 1

	def Home_Score(self):
		
		self.home_score_for = ((self.HPF / 17) + 3)
		
		print self.home_score_for


## home_score_against HPA / 17

app = Scores_App()

