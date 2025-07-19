def get_available_slots(zone, duration):
    return [
        {"time": "09:00", "date": "2025-07-20", "available": True},
        {"time": "10:30", "date": "2025-07-20", "available": False},
        {"time": "12:00", "date": "2025-07-20", "available": True},
    ]

def save_booking(name, phone, postcode, service, slot):
    print(f"Saving booking: {name}, {slot}")
