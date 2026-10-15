with open('熟語.txt') as file:
    total = sum(1 for _ in open('熟語.txt'))
    for i, line in enumerate(file, 1):
        print(f"{i}/{total} {line}")
        print(f"https://google.com/search?q={line.rstrip()}の日本語と台湾華語と広東語での読み方と意味")
        input()