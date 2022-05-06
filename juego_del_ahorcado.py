import random
from string import ascii_lowercase
import os

def sin_acentos(palabra):
    palabra = palabra.upper()
    c_acento=['Á','É','Í','Ó','Ú']
    s_acento=['A','E','I','O','U']
    
    ent = {k: i for i, k in enumerate(c_acento)}
    result = list(map(ent.get,palabra))
    for i in range(len(result)):
        if result[i]!=None:
            palabra = palabra.replace(palabra[i],s_acento[result[i]]) 
    return palabra
    
    print("List_2 after replacement: ",result)
    print(palabra)

    
    
    return palabra

def eleccion(num):
    if num == 0:
        print("                                  ")                                
        print("                                  ")      
        print("                                  ")                  
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")

    if num == 1:
        print("                                  ")                                
        print("          MMMMMMMMMMMMMM          ")      
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")                  
        print("        ▓▓              ▓▓        ")
        print("        ▓▓    ▓    ▓    ▓▓        ")
        print("        ▓▓   ╔══════╗   ▓▓        ")
        print("        ▓▓   ╚══════╝   ▓▓        ")
        print("        ▓▓              ▓▓        ")
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")

    if num == 2:
        print("                                  ")                                
        print("          MMMMMMMMMMMMMM          ")      
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")                  
        print("        ▓▓              ▓▓        ")
        print("        ▓▓    ▓    ▓    ▓▓        ")
        print("        ▓▓   ╔══════╗   ▓▓        ")
        print("        ▓▓   ╚══════╝   ▓▓        ")
        print("        ▓▓              ▓▓        ")
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
    
    if num == 3:
        print("                                  ")                                
        print("          MMMMMMMMMMMMMM          ")      
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")                  
        print("        ▓▓              ▓▓        ")
        print("        ▓▓    ▓    ▓    ▓▓        ")
        print("        ▓▓   ╔══════╗   ▓▓        ")
        print("        ▓▓   ╚══════╝   ▓▓        ")
        print("        ▓▓              ▓▓        ")
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("         ▓▓▓▓▓▓▓▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        
    if num == 4:
        print("                                  ")                                
        print("          MMMMMMMMMMMMMM          ")      
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")                  
        print("        ▓▓              ▓▓        ")
        print("        ▓▓    ▓    ▓    ▓▓        ")
        print("        ▓▓   ╔══════╗   ▓▓        ")
        print("        ▓▓   ╚══════╝   ▓▓        ")
        print("        ▓▓              ▓▓        ")
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")
        print("                                  ")

    if num == 5:
        print("                                  ")                                
        print("          MMMMMMMMMMMMMM          ")      
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")                  
        print("        ▓▓              ▓▓        ")
        print("        ▓▓    ▓    ▓    ▓▓        ")
        print("        ▓▓   ╔══════╗   ▓▓        ")
        print("        ▓▓   ╚══════╝   ▓▓        ")
        print("        ▓▓              ▓▓        ")
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓▓               ")
        print("                   ▓▓             ")
        print("                    ▓▓            ")
        print("                     ▓▓           ")
        print("                      ▓▓          ")
        print("                       ▓▓         ")
        print("                                  ")

    if num == 6:                             
        print("                                  ")                                
        print("          MMMMMMMMMMMMMM          ")      
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")                  
        print("        ▓▓              ▓▓        ")
        print("        ▓▓    -    -    ▓▓        ")
        print("        ▓▓              ▓▓        ")
        print("        ▓▓     ____     ▓▓        ")
        print("        ▓▓              ▓▓        ")
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("              ▓▓▓▓▓▓              ")
        print("            ▓▓  ▓▓  ▓▓            ")
        print("           ▓▓   ▓▓   ▓▓           ")
        print("          ▓▓    ▓▓    ▓▓          ")
        print("         ▓▓     ▓▓     ▓▓         ")
        print("                ▓▓                ")
        print("               ▓▓▓▓               ")
        print("             ▓▓    ▓▓             ")
        print("            ▓▓      ▓▓            ")
        print("           ▓▓        ▓▓           ")
        print("          ▓▓          ▓▓          ")
        print("         ▓▓            ▓▓         ")
        print("                                  ")

    if num == 7:                             
        print("            ¡¡YOU WIN!!           ")   
        print("                                  ")                             
        print("          MMMMMMMMMMMMMM          ")      
        print("          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ")                  
        print("        ▓▓              ▓▓        ")
        print("        ▓▓    O    O    ▓▓        ")
        print("        ▓▓     ____     ▓▓        ")
        print("        ▓▓    (____)    ▓▓        ")
        print("        ▓▓              ▓▓        ")
        print("   ▓▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓   ")
        print("     ▓▓         ▓▓         ▓▓     ")
        print("       ▓▓       ▓▓       ▓▓       ")
        print("         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("                ▓▓                ")
        print("               ▓▓▓▓               ")
        print("             ▓▓    ▓▓             ")
        print("            ▓▓      ▓▓            ")
        print("           ▓▓        ▓▓           ")
        print("          ▓▓          ▓▓          ")
        print("         ▓▓            ▓▓         ")
        print("                                  ")

def run():
    data = []
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        #for linea in data: #otra forma de recuperar palabras de un archivo -->lista
            #print(linea)
        data=list(enumerate(f))  #Crear lista a partir de archivo   
    print(len(data))
    r = random.randint(0,len(data)-1)
    word = data[r]
    word = str(word[1])
    word = word.upper()
    word = word.strip()
    word = sin_acentos(word) # Funcion quita acentos
    founded = ["_" for i in range(len(word))] 
    fail=0
    bandera=False
    elegidas = []
    
    while(fail<6):
        # Menu principal
        os.system("cls")
        print("Letras ya elegidas: ",elegidas)
        print("\n\n")
        eleccion(fail)  # funcion
        print("Adivina la palabra\n\n")
        print(founded)
        print("\n")
        letra = input("Dame una letra: ")
        letra = letra.upper()
        
        #Validacion
        assert letra.isalpha(), "Solo letras, no numeros"
        if(len(letra)!=1):
            print("Solo agrega una letra")
            continue
        
        # Mostrar letras ya ingresadas
        if(len(elegidas)==0):
            elegidas.append(letra)
        else:
            elegidas.append(letra)
            elegidas = list(dict.fromkeys(elegidas))
        
        # Comprueba la letra con las letras de la palabra a adivinar        
        for l in range(len(word)):
            if letra == word[l]:
                founded[l]=letra
                bandera=True
                
        # Si no hay coincidencias
        if bandera == False:        
            fail = fail+1
            
        # Si las hay, reinicio bandera "encontre una coincidencia"
        else:
            bandera = False
        
        # Si se encontro la palabra
        if word == "".join(founded):
            fail = 7
            os.system("cls")
            eleccion(fail)
            print("\n")
            print(founded)
        
        # Si no se encontró
        if fail == 6:
            os.system("cls")
            eleccion(fail)
            print("\n")
            print(founded)
            print("\n\nRespuesta correcta: ",word)
    
    
        
        
    
    
    #days = {"Mon","Tue","Wed","Thu"}
    #enum_days = enumerate(days)
    #enum_days = enumerate(days,5)
    #print(list(enum_days))
    
    ''' for enum_days in enumerate(days):
        print(enum_days) '''
    
    ''' for count,enum_days in enumerate(days,5):
        print(count,enum_days) '''


if __name__ == '__main__':
    run()