"""Extension of test.test_support to have new functions."""

import contextlib
import sys

from test.test_support import *
from test.test_support import _filterwarnings


@contextlib.contextmanager
def check_py3k_warnings(*filters, **kwargs):
    """Context manager to silence py3k warnings.

    Accept 2-tuples as positional arguments:
        ("message regexp", WarningCategory)

    Optional argument:
     - if 'quiet' is True, it does not fail if a filter catches nothing
        (default False)

    Without argument, it defaults to:
        check_py3k_warnings(("", DeprecationWarning), quiet=False)
    """
    if sys.py3kwarning:
        if not filters:
            filters = (("", DeprecationWarning),)
    else:
        # It should not raise any py3k warning
        filters = ()
    return _filterwarnings(filters, kwargs.get('quiet'))


_TPFLAGS_HAVE_GC = 1<<14
_TPFLAGS_HEAPTYPE = 1<<9

def check_sizeof(test, o, size):
    import _testcapi
    result = sys.getsizeof(o)
    # add GC header size
    if ((type(o) == type) and (o.__flags__ & _TPFLAGS_HEAPTYPE) or\
        ((type(o) != type) and (type(o).__flags__ & _TPFLAGS_HAVE_GC))):
        size += _testcapi.SIZEOF_PYGC_HEAD
    msg = 'wrong size for %s: got %d, expected %d' \
            % (type(o), result, size)
    test.assertEqual(result, size, msg)
