# coding: utf-8

import argparse
import sys

from mpienv import manager


parser = argparse.ArgumentParser(
    prog='mpienv exec',
    description='Call mpiexec with appropriate arguments')
parser.add_argument('args', nargs=argparse.REMAINDER,
                    default=[])


def main():
    args = sys.argv[1:]

    manager.exec_(args)


if __name__ == "__main__":
    main()
