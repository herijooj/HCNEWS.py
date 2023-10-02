#!/usr/bin/env python3

# Imports =============================================================================================================
from datetime import datetime, timedelta
# import argparse
# import os
# import sys

# Local imports
import header
import rss

# Functions ===========================================================================================================

# hcnews function
def hcnews(rss_array, time_delta=timedelta(hours=24), current_time=datetime.utcnow(), locale="pt_BR.UTF-8", heripoch=datetime(2021, 10, 7)):
    try:
        news = header.write_header(heripoch, locale)

        for rss_url in rss_array:
            news += "\n".join(rss.read_rss_feed(rss_url, time_delta, current_time))
            news += "\n\n"

        return news
    except Exception as e:
        return "An error occurred while parsing the RSS feed: " + str(e)


# Main ================================================================================================================
def main():
    rss_array = [
        'https://opopularpr.com.br/feed/',
        'https://www.newyorker.com/feed/magazine/rss',
        #'https://feeds.folha.uol.com.br/mundo/rss091.xml',
        #'https://www.formula1.com/content/fom-website/en/latest/all.xml',
        #'http://feeds.bbci.co.uk/news/world/latin_america/rss.xml'
    ]

    result = hcnews(rss_array)
    #print(result)
    return result

if __name__ == '__main__':
    main()
