percent_fat = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_water = int(input())

one_gram_fat_calories = 9
one_gram_proteins_calories = 4
one_gram_carbohydrates_calories = 4

gram_fat = (percent_fat / 100 * total_calories) / one_gram_fat_calories
gram_proteins = (percent_proteins / 100 * total_calories) / one_gram_proteins_calories
gram_carbohydrates = (percent_carbohydrates / 100 * total_calories) / one_gram_carbohydrates_calories

total_food = gram_carbohydrates + gram_fat + gram_proteins

calories_per_one_gram = total_calories / total_food

calories_water = (100 - percent_water) * calories_per_one_gram

print(f"{(calories_water / 100):.4f}")