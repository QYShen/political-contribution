from functools import reduce

from model.Contribution import Contribution
from statistics import median
from datetime import date


class Recipient(object):
    def __init__(self, identity):
        self.identity = identity

        self.txs_by_zipcode = {}  # {str:[]}
        self.total_num_tx_by_zipcode = {}  # {str:int}
        self.total_amount_by_zipcode = {}  # {str:int}
        self.stats_by_zipcode = None  # str

        self.txs_by_date = {}  # {int:[]}
        self.total_num_tx_by_date = {}  # {date:int}
        self.total_amount_by_date = {}  # {date:int}

    def receive_contribution(self, c: Contribution):
        zip_code = c.zip_code
        if zip_code:
            txs_of_zipcode = self.txs_by_zipcode.get(zip_code, [])
            txs_of_zipcode.append(c.amount)
            self.txs_by_zipcode[zip_code] = txs_of_zipcode
            median_by_zipcode = round(median(txs_of_zipcode))

            num = self.total_num_tx_by_zipcode.get(zip_code, 0) + 1
            self.total_num_tx_by_zipcode[zip_code] = num

            total_amount = self.total_amount_by_zipcode.get(zip_code, 0) + c.amount
            self.total_amount_by_zipcode[zip_code] = total_amount

            self.stats_by_zipcode = '%s|%s|%s|%s|%s' % (self.identity, c.zip_code, median_by_zipcode, num, total_amount)
        else:
            self.stats_by_zipcode = None

        cur_date = c.date
        if cur_date:
            txs_of_date = self.txs_by_date.get(c.date, [])
            txs_of_date.append(c.amount)
            self.txs_by_date[cur_date] = txs_of_date

            num = self.total_num_tx_by_date.get(cur_date, 0) + 1
            self.total_num_tx_by_date[cur_date] = num

            total_amount = self.total_amount_by_date.get(cur_date, 0) + c.amount
            self.total_amount_by_date[cur_date] = total_amount

    def stats_by_date(self) -> str:
        s = ''
        dates = list(self.txs_by_date.keys())
        dates.sort()
        for date0 in dates:
            txs = self.txs_by_date[date0]
            median0 = round(median(txs))
            count = len(txs)
            total = reduce(lambda acc, cur: acc + cur, txs)
            s += '%s|%s|%s|%s|%s\n' % (self.identity, format_date(date0), median0, count, total)
        return s


def format_date(d: date) -> str:
    return d.strftime('%m%d%Y')
