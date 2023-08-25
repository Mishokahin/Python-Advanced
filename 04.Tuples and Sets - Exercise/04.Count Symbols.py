symbols = input()

print('\n'.join(f"{symbol}: {symbols.count(symbol)} time/s" for symbol in sorted(set(symbols))))