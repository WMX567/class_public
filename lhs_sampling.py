import numpy as np
from pyDOE import lhs
from itertools import product

# Define the parameter ranges
# param_ranges = {
#     'omega_b': [0.015, 0.03],
#     'omega_cdm': [0.09, 0.15],
#     'ln_A_s_1e10': [2.5, 3.5],
#     'n_s': [0.85, 1.05],
#     'h': [0.4, 1.0],
#     'N_eff': [1.5, 5.5],
#     'tau_reio': [0.02, 0.20]
# }

# # Number of samples for each parameter
# n_samples = {
#     'omega_b': 8,
#     'omega_cdm': 8,
#     'ln_A_s_1e10': 8,
#     'n_s': 8,
#     'h': 8,
#     'N_eff': 8,
#     'tau_reio': 8
# }

# # Latin Hypercube Sampling for each parameter
# def lhs_sampling(param_ranges, n_samples):
#     sampled_params = {}
#     for param, n in n_samples.items():
#         # LHS sampling (scaled to [0, 1] and then to parameter range)
#         lhs_samples = lhs(n, samples=1)
#         min_val, max_val = param_ranges[param]
#         scaled_samples = min_val + (max_val - min_val) * lhs_samples.flatten()
#         sampled_params[param] = scaled_samples
#     return sampled_params

# # Function to combine LHS samples for each parameter into all possible combinations
# def generate_lhs_combinations(sampled_params):
    
#     sampled_arrays = [sampled_params[param] for param in sampled_params]
#     param_names = [param for param in sampled_params]

#     combined_samples = list(product(*sampled_arrays))
#     combined_data = np.array(combined_samples)
    
#     return param_names, combined_data


# # Function to split the combined data into Training, Validation, and Test sets
# def split_combined_data(combined_data, train_frac=0.75, val_frac=0.10):
#     total_samples = len(combined_data)
#     indices = np.arange(total_samples)
    
#     # Shuffle the indices
#     np.random.shuffle(indices)
#     np.random.shuffle(indices)
#     np.random.shuffle(indices)
    
#     # Calculate the number of samples for each set
#     train_size = int(train_frac * total_samples)
#     val_size = int(val_frac * total_samples)

#     train_indices = indices[:train_size]
#     val_indices = indices[train_size:train_size + val_size]
#     test_indices = indices[train_size + val_size:]
    
#     train_data_split = combined_data[train_indices[:42614]]
#     val_data_split = combined_data[val_indices]
#     test_data_split = combined_data[test_indices[:9531]]
    
#     return train_data_split, val_data_split, test_data_split

# # Perform LHS sampling
# sampled_params = lhs_sampling(param_ranges, n_samples)
# param_names, combined_samples = generate_lhs_combinations(sampled_params)

# # Extract each split (train, val, test) for saving
# train_data_split, val_data_split, test_data_split = split_combined_data(combined_samples)
# train_data = {param: train_data_split[:, index] for index, param in enumerate(param_names)}
# val_data = {param: val_data_split[:, index] for index, param in enumerate(param_names)}
# test_data = {param: test_data_split[:, index] for index, param in enumerate(param_names)}

# print(len(train_data['omega_b']), len(train_data['omega_cdm']), len(train_data['h']), len(train_data['tau_reio']), len(train_data['n_s']), len(train_data['ln_A_s_1e10']), len(train_data['N_eff']))

# Save each set into separate .npz files
train_path = 'dataset/neff_train_param.npz'
val_path = 'dataset/neff_val_param.npz'
test_path = 'dataset/neff_test_param.npz'

# # Save training data
# np.savez(train_path, 
#          omega_b=train_data['omega_b'],
#          omega_cdm=train_data['omega_cdm'],
#          h=train_data['h'],
#          tau_reio=train_data['tau_reio'],
#          n_s=train_data['n_s'],
#          ln_A_s_1e10=train_data['ln_A_s_1e10'],
#          N_eff=train_data['N_eff'])

# Save validation data
val_data = np.load(val_path)
np.savez(val_path, 
         omega_b=val_data['omega_b'],
         omega_cdm=val_data['omega_cdm'],
         h=val_data['h']*100,
         tau_reio=val_data['tau_reio'],
         n_s=val_data['n_s'],
         ln_A_s_1e10=val_data['ln_A_s_1e10'],
         N_eff=val_data['N_eff'])

# Save test data
test_data = np.load(test_path)
np.savez(test_path, 
         omega_b=test_data['omega_b'],
         omega_cdm=test_data['omega_cdm'],
         h=test_data['h']*100,
         tau_reio=test_data['tau_reio'],
         n_s=test_data['n_s'],
         ln_A_s_1e10=test_data['ln_A_s_1e10'],
         N_eff=test_data['N_ur'])

