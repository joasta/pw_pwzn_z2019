import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)

@pytest.fixture
def op_clc():
    return Calculator()

@pytest.mark.parametrize(
    'operate, param_1, param_2, expected',
    [
        pytest.param('+', '+', '-', '-', '/', '/', '*', '*', id='Operation'),  
		pytest.param(3, 12, 3, 12, 3, 12, 3, 12, id='First'),  
		pytest.param(3, 4, 3, 4, 3, 4, 3, 4, id='Second'),  
		pytest.param(6, 16, 0, 8, 1, 3, 9, 48, id='Expect'),  
    ],
)
def test_calculation(op_clc):
	assert op_clc.run(operate, param_1, param_2) == expected

def test_zero_division(op_clc):
    try:
        calc.run('/', 1, 0)
    except CalculatorError as exc:
        assert type(exc.__cause__) == ZeroDivisionError
    else:
        raise AssertionError

def test_memorisation(op_clc):
	op_clc.run('+', 11, 1)
	op_clc.memorize()
	assert op_clc.in_memory() == 12

@pytest.mark.parametrize(
    'operate, param_1, param_2, expected',
    [
        pytest.param('+', '+', '-', '-', '/', '/', '*', '*', id='Operation'),  
		pytest.param(3, 12, 3, 12, 3, 12, 3, 12, id='First'),  
		pytest.param(Null, Null, Null, Null, Null, Null, Null, Null, id='Second'),  
		pytest.param(6, 15, 0, 9, 1, 4, 9, 36, id='Expect'),  
    ],
)
def test_recall(op_clc):
	op_clc.run('+', 11, 1)
	op_clc.memorize()
	assert op_clc.run(operate, param_1) == expected

def test_missing_memory(op_clc):
	try:
        op_clc.in_memory()
    except CalculatorError as exc:
        assert type(exc) is EmptyMemory
    else:
        raise AssertionError

def test_missing_memory(op_clc):
	try:
        op_clc.run(operate, param_1)
    except CalculatorError as exc:
        assert type(exc) is EmptyMemory
    else:
        raise AssertionError

def test_wrong_operator(op_clc):
	try:
        a = op_clc.run('^', 2, 3)
    except CalculatorError as exc:
        assert type(exc) == WrongOperation
        assert a is None
    else:
        raise AssertionError

@pytest.mark.parametrize(
	'param_1, param_2',
	[ 
		pytest.param(3, '12', '3', id='First'),  
		pytest.param('4', 3, 'Null', id='Second'), 
	],
)
def test_wrong_type(op_clc):
	try:
        b = op_clc.run('+', param_1, param_2)
    except CalculatorError as exc:
        assert type(exc) == NotNumberArgument
        assert b is None
    else:
        raise AssertionError