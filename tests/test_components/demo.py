import argparse
from unittest import TestCase, main

from cliez import parser


class ParserTests(TestCase):
    def setUp(self):
        from ___pkg___ import main
        _ = main
        pass

    def test_exit(self):
        with self.assertRaises(SystemExit) as cm:
            parser.parse(argparse.ArgumentParser(),
                         argv=[
                             'command',
                             'demo'
                         ])
            pass

        self.assertEqual(cm.exception.code, 2)
        pass

    def test_settings(self):
        parser.parse(argparse.ArgumentParser(),
                     argv=[
                         'command',
                         'demo',
                         'hello',
                         '--settings',
                         '___pkg___.settings.online'])
        pass

    pass


if __name__ == '__main__':
    main()
