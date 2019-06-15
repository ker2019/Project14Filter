from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np
import os

#Init and compile model
def newModel(neurCount:'int')->'Model':
	l0 = Input((2,))
	l1 = Dense(neurCount, activation='sigmoid', use_bias=True)(l0)
	l2 = Dense(1, activation='sigmoid', use_bias=False)(l1)

	model = Model(input=l0, output=l2)
	model.compile(loss='mean_squared_error',
		optimizer='adam',
		metrics=['accuracy']
    	)
	return model

#Fit model
def studyFigure(isPointInFigure:'[Float, Float]->bool', 
		pointsCount=1000,
		neurCount=6,
		epochsCount=20000,
		verbose=False)->'Model':
	X = np.random.random((pointsCount, 2)) * 2 - 1
	Y = [1 if isPointInFigure([x, y]) else 0 for [x, y] in X]
	
	model = newModel(neurCount)

	model.fit(
	X, Y,
	epochs=epochsCount,
	verbose=verbose
	)
	return model

#Load model from a file, if exist, else refit them
def getModel(name:'String',
		isPointInFigure:'[Float, Float]->bool'=None, 
		pointsCount=1000,
		neurCount=6,
		epochsCount=20000,
		verbose=False)->'Model':
	if os.path.isfile(name + ".h5"):
		model = newModel(neurCount)
		model.load_weights(name + ".h5")
	else:
		model = studyFigure(isPointInFigure, pointsCount, neurCount, epochsCount, verbose=verbose)
		model.save(name + ".h5")
	return model


def saturate(v):
	return min(1, max(0, v))

#draw using neuro
def drawModel(model:'Model', density=40, grad=True):
	#fill flat by points
	c = np.r_[-1:1:1/density]

	flat = np.transpose([np.tile(c, len(c)), np.repeat(c, len(c))])

	res = model.predict(flat)
	if grad:
		for (x, y), r in zip(flat, res):
    			plt.scatter(x, y, color=[(1, 1-saturate(r[0]), 1-saturate(r[0]))])
	else:		
		for (x, y), r in zip(flat, res):
			plt.scatter(x, y, color='red' if r[0] >= 0.5 else 'green')
	plt.show()
	
#return lamda, checking is point(x, y) inner ellips
def ellips(horSeimAxis=0.5, verSeimAxis=0.5)->'[Float, Float]->bool':
	def isInnerEllips(point:'list')->bool:
		return (point[0]/horSeimAxis)**2 + (point[1]/verSeimAxis)**2 <= 1
	return isInnerEllips


def rectangle(height=0.5, width=0.5, angle=0.0)->'[Float, Float]->bool':
	c = np.math.cos(angle)
	s = np.math.sin(angle)
	def isInnerRectangle(point:'list')->bool:
		x = point[0]
		y = point[1]
		newx = c*x + s*y
		newy = -s*x + c*y
		return abs(newx) <= width and abs(newy) <= height
	return isInnerRectangle

def straight(angle=0.0, length=0.5, width=0.02)->'[Float, Float]->bool':
	return rectangle(height=width, width=length, angle=angle)
	
#draw figure without neuro 	
def drawFigure(isPointInFigure:'[Float, Float]->bool', density=40):
	#fill flat by points
	c = np.r_[-1:1:1/density]

	flat = np.transpose([np.tile(c, len(c)), np.repeat(c, len(c))])
	
	for [x, y] in flat:
		plt.scatter(x, y, color='red' if isPointInFigure([x, y]) else 'white')
	plt.show()

PROMPT = "[0] Exit\n[1] Round\n[2] Ellips\n[3] Rectangle\n[4] Straight"

if __name__=='__main__':
	while (True):
		print(PROMPT)
		ch = input()
		if ch == '0':
			break
		elif ch == '1':
			drawModel(getModel("round", ellips()))
		elif ch == '2':
			drawModel(getModel("ellips", ellips(0.3, 0.5)))
		elif ch == '3':
			drawModel(getModel("rectangle_30", rectangle(angle=np.math.pi/6)))
		elif ch == '4':
			drawModel(getModel("straight_70", straight(np.math.pi*7/18)))
		else:
			print("Incorrect")
#To recompute weights delete model file
