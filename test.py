#!/usr/bin/env python
from __future__ import absolute_import


def main():
    args = parse_args()
    if args.shortcut:
        if args.always:
            import colored_traceback.always
        else:
            import colored_traceback.auto
    else:
        from colored_traceback import add_hook
        add_hook(always=args.always, colors=args.colors, debug=args.debug)

    x = object()
    x.thing()


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--shortcut", action='store_true')
    parser.add_argument("--always", action='store_true')
    parser.add_argument("--colors", action='store', type=int)
    parser.add_argument("--debug", action='store_true')
    return parser.parse_args()


main()
