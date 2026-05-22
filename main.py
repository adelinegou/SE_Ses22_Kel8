def calculate_gym_membership(age: int, membership_type: str, access_day: str, membership_duration: int):
    if age < 12: return "Rejected: Age below 12"
    if membership_duration < 1 or membership_duration > 12: return "Rejected: Invalid duration"
    if membership_type not in ["Regular", "Student", "Premium"]: return "Rejected: Invalid membership type"
    if access_day not in ["Weekday", "Weekend"]: return "Rejected: Invalid access day"

    base_rate = 50.0 
    if age > 60:
        base_rate *= 0.7
    elif membership_type == "Student":
        base_rate *= 0.8

    surcharge = 0.0
    if access_day == "Weekend" and membership_type != "Premium":
        surcharge = 5.0

    return (base_rate + surcharge) * membership_duration

# simulate merge conflict 2
