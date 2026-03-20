def upset_probability(matchups):
    team1 = []
    team2 = []
    upset_prob = 0
    upset_list = []
    
    for matchup in matchups:
        team1 = [matchup[0], matchup[1]]
        team2 = [matchup[2], matchup[3]]
        print(team1, team2)
        higher_seed = min(team1[1], team2[1])
        lower_seed = max(team1[1], team2[1])
        print(lower_seed, higher_seed)
        
        upset_prob = round(higher_seed / (higher_seed + lower_seed),2)
        upset_list.append(upset_prob)
        print(upset_prob)
    return upset_list
        
    
br_line = "--------------------------\n"


input1_matchups = [
  ["Duke", 1, "Siena", 16],
  ["Ohio State", 8, "TCU", 9]
]

result1 = upset_probability(input1_matchups)
print(f"Output: {result1}")
print(br_line)


input2_matchups = matchups = [
  ["Michigan", 1, "Lehigh", 16],
  ["Nebraska", 4, "Troy", 13],
  ["Houston", 2, "Akron", 15]
]

result2 = upset_probability(input2_matchups)
print(f"Output: {result2}")
print(br_line)
