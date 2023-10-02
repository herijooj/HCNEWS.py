#!/usr/bin/env python3

# Imports =============================================================================================================
import feedparser
import argparse
from datetime import datetime, timedelta

# Functions ===========================================================================================================
def read_rss_feed(rss_url, time_delta=timedelta(hours=24), current_time=datetime.utcnow()):
    """
    Reads an RSS feed and returns the titles of the entries published within the last 24 hours.

    Parameters:
        rss_url (str): The URL of the RSS feed to be parsed.
        time_delta (int, optional): The time difference in hours. Defaults to 24.
        current_time (datetime.datetime, optional): The current time. Defaults to datetime.utcnow().

    Raises:
        Exception: If an error occurs while parsing the RSS feed.

    Returns:
        List[str]: The titles of the entries published within the last 24 hours.
    """
    try:
        # Parse the RSS feed
        
        # check the encoding of the rss feed
        feed = feedparser.parse(rss_url)
        
        # Check if the feed was successfully parsed
        if feed.get('bozo_exception'):
            return ["Error parsing RSS feed:", feed.bozo_exception]
        else:
            # Get the current time as utc and subtract 24 hours
            yesterday = current_time - time_delta

            # Store the feed title url without the protocol
            results = ["📰 " + feed.feed.link.split('//')[1] + " 📰"]

            # Loop through the entries and store the titles of those published within the last 24 hours
            for entry in feed.entries:
                if datetime(*entry.published_parsed[:6]) > yesterday:
                    results.append("📰 " + entry.title)
            
            return results
    except Exception as e:
        return ["An error occurred:", str(e)]

# help function
def get_arguments():
    """
    Parses the command line arguments and returns the parsed arguments.

    :return: The parsed command line arguments.
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description='Reads an RSS feed and prints the titles of the entries published within the last [-t] hours.'
    )
    parser.add_argument(
        'rss_url', 
        type=str, 
        help='The URL of the RSS feed to be parsed.'
    )
    parser.add_argument(
        '-t', '--time',
        type=int,
        default=24,
        help='The time difference in hours. Defaults to 24.'
    )
    return parser.parse_args()

# Main ================================================================================================================
def main():
    args = get_arguments()
    results = read_rss_feed(args.rss_url, timedelta(hours=args.time))
    print("\n".join(results))
    return results        

if __name__ == '__main__':
    main()