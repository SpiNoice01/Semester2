def linear_search(keywords,data):
    for i in range (len(data)):
        if str(data[i]).lower() == keywords.lower():
            print(f"Keyword {keywords} has found at indeks {i}")
            return i
    print(f"Keyword {keywords} not found")
    return -1

data = [23,43,64,75,334,67]
keyword = input("Input Keyword : ")
linear_search(keyword, data)