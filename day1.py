import csv

def main():
    with open('modules.txt', newline='') as file:
        reads = csv.reader(file, delimiter=',')
        total = 0
        for read in reads:
            fuel = fuel_required(int(read[0]))
            mod = rec_fuel_required(fuel, 0)
            total += mod
            total += fuel
            print("Module size: %s Module Fuel: %s and extra %s so module total %s running totAL %s" % (read[0], fuel, mod, (mod + fuel), total))
        print(total)

def fuel_required(fuel):
    total = int(fuel/3) -2
    return int(total)


def rec_fuel_required(module, total):
    curr = fuel_required(module)
    print("Current total %s and diff %s" % (total, curr))
    if curr < 0:
        return total
    else:
        total += curr
        return rec_fuel_required(curr, total)


if __name__== "__main__":
    main()
