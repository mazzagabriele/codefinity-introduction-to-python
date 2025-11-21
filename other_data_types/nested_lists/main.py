#lista prodotti
vegetables = ["tomatoes","potatoes","onions"]

#rimuovi cipolle
vegetables.remove("onions")

#aggiungi carote se non presenti
if "carrots" in vegetables:
    print("Carrots are already in the list")
else: 
     vegetables.append("carrots")

#aggiungi cetrioli se non presenti
if "cucumbers" in vegetables:
    print("Cucumbers are already in the list")
else: 
     vegetables.append("cucumbers")

#ordina lista
vegetables.sort()

# stampa lista aggiornata dei prodotti
print("Updated Vegetable Inventory: ", vegetables)
