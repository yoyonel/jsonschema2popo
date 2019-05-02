"""
"""
import os
from unittest import mock

from jsonschema2popo.jsonschema2popo import main


# FIXME: Use a pytest functionality here ! (like pytest-datadirs)
here = os.path.abspath(os.path.dirname(__file__))


def test_jsonschema2popo(tmpdir_factory):
    datas_dir = os.path.join(here, 'datas/')

    export_fn = tmpdir_factory.mktemp("export").join("test_schema.py")
    print(export_fn)
    # https://stackoverflow.com/questions/43390053/pytest-setting-command-line-arguments-for-main-function-tests/43390054
    with mock.patch(
            'sys.argv',
            [
                "jsonschema2popo",
                os.path.join(datas_dir, 'test_schema.json'),
                "-o", str(export_fn)
            ]
    ):
        main()
    # TODO: do some tests on generated python class from json schema
    # => Functional tests on export python classes file
