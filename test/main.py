from tests import tests
def test_all():
    for test in tests:
        test()
    
if __name__ == "__main__":
    test_all()