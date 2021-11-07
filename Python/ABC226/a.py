from decimal import Decimal,ROUND_HALF_UP

x = input()

result = Decimal(x)
a = result.quantize(Decimal('0'), rounding=ROUND_HALF_UP)

print(round(a))

