from model.Contribution import Contribution, parse_date, parse_zipcode


def test_parse_date_1():
    """If date is future, return None"""
    assert parse_date('01013000') is None


def test_parse_date_2():
    """non-int char inside, return None"""
    assert parse_date('010b3000') is None


def test_parse_date_3():
    """recipient field is empty"""
    text = ' |N|M2|P|201702039042410894|15|IND|DEEHAN, WILLIAM N|ALPHARETTA|GA|300047357|UNUM|SVP, SALES, ' \
           'CL|01312017|384||PR2283873845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029337 '
    c = Contribution.parse_contribution(text)
    assert c is None


def test_parse_date_4():
    """amount field is empty"""
    text = 'C00177436|N|M2|P|201702039042410894|15|IND|DEEHAN, WILLIAM N|ALPHARETTA|GA|300047357|UNUM|SVP, SALES, ' \
           'CL|01312017| ||PR2283873845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029337 '
    c = Contribution.parse_contribution(text)
    assert c is None


def test_parse_zipcode1():
    assert parse_zipcode('951a5') is None


def test_parse_zipcode2():
    assert parse_zipcode('95125169') == '95125'


def test_parse_zipcode3():
    assert parse_zipcode('95125-169') == '95125'
