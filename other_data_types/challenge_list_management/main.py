# creazione liste prodotti
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

#lista delle liste
deli_dept = [meat, cheese, condiment]
print("Initial Deli list: ", deli_dept)

#ricalcolo ammontare
meat_quantity = meat[2]
meat_new_quantity = 100
if ("Ham" in meat) and meat_quantity < 100:
    meat[2] = meat_new_quantity
    
#aggiungere una lista
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

#rimuovere una lista
deli_dept.remove(condiment)

#ordina per lettera alfabetica
deli_dept.sort()

print("Updated Deli list: ", deli_dept)


