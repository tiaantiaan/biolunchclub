import time
from datetime import date

class NextLunch:
	def __init__(self):
		'Set adjustment (Between 0 and 11)'
		self.adj=0;
		'Set week number of year'
		self.weeknum = date.today().isocalendar()[1]
		'Set names (Repeat to add 2 week shift for Mariaan)'
		self.names = ['Tiaan','Larry','Pietie','Stephen','Pieter']
		'Add Mariaan every 6th week'
		if ( (self.weeknum+5) % (6+self.adj) == 0) or ( (self.weeknum+5) % (7+self.adj) == 0) or ( (self.weeknum+5) % (8+self.adj) == 0) or ( (self.weeknum+5) % (9+self.adj) == 0) or ( (self.weeknum+5) % (10+self.adj) == 0) or ( (self.weeknum+5) % (11+self.adj) == 0) :
			self.names.append('Mariaan')
		'Set people count'
		self.names_count = 6
		'Adjust week number to sync current schedule'
		self.weeknum += self.adj

	def next(self):
		if (self.weeknum % self.names_count==0):
			return self.names_count
		else:
			return self.weeknum % self.names_count

	def printlist(self):
		n = self.next()-1
		response = '<table style="text-align:center;font-size:large;width:300px;height:300px;margin-top:-150px;margin-left:-150px;background-color:#d9d9d9;position:fixed;top:50%;left:50%;">'		
		for x in range(0,len(self.names)):
			response += '<tr><td>'
			response += '<b style="font-size:x-large">' if x==n else ''
			response += self.names[x]
			response += '<b>' if x==n else ''
			response += '</td></tr>'
		response += '</table>'
		return response
