import pytest

def run():
    pytest.main(["-v","./pytest_tests",
                 "--junitxml",'./report/log.xml'])
if __name__=="__main__":
    run()