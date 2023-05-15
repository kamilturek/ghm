import argparse

from ghm import hooks


def list_hooks():
    hooks.list_hooks()


def add_hook():
    pass


def run():
    parser = argparse.ArgumentParser(
        prog="ghm",
        description="lightweight git hooks manager",
    )
    subparsers = parser.add_subparsers()

    parser_list = subparsers.add_parser("list")
    parser_list.set_defaults(func=list_hooks)

    parser_add = subparsers.add_parser("add")
    parser_add.set_defaults(func=add_hook)

    args = parser.parse_args()
    args.func()


if __name__ == "__main__":
    run()
