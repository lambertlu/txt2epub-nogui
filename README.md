# TXT2EPUB

A simple tool for converting TXT books into ePub for headless Linux.

## Installation

You'll first need to have Python3 and Pip installed. If you're using Windows, then the default Python installer will come with Pip. If you're using Linux, you may need to install an extra package like `python3-pip`. The exact package name depends on your distro.

Then, execute the following command to install TXT2EPUB-nogui.

```shell
pip install txt2epub-nogui
```

## Usage

You may convert a file from the command line:

```shell
txt2epub convert -i <input> -o <output> -t <title> -a <author> -l <language> -c <cover>
```

## Chapter Detection

This program detects the book chapters and chapter titles following the standard TXT book format:

- Chapters are separated by three new lines (i.e., `\n\n\n`)
- The first line in a new chapter is the chapter's title.

For example, in the text below, there are two chapters with titles "Chapter 1" and "Chapter 2."

```txt
Chapter 1

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec at sapien ante.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.


Chapter 2

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec at sapien ante.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.
```
