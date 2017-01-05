from sinc2d import *

def test_sinc2c_x0y0():
    import numpy as ny
    expected_value=1
    calculated_value=sinc2d(0,0)
    assert expected_value==calculated_value
    
def test_sinc2c_x0y1():
    import numpy as ny
    expected_value=ny.sin(1)
    calculated_value=sinc2d(0,1)
    assert expected_value==calculated_value

def test_sinc2c_x1y0():
    import numpy as ny
    expected_value=ny.sin(1)
    calculated_value=sinc2d(1,0)
    assert expected_value==calculated_value

def test_sinc2c_x1y1():
    import numpy as ny
    expected_value=ny.sin(1)**2
    calculated_value=sinc2d(1,1)
    assert expected_value==calculated_value