from io import *


def Define_data():	
	# Headline
	print("Insert the iterations of your experiment followed by ´Enter´ key, when you are done, write ´DONE´.")

	#Variables
	x=False
	datos=open("data_base.txt","w")	
	tupla=[]

	#Input method for this program
	while x==False :
		tupla_datos=input()
		tupla_datos=str(tupla_datos)
		if tupla_datos=="DONE":
			x=True
		else:
			tupla.append(tupla_datos)
			tupla.append("\n")

	#Save data external file
	datos.writelines(tupla)
	datos.close()
	
# Run code
Define_data()