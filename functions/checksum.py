"""Checksum calculation of a dict."""

import pickle
import hashlib


def calculate_and_return_checksum(info_dict):
    """Return chacksum of info_dict."""
    pickle_dump = pickle.dumps(info_dict)
    chksm = hashlib.md5(pickle_dump).hexdigest()
    return chksm
