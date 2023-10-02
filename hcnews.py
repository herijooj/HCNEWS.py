#!/usr/bin/env python3

# Imports =============================================================================================================
import datetime
import argparse
import os
import sys

# Local imports
import header
import rss

# Functions ===========================================================================================================
def get_arguments():
    """
    Parses and retrieves the command line arguments.

    :return: The parsed command line arguments.
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description='Writes the HCNEWS file.'
    )
    parser.add_argument(
        '-l', '--locale',
        type=str,
        default="pt_BR.UTF-8",
        help='The locale of the header. Defaults to pt_BR.UTF-8.'
    )
    parser.add_argument(
        '-d', '--date',
        type=str,
        default="07/10/2021",
        help='The heripoch date. Defaults to 07/10/2021.'
    )
    parser.add_argument(
        '-o', '--output',
        type=bool,
        default=False,
        help='Whether the output goes to stdout or to a file. Defaults to False.'
    )
    return parser.parse_args()

# Main ================================================================================================================
def main():
   
    # Get the command line arguments
    args = get_arguments()
    args.date = datetime.datetime.strptime(args.date, "%d/%m/%Y") # Convert the date string to datetime

    current_time = datetime.datetime.utcnow() # Time now, used in the header and rss feed
    timedelta = datetime.timedelta(hours=24) # 24 hours interval

    # Create the "news" directory if it does not exist
    os.makedirs("news", exist_ok=True)

    # Create the file with the current date as the name
    news_file = open(f"news/{current_time.strftime('%Y-%m-%d')}.news", "w")      

    # Change the output to the news file
    if not args.output:
        sys.stdout = news_file

    # Write the header
    header.write_header(args.locale, args.date)

    rss_urls = [
        'https://opopularpr.com.br/feed/',
        # 'https://www.newyorker.com/feed/magazine/rss',
        # 'https://feeds.folha.uol.com.br/mundo/rss091.xml',
        # 'https://www.formula1.com/content/fom-website/en/latest/all.xml',
        # 'http://feeds.bbci.co.uk/news/world/latin_america/rss.xml'
    ]

    # for each rss url in the list
    for rss_url in rss_urls:
        # write the rss feed
        rss.read_rss_feed(rss_url, timedelta, current_time)
        print()
    
    news_file.close()

if __name__ == '__main__':
    main()