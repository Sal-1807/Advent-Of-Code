data = (
    "245284-286195,797927-983972,4949410945-4949555758,115-282,"
    "8266093206-8266228431,1-21,483873-655838,419252-466133,6190-13590,"
    "3876510-4037577,9946738680-9946889090,99954692-100029290,2398820-2469257,"
    "142130432-142157371,9797879567-9798085531,209853-240025,85618-110471,"
    "35694994-35766376,4395291-4476150,33658388-33694159,680915-772910,"
    "4973452995-4973630970,52-104,984439-1009605,19489345-19604283,"
    "22-42,154149-204168,7651663-7807184,287903-402052,2244-5558,"
    "587557762-587611332,307-1038,16266-85176,422394377-422468141"
)

def generate_repeated_numbers(limit):
    repeated = set()

    max_len = len(str(limit))

    for L in range(2, max_len + 1):
        for r in range(2, L + 1):
            if L % r != 0:
                continue
            k = L // r  
            if k == 0:
                continue

            start = 10**(k-1)
            end = 10**k - 1

            for s in range(start, end + 1):
                num = int(str(s) * r)
                if num > limit:
                    break
                repeated.add(num)

    return repeated


def solve(dataset):
    ranges = []
    for part in dataset.split(","):
        part = part.strip()
        if not part:
            continue
        lo, hi = map(int, part.split("-"))
        ranges.append((lo, hi))

    max_hi = max(hi for _, hi in ranges)

    repeated_nums = generate_repeated_numbers(max_hi)

    total = 0
    for lo, hi in ranges:
        for x in repeated_nums:
            if lo <= x <= hi:
                total += x

    return total


data = (
    "245284-286195,797927-983972,4949410945-4949555758,115-282,"
    "8266093206-8266228431,1-21,483873-655838,419252-466133,6190-13590,"
    "3876510-4037577,9946738680-9946889090,99954692-100029290,2398820-2469257,"
    "142130432-142157371,9797879567-9798085531,209853-240025,85618-110471,"
    "35694994-35766376,4395291-4476150,33658388-33694159,680915-772910,"
    "4973452995-4973630970,52-104,984439-1009605,19489345-19604283,"
    "22-42,154149-204168,7651663-7807184,287903-402052,2244-5558,"
    "587557762-587611332,307-1038,16266-85176,422394377-422468141"
)

def generate_repeated_numbers(limit):
    repeated = set()

    max_len = len(str(limit))

    for L in range(2, max_len + 1):
        for r in range(2, L + 1):
            if L % r != 0:
                continue
            k = L // r  
            if k == 0:
                continue

            start = 10**(k-1)
            end = 10**k - 1

            for s in range(start, end + 1):
                num = int(str(s) * r)
                if num > limit:
                    break
                repeated.add(num)

    return repeated


def solve(dataset):
    ranges = []
    for part in dataset.split(","):
        part = part.strip()
        if not part:
            continue
        lo, hi = map(int, part.split("-"))
        ranges.append((lo, hi))

    max_hi = max(hi for _, hi in ranges)

    repeated_nums = generate_repeated_numbers(max_hi)

    total = 0
    for lo, hi in ranges:
        for x in repeated_nums:
            if lo <= x <= hi:
                total += x

    return total


print("Sum of invalid IDs =", solve(data))