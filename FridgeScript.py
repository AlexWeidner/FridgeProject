# macht die print funktion fr Python 2 nutzbar
from __future__ import print_function
# sudo pip3 install keyboard um keyboard modul zu installieren
import keyboard
import time
# script muss als sudo python3 /home/pi/Desktop/FridgeScript.py gestartet werden

# todo: Timeout zu jeder Userinput aufforderung erstellen die bei ablauf mode = 0 setzt

# erstelle eine Funktion mit dem Namen xxx die einen Dateipfad und einen String erwartet
def search_string_in_file(file_name, string_to_search):
    line_number = 0
    list_of_results = []    
    with open(file_name, 'r') as read_obj:    
        for line in read_obj:
            line_number +=1
            if string_to_search in line:
                list_of_results.append((line_number, line.rstrip()))
    return list_of_results

def createitem(code):
    name = str(input("Produktname? "))
    try:  
        inhalt_raw = float(input("Inhalt? "))  
    except ValueError:
        print("Eingabe ist keine Zahl")
    else:
        inhalt = str(inhalt_raw)
        einheit = input("Einheit? ")
        try:                
            preis_raw = float(input("Preis in EUR? "))
        except ValueError:
            print("Eingabe ist keine Zahl")
        else:
            preis = str(preis_raw)
            try:
                mhdmod_raw = int(input("Wie lange ist der Artikel nach dem Anbruch haltbar? "))
            except ValueError:
                print("Eingabe ist keine Zahl")
            else:
                mhdmod = str(mhdmod_raw)
                # die manuellen Eingaben werden in eine .txt-Datei auf dem Desktop geschrieben
                # dabei gilt: data.txt enthalt alle bestehenden Daten die in clone.txt zusammen
                # mit den neuen Daten geschrieben werden. Danach ersetzt clone.txt den inhalt von data.txt
                # der inhalt von clone.txt wird beim nachsten Programmaufruf uberschrieben
                            
                data_path = '/home/pi/Desktop//data.txt'
                data_file = open(data_path,'r')
                data = data_file.read()

                clone_path = '/home/pi/Desktop//clone.txt'
                clone_file = open(clone_path,'w')
                            
                # Alle vorherigen Daten werden in clone.txt ubernommen

                clone_file.write(data)
                clone_file.write('\n')
                            
                # Alle statischen Werte zu dem gescannten Produkt werden in die Datei clone.txt geschrieben 
                            
                clone_file.write(code)
                clone_file.write('\n')
                clone_file.write(name)
                clone_file.write('\n')
                clone_file.write(inhalt)
                clone_file.write('\n')
                clone_file.write(einheit)
                clone_file.write('\n')
                clone_file.write(preis)
                clone_file.write('\n')
                clone_file.write(mhdmod)
                clone_file.write('\n')
                clone_file.write('0')
                clone_file.write('\n')
                # schliesst data.txt und clone.txt. Alle neuen Daten sind jetzt nur in clone.txt enthalten

                data_file.close()
                clone_file.close()
                            
                # offnet data.txt und clone.txt erneut wobei jetzt der Inhalt von clone.txt gelesen und in data.txt geschrieben wird
                            
                clone_file = open(clone_path,'r')
                clone = clone_file.read()

                data_file = open(data_path,'w')
                data_file.write(clone)
                            
                clone_file.close()
                data_file.close()
                
                print("Folgender Produkteintrag wurde erstellt: \n","Barcode :",code,"\n","Name :",name,"\n","Inhalt in",einheit,":",inhalt,"\n","Preis :",preis,"\n","Tage haltbar nach Anbruch :",mhdmod)
                    
def evaluate(code):
    matched_lines = search_string_in_file('/home/pi/Desktop//data.txt',code)
    result = len(matched_lines)
    return result

def additem(code):
    for elem in search_string_in_file('/home/pi/Desktop//data.txt',code):
                    zeile_code = elem[0]
                    # Da die Reihenfolge der Informationen immer gleich ist und die vorhandene Menge eines Produktes an letzter Stelle des Eintrags stehen soll
                    # wird die Position des Codes + 6 genommen um den Eintrag fur die Menge zu bekommen
                    zeile_anzahl = int(zeile_code) + 5
                    a_file = open('/home/pi/Desktop//data.txt','r')
                    list_of_lines = a_file.readlines()
                    # Die bisherige Menge wird in der Variable ubertrag gespeichert um nachfolgend um 1 erhoht zu werden, danach wird die Datei wieder geschlossen
                    ubertrag_raw = list_of_lines[zeile_anzahl]
                    ubertrag_raw_2 = ubertrag_raw.rstrip('\n')
                    ubertrag_int = int(ubertrag_raw_2)
                    ubertrag = ubertrag_int + 1
                    
                    # wandlung von int auf str um mit open('pfad','w') schreiben zu konnen
                    list_of_lines[zeile_anzahl] = str(ubertrag) + '\n'
                    a_file = open('/home/pi/Desktop//data.txt','w')
                    a_file.writelines(list_of_lines)
                    a_file.close()
                    print('Anzahl ist jetzt ',ubertrag)

def removeitem(code):
    fraction_raw = input('Menge die entnommen wird? ')
    fraction = float(fraction_raw.rstrip('\n'))
    for elem in search_string_in_file('/home/pi/Desktop//data.txt',code):
                    zeile_code = elem[0]
                    # Da die Reihenfolge der Informationen immer gleich ist und die vorhandene Menge eines Produktes an letzter Stelle des Eintrags stehen soll
                    # wird die Position des Codes + 6 genommen um den Eintrag fur die Menge zu bekommen
                    zeile_anzahl = int(zeile_code) + 5
                    a_file = open('/home/pi/Desktop//data.txt','r')
                    list_of_lines = a_file.readlines()
                    # Die bisherige Menge wird in der Variable ubertrag gespeichert um nachfolgend um 1 erhoht zu werden, danach wird die Datei wieder geschlossen
                    ubertrag_raw = list_of_lines[zeile_anzahl]
                    ubertrag_raw_2 = ubertrag_raw.rstrip('\n')
                    ubertrag_float = float(ubertrag_raw_2)
                    ubertrag = ubertrag_float - fraction
                    if ubertrag <= 0 :
                        print('Bestandsmenge kann nicht unter 0 fallen')
                        a_file.close()
                        break
                    else:
                    
                        # wandlung von int auf str um mit open('pfad','w') schreiben zu konnen
                        list_of_lines[zeile_anzahl] = str(ubertrag) + '\n'
                        a_file = open('/home/pi/Desktop//data.txt','w')
                        a_file.writelines(list_of_lines)
                        a_file.close()
                        print('Anzahl wurde um',fraction,'verringert')

def createrecipe(code):
    i = 1
    recipe_path = '/home/pi/Desktop//recipe.txt'
    recipe = recipe_file.read()
    recipe_file.close()                
    clone_path = '/home/pi/Desktop//clone.txt'
    clone_file = open(clone_path,'w')                
    clone_file.write(recipe)
    clone_file.write('\n')
    clone_file.write(code)
    clone_file.write('\n')
    clone_file.close()
    clone_file = open(clone_path,'r')
    clone = clone_file.read()
    clone_file.close()                
    recipe_file = open(recipe_path,'w')
    recipe_file.write(clone)                
    clone_file.close()
    recipe_file.close()
    # solange Zutaten weniger als 10
    if i <= 10 :
        try:
            ingredientname = str(input('Name der Zutat? '))                                 
        # wenn Zutatenabfrage mit Enter abbrechen
        except ingredientname == '' :
            # Solange Zutaten weniger als 10
            while i <= 10 :
                recipe_path = '/home/pi/Desktop//recipe.txt'
                recipe = recipe_file.read()
                recipe_file.close()                
                clone_path = '/home/pi/Desktop//clone.txt'
                clone_file = open(clone_path,'w')                
                clone_file.write(recipe)
                clone_file.write('\n')                
                #leere Zeile
                clone_file.write('\n')
                #leere Zeile
                clone_file.write('\n')
                #leere Zeile
                clone_file.write('\n')                             
                clone_file.close()                
                clone_file = open(clone_path,'r')
                clone = clone_file.read()
                clone_file.close()                
                recipe_file = open(recipe_path,'w')
                recipe_file.write(clone)                
                clone_file.close()
                recipe_file.close()
                print('Platzhalter ',i,'in Rezept aufgenommen')
                i = i + 1
                                 
        # wenn Zutatenname nicht abgebrochen
        else:        
                    
            try:
                ingredientquan = float(input('Menge der Zutat? '))
                                           
            except ValueError:
                print('Eingabe ist keine Zahl')                       
            else:
                ingredientquan = str(ingredientquan_raw)
                ingredientunit = str(input('Einheit der Zutat? '))
                recipe_path = '/home/pi/Desktop//recipe.txt'
                recipe = recipe_file.read()
                recipe_file.close()                
                clone_path = '/home/pi/Desktop//clone.txt'
                clone_file = open(clone_path,'w')                
                clone_file.write(recipe)
                clone_file.write('\n')                
                clone_file.write(ingredientname)
                clone_file.write('\n')
                clone_file.write(ingredientquan)
                clone_file.write('\n')
                clone_file.write(ingredientunit)
                clone_file.write('\n')                             
                clone_file.close()                
                clone_file = open(clone_path,'r')
                clone = clone_file.read()
                clone_file.close()                
                recipe_file = open(recipe_path,'w')
                recipe_file.write(clone)                
                clone_file.close()
                recipe_file.close()
                print(ingredientquan,ingredientunit,' ',ingredientname,' als Zutat aufgenommen')
                i = i + 1
                
    else:
        print('Zutatenliste komplett')
        i = 1

# erstelle eine Funktion mit dem Namen main die keine Argumente erwartet
def main():
    
    mode = 0
    # erstellt eine Dauerschleife die den code so lange ausfuhrt bis dieser einen abbruch uber ValueError oder korrekter Ausgabe (break) erzwingt 
    while True:
        # Wenn die Eingabe ein Integer ist wird die Variable 'code' beschrieben, wenn nicht wird die Funktion ValueError gecalled
        # Die Endung _raw wird fur alle Variablen verwendet die danach noch umgewandelt werden sollen    
        
        if keyboard.is_pressed('1'):
            mode = 1
            #create/add item
        elif keyboard.is_pressed('2'):
            mode = 2
            #remove/add item
        elif keyboard.is_pressed('3'):
            mode = 3
            #create/modify recipe
        elif keyboard.is_pressed('4'):
            mode = 4
        
        elif keyboard.is_pressed('5'):
            mode = 5
        
        elif keyboard.is_pressed('6'):
            mode = 6
            
        else:
        
            if mode == 1 :
        
                try:   
                    code_raw = int(input("Bitte Barcode einscannen: "))
                except ValueError:                                 
                    print("Abbruch")
                    mode = 0
                else:
                    #code in einen string wandeln um ihn als string in eine .txt-Datei zu speichern und um den String mit der vorhandenen Liste zu vergleichen
                    code = str(code_raw)
                    # der in code gespeicherte Barcode wird in der .txt-Datei gesucht und das ergebnis in matched_lines gespeichert            
                    #if code ist nicht vorhanden dann weitermachen ansonsten: jump to add
                    if evaluate(code) == 0 :
                        createitem(code)                            
                
                    else:
                        # Die Zeile in der der Barcode gefunden wurde wird durch elem[0] in zeile_code geschrieben
                        additem(code)
                
            elif mode == 2 :

                try:   
                    code_raw = int(input("Bitte Barcode einscannen: "))
                except ValueError:                                 
                    print("Abbruch")
                    mode = 0
                else:
                    #code in einen string wandeln um ihn als string in eine .txt-Datei zu speichern und um den String mit der vorhandenen Liste zu vergleichen
                    code = str(code_raw)
                    # der in code gespeicherte Barcode wird in der .txt-Datei gesucht und das ergebnis in matched_lines gespeichert
                    #if code ist nicht vorhanden dann weitermachen ansonsten: jump to add
                    if evaluate(code) == 0 :
                        createitem(code)                            
                
                    else:
                        # Die Zeile in der der Barcode gefunden wurde wird durch elem[0] in zeile_code geschrieben
                        removeitem(code)
                
            elif mode == 3 :
                
                try:   
                    code_raw = input("Bitte Rezeptname eingeben: ")
                except ValueError:                                 
                    print("Abbruch")
                    mode = 0
                else:
                    code = str(code_raw)
                    if evaluaterecipe(code) == 0 :
                        createrecipe(code)
                        mode = 0
                    else:
                        
                        #Wenn Rezept bereits vorhanden, dann modifizieren vorschlagen
                        
                        print("Rezept bereits vorhanden")
                        mode = 0
            
            elif mode == 0 :
            
                print("Warte auf Eingabe")
                time.sleep(0.5)
        
            else:
            
                time.sleep(1)

main()