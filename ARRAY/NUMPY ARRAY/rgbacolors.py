# import numpy as np

# # np.dtype() : define data

# # define custom dtype for colors
# # tuple is immutable so is used to specify a color and its data type
# rgbadtype = np.dtype([('R','u1'),('G','u1'),('B','u1'),('A','u1')])

# # an array of RBGA colors using custom dtype 
# custom_colors = np.array([(255,0,128,128),    # A red color with some blue, 50% opacity 
#                           (0,128,0,255),      # A green color, 100% opacity  
#                           (0,0,255,128)],     # A blue color, 50% opacity
#                          dtype=rgbadtype)

# red_channel = custom_colors['R']
# green_channel = custom_colors['G']
# blue_channel = custom_colors['B']
# alpha_channel = custom_colors['A']

# if __name__ == "__main__":
#     print(f"Red channel: {red_channel}")
#     print(f"Green channel: {green_channel}")
#     print(f"Blue channel: {blue_channel}")
#     print(f"Alpha channel: {alpha_channel}")

#     print(f"First color: {custom_colors[0]}")
#     print(f"Second color: {custom_colors[1]}")
#     print(f"Third color: {custom_colors[2]}")