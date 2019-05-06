from io import open
import math
#Class with all the basic statistical parameters
class OperacionesEstadisticas():

	def __init__(self):
		#Open file
		archivo_datos=open("data_base.txt","r")
		datos=archivo_datos.readlines()
		archivo_datos.close()
		datos.sort(key=float)  #Set the data that is storaged as str to float
		listado=[]
		for i in range (len(datos)):
			k=datos[i]
			listado.append(float(k))

		self.datos=listado
		self.n=len(self.datos)


	def Impresion(self):	#Print data
			
		print (self.datos)

	def Media (self):	#Calculate mean
		suma=0
		for i in self.datos:
			suma+=float(i)
		media=suma/self.n
		return media



	def DesviacionE(self,x):	#Standar deviation

		suma_DE=0
		
		for i in self.datos:
			temp=(float(i)-x)**2
			suma_DE=suma_DE+temp
		desviacion_estandar=suma_DE/self.n
		desviacion_estandar=math.sqrt(desviacion_estandar)
		return desviacion_estandar

	def Mediana(self):	#Calculate median
		if self.n%2==0:
			medidordown=round((self.n/2)-0.5)			
			mediana=(self.datos[medidordown]+self.datos[medidordown-1])/2
		else:
			mediana=self.datos[int((self.n/2)-0.5)]
		return mediana
	def Moda(self):		#Calculate mode

		repeticiones = 0                  #first part counts the max times a variable is repeated                                                      
		for i in self.datos:                                                                              
		    apariciones = (self.datos).count(i)                                                             
		    if apariciones > repeticiones:                                                       
		        repeticiones = apariciones                                                       
		modas = [] #Mode list(in case there are multiple modes)

		#second part, compares the previous count, and gets in the list those values that share the same reiterations value that the count value

		for i in self.datos:                                                                  
		    apariciones = (self.datos).count(i)                                                             
		    if apariciones == repeticiones and i not in modas:                                   
		        modas.append(i)                                                                  
		return modas

	def Cuartiles(self): #Quartiles
		pq2=self.Mediana()
		q1=(float(self.n+1)/4)
		q3=q1*3

		if isinstance(q1,int): 					#Check if the q1 and q3 are str or float
			pq1=self.datos[q1-1]
			pq3=self.datos[q3-1]
		else:
			q1down=int(round(q1-0.5))		
			j1=q1-q1down					#formula is q=xpos+(decimal)*(x(pos+1)-x(pos))
			q3down=int(round(q3-0.5))		
			j3=q3-q3down
			pq1=(self.datos[q1down-1])+j1*(self.datos[q1down]-self.datos[q3down-1])
			pq3=(self.datos[q3down-1])+j3*(self.datos[q3down]-self.datos[q3down-1])
		Cuartiles=[str(pq1),str(pq2),str(pq3)]
		return Cuartiles


	def Estado(self):
		print("La lista de datos es: ")
		self.Impresion()
		x=self.Media()
		de=self.DesviacionE(x)
		#Coefficient of variation operations, only valid if sample size long enough
		#There is another way to get it if the sample is to short, but it requieres the data to be normally distributed, not adequate to this program
		if self.n>40:
			cv=float(de)/x	
		else:
			cv="The sample is not big enough to the coefficient to be valid"	

		med=self.Mediana()
		mo=self.Moda()	                       
		q=self.Cuartiles()
		print("Mean value: ", str(x))
		print("Standar deviation value: ", str(de))
		print("Coefficient of variation value: ", str(cv))
		print("Median value: ", str(med))
		print("Mode(s) value is(are): ", str(mo))
		print("Quartil values are: ")
		p=0
		for j in q:
			p=p+1
			print("Q{}: {}".format(p,j))
		
#Run program

modelo=OperacionesEstadisticas()
modelo.Impresion()#Print data
modelo.Estado()# Print parameters

fin=input("Write anything to close the window")
