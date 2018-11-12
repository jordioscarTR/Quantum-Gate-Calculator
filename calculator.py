from math import sin, cos, atan, pi, sqrt #importem de la llibreria de mates les seguents operacions per treballar amb elles.
import sys #importem la llibreria per poder llegir el que escribim.

epsilon = 0.0001 #utilitzarem aquesta varible ~0 per simplificar els calculs.
sqrt22 = sqrt(2.)/2. #nombrem aquesta variable, per simplificar el programa (no escriure tant).

#creem les variables de la posició i les posem la posició inicial.
x = 0.
y = 0.
z = 1.

#creem les variables x,y,z temporal per poder fer els calculs sense canviar l'estat de la variable fins al final.
xt = x
yt = y
zt = z

#creem la variable de 'string' per els resulatas a la posició per defectre.
xnum = '0'
ynum = '0'
znum = '1'

#creem la variable del percentatge i la posem a la possicio de per defecre.
percentage0 = 100.
percentage1 = 0.

module = 0. #variable necessaria posteriorment.
totalm = 1. #per calcular el modul total del vector (comprobacioó).

read = 1 # 1=llegeix les comandes, 0=acaba el programa

print (xnum,",", ynum,",", znum) #imrimeix l'estat inicial + enter.
print ('\n')

while (read == 1): #sempre que no ho digem, llegeix lo escrit al programa.

	tecla = sys.stdin.read(1)

	if (tecla != '\n'): #cuan li dones al 'enter', aplica les diferents portes.
		print ('Aplicando puerta ', tecla)

		if (tecla == 'x'):
			xt = x
			yt = -y
			zt = -z

			x = xt
			y = yt
			z = zt  #fa els calculs per aplicar la porta x

		if (tecla == 'y'):
			xt = -x
			yt = y
			zt = -z

			x = xt
			y = yt
			z = zt #fa els calculs per aplicar la porta y

		if (tecla == 'z'):
			xt = -x
			yt = -y
			zt = z

			x = xt
			y = yt
			z = zt #fa els calculs per aplicar la porta z

		if (tecla == 'h'):
			xt = -(x)
			yt = -(z)
			zt = -(y)

			x = xt
			y = yt
			z = zt #fa els calculs per aplicar la porta h

		if (tecla == 't'):

			module = sqrt(x*x+y*y)

			if (abs(y) < epsilon): # Si y es igual a zero
				if (abs(x) < epsilon):

					xt = x
					yt = y
					zt = z


					x = xt
					y = yt
					z = zt

				elif ( x > epsilon):

					xt = sin ((pi/2) + (pi/4))
					yt = cos ((pi/2) + (pi/4))
					zt = z

					x = xt
					y = yt
					z = zt

				elif (x < epsilon):
					
					xt = sin ((3 * pi/2) + (pi/4))
					yt = cos ((3 * pi/2) + (pi/4))
					zt = z

					x = xt
					y = yt
					z = zt

			elif (y > epsilon):
				xt = sin (atan ( x/y ) + (pi/4))
				yt = cos (atan (x/y) + (pi/4))
				zt = z

				x = xt
				y = yt
				z = zt

			elif (y < epsilon):
				xt = sin (atan ( x/y ) + (pi/4) + pi)
				yt = cos (atan (x/y) + (pi/4) + pi)
				zt = z

				x = xt
				y = yt
				z = zt	

			x = x * module
			y = y * module #fa els calculs per aplicar la porta t

		if (tecla == 's'):

			module = sqrt(x*x+y*y)

			if (abs(y) < epsilon): # Si y es igual a zero
				if (abs(x) < epsilon):

					xt = x
					yt = y
					zt = z


					x = xt
					y = yt
					z = zt

				elif ( x > epsilon):

					xt = sin ((pi/2) + (pi/2))
					yt = cos ((pi/2) + (pi/2))
					zt = z

					x = xt
					y = yt
					z = zt

				elif (x < epsilon):
					
					xt = sin ((3*pi/2) + (pi/2))
					yt = cos ((3*pi/2) + (pi/2))
					zt = z

					x = xt
					y = yt
					z = zt

			elif (y > epsilon):
				xt = sin (atan ( x/y ) + (pi/2))
				yt = cos (atan (x/y) + (pi/2))
				zt = z

				x = xt
				y = yt
				z = zt

			elif (y < epsilon):
				xt = sin (atan ( x/y ) + (pi/2) + pi)
				yt = cos (atan (x/y) + (pi/2) + pi)
				zt = z

				x = xt
				y = yt
				z = zt	

			x = x * module
			y = y * module #fa els calculs per aplicar la porta s

		if (tecla == 'p'):

			percentage0 = str(round(((z + 1.) * 100 / 2), 4))
			percentage1 = str(round(((-z + 1.) * 100 / 2), 4))

			print ('Hi ha aproximadament un ' + percentage0 + '%'+' de probabilitat de que surti 0, i un ' + percentage1 + '%'+' de que surti 1') #calcula la probabilitat del col·lapse en 1 o en 0

		if (tecla =='r'):
			x = 0.
			y = 0.
			z = 1. #recupera l'estat inicial

		if (tecla == 'e'):
			read = 0
			print ('Fin del programa') #finalitza el programa.

		else: # una vegada aplicades les portes, simplifica els numeros que tinguin una diferencia menor a epsilon per a x,y,z.
			xnum = x
			if (abs(x)<epsilon): xnum = '0'
			if (abs(x-sqrt22) < epsilon): xnum = 'raiz(2)/2'
			if (abs(x+sqrt22) < epsilon): xnum = '-raiz(2)/2'
			if (abs(x-1.)<epsilon): xnum = '1'
			if (abs(x+1.)<epsilon): xnum = '-1'
			if (abs(x-0.5)<epsilon): xnum = '1/2'
			if (abs(x+0.5)<epsilon): xnum = '-1/2'
			
			ynum = y
			if (abs(y)<epsilon): ynum = '0'
			if (abs(y-sqrt22) < epsilon): ynum = 'raiz(2)/2'
			if (abs(y+sqrt22) < epsilon): ynum = '-raiz(2)/2'
			if (abs(y-1.)<epsilon): ynum = '1'
			if (abs(y+1.)<epsilon): ynum = '-1'
			if (abs(y-0.5)<epsilon): ynum = '1/2'
			if (abs(y+0.5)<epsilon): ynum = '-1/2'
			
			znum = z
			if (abs(z)<epsilon): znum = '0'
			if (abs(z-sqrt22) < epsilon): znum = 'raiz(2)/2'
			if (abs(z+sqrt22) < epsilon): znum = '-raiz(2)/2'
			if (abs(z-1.)<epsilon): znum = '1'
			if (abs(z+1.)<epsilon): znum = '-1'
			if (abs(z-0.5)<epsilon): znum = '1/2'
			if (abs(z+0.5)<epsilon): znum = '-1/2'
			
			totalm = sqrt((x*x)+(y*y)+(z*z)) #per comporbar si els calculs son correctes...

			print (xnum,",", ynum,",", znum)
			
			if ((abs(totalm) - 1.) > epsilon): #Cuando totalm no es 1...
				print ('ERROR')
				read = 0
				print ('Fin del programa')
			else: print (" x",round(x,4)," y",round(y,4)," z",round(z,4)) #si es correcte, imprimeix els resultats.
			print ('\n')