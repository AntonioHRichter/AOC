pInput = 34000000

def findHouse(pInput, deliveries, limit = None):
    limit = pInput if limit is None else limit
    d = pInput // deliveries
    houses = [0] * d
    for i in range(1, d + 1):
        for x in range(1, min(d // i, limit) + 1):
            houses[x * i - 1] += i * deliveries
        if houses[i - 1] >= pInput:
            return i

print(findHouse(pInput, 10))
print(findHouse(pInput, 11, 50))
