def profit(coast, sell, inv):
    coast_price = coast * inv
    sell_price = sell * inv
    return sell_price - coast_price


print(int(profit(34.76, 45, 1400)))
