""" Sample Python application.

"""
from argparse import ArgumentParser


def main(argv=None) -> int:
    """ Display a greeting.

    :param argv: argument list (sys.argv by default)
    :return: exit status
    """
    parser = ArgumentParser()
    parser.add_argument("--name", "-n", default="World", help="greeting name")
    args = parser.parse_args(argv)
    print(f"Hello, {args.name:s}.")
    return 0
 

if __name__ == "__main__":
    raise SystemExit(main())
