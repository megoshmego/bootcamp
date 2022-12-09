def weekday_name(day_of_week):
    DAYS = [
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    ]

    if day_of_week < 0 or day_of_week > 7:
        return None

    return DAYS[day_of_week]