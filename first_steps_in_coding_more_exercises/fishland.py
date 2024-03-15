price_of_mackerel_per_kilogram = float(input())
price_of_sprat_per_kilogram = float(input())
kilogram_of_bonito = float(input())
kilogram_of_scad = float(input())
kilogram_of_mussels = int(input())

price_of_bonito = price_of_mackerel_per_kilogram + 0.60 * price_of_mackerel_per_kilogram
price_of_scad = price_of_sprat_per_kilogram + 0.80 * price_of_sprat_per_kilogram
price_of_mussels = 7.50

bill = price_of_bonito * kilogram_of_bonito + price_of_scad * kilogram_of_scad + price_of_mussels * kilogram_of_mussels
print(f"{bill:.2f}")