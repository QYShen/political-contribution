from datetime import date


class Contribution(object):
    def __init__(self, recipient, zip_code, parsed_date, amount):
        self.recipient = recipient
        self.zip_code = zip_code  # optional
        self.date = parsed_date  # optional
        self.amount = amount

    def __str__(self) -> str:
        return 'Contribution: {recipient=%s, zip_code=%s, date=%s, amount=%s}' \
               % (self.recipient, self.zip_code, self.date, self.amount)

    @staticmethod
    def parse_contribution(text):
        a = list(map(lambda s: s.strip(), text.split('|')))
        if len(a) != 21:  # has other_id field
            return None

        if a[0] == '' or a[14] == '':
            return None

        if a[15] != '':
            return None

        return Contribution(recipient=a[0], zip_code=parse_zipcode(a[10]),
                            parsed_date=parse_date(a[13]), amount=int(a[14]))


def parse_date(s):
    if len(s) != 8:
        return None

    try:
        my_date = date(int(s[4:]), int(s[:2]), int(s[2:4]))
    except ValueError as e:
        print('invalid string: %s for date parsing' % s)
        print(e)
        return None

    return my_date


def parse_zipcode(s):
    if len(s) < 5:
        return None

    s1 = s[:5]
    if not s1.isdigit():
        return None

    return s1
