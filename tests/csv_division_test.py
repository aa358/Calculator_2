"""Testing addition"""
import glob
import os

import pandas as pd
from calc.operations.division import Division

# pylint: disable=too-few-public-methods, unnecessary-comprehension, consider-using-with, unspecified-encoding

dir_name = os.path.dirname(__file__)
folder = os.path.join(dir_name, 'csv')

files = glob.glob(folder + "/*.csv")
f = open("tests/log.txt", 'a')


def test_division_10_val_1():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10val1.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    division = Division(nums_tuple)
    assert division.get_result() == 46.12142552283398


def test_division_10_val_2():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10val2.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    division = Division(nums_tuple)
    assert division.get_result() == 305.9338235294118


def test_division_10_val_3():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10val3.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    division = Division(nums_tuple)
    assert division.get_result() == 9.801149750259166


def test_division_10_val_4():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10val4.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    division = Division(nums_tuple)
    assert division.get_result() == 0.3679713351891294


f.close()
