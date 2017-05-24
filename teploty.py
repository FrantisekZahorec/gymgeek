print("Převodu teplot - tabulka")

print()
a = int(input("Od [°F]: "))
b = int(input("Do [°F]: "))
print()

for i in range(a, b+1, 10):
    print("%5.1f °F = %6.1f °C" % (i, (i-32) / 1.8))    # `(T - 32) / 1.8` je vzorec pro převod °F na °C