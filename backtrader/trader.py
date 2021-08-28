
import backtrader
import datetime
import matplotlib


from strategies import TestStrategy

cerebro = backtrader.Cerebro()


cerebro.broker.set_cash(100000)

data = backtrader.feeds.YahooFinanceCSVData(
    dataname='tsla.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(1986, 3, 11),
    # Do not pass values after this date
    todate=datetime.datetime(2021, 8, 26),
    reverse=False)


cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

cerebro.addsizer(backtrader.sizers.FixedSize, stake=100)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())



cerebro.plot()


