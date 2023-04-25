def study_schedule(permanence_period, target_time):
    if not target_time and target_time != 0:
        return None

    count = 0
    for i in permanence_period:
        if type(i[0]) != int or type(i[1]) != int:
            return None
        if target_time >= i[0] and target_time <= i[1]:
            count += 1

    return count
