a = 24
for ia in range(3, a + 1): # range包括前者不包括后者
    for b in range(1, ia):
        for c in range(b, ia):
            for d in range(c, ia):
                if ia * ia * ia == b * b * b + c * c * c + d * d * d:
                    print(ia, b, c, d)