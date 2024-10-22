def split_equal(total_amount, users_count):
    return total_amount / users_count

def validate_percentage(splits):
    total_percentage = sum([split["percentage"] for split in splits])
    if total_percentage != 100:
        raise ValueError("Total percentages must add up to 100.")
