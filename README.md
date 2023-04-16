# YWH Collab

```
██╗   ██╗██╗    ██╗██╗  ██╗       ██████╗ ██████╗ ██╗     ██╗      █████╗ ██████╗ 
╚██╗ ██╔╝██║    ██║██║  ██║      ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗██╔══██╗
 ╚████╔╝ ██║ █╗ ██║███████║█████╗██║     ██║   ██║██║     ██║     ███████║██████╔╝
  ╚██╔╝  ██║███╗██║██╔══██║╚════╝██║     ██║   ██║██║     ██║     ██╔══██║██╔══██╗
   ██║   ╚███╔███╔╝██║  ██║      ╚██████╗╚██████╔╝███████╗███████╗██║  ██║██████╔╝
   ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝       ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ 
```

## Description

YWH Collab is a comparator of private program for hunters collaboration.
The goal of this tool is to be able to find common programs that accept collaboration between hunters without revealing the names of the clients of the private programs to which you are invited.

> **Please note that if you share the list of anonymized programs publicly, it will be possible for all other members of the program to know that you are also invited!**

## Installation

Install from [pip](https://pypi.org/project/ywh-collab):

```
▶ pip install ywh-collab
```

## Usage 

It is possible to provide the JWT as an argument or to provide credentials in an interactive session to log in your Yes We Hack account.

```bash
$ ywh-collab -h
usage: ywh-collab [-h] [-j JWT] -f FILENAME {export,compare}

Yes We Hack private program comparator for hunters collaboration by Aethlios.

positional arguments:
  {export,compare}      Export your list of program IDs or compare a list with your programs to find common programs that accept collab.

optional arguments:
  -h, --help            show this help message and exit
  -j JWT, --jwt JWT     The JWT token of the YWH session
  -f FILENAME, --filename FILENAME
                        The input or output filename
```

### Export

First, you can export the list of program IDs into `output.txt` file to share it with another hunter :

```bash
ywh-collab -f output.txt export
```

### Compare

In a second step, you can compare the list of program IDs of another hunter stored in `input.txt` file with your private programs in order to find common programs that accept hunters' collaboration.

```bash
ywh-collab -f input.txt compare
```

## Changelog
- v1.0.0 - Initial release
