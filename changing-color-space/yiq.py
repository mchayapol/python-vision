import numpy as np
rgb = [5,7,3]
yiq_factor = [
        [0.299,0.587,0.114],
        [-0.596,-0.275,-0.321],
        [0.212,-0.528,0.311]
    ]
yiq = np.dot(yiq_factor,rgb)
print('RGB = ',rgb)
print('YiQ = ',yiq)

# Now try to find RGB from YIQ
yiq_factor_inv = np.linalg.inv(yiq_factor)
print(yiq_factor_inv)
rgb = np.dot(yiq_factor_inv,yiq)
print('RGB = ',rgb)
