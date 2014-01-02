from os import system as sy

class Scores_App(object):

	def __init__(self):
		self.HName = raw_input('Home Team Name?> ')
		self.VName = raw_input('Visitor Team Name?> ')
		self.Stats = ['Points', 'Points Allowed', 'Games Played']
		self.Home = {
			'Points': 0,
			'Points Allowed': 0,
			'Games Played': 0,
			'AVGP': 0,
			'AVGPA': 0}
		self.Visitor = { 
			'Points': 0, 
			'Points Allowed': 0, 
			'Games Played': 0,
			'AVGP': 0,
			'AVGPA': 0}
		self.stat_fill()
		print self.Home
		self.Home_Score()

	def stat_ask(self, statvar):
		curstat = statvar
		try:
			sy('clear')
			print 'Home Team %s?' % curstat
			self.Home[curstat] = int(raw_input('> '))
			print 'Visitor %s?' % curstat
			self.Visitor[curstat] = int(raw_input('> '))
		except ValueError:
			print 'Type a Number!'
			self.stat_ask(curstat)

	def stat_fill(self):
		n = 0
		for item in self.Stats:
			self.stat_ask(self.Stats[n])
			n+= 1
		self.Home['AVGP'] = self.Home['Points'] / self.Home['Games Played']
		self.Home['AVGPA'] = self.Home['Points Allowed'] / self.Home['Games Played']
		

	def Home_Score(self):
		
		self.home_score = ((self.Home['AVGP'] - self.Visitor['AVGPA']) / 2) + self.Visitor['AVGPA'] + 3
		print '\n'
		print self.home_score


## home_score_against HPA / 17

app = Scores_App()

