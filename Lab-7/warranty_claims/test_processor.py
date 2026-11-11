import math

from hypothesis import given, settings, strategies as st
from warranty_claims import parse_claim, age_average, payable_charge

plans = st.sampled_from(["basic", "standard", "premium", " Standard ", "PREMIUM"])
numbers = st.floats(min_value=0, max_value=1e6, allow_nan=False, allow_infinity=False)
ages = st.integers(min_value=0, max_value=600)


@settings(max_examples=500)
@given(st.text() | st.none())
def test_parse_claim_no_crash(s):
    try:
        parse_claim(s)
    except Exception as e:
        assert False, f"parse_claim crashed with: {e!r}"


@settings(max_examples=500)
@given(st.text() | st.none())
def test_age_average_no_crash(s):
    try:
        age_average(s)
    except Exception as e:
        assert False, f"age_average crashed with: {e!r}"


@settings(max_examples=500)
@given(st.text() | st.none())
def test_payable_charge_no_crash(s):
    try:
        payable_charge(s)
    except Exception as e:
        assert False, f"payable_charge crashed with: {e!r}"


@given(plans, numbers)
def test_parse_claim_valid(plan, months):
    result = parse_claim(f"{plan}:{months}")
    assert result == (plan.strip().title(), months)


@given(st.from_regex(r"\A[a-z]*:(nan|inf|-inf|-[1-9][0-9]*)\Z"))
def test_parse_claim_rejects_bad_months(s):
    assert parse_claim(s) is None


@given(st.lists(ages, min_size=1, max_size=20))
def test_age_average_valid(values):
    result = age_average(",".join(str(v) for v in values))
    assert result is not None
    assert min(values) <= result <= max(values)


@given(st.lists(ages, max_size=5))
def test_age_average_empty_item(values):
    assert age_average(",".join(str(v) for v in values) + ",") is None


@given(numbers, numbers)
def test_payable_charge_valid(charge, discount):
    result = payable_charge(f"{charge}|{discount}")
    assert result is not None
    assert result >= 0
    assert math.isfinite(result)


@given(st.sampled_from(["nan", "inf", "-inf", "-5"]), numbers)
def test_payable_charge_rejects_bad_charge(charge, discount):
    assert payable_charge(f"{charge}|{discount}") is None
