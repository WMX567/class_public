# import necessary modules
# uncomment to get plots displayed in notebook
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

val_tt = np.load('dataset/plots_test.npz')['tt']
val_ll = np.load('dataset/plots_test.npz')['ll']


font = {'size': 14, 'family':'STIXGeneral'}
axislabelfontsize='medium'
matplotlib.rc('font', **font)
plt.rcParams["figure.figsize"] = [5.5,5.5]
plt.rcParams['legend.fontsize']='medium'


C_TT_LCDM = val_tt[0]
C_TT_model_eff = val_tt[1]
C_TT_model_ann = val_tt[2]
ll_0 = val_ll[0]
ll_1 = val_ll[1]
ll_2 = val_ll[2]
print(ll_0)

frac_residual_eff = (C_TT_model_eff - C_TT_LCDM) / C_TT_LCDM * 100
frac_residual_ann = (C_TT_model_ann - C_TT_LCDM) / C_TT_LCDM * 100

val_colors = ['purple', 'orange']
plt.plot(ll_1,  frac_residual_eff, color=val_colors[0],
             label=r'$N_\mathrm{eff}$', linewidth=2.0)
plt.plot(ll_2, frac_residual_ann, color=val_colors[1],
             label=r'$p_{\mathrm{ann}}$', linewidth=2.0)
plt.xlim(2, 3000)

plt.xlabel(r'$\ell$')
plt.ylabel(r'% Residual in $C_\ell^{TT}$')
plt.grid()
plt.legend()

plt.ylim(-1.0, 1.0)
plt.xlim(2, 2500)

plt.tight_layout()
plt.show()
plt.savefig('cltt.png')