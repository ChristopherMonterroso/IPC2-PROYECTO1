
from asyncio.windows_events import NULL
from operator import le
import xml.etree.ElementTree as ET
import os 
import easygui

from ListaEnlazada import ListaEnlazada as ListaEn
from Grafica import Graficar
global Menu
Menu=True
Contador_Periodos =1
Lista = ListaEn()

Lista_Reporte = ListaEn()
ids= ListaEn()
def CargarDatos():
    A=True
    while A:
        try:
            
            tree = ET.parse(easygui.fileopenbox(title="Escoga el archivo .xml"))
            root = tree.getroot()
            for i in range(len(root)):
                Datos = ListaEn()
                aux1 = ListaEn()
                aux2 = ListaEn()
                Datos.append(root[i][0][0].text)
                Datos.append(root[i][0][1].text)
                Datos.append(root[i][1].text)
                Datos.append(root[i][2].text)
                print(i+1,": paciente agregado")
                for j in range(len(root[i][3])):
                    aux1.append(root[i][3][j].get('f'))
                Datos.append(aux1)
                for k in range(len(root[i][3])):
                    aux2.append(root[i][3][k].get('c'))
                Datos.append(aux2)
                Lista.append(Datos)       
                ids.append(i+1)   
            
            A=False
        except :
            print("Error : Escoja un archivo válido")
def Generar():
    root = ET.Element("pacientes")
    for i in range(len(Lista_Reporte)):

        paciente = ET.SubElement(root,"paciente") 
        personales = ET.SubElement(paciente,"datospersonales")
        nombre = ET.SubElement(personales,"nombre").text=Lista_Reporte[i][0]
        edad = ET.SubElement(personales,"edad").text=Lista_Reporte[i][1]
        periodos = ET.SubElement(paciente,"periodos").text=Lista_Reporte[i][2]
        m = ET.SubElement(paciente,"m").text=Lista_Reporte[i][3]
        resultado = ET.SubElement(paciente,"resultado").text="Leve"
    archivo = ET.ElementTree(root)
    archivo.write("ReportePacientes.xml",encoding="utf-8",xml_declaration=True)
    print("Reporte generado con el nombre ReportePacientes.xml")
    os.startfile("ReportePacientes.xml")
def Agregar_al_Reporte(nombre,edad,periodos,m):
    ListaAux= ListaEn()
    ListaAux.append(nombre)
    ListaAux.append(edad)
    ListaAux.append(periodos)
    ListaAux.append(m)
    ListaAux.append("Leve")
    Lista_Reporte.append(ListaAux)

def Crear_Matriz(id):
    for i in range(int(Lista[int(id-1)][3])):
        Matriz.append([0]*int(Lista[int(id-1)][3]))     
    for i in range(len(Lista[int(id-1)][4])):
        Matriz[int(Lista[int(id-1)][4][i])][int(Lista[int(id-1)][5][i])]= 1




def Periodos_Auto(matriz,inicio,periodo):
    Contador_Periodos+=1
    for s in range(periodo-inicio):
        Nuevo_periodo(matriz)
                                


def Nuevo_periodo(matriz):
    CoordenadasX_Sanas=ListaEn()
    CoordenadasY_Sanas=ListaEn()
    CoordenadasX_Contagiadas=ListaEn()
    CoordenadasY_Contagiadas=ListaEn()
    final = len(matriz[0])-1
    for i in range(len(matriz)):
        for j in  range(len(matriz)):
            #Sanas
            if matriz[i][j]==0:
                
                # i+ mas es abajo
                # i- es arriba 
                # j+ es derecha
                # j- es izquierda
                   
                # esquina superior izquierda   
                if i == 0 and j == 0:
                    if matriz[i+1][j]==1 and matriz[i][j+1]==1 and matriz[i+1][j+1]==1:
                            matriz[i][j]=1
                #esquina inferior izquierda
                elif i ==final and j==0:
                    if matriz[i-1][j]==1 and matriz[i][j+1]==1 and matriz[i-1][j+1]==1:
                            matriz[i][j]=1
              

                #esquina superior derecha
                elif i ==0 and j==final:
                    if matriz[i+1][j]==1 and matriz[i][j-1]==1 and matriz[i+1][j-1]==1:
                            matriz[i][j]=1
                            

                #esquina inferior derecha
                elif i ==final and j==final:
                    if matriz[i-1][j]==1 and matriz[i][j-1]==1 and matriz[i-1][j-1]==1:
                            matriz[i][j]=1

                #pared izquierda
                elif i>0 and i<final and j==0 :
                    if (matriz[i-1][j]==1 and matriz[i-1][j+1]==1 and matriz[i][j+1]==1
                    or matriz[i-1][j+1]==1 and matriz[i][j+1]==1 and matriz[i+1][j+1]==1
                    or matriz[i][j+1]==1 and matriz[i+1][j+1]==1 and matriz[i+1][j]==1):
                        CoordenadasX_Sanas.append(j)
                        CoordenadasY_Sanas.append(i)
                            
                #pared superior
                elif i==0 and j>0 and j<final:
                    if (matriz[i][j-1]==1 and matriz[i+1][j-1]==1 and matriz[i+1][j]==1 
                    #  abajo - abajo derecha - derecha 
                    or matriz[i+1][j]==1 and matriz[i+1][j+1]==1 and matriz[i][j+1]==1
                    #solo abajo
                    or matriz[i+1][j]==1 and matriz[i+1][j+1]==1 and matriz[i+1][j-1]==1
                    ):
                        CoordenadasX_Sanas.append(j)
                        CoordenadasY_Sanas.append(i)
                #pared derecha
                elif i>0 and i <final and j==final :
                    if (matriz[i-1][j]==1 and matriz[i-1][j-1]==1 and matriz[i][j-1]==1
                    or matriz[i-1][j-1]==1 and matriz[i][j-1]==1 and matriz[i+1][j-1]==1
                    or matriz[i][j-1]==1 and matriz[i+1][j-1]==1 and matriz[i+1][j]==1):
                        CoordenadasX_Sanas.append(j)
                        CoordenadasY_Sanas.append(i)
                #pared inferior
                elif i==final and j>0 and j<final:
                    if (matriz[i][j-1]==1 and matriz[i-1][j-1]==1 and matriz[i-1][j]==1 
                    
                    or matriz[i-1][j]==1 and matriz[i-1][j+1]==1 and matriz[i][j+1]==1
                    #solo abajo
                    or matriz[i-1][j]==1 and matriz[i-1][j+1]==1 and matriz[i-1][j-1]==1
                    ):
                        CoordenadasX_Sanas.append(j)
                        CoordenadasY_Sanas.append(i) 
                else:    
                    # izquierda - izquierda abajo   abajo
                    if (matriz[i][j-1]==1 and matriz[i+1][j-1]==1 and matriz[i+1][j]==1):
                         CoordenadasX_Sanas.append(j)
                         CoordenadasY_Sanas.append(i)
                    #   abajo - abajo derecha - derecha 
                    elif matriz[i+1][j]==1 and matriz[i+1][j+1]==1 and matriz[i][j+1]==1:
                        CoordenadasX_Sanas.append(j)
                        CoordenadasY_Sanas.append(i)
                    # izquierda - izquierda arriba - arriba
                    elif matriz[i][j-1]==1 and matriz[i-1][j-1]==1 and matriz[i-1][j]==1 :  
                        CoordenadasX_Sanas.append(j)
                        CoordenadasY_Sanas.append(i)            
                    #arriba - arriba derecha - derecha
                    elif matriz[i-1][j]==1 and matriz[i-1][j+1]==1 and matriz[i][j+1]==1:
                        CoordenadasX_Sanas.append(j)
                        CoordenadasY_Sanas.append(i)
                    #todo arriba
                    elif matriz[i-1][j]==1 and matriz[i-1][j+1]==1 and matriz[i-1][j-1]==1:
                        CoordenadasX_Sanas.append(j)
                        CoordenadasY_Sanas.append(i)
                         
                    #todo abajo
                    elif matriz[i+1][j]==1 and matriz[i+1][j+1]==1 and matriz[i+1][j-1]==1:
                        CoordenadasX_Sanas.append(j)
                        CoordenadasY_Sanas.append(i)
                        
                    #todo izquierda
                    elif matriz[i-1][j-1]==1 and matriz[i][j-1]==1 and matriz[i+1][j-1]==1:
                        CoordenadasX_Sanas.append(j)
                        CoordenadasY_Sanas.append(i)
                          
                    #todo derecha
                    
                    elif matriz[i-1][j+1]==1 and matriz[i][j+1]==1 and matriz[i+1][j+1]==1:
                        CoordenadasX_Sanas.append(j)
                        CoordenadasY_Sanas.append(i)

            #CONTAGIADAS ------------------------------------------------------------------------------------------------------------------------------------------------                                    
            elif matriz[i][j]==1:
                    if i == 0 and j == 0:
                        if matriz[i+1][j]==0 and matriz[i+1][j+1]==0 or matriz[i][j+1]==0 and matriz[i+1][j+1]==0:
                                matriz[i][j]=0
                                 
                    elif i ==final and j==0:
                        if matriz[i-1][j]==0 and matriz[i-1][j+1]==0 or matriz[i][j+1]==0 and matriz[i-1][i+1]:
                            matriz[i][j]=0

                    elif i ==0 and j==final:
                        if matriz[i+1][j]==0 and matriz[i+1][j-1]==0 or matriz[i][j-1]==0 and matriz[i+1][j-1]==0:
                            matriz[i][j]=0
                    
                    elif i ==final and j==final:
                        if matriz[i-1][j]==0 and matriz[i-1][j-1]==0 or matriz[i][j-1]==0 and matriz[i-1][j-1]==0:
                            matriz[i][j]=0
                    #pared izquierda
                    elif i>0 and i<final and j==0 :
                         if (matriz[i-1][j]==0 and matriz[i-1][j+1]==0 or matriz[i-1][j+1]==0 and matriz[i][j+1]==0
                            or matriz[i][j+1]==0 and matriz[i+1][j+1]==0 or matriz[i+1][j+1]==0 and matriz[i+1][j]==0):
                                CoordenadasX_Contagiadas.append(j)
                                CoordenadasY_Contagiadas.append(i)
                    #pared superior
                    elif i==0 and j>0 and j<final:
                        if (matriz[i][j-1]==0 and matriz[i+1][j-1]==0 or matriz[i+1][j-1]==0 and  matriz[i+1][j]==0 
                        or matriz[i+1][j]==0 and matriz[i+1][j+1]==0 or matriz[i+1][j+1]==0 and matriz[i][j+1]==0 ):
                            CoordenadasX_Contagiadas.append(j)
                            CoordenadasY_Contagiadas.append(i)
                    #pared derecha
                    elif i>0 and i <final and j==final :
                        if (matriz[i-1][j]==0 and matriz[i-1][j-1]==0 or matriz[i-1][j-1]==0 and  matriz[i][j-1]==0
                        or matriz[i][j-1]==0 and matriz[i+1][j-1]==0 or matriz[i+1][j-1]==0 and  matriz[i+1][j]==0):
                            CoordenadasX_Contagiadas.append(j)
                            CoordenadasY_Contagiadas.append(i)   

                    elif i==final and j>0 and j<final:
                        if (matriz[i][j-1]==0 and matriz[i-1][j-1]==0 or matriz[i-1][j-1]==0 and matriz[i-1][j]==0 
                        or matriz[i-1][j]==0 and matriz[i-1][j+1]==0 or matriz[i-1][j+1]==0 and matriz[i][j+1]==0):
                            CoordenadasX_Contagiadas.append(j)
                            CoordenadasY_Contagiadas.append(i)
                    else:    
                        if (matriz[i-1][j]==0 and matriz[i-1][j+1]==0 and matriz[i][j+1]==0 and matriz[i+1][j+1]==0
                        and matriz[i+1][j]==0 and matriz[i+1][j-1]==0 and matriz[i][j-1]==0 and matriz[i-1][j-1]==0):
                            CoordenadasX_Contagiadas.append(j)
                            CoordenadasY_Contagiadas.append(i)
                        else:
                            if matriz[i-1][j-1]==1:
                                if (matriz[i-1][j]==1 or matriz[i-1][j+1]==1 or matriz[i][j+1]==1 or matriz[i+1][j+1]==1
                                    or matriz[i+1][j]==1 or matriz[i+1][j-1]==1 or matriz[i][j-1]==1):
                                    continue  
                                else:
                                    CoordenadasX_Contagiadas.append(j)
                                    CoordenadasY_Contagiadas.append(i)
                            elif matriz[i-1][j]==1:
                                if (matriz[i-1][j-1]==1 or matriz[i-1][j+1]==1 or matriz[i][j+1]==1 or matriz[i+1][j+1]==1
                                    or matriz[i+1][j]==1 or matriz[i+1][j-1]==1 or matriz[i][j-1]==1):
                                    continue  
                                else:
                                    CoordenadasX_Contagiadas.append(j)
                                    CoordenadasY_Contagiadas.append(i)
                            elif matriz[i-1][j+1]==1:
                                if (matriz[i-1][j-1]==1 or matriz[i-1][j]==1 or matriz[i][j+1]==1 or matriz[i+1][j+1]==1
                                    or matriz[i+1][j]==1 or matriz[i+1][j-1]==1 or matriz[i][j-1]==1):
                                    continue  
                                else:
                                    CoordenadasX_Contagiadas.append(j)
                                    CoordenadasY_Contagiadas.append(i)
                            elif matriz[i][j+1]==1:
                                if (matriz[i-1][j-1]==1 or matriz[i-1][j]==1 or matriz[i-1][j+1]==1 or matriz[i+1][j+1]==1
                                    or matriz[i+1][j]==1 or matriz[i+1][j-1]==1 or matriz[i][j-1]==1):
                                    continue  
                                else:
                                    CoordenadasX_Contagiadas.append(j)
                                    CoordenadasY_Contagiadas.append(i)
                            elif matriz[i+1][j+1]==1:
                                if (matriz[i-1][j-1]==1 or matriz[i-1][j]==1 or matriz[i-1][j+1]==1 or matriz[i][j+1]==1
                                    or matriz[i+1][j]==1 or matriz[i+1][j-1]==1 or matriz[i][j-1]==1):
                                    continue  
                                else:
                                    CoordenadasX_Contagiadas.append(j)
                                    CoordenadasY_Contagiadas.append(i)
                            elif matriz[i+1][j]==1:
                                if (matriz[i-1][j-1]==1 or matriz[i-1][j]==1 or matriz[i-1][j+1]==1 or matriz[i][j+1]==1
                                    or matriz[i+1][j+1]==1 or matriz[i+1][j-1]==1 or matriz[i][j-1]==1):
                                    continue  
                                else:
                                    CoordenadasX_Contagiadas.append(j)
                                    CoordenadasY_Contagiadas.append(i)
                            elif matriz[i+1][j]==1:
                                if (matriz[i-1][j-1]==1 or matriz[i-1][j]==1 or matriz[i-1][j+1]==1 or matriz[i][j+1]==1
                                    or matriz[i+1][j+1]==1 or matriz[i+1][j-1]==1 or matriz[i][j-1]==1):
                                    continue  
                                else:
                                    CoordenadasX_Contagiadas.append(j)
                                    CoordenadasY_Contagiadas.append(i)
                            elif matriz[i+1][j-1]==1:
                                if (matriz[i-1][j-1]==1 or matriz[i-1][j]==1 or matriz[i-1][j+1]==1 or matriz[i][j+1]==1
                                    or matriz[i+1][j+1]==1 or matriz[i+1][j]==1 or matriz[i][j-1]==1):
                                    continue  
                                else:
                                    CoordenadasX_Contagiadas.append(j)
                                    CoordenadasY_Contagiadas.append(i)
                            elif matriz[i][j-1]==1:
                                if (matriz[i-1][j-1]==1 or matriz[i-1][j]==1 or matriz[i-1][j+1]==1 or matriz[i][j+1]==1
                                    or matriz[i+1][j+1]==1 or matriz[i+1][j]==1 or matriz[i+1][j-1]==1):
                                    continue  
                                else:
                                    CoordenadasX_Contagiadas.append(j)
                                    CoordenadasY_Contagiadas.append(i)                        
    for i in range(len(CoordenadasY_Sanas)):
        matriz[CoordenadasY_Sanas[i]][CoordenadasX_Sanas[i]]=1 
    for i in range(len(CoordenadasY_Contagiadas)):
        matriz[CoordenadasY_Contagiadas[i]][CoordenadasX_Contagiadas[i]]=0

                        
def eleccion(opcion):
    while True:
        try:
            entrada = int(input())
            return entrada
        except:
            print("La opción ingresada no es válida\n"+
                  "Intentelo de nuevo")
            if opcion==1:
                Menu_Principal()
            if opcion==2:
                MenuPacientes()
            for i in range(len(Lista)):
                if ids[i] == opcion:
                    MenuInvestigacion(opcion)
                
def MenuInvestigacion(paciente):
    
    print("\n▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
    print("|  Investigación epidemilógica de Guatemala  |")
    print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    print("|--------------------------------------------|")
    for i in range(len(Lista)):
        if paciente==ids[i]:
            print("|  Paciente:",Lista[ids[i]-1][0],"  periodo: ",Contador_Periodos,"/",Lista[ids[i]-1][2],"       |")
    print("|         1. Avanzar un periodo              |")
    print("|         2. Avanzar de forma automática     |")
    print("|         3. Graficar estado actual          |")
    print("|         0.    Regresar                     |")
    print("|============================================|\n")
    print("Escoja una opción marcando el número asignado.")      


def MenuPacientes():
        print("\n▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
        print("|  Investigación epidemilógica de Guatemala  |")
        print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
        print("|-----------------Pacientes------------------|")
        for i in range(len(Lista)):
            print("|     #",ids[i]," Nombre: ",Lista[i][0]," Edad: ",Lista[i][1],"         |")
        print("|                                            |")
        print("|             0.   Regresar                  |")
        print("|============================================|\n")
        print("Escoja el paciente con el número asignado.")

def Menu_Principal():
        print("\n▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
        print("|  Investigación epidemilógica de Guatemala  |")
        print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
        print("|-------------------Menú---------------------|")
        print("|             1. Cargar archivo              |")
        print("|             2.   Iniciar                   |")
        print("|             3.   Generar reporte           |")
        print("|             0.    Salir                    |")
        print("|============================================|\n")
        print("Escoja una opción marcando el número asignado.")
            
while Menu:
    Menu_Principal()
    opcion=eleccion(1) 
    if opcion==1:
        print("Cargue su archivo")
        CargarDatos()
        print("Carga completada")


    elif opcion==2:
        Matriz=ListaEn()
        if len(Lista)>0:
            print("--Entrando al registro de pacientes--")
            ver_pacientes = True
            while ver_pacientes:
                MenuPacientes()
                opcion=eleccion(2)
                if opcion==0:
                        ver_pacientes=False
                elif opcion>len(ids):
                    print("paciente no encontrado")
                
                else:
                    for i in range(len(Lista)):
                        if opcion==ids[i]:
                            Contador_Periodos= 1
                            paciente = Lista[opcion-1][0]
                            edad = Lista[opcion-1][1]
                            periodo = int (Lista[opcion-1][2])
                            t= Lista[opcion-1][3]
                            codigo = opcion
                            
                            Crear_Matriz(codigo)
                            Agregar_al_Reporte(paciente,edad,str(periodo),t)
                            Investigacion=True
                            break
                    while Investigacion:
                            
                            MenuInvestigacion(codigo)
                            opcion= eleccion(codigo)
                            
                            if (opcion==0):
                                Investigacion=False
                                ver_pacientes=False
                                Matriz=NULL

                            elif opcion==1:
                                Contador_Periodos+=1
                                Nuevo_periodo(Matriz)
                            elif opcion==2:
                                
                                Periodos_Auto(Matriz,Contador_Periodos, periodo)
                            elif opcion==3:
                                Graficar(Matriz,paciente)
        else:
            print("[ERROR] Primero cargue un archivo")      
    elif opcion==3:
        Generar()
    elif opcion==0:
        print("Saliendo...")      
        Menu=False
    
        

    
     
   
     



       
        

    