import numpy as np
import log
from classy import Class  # 确保你已经导入Class库
import argparse


parser = argparse.ArgumentParser(description='Data Generation')
parser.add_argument('--start', type=int, default=0, help='start index')
parser.add_argument('--end', type=int, default=100, help='end index')
args = parser.parse_args()

io = log.IOStream()

for file_name in ['dataset/neff_train_param.npz','dataset/neff_val_param.npz', 'dataset/neff_test_param.npz']:
    data = np.load(file_name)
    tt = []
    ll = []
    
    range_ = range(len(data["omega_b"]))

    for i in range_:
      
        common_settings = {
            'h': data['h'][i],
            'omega_b': data['omega_b'][i],
            'omega_cdm': data['omega_cdm'][i],
            'ln_A_s_1e10': data['ln_A_s_1e10'][i],
            'n_s': data['n_s'][i],
            'tau_reio': data['tau_reio'][i],
            'N_ur': data['N_eff'][i],
            'output': 'tCl'
        }

        io.cprint('Computing %d/%d' % (i + 1, range_))
        cosmo = Class() 
        cosmo.set(common_settings)
        cosmo.compute()
        
        cl = cosmo.raw_cl(2500)
        tt.append(cl['tt'][2:])  
        ll.append(cl['ell'][2:]) 
        
        cosmo.struct_cleanup()
        cosmo.empty()


    tt = np.array(tt)
    ll = np.array(ll)
    output_file = file_name.replace('param', 'tt')
    np.savez(output_file, features=np.log(tt), modes=ll)