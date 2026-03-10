def find_unique_words(transcript):
    del_punctuation = [".", ",", ";", ":", "!", "?", "(", ")", "-"]
    align_transcript = transcript.lower()

    for char in del_punctuation:
        align_transcript = align_transcript.replace(char, "")
    
    unique_words = set(align_transcript.split())
    print(unique_words)
    
    len_unique_words = len(unique_words)
    return len_unique_words

br_line = "--------------------------\n"


input1 = "Mr. Watson, come here, I want to see you."

result1 = find_unique_words(input1)
print(f"Output: {result1}")
print(br_line)


input2 = "Hello Neil and Buzz, I am talking to you by telephone from the Oval Room at the White House, and this certainly has to be the most historic telephone call ever made."

result2 = find_unique_words(input2)
print(f"Output: {result2}")
print(br_line)


input3 = "Potato, Potato!"

result3 = find_unique_words(input3)
print(f"Output: {result3}")
print(br_line)