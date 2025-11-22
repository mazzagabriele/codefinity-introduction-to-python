#definizione del dizionario
grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

#dettagli del prodotto pane
bread_details = grocery_inventory.get("Bread")

#aggiungere prodotto torta
grocery_inventory.update({"Cookies":(143, "Bakery")})

#stampe
print("Details of Bread: ", bread_details)
print("Inventory after adding Cookies: ", grocery_inventory)

#rimuovere uova
grocery_inventory.pop("Eggs")

#nuova stampa
print ("Inventory after removing Eggs: ", grocery_inventory)