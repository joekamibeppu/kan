with open('熟語.txt') as file:
    for line in file:
        print(line)
        print(f"https://google.com/search?q=日本語と台湾華語と広東語読み方と意味{line}")
        input()