def main():
    i = 1
    while True
        # solange Zutaten weniger als 10
        if i <= 10:
            
            ingredientname = str(input('Name der Zutat? ')                                 
            # wenn Zutatenabfrage mit Enter abbrechen
            if ingredientname == '' :
                # Solange Zutaten weniger als 10
                while i <= 10:
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
                    
                try ingredientquan = float(input('Menge der Zutat? '))
                                           
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
                
                
                
                
                
                
                
                
                