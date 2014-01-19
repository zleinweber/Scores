# The gui for the Scores program.

from Tkinter import *
from Scores_Base import Scores_App as Scores

class App(Scores):

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		
		self.HName = StringVar()
		self.HName.set("Home")
		Entry(frame, textvariable=self.HName).grid(row=0, column=1)
		Label(frame, text='Home Team Name:').grid(row=0, column=0)

		self.VName = StringVar() 
		self.VName.set('Visitor')
		Entry(frame, textvariable=self.VName).grid(row=1, column=1)
		Label(frame, text='Visitor Team Name:').grid(row=1, column=0)
		
		self.Home = {
			'Points': DoubleVar(),
			'Points Allowed': DoubleVar(),
			'Games': DoubleVar()}
		Entry(frame, textvariable=self.Home['Points']).grid(row=2, column=1)
		Label(frame, text='Home Points:').grid(row=2, column=0)
		Entry(frame, textvariable=self.Home['Points Allowed']).grid(row=3, column=1)
		Label(frame, text='Home Allowed:').grid(row=3, column=0)
		Entry(frame, textvariable=self.Home['Games']).grid(row=4, column=1)
		Label(frame, text='Home Played:').grid(row=4, column=0)

		self.Visitor = { 
			'Points': DoubleVar(),
			'Points Allowed': DoubleVar(), 
			'Games': DoubleVar()}
		Entry(frame, textvariable=self.Visitor['Points']).grid(row=5, column=1)
		Label(frame, text='Visitor Points:').grid(row=5, column=0)
		Entry(frame, textvariable=self.Visitor['Points Allowed']).grid(row=6, column=1)
		Label(frame, text='Visitor Allowed:').grid(row=6, column=0)
		Entry(frame, textvariable=self.Visitor['Games']).grid(row=7, column=1)
		Label(frame, text='Visitor Played:').grid(row=7, column=0)

		self.HRes = DoubleVar()
		self.VRes = DoubleVar()

		frame2 = Frame(frame)
		frame2.grid(row=8, column=0)
		Label(frame2, textvariable=self.HName, anchor=W, width=10, fg='red').grid(row=0, column=0)
		Label(frame2, textvariable=self.HRes).grid(row=0, column=1)

		frame3 = Frame(frame)
		frame3.grid(row=8, column=1)
		Label(frame3, textvariable=self.VName, anchor=W, width=10, fg='red').grid(row=0, column=0)
		Label(frame3, textvariable=self.VRes).grid(row=0, column=1)

		Button(frame, text='Calculate', command=self.Stat_Get).grid(row=9, columnspan=2)

	def Stat_Get(self):
		hp = self.Home['Points'].get(); hpa = self.Home['Points Allowed'].get()
		hpg = self.Home['Games'].get()
		vp = self.Visitor['Points'].get(); vpa = self.Visitor['Points Allowed'].get()
		vpg = self.Visitor['Games'].get()

		self.hap = hp / hpg; self.hapa = hpa / hpg
		self.vap = vp / vpg; self.vapa = vpa / vpg
		hstat = [self.hap, self.hapa]
		vstat = [self.vap, self.vapa]
		self.Score_Calc(hstat, vstat)
		self.HRes.set(self.hsco); self.VRes.set(self.vsco)

root = Tk(); root.wm_title('Scores')
app = App(root)

root.mainloop()
