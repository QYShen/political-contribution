from model.Recipient import format_date
from datetime import date


def test_format_date():
    assert format_date(date(1900, 1, 1)) == '01011900'


def test_dates_sorting():
    d1 = date(2017, 12, 3)
    d2 = date(2017, 8, 2)
    d3 = date(2017, 1, 1)
    m_map = {
        d1: [],
        d2: [],
        d3: []
    }
    dates = list(m_map.keys())
    dates.sort()
    print('sort map keys', dates)
