import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#data1 - Serie of measurements the frequence of steel rot's wobble

PROMPT = "You can:\n[0] Exit\n[1] Load a new data\n[2] Unload a data\n[3] Build graphic\n[4] To KS-test\n""[5] Show list of loaded data\n[6] Show data"

Data = {}

def loadData(filename: 'String', name=filename):
	data = pd.read_csv(filename)
	Data[name] = data

def unloadData(name: 'String'):
	try:
		del Data[name]
	except:
		print("Error: nonexistent")
		
def buildGraphic(name: 'String'):
	try:
		Data[name].plot.kde()
		plt.show()
	except:
		print("Error: nonexistent")
		
def ksTest(name: 'String', seriename: 'String'):
	try:
		serie = Data[name][seriename]
		print(stats.kstest(serie, 'norm', (serie.mean(), serie.std())))
	except:
		print("Error: nonexistent")

def showData(name: 'String'):
	try:L
		print(Data[name])
	except:
		print("Error: nonexistent")

if __name__=='__main__':
	while (True):
		print(PROMPT)
		ch = input()
		if ch == '0':
			break
		elif ch == '1':
			filename = input("Write name of file contains data:")
			name = input("Write name you would use to call data:")
			if name == "":
				loadData(filename)
			else:
				loadData(filename, name)
		elif ch == '2':
			name = input("Write name of data:")
			unloadData(name)
		elif ch == '3':
			name = input("Write name of data:")
			buildGraphic(name)
		elif ch == '4':
			name = input("Write name of data:")
			seriename = input("Write name of serie:")
			ksTest(name, seriename)
		elif ch == '5':
			print(Data.keys())
		elif ch == '6':
			name = input("Write name of data:")
			showData(name)
		else:
			print("Incorrect")
