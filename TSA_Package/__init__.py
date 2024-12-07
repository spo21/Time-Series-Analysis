

from .data_preprocessing import analyse_data, data_split, normalise_data
from .get_data import get_data
from .ml_techniques import linear_regression



# Define package-level metadata
__version__ = "1.0.0"
__author__ = "Stuart Ogborne"
__all__ = ["analyse_data", "get_data", "data_split", "linear_regression"]