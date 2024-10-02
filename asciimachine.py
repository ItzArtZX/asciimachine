import os
import cowsay
from pyfiglet import Figlet
import pyperclip


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    
    clear_screen()

    
    print("1) Cowsay")
    print("2) Pyfiglet")
    print("3) Pyfiglet (with font input)")
    print("4) Exit")
    
    
    choice = input(" >>> ")

    
    clear_screen()

    if choice == "1":
        print("Enter text for Cowsay:")
        cowinput = input(" >>> ")
        cowsay_output = cowsay.get_output_string('cow', cowinput)
        print(cowsay_output)
        pyperclip.copy(cowsay_output)  
        print("\nText has been copied to clipboard!")

    elif choice == "2":
        print("Enter text for Pyfiglet:")
        figletinput = input(" >>> ")
        f = Figlet()
        pyfiglet_output = f.renderText(figletinput)
        print(pyfiglet_output)
        pyperclip.copy(pyfiglet_output)  
        print("\nText has been copied to clipboard!")

    elif choice == "3":
        print("Enter text for Pyfiglet:")
        figletinput = input(" >>> ")
        print("Enter font (e.g., 'slant', 'block', etc.):")
        fontinput = input(" >>> ")
        try:
            f = Figlet(font=fontinput)
            pyfiglet_output = f.renderText(figletinput)
            print(pyfiglet_output)
            pyperclip.copy(pyfiglet_output)  
            print("\nText has been copied to clipboard!")
        except Exception as e:
            print(f"Error: {e}. Font not found.")
    
    elif choice == "valid option":
        print("Hello. This is an easter egg in the app!")

    elif choice == "4":
        break  

    else:
        print("Invalid choice. Please select valid option!")
    
    input("\nPress Enter to continue...")