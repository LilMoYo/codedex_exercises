sz = ["summer", "fall", "winter", "spring"]
ranking = ["2", "1", "3", "4"]
print(sz) # prints out the list

sz.append('eclipse') # adds eclipse to the end of the list
sz.pop(4) # removes the value at index 4
sz.remove("summer") # removes the value summer
sz.insert(0,"summer")

zipped_data = zip(sz, ranking) #combines the list data

list_zip = list(zipped_data)

print(min(ranking))
print(max(ranking))
print(len(list_zip))
print(list_zip)