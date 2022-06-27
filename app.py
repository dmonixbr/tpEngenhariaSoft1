from src.Alarme import Alarme
from src.AreaEdificio import AreaEdificio
import os

print("Declare o numero de Areas no Edificio:")
numeroAreas = int(input())
os.system('clear')

zonas = {
    0:[],
    1:['amarelo'],
    2:['azul'],
    3:['amarelo', 'azul']
}

area=[]

def switchZona(tipoArea):
    if tipoArea < 0 or tipoArea > 3:
        print("Area invalida")
        return zonas[0]

    return zonas[tipoArea]

listaAreas = []

for i in range(0, numeroAreas):
    doc = AreaEdificio()
    print("Area {} do edificio:".format(i))
    print("Selecione as zonas da area {}:".format(i))
    print('0 - Nenhuma marcacao')
    print('1 - Zona amarela')
    print('2 - Zona azul')
    print('3 - Zona amarela e azul')
    zona = int(input())
    doc.setZona(switchZona(int(zona)))
    os.system('clear')
    
    print('Digite quantos alarmes têm na area {}'.format(i))
    numeroAlarmes = int(input())
    os.system('clear')
    listaAlarmes = []

    for j in range(0, numeroAlarmes):
        alarme = Alarme()
        listaAlarmes.append(alarme)

        os.system('clear')

    doc.setAlarmesDoEdificio(listaAlarmes)
    listaAreas.append(doc)