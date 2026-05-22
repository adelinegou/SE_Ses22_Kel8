def calculate_gym_membership(age: int, membership_type: str, access_day: str, membership_duration: int):
    if age < 12: 
        return "Rejected: Age below 12"
        
    base_rate = 50.0 
    if membership_type == "Student":
        base_rate *= 0.8
        
    return base_rate * membership_duration
