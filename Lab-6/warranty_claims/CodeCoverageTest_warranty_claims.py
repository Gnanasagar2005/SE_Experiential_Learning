"""Line (statement) coverage tests for warranty_claims.py.

Each test is picked so that every statement in the module runs at least once.
"""
import pytest

from warranty_claims import out_of_warranty_charge, claim_allowed, sla_status


# out_of_warranty_charge

def test_within_warranty():
    assert out_of_warranty_charge("standard", 20, "defect", False) == 0


def test_unknown_plan_raises():
    with pytest.raises(ValueError, match="unknown plan"):
        out_of_warranty_charge("gold", 10, "defect", False)


def test_negative_age_raises():
    with pytest.raises(ValueError, match="invalid age"):
        out_of_warranty_charge("basic", -1, "defect", False)


def test_registered_accidental_small_excess():
    # standard 24 + 6 for registration = 30 months covered, 10 months over
    assert out_of_warranty_charge("standard", 40, "accidental", True) == 10 * 200


def test_accidental_large_excess():
    # basic covers 12 months, 18 months over, rate 200 + 50 + 25
    assert out_of_warranty_charge("basic", 30, "accidental", False) == 18 * 275


# claim_allowed

def test_claim_allowed():
    assert claim_allowed(60, 1, False) is True


def test_recall_claim():
    assert claim_allowed(5, 4, True) is True


def test_claim_too_soon():
    assert claim_allowed(10, 0, False) is False


# sla_status

def test_hardware_on_track():
    assert sla_status(50, True, False) == "on_track"


def test_software_priority_at_risk():
    # cutoff 24 + 24 = 48, at risk from 36 to 47
    assert sla_status(40, False, True) == "at_risk"


def test_software_critical():
    assert sla_status(5, False, False) == "critical"
