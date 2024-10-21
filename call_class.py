import numpy as np
from classy import Class

for file_name in ['dataset/neff_train_param.npz', 'dataset/neff_val_param.npz', 'dataset/neff_test_param.npz']:
    data = np.load(file_name)
    tt = []
    ll = []

    for i in range(len(data["omega_b"])):

        common_settings = {'h':data['h'][i],
                            'omega_b':data['omega_b'][i],
                            'omega_cdm':data['omega_cdm'][i],
                            'ln_A_s_1e10':data['ln_A_s_1e10'][i],
                            'n_s':data['n_s'][i],
                            'tau_reio':data['tau_reio'][i],
                            'N_eff':data['N_eff'][i],
                            'output':'tCl'}

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
    np.savez(file_name.replace('param', 'tt'), features=np.log(tt), modes=ll)
