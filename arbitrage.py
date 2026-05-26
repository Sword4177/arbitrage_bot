import ccxt
import time
import csv
from datetime import datetime

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
    
    if abs(spread_pct) > 0.05:
        print("⚠️ 套利机会！")
    
    print("-" * 40)
    
    with open('spread_log.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), binance_price, okx_price, spread, spread_pct])
    
    time.sleep(5)
    
        
    




    


    
