import numpy as np

# nan means Not-a-number

# expression:
0 * np.nan                  # Outputs: nan
np.nan == np.nan            # Outputs: False (NaN values are not equal to themselves)
np.inf > np.nan             # Outputs: False (infinity is not greater than NaN)
np.nan - np.nan             # Outputs: nan (mathematical operations with NaN result in NaN)
np.nan in set([np.nan])     # Outputs: True (NaN is in the set containing NaN)
0.3 == 3 * 0.1              # Outputs: False (due to floating-point precision, 0.3 is not exactly equal to 3 * 0.1)