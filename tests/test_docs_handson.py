"""Tests for the project.docs_handson module."""

import pytest

from project.docs_handson import calculate_bmi


def test_calculate_bmi__known_value():
    result = calculate_bmi(weight_kg=80.0, height_m=1.80)
    assert result == pytest.approx(24.691358, rel=1e-6)
