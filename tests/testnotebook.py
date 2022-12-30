
from testbook import testbook
@testbook('mynote.ipynb', execute=True)
def test_second(tb):
    func = tb.ref("mysum")
    assert func(3,4) == 7


# "run": "pytest -v --no-header tests/testnotebook.py",
