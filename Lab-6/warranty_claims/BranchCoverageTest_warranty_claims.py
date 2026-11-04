"""Branch coverage tests for warranty_claims.py.

Every if/elif/else in the module is driven both ways, and the boundary values
on each comparison are checked as well.
"""
import pytest

from warranty_claims import out_of_warranty_charge, claim_allowed, sla_status


# out_of_warranty_charge

def test_unknown_plan_raises():
    with pytest.raises(ValueError, match="unknown plan"):
        out_of_warranty_charge("gold", 10, "defect", False)


def test_negative_age_raises():
    with pytest.raises(ValueError, match="invalid age"):
        out_of_warranty_charge("basic", -1, "defect", False)


def test_age_zero_is_valid():
    assert out_of_warranty_charge("basic", 0, "defect", False) == 0


def test_within_warranty():
    assert out_of_warranty_charge("standard", 20, "defect", False) == 0


def test_exactly_at_coverage_end_is_free():
    # excess == 0 takes the "<= 0" branch
    assert out_of_warranty_charge("basic", 12, "defect", False) == 0


def test_registration_extends_basic_and_standard():
    # 28 months would be 4 over on standard, but registration adds 6
    assert out_of_warranty_charge("standard", 28, "defect", True) == 0
    assert out_of_warranty_charge("basic", 18, "defect", True) == 0


def test_registration_does_not_extend_premium():
    # premium stays at 36 even when registered, so 40 months is 4 over
    assert out_of_warranty_charge("premium", 40, "defect", True) == 4 * 100


def test_defect_small_excess():
    assert out_of_warranty_charge("basic", 13, "defect", False) == 1 * 100


def test_accidental_small_excess():
    assert out_of_warranty_charge("standard", 40, "accidental", True) == 10 * 200


def test_excess_of_exactly_12_has_no_surcharge():
    assert out_of_warranty_charge("basic", 24, "defect", False) == 12 * 100
    assert out_of_warranty_charge("basic", 24, "accidental", False) == 12 * 200


def test_defect_large_excess():
    # 13 months over: rate 100 + 50
    assert out_of_warranty_charge("basic", 25, "defect", False) == 13 * 150


def test_accidental_large_excess():
    # 18 months over: rate 200 + 50 + 25
    assert out_of_warranty_charge("basic", 30, "accidental", False) == 18 * 275


# claim_allowed

def test_claim_allowed():
    assert claim_allowed(60, 1, False) is True


def test_recall_within_limit():
    assert claim_allowed(5, 5, True) is True


def test_recall_over_limit():
    assert claim_allowed(5, 6, True) is False


def test_claim_too_soon():
    assert claim_allowed(29, 0, False) is False


def test_claim_at_30_days():
    assert claim_allowed(30, 2, False) is True


def test_too_many_claims():
    assert claim_allowed(90, 3, False) is False


# sla_status

def test_hardware_on_track():
    assert sla_status(48, True, False) == "on_track"


def test_hardware_at_risk():
    assert sla_status(36, True, False) == "at_risk"


def test_hardware_priority_critical():
    # cutoff 72, at risk from 60, so 59 is critical
    assert sla_status(59, True, True) == "critical"


def test_software_on_track():
    assert sla_status(24, False, False) == "on_track"


def test_software_priority_at_risk():
    assert sla_status(40, False, True) == "at_risk"


def test_software_critical():
    assert sla_status(11, False, False) == "critical"
