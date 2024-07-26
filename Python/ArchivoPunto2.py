import os
import shutil

menu = True

def displayMenu():
    print("\nMenu:")
    print("1) Ver los archivos en el directorio actual")
    print("2) Copiar un archivo en el directorio actual")
    print("3) Borrar un archivo en el directorio actual")
    print("4) Salir")

def viewFiles():
    print("\nArchivos en el directorio actual:")
    for file in os.listdir():
        print(file)

def copyFile():
    fileName = input("\nIngresa el nombre del archivo que quieres copiar: ")
    if os.path.exists(fileName):
        newName = input("Ingresa el nombre del nuevo archivo: ")
        shutil.copy(fileName, newName)
        print(f"{fileName} ha sido copiado a {newName}")
    else:
        print(f"Error: {fileName} no existe en el directorio actual.")

def deleteFile():
    fileName = input("Ingresa el nombre del archivo que quieres borrar: ")
    if os.path.exists(fileName):
        os.remove(fileName)
        print(f"{fileName} ha sido borrado.")
    else:
        print(f"Error: {fileName} no existe en el directorio actual.")



while menu == True:
    displayMenu()
    choice = input("\nElige la accion que quieres realizar: ")

    if choice == '1':
        viewFiles()
    elif choice == '2':
        copyFile()
    elif choice == '3':
        deleteFile()
    elif choice == '4':
        print("\nPrograma finalizado")
        menu = False
        break
    else:
        print("\nLa opcion ingresada no es valida.")


