#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This module reads specific data from a CSV file and returns desired output.
    The CSV file holds the share price information of N cpmpanies.
    This information is for each month of years ranging from 1990 onwards.

    The output gives out the month with highest share value for each company.

    :copyright: (c) 2013 by Shalabh Aggarwal
    :license: GPLv3

Usage: python script.py <file path>

Options:
    -h, --help      show this help
"""
import sys
from decimal import Decimal
import csv

__all__ = ['process_csv']


def process_csv(file_path):
    """Process the CSV and return the highest share prices for each company
    with the year and month in the form of a dictionary/map.

    :param file_path: The path to the CSV file. This path can be absolute or
                      relative. (Absolute path preferred)
    """
    company_result_dict = {}
    with open(file_path, 'rb') as csv_file:
        # Read the CSV file as a dictionary with the first row as the header
        # The header values becomes the keys when each row is accessed
        reader = csv.DictReader(csv_file)

        # Iterate over each row
        for row in reader:
            # Get the year and month
            year, month = row.pop('Year'), row.pop('Month')

            for company, share_price in row.iteritems():
                # Iterate for each company
                if not company_result_dict.get(company):
                    # Create an empty dict for each company if its the first
                    # time this company is being accessed
                    company_result_dict[company] = {}
                if company_result_dict.get(company) and \
                        Decimal(company_result_dict[company]['Price']) >= \
                        Decimal(share_price):
                    # If the current value of share price stored in dict for
                    # the company is highest, just continue the loop without
                    # changing the current stored values
                    continue

                # A new high share value is encountered, update the dict
                company_result_dict[company]['Price'] = share_price
                company_result_dict[company]['Year'] = year
                company_result_dict[company]['Month'] = month

    return company_result_dict


def main():
    if any(['-h' in sys.argv, '--help' in sys.argv]):
        print __doc__
        return

    result = process_csv(sys.argv[1])

    for company, data in result.iteritems():
        print "{0} had highest share price of {1} on {2}, {3}".format(
            company, data['Price'], data['Month'], data['Year']
        )


if __name__ == "__main__":
    "Run as a script"
    main()
