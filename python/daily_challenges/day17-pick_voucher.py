def pick_voucher(vouchers, delays, max_wait):
    usd_per_hour = 0
    usd_per_hours = []
    
    for voucher in vouchers:
        delay = delays[vouchers.index(voucher)]
        print(f"Delay: {delay}")
        print(max_wait)
        if max_wait < delay:
            print("Delay exceeds max wait time")
            usd_per_hour = -1
            usd_per_hours.append(usd_per_hour)
        else:
            usd_per_hour = voucher / delay
            usd_per_hours.append(usd_per_hour)
            print(f"usd per hour: {usd_per_hour}")
            
                
    max_usd_ph = max(usd_per_hours)
    
    if max_usd_ph < 0:
        return -1
    else:
        option = usd_per_hours.index(max_usd_ph)
    
    return option
        
    
br_line = "--------------------------\n"


input1_vouchers = [50, 120, 20]
input1_delays = [2, 4, 1]
input1_max_wait = 3

result1 = pick_voucher(input1_vouchers, input1_delays, input1_max_wait)
print(f"Output: {result1}")
print(br_line)


input2_vouchers = [300, 400, 1000]
input2_delays = [5, 6, 10]
input2_max_wait = 4

result2 = pick_voucher(input2_vouchers, input2_delays, input2_max_wait)
print(f"Output: {result2}")
print(br_line)
