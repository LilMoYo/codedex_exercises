def check_url(address):
    url_check_1 = address
    if url_check_1.startswith("http://") or url_check_1.startswith("https://"):
        print("valid")
        url_parts = url_check_1.split("://")
        print((url_parts))
        
        url_http_part = url_parts[0]
        print(url_http_part)
        
        url_domain = url_parts[1]
        print(url_domain)
        
        url_domain_parts = url_domain.split(".")
        print(url_domain_parts)
        
        url_dolen = len(url_domain_parts)
        print(url_dolen)
        
        if url_dolen >= 2:
            print("valid?")
            if len(url_domain_parts[url_dolen-1]) > 3 and url_domain_parts[url_dolen-1] != "online" :
                print("invalid")
                return("invalid")
            else:
                allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-."
                
                for char in url_domain_parts[url_dolen-2] and url_domain_parts[url_dolen-1]:
                    if char not in allowed_chars:
                        print("invalid")
                        return("invalid")
                    else:
                        print("valid")
                        return("valid")
        else:
            return("invalid")
    else:
        return("invalid")

br_line = "--------------------------\n"


input1 = "https://codedex.io"

result1 = check_url(input1)
print(f"Output: {result1}")
print(br_line)


input2 = "https://netflixcom"

result2 = check_url(input2)
print(f"Output: {result2}")
print(br_line)


input3 = "http://en.wikipedia.org"

result3 = check_url(input3)
print(f"Output: {result3}")
print(br_line)


input4 = "https://net.flixcom"

result4 = check_url(input4)
print(f"Output: {result4}")
print(br_line)


input5 = "netflixcom."

result5 = check_url(input5)
print(f"Output: {result5}")
print(br_line)

input6 = "https://netflixcom.)91"

result6 = check_url(input6)
print(f"Output: {result6}")
print(br_line)


input7 = "https://netflixcom.online"

result7 = check_url(input7)
print(f"Output: {result7}")
print(br_line)