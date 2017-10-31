import sys
import os
from model.Contribution import Contribution
from model.Recipient import Recipient


def main():
    recipients = {}
    out_zip = open(sys.argv[2], 'w+')
    with open(sys.argv[1], 'r') as in_log:
        for line in in_log:
            c = Contribution.parse_contribution(line)
            if c is None:
                continue

            name = c.recipient
            recipient = recipients.get(name, Recipient(name))
            recipient.receive_contribution(c)
            if name not in recipients:
                recipients[name] = recipient
            zip_stats = recipient.stats_by_zipcode
            if zip_stats:
                out_zip.write(zip_stats + '\n')
    out_zip.close()

    date_out_file = sys.argv[3]
    try_remove(date_out_file)
    ids = list(recipients.keys())
    ids.sort()
    for identifier in ids:
        stats = recipients[identifier].stats_by_date()
        with open(date_out_file, 'a+') as out_date:
            out_date.write(stats)


def try_remove(file_path):
    try:
        os.remove(file_path)
    except OSError:
        pass


if __name__ == '__main__':
    main()
