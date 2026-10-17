import webbrowser

with open('熟語.txt') as file:
    合計 = sum(1 for _ in open('熟語.txt'))
    要確認 = []
    for i, line in enumerate(file, 1):
        言葉 = line.rstrip()
        print(f"{i}/{合計} {言葉}")
        読めなかった = input()
        if 読めなかった:
            要確認.append(言葉)

    for 読めなかった言葉 in 要確認:
        webbrowser.open(f"https://google.com/search?q={読めなかった言葉}の日本語と台湾華語と広東語での読み方と意味")