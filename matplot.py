import matplotlib.pyplot as plt

#preguntamosd por el año inicial
inicio = int(input('introduce el año incial: '))
#preguntamos por el año final
final = int(input('introzuca el año final: '))

#definimos un diccionario vacio para guarda las ventas por año
ventas={}

#Bucle iterativo para preguntar  las ventas de cda año y guardaslas en el diccionario

for i in range(inicio,final+1):
    ventas[i] = int(input('introduzca las ventas en el año: '+str(i)+':'))

fig,ax = plt.subplots()
ax.plot(ventas.keys(),ventas.values() )
ax.set_title('Ventas por año')
ax.set_xlabel('años')
ax.set_ylabel('ventas')
ax.set_xticks(list(ventas.keys()))
plt.show()