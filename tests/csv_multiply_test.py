"""Testing addition"""
import glob
import os

import pandas as pd
from calc.operations.multiplication import Multiplication

# pylint: disable=too-few-public-methods, unnecessary-comprehension, consider-using-with, unspecified-encoding

dir_name = os.path.dirname(__file__)
folder = os.path.join(dir_name, 'csv')

files = glob.glob(folder + "/*.csv")
f = open(folder + "log.txt", 'a')


def test_multiplication_10_val_1():
    """testing calc result"""
    nums = pd.read_csv(folder+'/10val1.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    multiplication = Multiplication(nums_tuple)
    assert int(multiplication.get_result()) == 25926700


def test_multiplication_10_val_2():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10val2.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    multiplication = Multiplication(nums_tuple)
    assert int(multiplication.get_result()) == 9981685728


def test_multiplication_10_val_3():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10val3.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    multiplication = Multiplication(nums_tuple)
    assert int(multiplication.get_result()) == 1287173721


def test_multiplication_10_val_4():
    """testing calc result"""
    nums = pd.read_csv('tests/csv/10val4.csv')
    num_list = [item for item in nums]
    nums_tuple = tuple(num_list)
    multiplication = Multiplication(nums_tuple)
    assert int(multiplication.get_result()) == 1390992523


f.close()
