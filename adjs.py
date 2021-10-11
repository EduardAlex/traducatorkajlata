class ncadj:
	def __init__(self, adj, number, case):
		self.suff = {"NOM" : ("ą", "ai"), "ACC" : ("ą", "ai"), 
			"LOC" : ("ą", "ai"), "GEN" : ("ai", "aŭ"), 
			"DAT" : ("ai", "aŭ"), "INS" : ("as", "inx"), 
			"ALL" : ("as", "inx"), "ABL" : ("as", "inx")}

		self.adj = adj
		self.number = number
		self.case = case
		with open("adjdb.dat", "r", encoding='utf-8') as f:
			self.adjs = {i[0] : i[1] for i in [j.split(":") for j in f.read().split("\n")]}
		self.conj()

	def __str__(self):
		return self.adj

	def conj(self):
		self.adj = self.adjs[self.adj]
		if self.number in "SGPA":
			suf = self.suff[self.case][0]
		elif self.number == "PL":
			suf = self.suff[self.case][1]
		self.adj = self.adj + suf
