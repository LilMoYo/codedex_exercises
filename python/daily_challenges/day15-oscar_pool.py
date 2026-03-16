def oscar_pool(predictions):
    oscar_winners = [
       ["Best Picture", "One Battle After Another"],
       ["Best Actor", "Michael B. Jordan"],
       ["Best Actress", "Jessie Buckley"],
       ["Best Director", "Paul Thomas Anderson"]
       ]
    
    pred_list = []
    prediction_winner = []
    win_counter = []
    prediction_tie = ""
    
    for prediction in predictions:
        prediction_count = 0
        for category in oscar_winners:
            for i in range(len(prediction)):
                if prediction[i] == category[1]:
                    prediction_count += 1
                    print(prediction_count)
        win_counter.append(prediction_count)
        pred_list.append([prediction[0],prediction_count])
        print(pred_list)
        print(f'Counter: {win_counter}')
        
    for winner in pred_list:
        if winner[1] == max(win_counter):
            prediction_winner.append(winner[0])
            
    if len(prediction_winner) >= 2:
        prediction_tie = "Tie"
        return prediction_tie
    else:
        return prediction_winner[0]
    
br_line = "--------------------------\n"


input1_predictions = [
  ["@sonny", "One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Ryan Cooger"],
  ["@brit896", "Marty Supreme", "Timothée Chalamet", "Jessie Buckley", "Josh Safdie"],
  ["@tylerwhit", "Sinners", "Michael B. Jordan", "Rose Byrne", "Paul Thomas Anderson"]
]

result1 = oscar_pool(input1_predictions)
print(f"Output: {result1}")
print(br_line)


input2_predictions = [
  ["Kalshi", "One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Paul Thomas Anderson"],
  ["Polymarket", "One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Paul Thomas Anderson"]
]

result2 = oscar_pool(input2_predictions)
print(f"Output: {result2}")
print(br_line)


input3_predictions = [
  ["Rotten Tomatoes", "The Secret Agent", "Wagner Moura", "Renate Reinsve", "Kleber Mendonça Filho"],
  ["IMDb", "One Battle After Another", "Timothée Chalamet", "Jessie Buckley", "Chloé Zhao"]
]

result3 = oscar_pool(input3_predictions)
print(f"Output: {result3}")
print(br_line)

