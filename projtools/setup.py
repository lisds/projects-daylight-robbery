""" Setup code

This file sets up the initial environment.
"""
import hashlib
from pathlib import Path
import pandas as pd

def get_data_hash(filename):
    """ Get the hash of the data file
    
    Parameters
    ----------
    filename : str
        The name of the data file to check the hash of.
        
    Returns
    -------
    hash : str
        The hash of the data file.
    """
    base = Path(__file__).parent.parent
    filename = base / "data" / filename
    return hashlib.sha1(filename.read_bytes()).hexdigest()
