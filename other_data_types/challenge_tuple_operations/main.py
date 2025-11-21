# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# conteggio mele
apple_count = shelf.count("apples")
print ("Number of Apples: ", apple_count)

#indice banana
banana_index = shelf.index("bananas")
print ("First Banana Index: ", banana_index)

#verifica numero delle mele
if apple_count < 5:
    print ("Apples need to be restocked.")
else:
    print ("Apples are sufficiently stocked.")

#conteggio uva
grapes_count = shelf.count("grapes")
#verifica conteggio uva
if grapes_count == 1:
    print ("Grapes need to be restocked.")
else:
    print ("Grapes are sufficiently stocked.")

#indice arance
oranges_index = shelf.index("oranges")
oranges = "oranges"
if oranges in shelf:
    print ("Oranges are at index: ", oranges_index)
else:
    print("Oranges are out of stock")
    