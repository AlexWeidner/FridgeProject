# mach die print funktion für Python 2.x nutzbar
from __future__ import print_function
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
# erstelle eine Funktion mit dem Namen scan die keine Argumente erwartet
def scan():
    # erstellt eine Dauerschleife die den code so lange ausführt bis dieser einen abbruch über ValueError oder korrekter Ausgabe (break) erzwingt
    while True:
        # Wenn die Eingabe ein Integer ist wird die Variable 'code' beschrieben, wenn nicht wird die Funktion ValueError gecalled
        # Die Endung _raw wird für alle Variablen verwendet die danach noch umgewandelt werden sollen
        try:   
            code_raw = int(input("Bitte Barcode einscannen: "))
        except ValueError:                                 
            print("ungültiger Barcode")
        else:
            #code in einen string wandeln um ihn als string in eine .txt-Datei zu speichern und um den String mit der vorhandenen Liste zu vergleichen
            code = str(code_raw)
            # der in code gespeicherte Barcode wird in der .txt-Datei gesucht und das ergebnis in matched_lines gespeichert
            matched_lines = search_string_in_file('/home/pi/Desktop//data.txt',code)
            #if code ist nicht vorhanden dann weitermachen ansonsten: jump to add
            if len(matched_lines) == 0 :
                name = str(input("Produktname? "))
                try:  
                    inhalt_raw = int(input("Füllmenge? "))  
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
                            mhdmod_raw = int(input("Wie lange ist der Artikel nach dem Öffnen haltbar? "))
                        except ValueError:
                            print("Eingabe ist keine Zahl")
                        else:
                            mhdmod = str(mhdmod_raw)
                            # die manuellen Eingaben werden in eine .txt-Datei auf dem Desktop geschrieben
                            # dabei gilt: data.txt enthält alle bestehenden Daten die in clone.txt zusammen
                            # mit den neuen Daten geschrieben werden. Danach ersetzt clone.txt den inhalt von data.txt
                            # der inhalt von clone.txt wird beim nächsten Programmaufruf überschrieben
                            
                            data_path = '/home/pi/Desktop//data.txt'
                            data_file = open(data_path,'r')
                            data = data_file.read()

                            clone_path = '/home/pi/Desktop//clone.txt'
                            clone_file = open(clone_path,'w')
                            
                            # Alle vorherigen Daten werden in clone.txt übernommen

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
                            # schließt data.txt und clone.txt. Alle neuen Daten sind jetzt nur in clone.txt enthalten

                            data_file.close()
                            clone_file.close()
                            
                            # öffnet data.txt und clone.txt erneut wobei jetzt der Inhalt von clone.txt gelesen und in data.txt geschrieben wird
                            
                            clone_file = open(clone_path,'r')
                            clone = clone_file.read()

                            data_file = open(data_path,'w')
                            data_file.write(clone)
                            
                            clone_file.close()
                            data_file.close()
                            
                            print("Folgendes Produkt wurde hinzugefügt: \n","Barcode :",code,"\n","Name :",name,"\n","Füllmenge in",einheit,":",inhalt,"\n","Preis :",preis,"\n","Tage haltbar nach Anbruch :",mhdmod)
            else:
                # Die Zeile in der der Barcode gefunden wurde wird durch elem[0] in zeile_code geschrieben
                for elem in matched_lines:
                    zeile_code = elem[0]
                    # Da die Reihenfolge der Informationen immer gleich ist und die vorhandene Menge eines Produktes an letzter Stelle des Eintrags stehen soll
                    # wird die Position des Codes + 6 genommen um den Eintrag für die Menge zu bekommen
                    zeile_anzahl = int(zeile_code) + 5
                    a_file = open('/home/pi/Desktop//data.txt','r')
                    list_of_lines = a_file.readlines()
                    # Die bisherige Menge wird in der Variable übertrag gespeichert um nachfolgend um 1 erhöht zu werden, danach wird die Datei wieder geschlossen
                    übertrag_raw = list_of_lines[zeile_anzahl]
                    übertrag_raw_2 = übertrag_raw.rstrip('\n')
                    übertrag_int = int(übertrag_raw_2)
                    übertrag = übertrag_int + 1
                    
                    # wandlung von int auf str um mit open('pfad','w') schreiben zu können
                    list_of_lines[zeile_anzahl] = str(übertrag) + '\n'
                    a_file = open('/home/pi/Desktop//data.txt','w')
                    a_file.writelines(list_of_lines)
                    a_file.close()
                print('Anzahl wurde um 1 erhöht')
            break
        
scan()