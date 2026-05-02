import ccxt
binance = ccxt.binance()
binance_price = binance.fetch_ticker('BTC/USD')['last']
print(binance_price)


        
    




    


    