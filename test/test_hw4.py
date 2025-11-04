import pytest
from hw4 import count_simba, get_day_month_year, compute_distance, sum_general_int_list
import datetime as dt
import pandas as pd


# ----------------------------------------------------------
# 1) count_simba
# ----------------------------------------------------------

def test_count_simba_with_simba():

    sentences = [
        "Simba and Nala are lions.",
        "I laugh in the face of danger.",
        "Hakuna matata",
        "Timon, Pumba and Simba are friends, but Simba could eat the other two."
    ]
    output = count_simba(sentences)
    expected_output = 3
    assert output == expected_output

def test_count_simba_without_simba():

    sentences = [
        "I laugh in the face of danger.", 
        "Hakuna matata"
    ]
    output = count_simba(sentences)
    expected_output = 0
    assert output == expected_output


# ----------------------------------------------------------
# 2) get_day_month_year
# ----------------------------------------------------------

def test_get_day_month_year():

    dates = [
        dt.date(2025, 3, 23),
        dt.date(1978, 11, 21),
        dt.date(2015, 12, 7)
    ]
    output = get_day_month_year(dates)
    expected_output = pd.DataFrame({
        "day": [23, 21, 7],
        "month": [3, 11, 12],
        "year": [2025, 1978, 2015]
    })
    pd.testing.assert_frame_equal(output.reset_index(drop=True), expected_output)

def test_get_day_month_year_empty():

    dates = [
    ]
    output = get_day_month_year(dates)
    assert isinstance(output, pd.DataFrame)
    assert output.empty


# ----------------------------------------------------------
# 3) compute_distance
# ----------------------------------------------------------

def test_compute_distance_one_pair():

    coord = [
        ((41.23, 23.5), (41.5, 23.4))
    ]
    output = compute_distance(coord)
    assert isinstance(output, list)
    assert len(output) == 1


def test_compute_distance_multiple_pairs():

    coord = [
        ((41.23, 23.5), (41.5, 23.4)),
        ((52.38, 20.1), (52.3, 17.8))
    ]
    output = compute_distance(coord)
    assert isinstance(output, list)
    assert len(output) == 2
    assert all(isinstance(x, float) for x in output)

def test_compute_distance_empty():

    coord = [
    ]
    output = compute_distance(coord)
    assert isinstance(output, list)
    assert output == []


# ----------------------------------------------------------
# 4) sum_general_int_list
# ----------------------------------------------------------

def test_sum_general_int_list():

    input_list = [
        [[2], 4, 5, [1, [2], [3, 5, [7, 8]], 10], 1]
    ]
    output = sum_general_int_list(input_list)
    expected_output = 48
    assert output == expected_output

def test_sum_general_int_list_empty():

    input_list = [
    ]
    output = sum_general_int_list(input_list)
    expected_output = 0
    assert output == expected_output