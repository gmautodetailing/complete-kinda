def get_zone_by_postcode(postcode):
    postcode = postcode.replace(" ", "").lower()
    if postcode.startswith("sw148") or postcode.startswith("sw146"):
        return "east"
    return "west"
