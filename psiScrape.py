from lxml import html
import requests
import csv
#page = requests.get('http://www.nea.gov.sg/anti-pollution-radiation-protection/air-pollution-control/psi/historical-psi-readings/year/2015/month/6/day/7')

#tree=html.fromstring(page.content)
#psi = tree.xpath('//span[]/text()')

def int2(s):
	i=0
	try:
		i = int(s)
	except ValueError:
		pass
	finally:
		return i

def scrapePSI(url,interval = 7):
	print url
	page = requests.get(url)
	tree=html.fromstring(page.content)
	psi = tree.xpath('//span/text()')
	ind = psi.index('1am')
	ind2 = psi.index('12am')+interval
	North = psi[ind+1:ind2:interval]
	South= psi[ind+2:ind2:interval]
	East= psi[ind+3:ind2:interval]
	West= psi[ind+4:ind2:interval]
	Central= psi[ind+5:ind2:interval]
	Overall= psi[ind+6:ind2:interval]
	North = map(int,North)
	South = map(int,South)
	East = map(int,East)
	West = map(int,West)
	Central = map(int,Central)
	#Overall = map(int,Overall)
	return North,South,East,West,Central,Overall
	
def scrapePSI4pm(url,interval = 7):
	print url
	page = requests.get(url)
	tree=html.fromstring(page.content)
	psi = tree.xpath('//span/text()')
	ind = psi.index('4pm')
	North = int(psi[ind+1])
	South= int(psi[ind+2])
	East= int(psi[ind+3])
	West= int(psi[ind+4])
	Central= int(psi[ind+5])
	Overall= (psi[ind+6])

	return North,South,East,West,Central,Overall

def main():
	N=[]
	S=[]
	E=[]
	W=[]
	C=[]
	year = 2013
	#url = 'http://www.nea.gov.sg/anti-pollution-radiation-protection/air-pollution-control/psi/historical-psi-readings/year/2015/'
	for i in range(12):
		month = i+1
		if month == 2:
			for j in range(28):
				day = j+1
				url = 'http://www.nea.gov.sg/anti-pollution-radiation-protection/air-pollution-control/psi/historical-psi-readings/year/%s/month/%s/day/%s'%(year,month,day)
				North,South,East,West,Central,Overall=scrapePSI4pm(url,13)
				N.append(North)
				S.append(South)
				E.append(East)
				W.append(West)
				C.append(Central)
		elif month in [1,3,5,7,8,10,12]:
			for j in range(31):
				day = j+1
				url = 'http://www.nea.gov.sg/anti-pollution-radiation-protection/air-pollution-control/psi/historical-psi-readings/year/%s/month/%s/day/%s'%(year,month,day)
				North,South,East,West,Central,Overall=scrapePSI4pm(url,13)
				N.append(North)
				S.append(South)
				E.append(East)
				W.append(West)
				C.append(Central)
		else:
			for j in range(30):
				day = j+1
				url = 'http://www.nea.gov.sg/anti-pollution-radiation-protection/air-pollution-control/psi/historical-psi-readings/year/%s/month/%s/day/%s'%(year,month,day)
				North,South,East,West,Central,Overall=scrapePSI4pm(url,13)
				N.append(North)
				S.append(South)
				E.append(East)
				W.append(West)
				C.append(Central)
#	North,South,East,West,Central,Overall = scrapePSI(url)
	file1 = open('North.txt', 'wb')
	file2 = open('South.txt', 'wb')
	file3 = open('East.txt', 'wb')
	file4 = open('West.txt', 'wb')
	file5 = open('Central.txt', 'wb')
	wr = csv.writer(file1)
	wr.writerow(N)
	file1.close()
	wr = csv.writer(file2)
	wr.writerow(S)
	file2.close()
	wr = csv.writer(file3)
	wr.writerow(E)
	file3.close()
	wr = csv.writer(file4)
	wr.writerow(W)
	file4.close()
	wr = csv.writer(file5)
	wr.writerow(C)
	file5.close()
	
if __name__ == '__main__':
	main()
