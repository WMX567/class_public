import numpy as np
from classy import Class  # 确保你已经导入Class库

with open('log.txt', 'w') as f:
    for file_name in ['dataset/neff_train_param.npz', 'dataset/neff_val_param.npz', 'dataset/neff_test_param.npz']:
        data = np.load(file_name)
        tt = []
        ll = []

        for i in range(len(data["omega_b"])):
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
            
            f.write(str(i+1) + '\n')  # 添加换行符
            
            cosmo = Class()  # 创建Class实例
            cosmo.set(common_settings)
            cosmo.compute()
            
            cl = cosmo.raw_cl(2500)
            tt.append(cl['tt'][2:])  # 提取tt模式
            ll.append(cl['ell'][2:])  # 提取ell模式
            
            cosmo.struct_cleanup()
            cosmo.empty()

        # 将结果保存为新的文件
        tt = np.array(tt)
        ll = np.array(ll)
        output_file = file_name.replace('param', 'tt')
        np.savez(output_file, features=np.log(tt), modes=ll)