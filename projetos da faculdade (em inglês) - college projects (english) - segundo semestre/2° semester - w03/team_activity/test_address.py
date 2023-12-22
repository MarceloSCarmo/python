
from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city ("525 S Center St, Rexburg, ID 83460") == \
        "Rexburg"
    assert extract_city ("2193 S Main St, South Salt Lake, UT 60080") == \
        "South Salt Lake" 

def test_extract_state():
    assert extract_state ("525 S Center St, Rexburg, ID 83460") == \
        "ID" 
    assert extract_state ("2193 S Main St, South Salt Lake, UT 60080") == \
        "UT" 
    
def test_extract_zipcode():
    assert extract_zipcode ("525 S Center St, Rexburg, ID 83460") == \
        "83460"
    assert extract_zipcode ("2193 S Main St, South Salt Lake, UT 60080") == \
        "60080"

pytest.main(["-v", "--tb=line", "-rN", __file__])