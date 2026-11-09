
from sdc.files import read_sdc_tileset
from sdc.pf import partition_function, partition_function_database, partition_function_database_2

import math


def test_partition_function__bitcopy_4pos_0():
    Z = partition_function(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos_0.json"), 273.15 + 37)
    assert math.isclose(Z, 54.730, abs_tol = 0.001)
    # assert math.isclose(Z, 55.604, abs_tol = 0.001)

def test_partition_function__bitcopy_4pos_1():
    Z = partition_function(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos_1.json"), 273.15 + 37)
    assert math.isclose(Z, 54.738, abs_tol = 0.001)
    # assert math.isclose(Z, 55.612, abs_tol = 0.001)



def test_partition_function__bitcopy_11pos_0():
    pf = partition_function(read_sdc_tileset("./data/sdc/1D/bitcopy_11pos_0.json"), 273.15 + 37)
    assert math.isclose(pf, 361527.976, abs_tol = 0.001)

def test_partition_function__bitcopy_11pos_1():
    pf = partition_function(read_sdc_tileset("./data/sdc/1D/bitcopy_11pos_1.json"), 273.15 + 37)
    assert math.isclose(pf, 361578.034, abs_tol = 0.001)



def test_partition_function_database__bitcopy_4pos_0():
    C, Z = partition_function_database(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos_0.json"), 273.15 + 37)
    assert len(C) == 2 * 3 * 3 * 3
    assert math.isclose(Z, 55.604, abs_tol = 0.001)

def test_partition_function_database__bitcopy_4pos_1():
    C, Z = partition_function_database(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos_1.json"), 273.15 + 37)
    assert len(C) == 2 * 3 * 3 * 3
    assert math.isclose(Z, 55.612, abs_tol = 0.001)




# def test_partition_function_database__bitcopy_11pos_0():
#     C, Z = partition_function_database(read_sdc_tileset("./data/sdc/1D/bitcopy_11pos_0.json"), 273.15 + 37)
#     assert len(C) == 2 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3
#     assert math.isclose(Z, 389147.454, abs_tol = 0.001)

# def test_partition_function_database__bitcopy_11pos_1():
#     C, Z = partition_function_database(read_sdc_tileset("./data/sdc/1D/bitcopy_11pos_1.json"), 273.15 + 37)
#     assert len(C) == 2 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3
#     assert math.isclose(Z, 389201.872, abs_tol = 0.001)




def test_partition_function_database_2__bitcopy_4pos_0():
    C, Z = partition_function_database_2(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos_0.json"), 273.15 + 37)
    assert len(C) == 2 * 3 * 3 * 3
    assert math.isclose(Z, 55.604, abs_tol = 0.001)

def test_partition_function_database_2__bitcopy_4pos_1():
    C, Z = partition_function_database_2(read_sdc_tileset("./data/sdc/1D/bitcopy_04pos_1.json"), 273.15 + 37)
    assert len(C) == 2 * 3 * 3 * 3
    assert math.isclose(Z, 55.612, abs_tol = 0.001)
