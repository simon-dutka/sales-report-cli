import pytest

from src.calculations import calculate_overall


def test_calculate_overall_single_transaction():
    transactions = [
        {
            "date": "2026-01-05",
            "product": "Laptop",
            "category": "Electronics",
            "salesperson": "Ann",
            "cost_price": 100.0,
            "sell_price": 200.0,
            "quantity": 1,
        }
    ]

    result = calculate_overall(transactions)
    assert result["revenue"] == 200
    assert result["cost"] == 100
    assert result["profit"] == 100
    assert result["margin"] == 50


def test_calculate_overall_quantity_multiplication():
    transactions = [
        {
            "date": "2026-01-09",
            "product": "Keyboard",
            "category": "Electronics",
            "salesperson": "Bob",
            "cost_price": 80,
            "sell_price": 150,
            "quantity": 3,
        }
    ]

    result = calculate_overall(transactions)
    assert result["revenue"] == 450
    assert result["cost"] == 240
    assert result["profit"] == 210
    assert result["margin"] == pytest.approx(46.67, rel=0.01)


def test_calculate_overall_zero_revenue():
    transactions = [
        {
            "date": "2026-01-07",
            "product": "Mouse",
            "category": "Electronics",
            "salesperson": "Ann",
            "cost_price": 40,
            "sell_price": 0,
            "quantity": 1,
        }
    ]

    result = calculate_overall(transactions)
    assert result["revenue"] == 0
    assert result["cost"] == 40
    assert result["profit"] == -40
    assert result["margin"] == 0


def test_calculate_overall_multiple_transactions():
    transactions = [
        {
            "date": "2026-01-10",
            "product": "Chair",
            "category": "Furniture",
            "salesperson": "Cara",
            "cost_price": 120,
            "sell_price": 300,
            "quantity": 3,
        },
        {
            "date": "2026-01-11",
            "product": "Mouse",
            "category": "Electronics",
            "salesperson": "Ann",
            "cost_price": 40,
            "sell_price": 80,
            "quantity": 4,
        },
    ]

    result = calculate_overall(transactions)

    assert result["revenue"] == 1220
    assert result["cost"] == 520
    assert result["profit"] == 700
    assert result["margin"] == pytest.approx(57.37, rel=0.01)
