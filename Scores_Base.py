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
			'Games Played': 0}
		self.Visitor = { 
			'Points': 0, 
			'Points Allowed': 0, 
			'Games Played': 0}
		self.stat_fill()

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
		hap = self.Home['Points'] / self.Home['Games Played']
		hapa = self.Home['Points Allowed'] / self.Home['Games Played']
		
		vap = self.Visitor['Points'] / self.Visitor['Games Played']
		vapa = self.Visitor['Points Allowed'] / self.Visitor['Games Played']
			
		hstat = [hap, hapa]
		vstat = [vap, vapa]
		self.Score_Calc(hstat, vstat)

		print '\n'
		print 'Score: %s = %d and %s = %d' % (self.HName, self.hsco, self.VName, self.vsco) 

	# This method is the one that actually uses Butch's calculation.
	# There are two different calculations that are condition based.
	def Score_Calc(self, ht, vt):
		self.hst = ht
		self.vst = vt
		
		if self.hst[0] >= self.vst[1]:
			self.hsco = round(((self.hst[0] - self.vst[1]) / 2) + self.vst[1] + 3)
		else:
			self.hsco = round(((self.vst[1] - self.hst[0]) / 2) + self.hst[0] + 3)
		if self.vst[0] >= self.hst[1]:
			self.vsco = round(((self.vst[0] - self.hst[1]) / 2) + self.hst[1])
		else:
			self.vsco = round(((self.hst[1] - self.vst[0]) / 2) + self.vst[0])

