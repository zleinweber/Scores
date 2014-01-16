# This is a program requested by Butch Miller.
# It takes input in the form of a few football team stats.
# Then it outputs a score guess based on a calculation Butch provided.

from os import system as sy

# Currently, the entire app is contained in this one class.
# I haven't found any reason to use regular functions instead or
# add any additional classes.  I would also like to add a Tk interface going forward.
class Scores_App(object):

	# Currently init defines the important instance variables
	# Then automatically runs the method for populating them
	def __init__(self):
		# These two varialbes are strings containing team name
		self.HName = raw_input('Home Team Name?> ')
		self.VName = raw_input('Visitor Team Name?> ')
		# This is an index for team stats
		self.Stats = ['Points', 'Points Allowed', 'Games Played']
		# Two dictoinaries that will get populated with the actual stats
		# Related to the home team and away team.
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
		# Init auto runs the method to populate the stats.  This will change I think.
		self.stat_fill()
		# This is just a placeholder to make sure everything populated as it should.
		print self.Home
		# This autoruns the method to calculate 'guessed score'.
		# This will require user input in the future.
		self.Home_Score()

	# Stat population is broke into two methods.
	# This one actually asks the user to input the stat.
	# This is seperate from Stat_Fill so that the except clause can begin
	# On the same stat where the exception occured.
	def stat_ask(self, statvar):
		# This variable contains the key to be used for each teams stat value.
		curstat = statvar
		# Try except takes input as raw_input then converts it to int
		# If that fails then it ouputs the error and tries again.
		try:
			sy('clear') # Clears Screen. Bear in mind. This won't work in Windows.
			print 'Home Team %s?' % curstat
			self.Home[curstat] = int(raw_input('> '))
			print 'Visitor %s?' % curstat
			self.Visitor[curstat] = int(raw_input('> '))
		except ValueError:
			print 'Type a Number!'
			self.stat_ask(curstat)

	# This method populates teams variables with the appropriate stat.
	# For variables that require user input it invokes stat_ask to get it.
	# For the rest it calculates it (The rest are averages).
	def stat_fill(self):
		# Scans through the stats using index points.
		n = 0
		for item in self.Stats:
			# Ask user to input the stat.
			# self.Stats[n] refers to the key currently in use.
			self.stat_ask(self.Stats[n])
			# Add one to go to the next index point.
			n += 1
		# Calculates the remaining averages from the user input stats.
		self.Home['AVGP'] = self.Home['Points'] / self.Home['Games Played']
		self.Home['AVGPA'] = self.Home['Points Allowed'] / self.Home['Games Played']
		

	# This method is the one that actually uses Butch's calculation.
	# There are two different calculations that are condition based.
	def Home_Score(self):
		
		self.home_score = ((self.Home['AVGP'] - self.Visitor['AVGPA']) / 2) + self.Visitor['AVGPA'] + 3
		print '\n'
		print self.home_score



app = Scores_App()

