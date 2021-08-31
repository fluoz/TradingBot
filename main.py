import logging

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient("0a8b8bfd5f5be56978de775325f950fe3877520c4a51aa485e1d5f57d0989c1d", "e643856642daefa0101c905d0601be2253e2a9f5391aebc01d9d187671e06abc", True)
    bitmex = BitmexClient("vqIRm7vrGtughbJM93FeIHru", "O4VB7VBHhU3SJKngKotJuszNCTxHD64-eD4TIiuwqW8K7FL3", True)


    root = Root(binance, bitmex)
    root.mainloop()
