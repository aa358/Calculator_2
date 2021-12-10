"""Testing addition"""
import glob
import os

import pandas as pd
from calc.operations.subtraction import Subtraction

# pylint: disable=too-few-public-methods, unnecessary-comprehension, consider-using-with, unspecified-encoding

dir_name = os.path.dirname(__file__)
folder = os.path.join(dir_name, 'csv')

files = glob.glob(folder + "/*.csv")
f = open("tests/log.txt", 'a')


def test_addition_10_val_1():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10val1.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    subtraction = Subtraction(nums_tuple)
    assert int(subtraction.get_result()) == -89


def test_addition_10_val_2():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10val2.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    subtraction = Subtraction(nums_tuple)
    assert int(subtraction.get_result()) == -133


def test_addition_10_val_3():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10val3.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    subtraction = Subtraction(nums_tuple)
    assert int(subtraction.get_result()) == -98


def test_addition_10_val_4():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10val4.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    subtraction = Subtraction(nums_tuple)
    assert int(subtraction.get_result()) == -108


def test_addition_10000_val_1():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10000val1.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    subtraction = Subtraction(nums_tuple)
    assert int(subtraction.get_result()) == -50167282


def test_addition_10000_val_2():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10000val2.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    subtraction = Subtraction(nums_tuple)
    assert int(subtraction.get_result()) == -49341183


def test_addition_10000_val_3():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10000val3.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    subtraction = Subtraction(nums_tuple)
    assert int(subtraction.get_result()) == -49831624


def test_addition_10000_val_4():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10000val4.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    subtraction = Subtraction(nums_tuple)
    assert int(subtraction.get_result()) == -50037047


f.close()
