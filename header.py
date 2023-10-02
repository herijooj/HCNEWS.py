#!/usr/bin/env python3

import argparse
import datetime
import locale

# Functions ===========================================================================================================
def write_header(locale_arg="pt_BR.UTF-8", heripoch_date=datetime.datetime(2021, 10, 7)):
    """
    Sets the locale and prints a header for the HCNews edition.

    :param locale_arg: (str) The locale argument to set the locale. Default is "pt_BR.UTF-8".
    :param heripoch_date: (datetime.datetime) The Heripoch date to calculate the edition. Default is datetime.datetime(2021, 10, 7).
    """
    locale.setlocale(locale.LC_ALL, locale_arg)

    date = datetime.datetime.now().strftime("%A, %d de %B de %Y")
    edition = str((datetime.datetime.now() - heripoch_date).days)
    days_since = str(datetime.datetime.now().timetuple().tm_yday)

    print("📰 HCNews, Edição", edition, "🗞")
    print("📌 De Araucária Paraná 🇧🇷")
    print("🗺 Notícias do Brasil e do Mundo 🌎")
    print("📅", date)
    print("⏳", days_since + "º dia do ano")
    print("")

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
        '-l', '--locale',
        type=str,
        help='The locale of the header. Defaults to pt_BR.UTF-8.'
    )
    parser.add_argument(
        '-d', '--date',
        type=str,
        default="07/10/2021",
        help='The heripoch date. Defaults to 07/10/2021.'
    )
    return parser.parse_args()

# Main ================================================================================================================
def main():
    args = get_arguments()
    args.date = datetime.datetime.strptime(args.date, "%d/%m/%Y")
    write_header(args.locale, args.date)

if __name__ == '__main__':
    main()