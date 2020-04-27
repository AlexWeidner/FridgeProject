# FridgeProject
Use a Raspberry Pi and a Barcode Scanner to manage my fridge.

The Raspberry Pi gets input from a Barcode Scanner (and maybe a numpad with T9 ???)

Example how this should work:

Add function:
1) Scan function code
2) Scan Barcode of a product => 20004002\n
3) Programm will check if there is already an entry in data.txt using this barcode
    a) product is known => Add +1 to quantity
    b) product is new => get data on this product from userinputs then add them to data.txt
    
Remove function: 
1) Scan function code
2) Scan Barcode of a product => 20004002\n
3) Program will check if there is already an entry in data.txt using this barcode
4) If an entry exists it will ask to scan another barcode to define how much will be removed
5) Check if quantity is dividable by packaging unit to determine if there will be an open package
6) if an open package is detected the MHD/BBD will be altered by 'mhdmod' to reflect the new date it expires
7) if there is no open package left after removing a product the MHD/BBD will jump to the next date.

Compare function:
1) If neither Add nor Remove functions are currently operating, the programm will compare the existing products and their respecting quantities to a list of recipies and display only those recipies that are currently craftable using only products that are recorded.

