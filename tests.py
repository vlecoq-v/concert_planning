from find_sum import find_sum

if __name__ != "__main__":
    exit()

if find_sum(3, [1, 1, 1]) != [0, 1, 2]:
    print("TEST 1: KO")
else:
    print("TEST 1: OK")

if find_sum(3, [1, 2, 3, 4, 5, 6]) != None:
    print("TEST 2: KO")
else:
    print("TEST 2: OK")

if find_sum(1000, [1, 2, 3, 4, 5, 6]) != None:
    print("TEST 3: KO")
else:
    print("TEST 3: OK")

if find_sum(8, [1, 2, 3, 4, 5, 6]) != [0, 1, 4]:
    print("TEST 4: KO")
else:
    print("TEST 4: OK")

if find_sum(15, [1, 2, 3, 4, 5, 6]) != [3, 4, 5]:
    print("TEST 5: KO")
else:
    print("TEST 5: OK")
