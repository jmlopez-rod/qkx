"""Command line use of qkx

To run qkx from the command line do the following:

    python -m qkx [-h] subcommand

Use the option --help for more information.

"""
import argparse
import textwrap
from os.path import split, abspath
from glob import iglob
from qkx.__version__ import VERSION
from qkx.command import import_mod


DESC = """
`qkx` is a manager which allows to execute commands on a remote
server via `ssh` without the needs of administrator privileges.

use the help option with a command for more information on what
qkx can do.

"""
EPI = """
more info:
  http://qkx.rtfd.org/

version:
  qkx %s

""" % VERSION


def parse_options(mod):
    """Interpret the command line inputs and options. """
    ver = "qkx %s" % VERSION
    raw = argparse.RawDescriptionHelpFormatter
    argp = argparse.ArgumentParser(formatter_class=raw,
                                   description=textwrap.dedent(DESC),
                                   epilog=textwrap.dedent(EPI))
    argp.add_argument('-v', '--version',
                      action='version',
                      version=ver)
    subp = argp.add_subparsers(title='subcommands',
                               dest='parser_name',
                               help='additional help',
                               metavar="<command>")
    names = sorted(mod.keys())
    for name in names:
        mod[name].add_parser(subp, raw)
    return argp.parse_args()


def run():
    """Run qkx from the command line. """
    mod = {}
    root = split(abspath(__file__))[0]

    mod_names = [name for name in iglob('%s/command/*.py' % root)]
    for name in mod_names:
        tmp_name = split(name)[1][:-3]
        tmp_mod = import_mod('qkx.command.%s' % tmp_name)
        if hasattr(tmp_mod, 'add_parser'):
            mod[tmp_name] = tmp_mod

    arg = parse_options(mod)
    mod[arg.parser_name].run(arg)

if __name__ == '__main__':
    run()
