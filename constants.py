TAX_RATE = 0.0875

def main():
    cost = 10.24
    tax = cost * TAX_RATE
    total = cost + tax

    print('Cost: $', cost)
    print('Tax: $', tax)
    print('Total: $', total)

main()