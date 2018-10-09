"""Function to create a random numbners."""

import datetime
import random
import string
from datetime import date


def random_id():
    """Create a random number based on time."""
    date_str = date.today().strftime('%Y%m%d')[
        2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str
