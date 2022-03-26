
# # задание 5
com_prices = [2.22, 20, 0.30, 9.13, 1]
com_prices.sort(reverse= 1)
for price in com_prices:
    rub = int(price)
    kop = (price -rub) * 100
    print(f'{rub:02} руб {kop:02.0f} копеек,', end=' ')
