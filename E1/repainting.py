nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
materials_sum = (nylon + 2) * 1.50 + \
                paint * 1.1 * 14.50 + \
                thinner * 5 + \
                0.40
salary = materials_sum * 0.30 * hours
total_sum = salary + materials_sum
print(total_sum)

#nylon = int(input())
#paint = int(input())
#thinner = int(input())
#hours = int(input())                                  #paint * 1.1 * 14.50 = (paint + 10%) * 14.50
#materials_sum = (nylon + 2) * 1.50 + \
                #(paint + (paint * 0.10)) * 14.50 + \
                #thinner * 5 + \
                #0.40
#salary = materials_sum * 0.30 * hours
#total_sum = salary + materials_sum
#print(total_sum)

#nylon = int(input())
#paint = int(input())
#thinner = int(input())
#hours = int(input())
#materials_sum = (nylon + 2) * 1.50 + \
                #(paint + 0.10 * paint) * 14.50 + \
                #thinner * 5 + \
                #0.40
#salary = materials_sum * 0.30 * hours
#total_sum = salary + materials_sum
#print(total_sum)
