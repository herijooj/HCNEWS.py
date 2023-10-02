#!/usr/bin/env python3

import argparse
import datetime
import locale

# Functions ===========================================================================================================
def write_header(heripoch=datetime.datetime(2021, 10, 7), locale_str="pt_BR.UTF-8"):
    today = datetime.datetime.now()
    locale.setlocale(locale.LC_TIME, locale_str)
    date_verbose = today.strftime("%A, %d de %B de %Y")
    edition = str((today - heripoch).days + 1)
    days_since = str(today.timetuple().tm_yday)

    header = "📰 HCNews, Edição " + edition + " 🗞\n"
    header += "📌 De Araucária Paraná 🇧🇷\n"
    header += "🗺 Notícias do Brasil e do Mundo 🌎\n"
    header += "📅 " + date_verbose + "\n"
    header += "⏳ " + days_since + "º dia do ano\n"
    header += "\n"

    return header

# help function
def get_arguments():
    """
    Parses and retrieves the command line arguments.

    :return: The parsed command line arguments.
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description='Writes the header of the news file.'
    )
    parser.add_argument(
        '-d', '--date',
        type=str,
        default="07/10/2021",
        help='The heripoch date. Defaults to 07/10/2021.'
    )
    parser.add_argument(
        '-l', '--locale',
        type=str,
        default="pt_BR.UTF-8",
        help='The locale to be used. Defaults to pt_BR.UTF-8.'
    )
    return parser.parse_args()

# Main ================================================================================================================
def main():
    args = get_arguments()

    # heripoch date as datetime object
    heripoch = datetime.datetime.strptime(args.date, "%d/%m/%Y")

    # print(write_header(heripoch, args.locale))
    return write_header(heripoch, args.locale)

if __name__ == '__main__':
    main()