def calculate_sleep_debt(planned, actual):
    temp_sleep = 0
    temp_sleep_list = []
    i = 0
    
    for sleep_plan in planned:
        actual_sleep = actual[i]
        i += 1
        temp_sleep = sleep_plan - actual_sleep
        
        if temp_sleep < 0:
            temp_sleep = 0 
        temp_sleep_list.append(temp_sleep)
        print(temp_sleep)
    
    sleep_streak_count = 0
    sleep_streak = []
    
    for temp_sleep in temp_sleep_list:
        if  temp_sleep != 0:
            sleep_streak_count += 1
            sleep_streak.append(sleep_streak_count)
            print(f"Streak Counter: {sleep_streak_count} days")
        else:
            sleep_streak_count -= 1
            sleep_streak.append(sleep_streak_count)
            print(f"Streak Counter: {sleep_streak_count} days")
    
    max_sleep_streak = max(sleep_streak)
    if max_sleep_streak <= 0:
        max_sleep_streak = 1
    print(f"Longest Sleep Streak: {max_sleep_streak} days")
    print(temp_sleep_list)
    
    sleep_debt = max(0,sum(temp_sleep_list))
    dl_saving_hour = 1
    sleep_debt = sleep_debt + dl_saving_hour
    print(f"Sleep Debt: {sleep_debt} hours\n")
    return sleep_debt, max_sleep_streak

br_line = "--------------------------\n"

planned1 = [7.5, 8, 7.5, 8, 8.5, 8, 7.5]
actual1 = [5, 12, 6, 6, 9, 8, 6.5]
             
plannedCheck1 = calculate_sleep_debt(planned1, actual1)
print(f"{plannedCheck1}")
print(br_line)

planned2 = [6, 6, 6, 6, 6, 8, 8]
actual2 = [5, 7, 2.5, 5, 5.5, 6, 4]
             
plannedCheck2 = calculate_sleep_debt(planned2, actual2)
print(f"{plannedCheck2}")
print(br_line)

planned3 = [8, 8, 8, 8, 8, 8, 8]
actual3 = [8, 9, 8, 7.5, 8, 10, 8]
             
plannedCheck3 = calculate_sleep_debt(planned3, actual3)
print(f"{plannedCheck3}")
print(br_line)
