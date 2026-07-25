from ai.normalizer import normalize_value


def check_eligibility(profile, scheme):

    eligible = True
    reasons = []

    eligibility = scheme.get("eligibility", {})

    # Normalize profile values
    user_occupation = normalize_value(profile["occupation"])
    user_gender = normalize_value(profile["gender"])
    user_state = normalize_value(profile["state"])

    # Occupation
    if "occupation" in eligibility:

        scheme_occ = normalize_value(eligibility["occupation"])

        if user_occupation == scheme_occ:
            reasons.append("Occupation matches.")

        else:
            eligible = False
            reasons.append("Occupation does not match.")

    # Gender
    if "gender" in eligibility:

        scheme_gender = normalize_value(eligibility["gender"])

        if user_gender == scheme_gender:
            reasons.append("Gender matches.")

        else:
            eligible = False
            reasons.append("Gender does not match.")

    # State
    if "state" in eligibility:

        scheme_state = normalize_value(eligibility["state"])

        if scheme_state != "all states":

            if user_state == scheme_state:
                reasons.append("State matches.")

            else:
                eligible = False
                reasons.append("State does not match.")

    # Income
    income_limit = eligibility.get("income_limit")

    if income_limit is not None:

        if int(profile["income"]) <= income_limit:
            reasons.append("Income within limit.")

        else:
            eligible = False
            reasons.append("Income exceeds limit.")

    # Age
    if "age" in eligibility:

        minimum, maximum = map(
            int,
            eligibility["age"].split("-")
        )

        age = int(profile["age"])

        if minimum <= age <= maximum:
            reasons.append("Age matches.")

        else:
            eligible = False
            reasons.append("Age does not match.")

    return eligible, reasons