import re
import sys
import os

search = True

def searchAndReplace(fileToSearchOn, textToBeReplaced, replacementText): 
    try:
        with open(fileToSearchOn, 'r') as file:
            targetFile = file.read()

        newContent, count = re.subn(textToBeReplaced, replacementText, targetFile)

        with open(fileToSearchOn, 'w') as file:
            file.write(newContent)

        if count > 0:
            print(f"\nReemplazo completado. Se han reemplazado {count} instancias de {textToBeReplaced}.\n")
        else:
            print(f'No se ha encontrado ninguna instancia de "{textToBeReplaced}" en el archivo {fileToSearchOn}')

    except FileNotFoundError:
        print(f'Error: No se ha encontrado el archivo "{fileToSearchOn}".')
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def verifyFile():
    while True:
        fileToSearchOn = input("Ingresa el archivo en el cual quieres remplazar texto: ").strip()
        
        if os.path.isfile(fileToSearchOn):
            return fileToSearchOn
        else:
            print(f'Error: No se ha encontrado el archivo "{fileToSearchOn}" en el directorio actual.')
        
        
    
while search == True:
    userChoise = input("Quieres reemplazar texto en uno de los archivos? (y/n): ").lower()
        
    if userChoise == "y":
        fileToSearchOn = verifyFile()
        textToBeReplaced = input("Escribe el texto que quieres buscar y reemplazar en uno de los archivos del directorio: ").strip()
        replacementText = input("Escribe el texto con el quieres reemplazar el anterior: ").strip()
        
        searchAndReplace(fileToSearchOn, textToBeReplaced, replacementText)
    elif userChoise == "n":
        search = False
        print("Programa finalizado")
        break
    else:
        print("La opcion ingresada no es valida")

    
    
   

    
