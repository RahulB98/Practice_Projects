def solve(s):
    S = s.split()
    for item in S:
        i = item.capitalize()
        s = s.replace(item, i)


    print(s)
    return s

r = solve("Hello  World Lol")