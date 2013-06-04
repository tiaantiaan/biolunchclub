import time
from datetime import date

class NextLunch:
	def __init__(self):
		'Set week number of year'
		self.weeknum = date.today().isocalendar()[1]
		'Set names (Repeat to add 2 week shift for Mariaan)'
		self.names = ['Tiaan','Larry','Pietie','Stephen','Pieter']
		'Add Mariaan every 6th week'
		if self.weeknum % 6 ==0 : self.names.append('Mariaan')
		'Set people count'
		self.names_count = len(self.names)
		'Adjust week number to sync current schedule'

	def next(self):
		return ( self.names_count-1 if self.weeknum % self.names_count==-1 else self.weeknum % self.names_count-1)

	def printlist(self):
		n = self.next()
		response = '<table style="text-align:center;font-size:large;width:300px;height:300px;margin-top:-150px;margin-left:-150px;background-color:#d9d9d9;position:fixed;top:50%;left:50%;">'		
		for x in range(0,self.names_count):
			response += '<tr><td>'
			response += '<b style="font-size:x-large">' if x==n else ''
			response += self.names[x]
			response += '<b>' if x==n else ''
			response += '</td></tr>'
		response += '</table>'
		return response
