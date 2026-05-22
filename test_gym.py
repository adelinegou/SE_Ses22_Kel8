import pytest
from main import calculate_gym_membership

@pytest.mark.parametrize(
    "age, membership_type, access_day, membership_duration, expected_output",
    [
        (25, "Regular", "Weekday", 6, 300.0),
        (20, "Student", "Weekend", 3, 135.0),
        (65, "Regular", "Weekend", 12, 480.0),
        (35, "Premium", "Weekend", 1, 50.0),
        (10, "Regular", "Weekday", 6, "Rejected: Age below 12"),
        (0, "Regular", "Weekday", 6, "Rejected: Age below 12"),
        (25, "Regular", "Weekday", 0, "Rejected: Invalid duration"),
        (25, "Regular", "Weekday", 13, "Rejected: Invalid duration"),
        (25, "Unknown", "Weekday", 6, "Rejected: Invalid membership type"),
        (25, "Regular", "InvalidDay", 6, "Rejected: Invalid access day"),
    ]
)
def test_all_gym_rules(age, membership_type, access_day, membership_duration, expected_output):
    assert calculate_gym_membership(age, membership_type, access_day, membership_duration) == expected_output
