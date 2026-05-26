import ccxt
import time

binance = ccxt.binance()
okx = ccxt.okx()

while True:
    binance_price = binance.fetch_ticker('BTC/USDT')['last']
    okx_price = okx.fetch_ticker('BTC/USDT')['last']
    
    spread = okx_price - binance_price
    spread_pct = (spread / binance_price) * 100
    
    print(f"Binance: {binance_price}")
    print(f"OKX:     {okx_price}")
    print(f"价差:    {spread:.2f} USDT ({spread_pct:.4f}%)")
    print("-" * 40)
    
    time.sleep(5)
        
    




    


    
