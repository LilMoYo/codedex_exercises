def minimum_components(components):
    sum_components = sum(components)
    count_components = len(components)
    sorted_components = sorted(components, reverse=True)
    ultimate_answer = 42
    answer = ultimate_answer
    if components == []:
        return -1
    else:
        print(sum_components, count_components, sorted_components)
        
        calc = ultimate_answer % sum_components
        print(f"calc sum_components {calc}")
        
        if calc == 0:
            print("No combination sums to exactly 42.")
            return -1
        else:
            count = 0 
            for component in sorted_components: 
                answer = answer - component
                print(f"answer: {answer}")
                count += 1
                print(f"count: {count}")
                    
                if answer <= 0:
                    break
    return count

br_line = "--------------------------\n"


input1 = [10, 20, 5, 15, 7]

result1 = minimum_components(input1)
print(f"Output: {result1}")
print(br_line)


input2 = [1, 2, 3, 4, 5, 6]

result2 = minimum_components(input2)
print(f"Output: {result2}")
print(br_line)


input3 = [42, 1, 1, 1]

result3 = minimum_components(input3)
print(f"Output: {result3}")
print(br_line)


input4 = []

result4 = minimum_components(input4)
print(f"Output: {result4}")
print(br_line)