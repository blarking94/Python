import pytest

# A simple function that adds one to a number 
def simple_addition(x):
	return x + 1 


# Simple assert to test the function works, you can include your own assertion message. Using the Test Key Word 
def test_simple_addition():
	assert simple_addition(5) == 6, "your simple addition function didn't work!"

# We can also test that errors are thrown, this test should throw a type error. Good for when we want to test exceptions are thrown 
def test_error_should_be_thrown():
	with pytest.raises(TypeError) as addition_error:
			assert simple_addition("Pass") == 6

# Similar to above but maybe better for when there's a known bug in a dependancy and you don't want to forget 
@pytest.mark.xfail(raises=TypeError)
def test_error_should_be_thrown_2():
    simple_addition("Pass") == 6


@pytest.fixture
def base_input():
	return 10

def test_divisable_by_5(base_input):
	assert base_input % 5 == 0

def test_divisable_by_3(base_input):
	assert base_input % 3 == 0, " failed as remainder is " + str(base_input % 3)


@pytest.yield_fixture
def setup_teardown(autouse=True):
    
    # Set up Tables / Databases here

    yield # Run the tests 
    
    # Drop the tables here

    