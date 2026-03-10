def calculate_descent(altitude):
    total_descent_time = 0.0
    
    # [Layer Name, Lower Boundary (km), Upper Boundary (km), Rate (m/s)]
    atmosphere_layers = [
        ['Exosphere', 700, 10000, 2000],
        ['Thermosphere', 85, 700, 500],
        ['Mesosphere', 50, 85, 200],
        ['Stratosphere', 12, 50, 75],
        ['Troposphere', 0, 12, 20],
    ]

    for name, lower, upper, rate in atmosphere_layers:
        # Check if the capsule is currently in or above this specific layer
        if altitude > lower:
            top_of_descent_in_layer = min(altitude, upper)
            
            # Distance traveled in this layer in kilometers
            distance_km = top_of_descent_in_layer - lower
            
            # Calculate time: (distance in meters) / (rate in m/s)
            # Formula: t = (km * 1000) / v
            section_time = (distance_km * 1000) / rate
            total_descent_time += section_time

    # Return the total time rounded to one decimal place
    return round(total_descent_time, 1)

br_line = "--------------------------\n"

# Starting at 200 km (Thermosphere)
input1 = 200
result1 = calculate_descent(input1)
print(f"Input: {input1}km")
print(f"Output: {result1}")
print(br_line)

# Starting at 12 km (Edge of Troposphere)
input2 = 12
result2 = calculate_descent(input2)
print(f"Input: {input2}km")
print(f"Output: {result2}")