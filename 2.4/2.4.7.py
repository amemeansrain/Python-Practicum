for i in range(n := int(input())):
    for count in range(3 + i, 0, -1):
        print(f'До старта {count} секунд(ы)')
    print(f'Старт {i + 1}!!!')