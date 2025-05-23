#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import pathlib
import sys

from .txt2epub import Txt2Epub

def main() -> int:
    parser = argparse.ArgumentParser(
        prog="txt2epub",
        description="TXT to ePub converter.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    subparsers = parser.add_subparsers(
        help="Use [subcommand] -h to print help for each subcommand", dest="command"
    )

    convert_parser = subparsers.add_parser(
        "convert", help="Convert a TXT file to an ePub file"
    )
    convert_parser.add_argument(
        "-i",
        "--input",
        type=pathlib.Path,
        help="Path to the input txt file",
        required=True,
    )
    convert_parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        help="Path to the output ePub file",
    )
    convert_parser.add_argument(
        "-t",
        "--title",
        help="Title of the book",
    )
    convert_parser.add_argument(
        "-a",
        "--author",
        help="Author of the book",
    )
    convert_parser.add_argument(
        "-l",
        "--language",
        help="Language of the book",
    )
    convert_parser.add_argument(
        "--identifier",
        help="Identifier of the book",
    )
    convert_parser.add_argument(
        "-c",
        "--cover",
        type=pathlib.Path,
        help="Path to the cover image of the book",
    )

    args = parser.parse_args()

    if args.command == "convert":
        Txt2Epub.create_epub(
            input_file=args.input,
            output_file=args.output,
            book_identifier=args.identifier,
            book_title=args.title,
            book_author=args.author,
            book_language=args.language,
            book_cover=args.cover,
        )
    else:
        parser.print_help()
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
