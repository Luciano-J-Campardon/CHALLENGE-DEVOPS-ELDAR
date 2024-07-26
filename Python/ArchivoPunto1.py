import os

search = True
userChoise = ""

def searchFiles(word):
    foundFiles = []
    currentDirectory = os.getcwd()
    
    for file in os.listdir(currentDirectory):
        if os.path.isfile(file):
            try:
                with open(file, 'r', encoding='utf-8') as currentFile:
                    if word.lower() in currentFile.read().lower():
                        foundFiles.append(file)
            except Exception as e:
                print(f"Error leyendo {file}: {e}")
    
    return foundFiles

def main():
    word = input("Escribe la palabra que quieres buscar:")
    matchingFiles = searchFiles(word)
    
    if matchingFiles:
        print(f'Los archivos que contienen la palabra "{word}" son:')
        for file in matchingFiles:
            print(file)
    else:
        print(f'No se han encontrado archivos que contengan la palabra "{word}".')
        
        
        
while search == True:
    userChoise = input("Queres buscar una palabra en los archivos del directorio local?(y/n): ").lower()
    
    if userChoise == "y":
        main()
    elif userChoise == "n":
        search = False
        print("Programa finalizado")
        break
    else:
        print("La opcion ingresada no es valida")
    
            
                
