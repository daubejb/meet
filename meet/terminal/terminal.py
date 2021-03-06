#!usr/bin/python
#  terminal.py

import argparse


def main():
    pass


def get_user_input():
    try:
        parser = argparse.ArgumentParser(description='a cli application to \
                create a meeting notes google doc or local markdown file for a \
                current or impending meeting on your google calendar')
        parser._optionals.title = 'meeting notes arguments'
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-g', '--google',
                           help='create a new google doc with minutes',
                           action='store_true',
                           dest='google')
        group.add_argument('-m', '--markdown',
                           help='create a local markdown file with minutes',
                           action='store_true',
                           dest='markdown')
        # parser.add_argument('-s', '--share',
        #                     help='automatically share the google doc with \
        #                         meeting participants',
        #                     action='store_true',
        #                     dest='share')
        args = parser.parse_args()
        if not args.google and not args.markdown:
            parser.print_help()
        return args
    except ImportError:
        flags = None

if __name__ == '__main__':
    main()
