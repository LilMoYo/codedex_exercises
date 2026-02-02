seasons = ["summer", "fall", "winter", "spring"]
ranking = [2, 1, 4, 3]

seasons.append('eclipse') # adds eclipse to the end of the list
seasons.pop(4) # removes the value at index 4
seasons.remove("summer") # removes the value summer
seasons.insert(0,"summer") # Add summer back to seasons at index 0

print(min(ranking)) # Show lowest ranking
print(max(ranking)) # Show highest ranking
print(len(seasons)) # Show seasons length
print(sum(ranking)) # Sum everything in ranking

new_seasons_ranking = zip(seasons, ranking) # zip both lists into one
print(list(new_seasons_ranking)) # Print new_seasons_ranking as a list
