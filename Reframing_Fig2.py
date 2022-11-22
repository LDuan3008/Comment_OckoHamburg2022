from Fun_final import final_emissions
from Fun_final import fun_rfCO2, fun_rfCH4, fun_rfH2
from Fun_final import fun_agwpCO2, fun_agwpCH4, fun_agwpH2
from Fun_final import fun_tCO2, fun_tCH4, fun_tH2
from Fun_final import fun_rfCO2sustained, fun_rfCH4sustained, fun_rfH2sustained
from Fun_final import fun_agwpCO2sustained, fun_agwpCH4sustained, fun_agwpH2sustained
from Fun_final import fun_tCO2sustained, fun_tCH4sustained, fun_tH2sustained
from Fun_final import fun_rfH2_lifetime14, fun_rfH2_lifetime25, fun_tH2_lifetime14, fun_tH2_lifetime25
from Fun_final import fun_rfH2sustained_lifetime14, fun_rfH2sustained_lifetime25, fun_tH2sustained_lifetime14, fun_tH2sustained_lifetime25
from Fun_final import fun_rfCH4_addCO2, fun_rfCH4sustained_addCO2, fun_tCH4_addCO2, fun_tCH4sustained_addCO2
import numpy as np 
import matplotlib.pyplot as plt 

LeakageRate_best = [0.01, 0.01]
LeakageRate_worst = [0.1, 0.03]
emissions_dic = []
emissions_dic.append( final_emissions(LeakageRate_best[1], LeakageRate_best[0]) )
emissions_dic.append( final_emissions(LeakageRate_worst[1], LeakageRate_worst[0]) )


############################################################################################################################################
"""
### Figure 2/3
nYear = 501
# scale_CO2_100yr, scale_CH4_100yr, scale_H2_100yr = np.array(fun_rfCO2(np.arange(nYear))), np.array(fun_rfCH4(np.arange(nYear))), np.array(fun_rfH2(np.arange(nYear)))
scale_CO2_100yr, scale_CH4_100yr, scale_H2_100yr = np.array(fun_tCO2(np.arange(nYear))), np.array(fun_tCH4(np.arange(nYear))), np.array(fun_tH2(np.arange(nYear)))
rf_H2Ele, rf_H2Ock, rf_CH4Bu = np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear])
for idx in range(len(emissions_dic)):
    rf_H2Ele[idx] = scale_CO2_100yr * emissions_dic[idx][0, 0] + scale_CH4_100yr * emissions_dic[idx][0, 1] + scale_H2_100yr * emissions_dic[idx][0, 2]
    rf_H2Ock[idx] = scale_CO2_100yr * emissions_dic[idx][1, 0] + scale_CH4_100yr * emissions_dic[idx][1, 1] + scale_H2_100yr * emissions_dic[idx][1, 2]
    rf_CH4Bu[idx] = scale_CO2_100yr * emissions_dic[idx][3, 0] # + scale_CH4_100yr * emissions_dic[idx][3, 1] + scale_H2_100yr * emissions_dic[idx][3, 2]

# scale_CO2_100yr, scale_CH4_100yr, scale_H2_100yr = np.array(fun_rfCO2sustained(np.arange(nYear))), np.array(fun_rfCH4sustained(np.arange(nYear))), np.array(fun_rfH2sustained(np.arange(nYear)))
scale_CO2_100yr, scale_CH4_100yr, scale_H2_100yr = np.array(fun_tCO2sustained(np.arange(nYear))), np.array(fun_tCH4sustained(np.arange(nYear))), np.array(fun_tH2sustained(np.arange(nYear)))
rf_H2Ele2, rf_H2Ock2, rf_CH4Bu2 = np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear])
for idx in range(len(emissions_dic)):
    rf_H2Ele2[idx] = scale_CO2_100yr * emissions_dic[idx][0, 0]*0.01 + scale_CH4_100yr * emissions_dic[idx][0, 1]*0.01 + scale_H2_100yr * emissions_dic[idx][0, 2]*0.01
    rf_H2Ock2[idx] = scale_CO2_100yr * emissions_dic[idx][1, 0]*0.01 + scale_CH4_100yr * emissions_dic[idx][1, 1]*0.01 + scale_H2_100yr * emissions_dic[idx][1, 2]*0.01
    rf_CH4Bu2[idx] = scale_CO2_100yr * emissions_dic[idx][3, 0]*0.01 # + scale_CH4_100yr * emissions_dic[idx][3, 1]*0.01 + scale_H2_100yr * emissions_dic[idx][3, 2]*0.01

# scale_CO2_100yrTp100, scale_CH4_100yrTp100, scale_H2_100yrTp100 = np.array(fun_rfCO2sustained(np.arange(nYear-100))), np.array(fun_rfCH4sustained(np.arange(nYear-100))), np.array(fun_rfH2sustained(np.arange(nYear-100)))
scale_CO2_100yrTp100, scale_CH4_100yrTp100, scale_H2_100yrTp100 = np.array(fun_tCO2sustained(np.arange(nYear-100))), np.array(fun_tCH4sustained(np.arange(nYear-100))), np.array(fun_tH2sustained(np.arange(nYear-100)))
scale_CO2_100yrTp100 = np.r_[np.zeros(100), scale_CO2_100yrTp100];      scale_CO2_100yrNew = scale_CO2_100yr - scale_CO2_100yrTp100
scale_CH4_100yrTp100 = np.r_[np.zeros(100), scale_CH4_100yrTp100];      scale_CH4_100yrNew = scale_CH4_100yr - scale_CH4_100yrTp100
scale_H2_100yrTp100  = np.r_[np.zeros(100), scale_H2_100yrTp100];       scale_H2_100yrNew  = scale_H2_100yr - scale_H2_100yrTp100
rf_H2Ele3, rf_H2Ock3, rf_CH4Bu3 = np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear]) 
for idx in range(len(emissions_dic)):
    rf_H2Ele3[idx] = scale_CO2_100yrNew * emissions_dic[idx][0, 0]*0.01 + scale_CH4_100yrNew * emissions_dic[idx][0, 1]*0.01 + scale_H2_100yrNew * emissions_dic[idx][0, 2]*0.01
    rf_H2Ock3[idx] = scale_CO2_100yrNew * emissions_dic[idx][1, 0]*0.01 + scale_CH4_100yrNew * emissions_dic[idx][1, 1]*0.01 + scale_H2_100yrNew * emissions_dic[idx][1, 2]*0.01
    rf_CH4Bu3[idx] = scale_CO2_100yrNew * emissions_dic[idx][3, 0]*0.01 # + scale_CH4_100yrNew * emissions_dic[idx][3, 1]*0.01 + scale_H2_100yrNew * emissions_dic[idx][3, 2]*0.01


# ratioBH_1 = rf_H2Ock[1]/rf_CH4Bu[1]
# ratioBH_2 = rf_H2Ock2[1]/rf_CH4Bu2[1]
# ratioBH_3 = rf_H2Ock3[1]/rf_CH4Bu3[1]
# print (ratioBH_1[5:25])
# print (ratioBH_2[5:25])
# print (ratioBH_3[5:25])
# stop 



# Stack plot
plt.stackplot(np.arange(nYear), [rf_H2Ele[0], rf_H2Ock[0]-rf_H2Ele[0]], colors=['green', 'blue'], alpha=0.3)
plt.plot(np.arange(nYear), rf_CH4Bu[0], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1); plt.ylim(0, 3e-14)
# plt.xlim(0, nYear-1); plt.ylim(0, 1.1e-14)
# plt.xlim(0, nYear-1); plt.ylim(0, 4.5e-14)
plt.xlim(0, nYear-1); plt.ylim(0, 3.5e-14)
# plt.show(); plt.clf() 
plt.savefig('Fig2a.ps'); plt.clf() 
plt.stackplot(np.arange(nYear), [rf_H2Ele[1], rf_H2Ock[1]-rf_H2Ele[1]], colors=['green', 'blue'], alpha=0.3)
plt.plot(np.arange(nYear), rf_CH4Bu[1], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1); plt.ylim(0, 3e-14) 
# plt.xlim(0, nYear-1); plt.ylim(0, 1.1e-14)
# plt.xlim(0, nYear-1); plt.ylim(0, 4.5e-14)
plt.xlim(0, nYear-1); plt.ylim(0, 3.5e-14)
# plt.show(); plt.clf() 
plt.savefig('Fig2b.ps'); plt.clf() 

plt.stackplot(np.arange(nYear), [rf_H2Ele2[0], rf_H2Ock2[0]-rf_H2Ele2[0]], colors=['green', 'blue'], alpha=0.3)
plt.plot(np.arange(nYear), rf_CH4Bu2[0], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1); plt.ylim(0, 4.5e-14)
# plt.xlim(0, nYear-1); plt.ylim(0, 3.5e-14)
# plt.xlim(0, nYear-1); plt.ylim(0, 4.5e-14)
plt.xlim(0, nYear-1); plt.ylim(0, 3.5e-14)
# plt.show(); plt.clf() 
plt.savefig('Fig2c.ps'); plt.clf() 
plt.stackplot(np.arange(nYear), [rf_H2Ele2[1], rf_H2Ock2[1]-rf_H2Ele2[1]], colors=['green', 'blue'], alpha=0.3)
plt.plot(np.arange(nYear), rf_CH4Bu2[1], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1); plt.ylim(0, 4.5e-14)
# plt.xlim(0, nYear-1); plt.ylim(0, 3.5e-14)
# plt.xlim(0, nYear-1); plt.ylim(0, 4.5e-14)
plt.xlim(0, nYear-1); plt.ylim(0, 3.5e-14)
# plt.show(); plt.clf() 
plt.savefig('Fig2d.ps'); plt.clf() 

plt.stackplot(np.arange(nYear), [rf_H2Ele3[0], rf_H2Ock3[0]-rf_H2Ele3[0]], colors=['green', 'blue'], alpha=0.3)
plt.plot(np.arange(nYear), rf_CH4Bu3[0], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1); plt.ylim(0, 1.4e-14)
# plt.xlim(0, nYear-1); plt.ylim(0, 0.8e-14)
# plt.xlim(0, nYear-1); plt.ylim(0, 4.5e-14)
plt.xlim(0, nYear-1); plt.ylim(0, 3.5e-14)
# plt.show(); plt.clf() 
plt.savefig('Fig2e.ps'); plt.clf() 
plt.stackplot(np.arange(nYear), [rf_H2Ele3[1], rf_H2Ock3[1]-rf_H2Ele3[1]], colors=['green', 'blue'], alpha=0.3)
plt.plot(np.arange(nYear), rf_CH4Bu3[1], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1); plt.ylim(0, 1.4e-14)
# plt.xlim(0, nYear-1); plt.ylim(0, 0.8e-14)
# plt.xlim(0, nYear-1); plt.ylim(0, 4.5e-14)
plt.xlim(0, nYear-1); plt.ylim(0, 3.5e-14)
# plt.show(); plt.clf() 
plt.savefig('Fig2f.ps'); plt.clf() 




# Line plot 

# plt.plot(np.arange(nYear), rf_H2Ele[0], color='green',  linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_H2Ock[0], color='blue',    linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_CH4Bu[0], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1)
# # plt.ylim(0, 3e-14)
# plt.ylim(0, 1.1e-14)
# plt.show()
# # plt.savefig('Fig2a.ps')
# plt.clf() 
# plt.plot(np.arange(nYear), rf_H2Ele[1], color='green',  linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_H2Ock[1], color='blue',    linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_CH4Bu[1], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1)
# # plt.ylim(0, 3e-14)
# plt.ylim(0, 1.1e-14)
# plt.show()
# # plt.savefig('Fig2b.ps')
# plt.clf() 

# plt.plot(np.arange(nYear), rf_H2Ele2[0], color='green',  linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_H2Ock2[0], color='blue',    linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_CH4Bu2[0], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1)
# # plt.ylim(0, 4.5e-14)
# plt.ylim(0, 3.5e-14)
# plt.show()
# # plt.savefig('Fig2c.ps')
# plt.clf() 
# plt.plot(np.arange(nYear), rf_H2Ele2[1], color='green',  linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_H2Ock2[1], color='blue',    linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_CH4Bu2[1], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1)
# # plt.ylim(0, 4.5e-14)
# plt.ylim(0, 3.5e-14)
# plt.show()
# # plt.savefig('Fig2d.ps')
# plt.clf() 

# plt.plot(np.arange(nYear), rf_H2Ele3[0], color='green',  linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_H2Ock3[0], color='blue',    linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_CH4Bu3[0], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1)
# # plt.ylim(0, 1.4e-14)
# plt.ylim(0, 0.8e-14)
# plt.show()
# # plt.savefig('Fig2e.ps')
# plt.clf() 
# plt.plot(np.arange(nYear), rf_H2Ele3[1], color='green',  linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_H2Ock3[1], color='blue',    linestyle='-', linewidth=2)
# plt.plot(np.arange(nYear), rf_CH4Bu3[1], color='purple', linestyle='-', linewidth=2)
# plt.xlim(0, nYear-1)
# # plt.ylim(0, 1.4e-14)
# plt.ylim(0, 0.8e-14)
# plt.show()
# # plt.savefig('Fig2f.ps')
# plt.clf() 
# """



############################################################################################################################################
# """
### Uncertainty 
nYear = 501
type = 't'

if type == 'rf': 
    scale_CO2_100yr = np.array(fun_rfCO2(np.arange(nYear)))
    scale_CH4_100yr = np.array(fun_rfCH4(np.arange(nYear)))
    scale_H2_100yr = np.array(fun_rfH2(np.arange(nYear)))
    scale_H2_lifetime14 = np.array(fun_rfH2_lifetime14(np.arange(nYear)))
    scale_H2_lifetime25 = np.array(fun_rfH2_lifetime25(np.arange(nYear)))
    scale_CH4_addCO2 = np.array(fun_rfCH4_addCO2(np.arange(nYear)))
    scale_CO2sus_100yr = np.array(fun_rfCO2sustained(np.arange(nYear)))
    scale_CH4sus_100yr = np.array(fun_rfCH4sustained(np.arange(nYear)))
    scale_H2sus_100yr = np.array(fun_rfH2sustained(np.arange(nYear)))
    scale_H2sus_lifetime14 = np.array(fun_rfH2sustained_lifetime14(np.arange(nYear)))
    scale_H2sus_lifetime25 = np.array(fun_rfH2sustained_lifetime25(np.arange(nYear)))
    scale_CH4sus_addCO2 = np.array(fun_rfCH4sustained_addCO2(np.arange(nYear)))
    scale_CO2sus_tp100 = np.array(fun_rfCO2sustained(np.arange(nYear-100)))
    scale_CH4sus_tp100 = np.array(fun_rfCH4sustained(np.arange(nYear-100)))
    scale_H2sus_tp100 = np.array(fun_rfH2sustained(np.arange(nYear-100)))
    scale_H2sus_tp100_lifetime14 = np.array(fun_rfH2sustained_lifetime14(np.arange(nYear-100)))
    scale_H2sus_tp100_lifetime25 = np.array(fun_rfH2sustained_lifetime25(np.arange(nYear-100)))
    scale_CH4sus_tp100_addCO2 = np.array(fun_rfCH4sustained_addCO2(np.arange(nYear-100)))
    scale_CO2sus_tp100 = np.r_[np.zeros(100), scale_CO2sus_tp100]; scale_CO2sus_tp100 = scale_CO2sus_100yr - scale_CO2sus_tp100
    scale_CH4sus_tp100 = np.r_[np.zeros(100), scale_CH4sus_tp100]; scale_CH4sus_tp100 = scale_CH4sus_100yr - scale_CH4sus_tp100
    scale_H2sus_tp100 = np.r_[np.zeros(100), scale_H2sus_tp100]; scale_H2sus_tp100 = scale_H2sus_100yr - scale_H2sus_tp100
    scale_H2sus_tp100_lifetime14 = np.r_[np.zeros(100), scale_H2sus_tp100_lifetime14]; scale_H2sus_tp100_lifetime14 = scale_H2sus_lifetime14 - scale_H2sus_tp100_lifetime14
    scale_H2sus_tp100_lifetime25 = np.r_[np.zeros(100), scale_H2sus_tp100_lifetime25]; scale_H2sus_tp100_lifetime25 = scale_H2sus_lifetime25 - scale_H2sus_tp100_lifetime25
    scale_CH4sus_tp100_addCO2 = np.r_[np.zeros(100), scale_CH4sus_tp100_addCO2]; scale_CH4sus_tp100_addCO2 = scale_CH4sus_addCO2 - scale_CH4sus_tp100_addCO2
if type == 't':
    scale_CO2_100yr = np.array(fun_tCO2(np.arange(nYear))) 
    scale_CH4_100yr = np.array(fun_tCH4(np.arange(nYear)))
    scale_H2_100yr = np.array(fun_tH2(np.arange(nYear)))
    scale_H2_lifetime14 = np.array(fun_tH2_lifetime14(np.arange(nYear)))
    scale_H2_lifetime25 = np.array(fun_tH2_lifetime25(np.arange(nYear)))
    scale_CH4_addCO2 = np.array(fun_tCH4_addCO2(np.arange(nYear)))
    scale_CO2sus_100yr = np.array(fun_tCO2sustained(np.arange(nYear)))
    scale_CH4sus_100yr = np.array(fun_tCH4sustained(np.arange(nYear)))
    scale_H2sus_100yr = np.array(fun_tH2sustained(np.arange(nYear)))
    scale_H2sus_lifetime14 = np.array(fun_tH2sustained_lifetime14(np.arange(nYear)))
    scale_H2sus_lifetime25 = np.array(fun_tH2sustained_lifetime25(np.arange(nYear)))
    scale_CH4sus_addCO2 = np.array(fun_tCH4sustained_addCO2(np.arange(nYear)))
    scale_CO2sus_tp100 = np.array(fun_tCO2sustained(np.arange(nYear-100)))
    scale_CH4sus_tp100 = np.array(fun_tCH4sustained(np.arange(nYear-100)))
    scale_H2sus_tp100 = np.array(fun_tH2sustained(np.arange(nYear-100)))
    scale_H2sus_tp100_lifetime14 = np.array(fun_tH2sustained_lifetime14(np.arange(nYear-100)))
    scale_H2sus_tp100_lifetime25 = np.array(fun_tH2sustained_lifetime25(np.arange(nYear-100)))
    scale_CH4sus_tp100_addCO2 = np.array(fun_tCH4sustained_addCO2(np.arange(nYear-100)))
    scale_CO2sus_tp100 = np.r_[np.zeros(100), scale_CO2sus_tp100]; scale_CO2sus_tp100 = scale_CO2sus_100yr - scale_CO2sus_tp100
    scale_CH4sus_tp100 = np.r_[np.zeros(100), scale_CH4sus_tp100]; scale_CH4sus_tp100 = scale_CH4sus_100yr - scale_CH4sus_tp100
    scale_H2sus_tp100 = np.r_[np.zeros(100), scale_H2sus_tp100]; scale_H2sus_tp100 = scale_H2sus_100yr - scale_H2sus_tp100
    scale_H2sus_tp100_lifetime14 = np.r_[np.zeros(100), scale_H2sus_tp100_lifetime14]; scale_H2sus_tp100_lifetime14 = scale_H2sus_lifetime14 - scale_H2sus_tp100_lifetime14
    scale_H2sus_tp100_lifetime25 = np.r_[np.zeros(100), scale_H2sus_tp100_lifetime25]; scale_H2sus_tp100_lifetime25 = scale_H2sus_lifetime25 - scale_H2sus_tp100_lifetime25
    scale_CH4sus_tp100_addCO2 = np.r_[np.zeros(100), scale_CH4sus_tp100_addCO2]; scale_CH4sus_tp100_addCO2 = scale_CH4sus_addCO2 - scale_CH4sus_tp100_addCO2

# 1) Central case 
H2Ele, H2Ock, CH4Bu = np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear])
for idx in range(len(emissions_dic)):
    H2Ele[idx] = scale_CO2_100yr * emissions_dic[idx][0, 0] + scale_CH4_100yr * emissions_dic[idx][0, 1] + scale_H2_100yr * emissions_dic[idx][0, 2]
    H2Ock[idx] = scale_CO2_100yr * emissions_dic[idx][1, 0] + scale_CH4_100yr * emissions_dic[idx][1, 1] + scale_H2_100yr * emissions_dic[idx][1, 2]
    CH4Bu[idx] = scale_CO2_100yr * emissions_dic[idx][3, 0] # + scale_CH4_100yr * emissions_dic[idx][3, 1] + scale_H2_100yr * emissions_dic[idx][3, 2]
H2Ele2, H2Ock2, CH4Bu2 = np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear])
for idx in range(len(emissions_dic)):
    H2Ele2[idx] = scale_CO2sus_100yr * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_100yr * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_100yr * emissions_dic[idx][0, 2]*0.01
    H2Ock2[idx] = scale_CO2sus_100yr * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_100yr * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_100yr * emissions_dic[idx][1, 2]*0.01
    CH4Bu2[idx] = scale_CO2sus_100yr * emissions_dic[idx][3, 0]*0.01 # + scale_CH4sus_100yr * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_100yr * emissions_dic[idx][3, 2]*0.01
H2Ele3, H2Ock3, CH4Bu3 = np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear])
for idx in range(len(emissions_dic)):
    H2Ele3[idx] = scale_CO2sus_tp100 * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_tp100 * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_tp100 * emissions_dic[idx][0, 2]*0.01
    H2Ock3[idx] = scale_CO2sus_tp100 * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_tp100 * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_tp100 * emissions_dic[idx][1, 2]*0.01
    CH4Bu3[idx] = scale_CO2sus_tp100 * emissions_dic[idx][3, 0]*0.01 # + scale_CH4sus_tp100 * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_tp100 * emissions_dic[idx][3, 2]*0.01

# 2) Included CH4 leakage or not for FF
CH4Bu_CH4Leak = np.zeros([2, nYear])
CH4Bu2_CH4Leak = np.zeros([2, nYear])
CH4Bu3_CH4Leak = np.zeros([2, nYear])
for idx in range(len(emissions_dic)):
    CH4Bu_CH4Leak[idx]  = scale_CO2_100yr * emissions_dic[idx][3, 0]    + scale_CH4_100yr * emissions_dic[idx][3, 1]    + scale_H2_100yr * emissions_dic[idx][3, 2]
    CH4Bu2_CH4Leak[idx] = scale_CO2sus_100yr * emissions_dic[idx][3, 0]*0.01 + scale_CH4sus_100yr * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_100yr * emissions_dic[idx][3, 2]*0.01
    CH4Bu3_CH4Leak[idx] = scale_CO2sus_tp100 * emissions_dic[idx][3, 0]*0.01 + scale_CH4sus_tp100 * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_tp100 * emissions_dic[idx][3, 2]*0.01

# 3) H2 lifetime, affecting green and blue hydrogen
H2Ele_lifetime14, H2Ele_lifetime25, H2Ock_lifetime14, H2Ock_lifetime25 = np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear])
H2Ele2_lifetime14, H2Ele2_lifetime25, H2Ock2_lifetime14, H2Ock2_lifetime25 = np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear])
H2Ele3_lifetime14, H2Ele3_lifetime25, H2Ock3_lifetime14, H2Ock3_lifetime25 = np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear]), np.zeros([2, nYear])
for idx in range(len(emissions_dic)):
    H2Ele_lifetime14[idx] = scale_CO2_100yr * emissions_dic[idx][0, 0] + scale_CH4_100yr * emissions_dic[idx][0, 1] + scale_H2_lifetime14 * emissions_dic[idx][0, 2]
    H2Ele_lifetime25[idx] = scale_CO2_100yr * emissions_dic[idx][0, 0] + scale_CH4_100yr * emissions_dic[idx][0, 1] + scale_H2_lifetime25 * emissions_dic[idx][0, 2]
    H2Ock_lifetime14[idx] = scale_CO2_100yr * emissions_dic[idx][1, 0] + scale_CH4_100yr * emissions_dic[idx][1, 1] + scale_H2_lifetime14 * emissions_dic[idx][1, 2]
    H2Ock_lifetime25[idx] = scale_CO2_100yr * emissions_dic[idx][1, 0] + scale_CH4_100yr * emissions_dic[idx][1, 1] + scale_H2_lifetime25 * emissions_dic[idx][1, 2]
    H2Ele2_lifetime14[idx] = scale_CO2sus_100yr * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_100yr * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_lifetime14 * emissions_dic[idx][0, 2]*0.01
    H2Ele2_lifetime25[idx] = scale_CO2sus_100yr * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_100yr * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_lifetime25 * emissions_dic[idx][0, 2]*0.01
    H2Ock2_lifetime14[idx] = scale_CO2sus_100yr * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_100yr * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_lifetime14 * emissions_dic[idx][1, 2]*0.01
    H2Ock2_lifetime25[idx] = scale_CO2sus_100yr * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_100yr * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_lifetime25 * emissions_dic[idx][1, 2]*0.01
    H2Ele3_lifetime14[idx] = scale_CO2sus_tp100 * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_tp100 * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_tp100_lifetime14 * emissions_dic[idx][0, 2]*0.01
    H2Ele3_lifetime25[idx] = scale_CO2sus_tp100 * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_tp100 * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_tp100_lifetime25 * emissions_dic[idx][0, 2]*0.01
    H2Ock3_lifetime14[idx] = scale_CO2sus_tp100 * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_tp100 * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_tp100_lifetime14 * emissions_dic[idx][1, 2]*0.01
    H2Ock3_lifetime25[idx] = scale_CO2sus_tp100 * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_tp100 * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_tp100_lifetime25 * emissions_dic[idx][1, 2]*0.01

# 4) CH4 to CO2
H2Ock_addCO2, CH4Bu_addCO2 = np.zeros([2, nYear]), np.zeros([2, nYear])
H2Ock2_addCO2, CH4Bu2_addCO2 = np.zeros([2, nYear]), np.zeros([2, nYear])
H2Ock3_addCO2, CH4Bu3_addCO2 = np.zeros([2, nYear]), np.zeros([2, nYear])
for idx in range(len(emissions_dic)):
    H2Ock_addCO2[idx] = scale_CO2_100yr * emissions_dic[idx][1, 0] + scale_CH4_addCO2 * emissions_dic[idx][1, 1] + scale_H2_100yr * emissions_dic[idx][1, 2]
    CH4Bu_addCO2[idx] = scale_CO2_100yr * emissions_dic[idx][3, 0] + scale_CH4_addCO2 * emissions_dic[idx][3, 1] + scale_H2_100yr * emissions_dic[idx][3, 2]
    H2Ock2_addCO2[idx] = scale_CO2sus_100yr * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_addCO2 * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_100yr * emissions_dic[idx][1, 2]*0.01
    CH4Bu2_addCO2[idx] = scale_CO2sus_100yr * emissions_dic[idx][3, 0]*0.01 + scale_CH4sus_addCO2 * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_100yr * emissions_dic[idx][3, 2]*0.01
    H2Ock3_addCO2[idx] = scale_CO2sus_tp100 * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_tp100_addCO2 * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_tp100 * emissions_dic[idx][1, 2]*0.01
    CH4Bu3_addCO2[idx] = scale_CO2sus_tp100 * emissions_dic[idx][3, 0]*0.01 + scale_CH4sus_tp100_addCO2 * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_tp100 * emissions_dic[idx][3, 2]*0.01

plt.plot(np.arange(nYear), H2Ele[0], color='green',  linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), H2Ock[0], color='blue',    linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), CH4Bu[0], color='purple', linestyle='-', linewidth=2)
plt.fill_between(np.arange(nYear), H2Ele_lifetime14[0], H2Ele_lifetime25[0], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock_lifetime14[0], H2Ock_lifetime25[0], facecolor='blue', edgecolor='none', alpha=0.3)
plt.plot(np.arange(nYear), H2Ock_addCO2[0], color='blue', linestyle='--', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu_CH4Leak[0], color='purple', linestyle=':', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu_addCO2[0], color='purple', linestyle='--', linewidth=0.8)
plt.xlim(0, nYear-1)
# plt.ylim(0, 5e-14)
plt.ylim(0, 1.8e-14)
# plt.show()
plt.savefig('Fig2a.ps')
plt.clf() 
plt.plot(np.arange(nYear), H2Ele[1], color='green',  linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), H2Ock[1], color='blue',    linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), CH4Bu[1], color='purple', linestyle='-', linewidth=2)
plt.fill_between(np.arange(nYear), H2Ele_lifetime14[1], H2Ele_lifetime25[1], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock_lifetime14[1], H2Ock_lifetime25[1], facecolor='blue', edgecolor='none', alpha=0.3)
plt.plot(np.arange(nYear), H2Ock_addCO2[1], color='blue', linestyle='--', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu_CH4Leak[1], color='purple', linestyle=':', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu_addCO2[1], color='purple', linestyle='--', linewidth=0.8)
plt.xlim(0, nYear-1)
# plt.ylim(0, 5e-14)
plt.ylim(0, 1.8e-14)
# plt.show()
plt.savefig('Fig2b.ps')
plt.clf() 

plt.plot(np.arange(nYear), H2Ele2[0], color='green',  linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), H2Ock2[0], color='blue',    linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), CH4Bu2[0], color='purple', linestyle='-', linewidth=2)
plt.fill_between(np.arange(nYear), H2Ele2_lifetime14[0], H2Ele2_lifetime25[0], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock2_lifetime14[0], H2Ock2_lifetime25[0], facecolor='blue', edgecolor='none', alpha=0.3)
plt.plot(np.arange(nYear), H2Ock2_addCO2[0], color='blue', linestyle='--', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu2_CH4Leak[0], color='purple', linestyle=':', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu2_addCO2[0], color='purple', linestyle='--', linewidth=0.8)
plt.xlim(0, nYear-1)
# plt.ylim(0, 5.5e-14)
plt.ylim(0, 4e-14)
# plt.show()
plt.savefig('Fig2c.ps')
plt.clf() 
plt.plot(np.arange(nYear), H2Ele2[1], color='green',  linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), H2Ock2[1], color='blue',    linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), CH4Bu2[1], color='purple', linestyle='-', linewidth=2)
plt.fill_between(np.arange(nYear), H2Ele2_lifetime14[1], H2Ele2_lifetime25[1], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock2_lifetime14[1], H2Ock2_lifetime25[1], facecolor='blue', edgecolor='none', alpha=0.3)
plt.plot(np.arange(nYear), H2Ock2_addCO2[1], color='blue', linestyle='--', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu2_CH4Leak[1], color='purple', linestyle=':', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu2_addCO2[1], color='purple', linestyle='--', linewidth=0.8)
plt.xlim(0, nYear-1)
# plt.ylim(0, 5.5e-14)
plt.ylim(0, 4e-14)
# plt.show()
plt.savefig('Fig2d.ps')
plt.clf() 

plt.plot(np.arange(nYear), H2Ele3[0], color='green',  linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), H2Ock3[0], color='blue',    linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), CH4Bu3[0], color='purple', linestyle='-', linewidth=2)
plt.fill_between(np.arange(nYear), H2Ele3_lifetime14[0], H2Ele3_lifetime25[0], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock3_lifetime14[0], H2Ock3_lifetime25[0], facecolor='blue', edgecolor='none', alpha=0.3)
plt.plot(np.arange(nYear), H2Ock3_addCO2[0], color='blue', linestyle='--', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu3_CH4Leak[0], color='purple', linestyle=':', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu3_addCO2[0], color='purple', linestyle='--', linewidth=0.8)
plt.xlim(0, nYear-1)
# plt.ylim(0, 1.8e-14)
plt.ylim(0, 1e-14)
# plt.show()
plt.savefig('Fig2e.ps')
plt.clf() 
plt.plot(np.arange(nYear), H2Ele3[1], color='green',  linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), H2Ock3[1], color='blue',    linestyle='-', linewidth=2)
plt.plot(np.arange(nYear), CH4Bu3[1], color='purple', linestyle='-', linewidth=2)
plt.fill_between(np.arange(nYear), H2Ele3_lifetime14[1], H2Ele3_lifetime25[1], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock3_lifetime14[1], H2Ock3_lifetime25[1], facecolor='blue', edgecolor='none', alpha=0.3)
plt.plot(np.arange(nYear), H2Ock3_addCO2[1], color='blue', linestyle='--', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu3_CH4Leak[1], color='purple', linestyle=':', linewidth=0.8)
plt.plot(np.arange(nYear), CH4Bu3_addCO2[1], color='purple', linestyle='--', linewidth=0.8)
plt.xlim(0, nYear-1)
# plt.ylim(0, 1.8e-14)
plt.ylim(0, 1e-14)
# plt.show()
plt.savefig('Fig2f.ps')
plt.clf() 



# # 4) Avoided CO2
# emissions_dic_5kg = []
# emissions_dic_5kg.append( final_emissions(LeakageRate_best[1], LeakageRate_best[0], 5) )
# emissions_dic_5kg.append( final_emissions(LeakageRate_worst[1], LeakageRate_worst[0], 5) )
# emissions_dic_15kg = []
# emissions_dic_15kg.append( final_emissions(LeakageRate_best[1], LeakageRate_best[0], 15) )
# emissions_dic_15kg.append( final_emissions(LeakageRate_worst[1], LeakageRate_worst[0], 15) )
# CH4Bu_5k, CH4Bu_15k = np.zeros([2, nYear]), np.zeros([2, nYear])
# CH4Bu2_5k, CH4Bu2_15k = np.zeros([2, nYear]), np.zeros([2, nYear])
# CH4Bu3_5k, CH4Bu3_15k = np.zeros([2, nYear]), np.zeros([2, nYear])
# for idx in range(len(emissions_dic)):
#     CH4Bu_5k[idx] = scale_CO2_100yr * emissions_dic_5kg[idx][3, 0] # + scale_CH4_100yr * emissions_dic[idx][3, 1] + scale_H2_100yr * emissions_dic[idx][3, 2]
#     CH4Bu_15k[idx] = scale_CO2_100yr * emissions_dic_15kg[idx][3, 0] # + scale_CH4_100yr * emissions_dic[idx][3, 1] + scale_H2_100yr * emissions_dic[idx][3, 2]
#     CH4Bu2_5k[idx] = scale_CO2sus_100yr * emissions_dic_5kg[idx][3, 0]*0.01 # + scale_CH4_100yr * emissions_dic[idx][3, 1] + scale_H2_100yr * emissions_dic[idx][3, 2]
#     CH4Bu2_15k[idx] = scale_CO2sus_100yr * emissions_dic_15kg[idx][3, 0]*0.01 # + scale_CH4_100yr * emissions_dic[idx][3, 1] + scale_H2_100yr * emissions_dic[idx][3, 2]
#     CH4Bu3_5k[idx] = scale_CO2sus_tp100 * emissions_dic_5kg[idx][3, 0]*0.01 # + scale_CH4_100yr * emissions_dic[idx][3, 1] + scale_H2_100yr * emissions_dic[idx][3, 2]
#     CH4Bu3_15k[idx] = scale_CO2sus_tp100 * emissions_dic_15kg[idx][3, 0]*0.01 # + scale_CH4_100yr * emissions_dic[idx][3, 1] + scale_H2_100yr * emissions_dic[idx][3, 2]
# plt.plot(np.arange(nYear), CH4Bu[0], color='purple', linestyle='-', linewidth=2)
# plt.fill_between(np.arange(nYear), CH4Bu_5k[0], CH4Bu_15k[0], facecolor='purple', edgecolor='none', alpha=0.3)
# plt.xlim(0, nYear-1)
# plt.ylim(0, 1.2e-14)
# # plt.show()
# plt.savefig('FigSXa.ps')
# plt.clf() 
# plt.plot(np.arange(nYear), CH4Bu2[0], color='purple', linestyle='-', linewidth=2)
# plt.fill_between(np.arange(nYear), CH4Bu2_5k[0], CH4Bu2_15k[0], facecolor='purple', edgecolor='none', alpha=0.3)
# plt.xlim(0, nYear-1)
# plt.ylim(0, 5e-14)
# # plt.show()
# plt.savefig('FigSXb.ps')
# plt.clf() 
# plt.plot(np.arange(nYear), CH4Bu3[0], color='purple', linestyle='-', linewidth=2)
# plt.fill_between(np.arange(nYear), CH4Bu3_5k[0], CH4Bu3_15k[0], facecolor='purple', edgecolor='none', alpha=0.3)
# plt.xlim(0, nYear-1)
# plt.ylim(0, 1e-14)
# # plt.show()
# plt.savefig('FigSXc.ps')
# plt.clf() 
# """




############################################################################################################################################
"""
### Unceratinty T function 
from Fun_final import fun_tCO2_Uncertainty, fun_tCH4_Uncertainty, fun_tH2_Uncertainty
from Fun_final import fun_tCO2sustained_Uncertainty, fun_tCH4sustained_Uncertainty, fun_tH2sustained_Uncertainty
nYear = 501
type = 't'

scale_CO2_100yr = np.array(fun_tCO2_Uncertainty(np.arange(nYear)))
scale_CH4_100yr = np.array(fun_tCH4_Uncertainty(np.arange(nYear)))
scale_H2_100yr = np.array(fun_tH2_Uncertainty(np.arange(nYear)))
scale_CO2sus_100yr = np.array(fun_tCO2sustained_Uncertainty(np.arange(nYear)))
scale_CH4sus_100yr = np.array(fun_tCH4sustained_Uncertainty(np.arange(nYear)))
scale_H2sus_100yr = np.array(fun_tH2sustained_Uncertainty(np.arange(nYear)))
scale_CO2sus_tp100 = np.array(fun_tCO2sustained_Uncertainty(np.arange(nYear-100))); scale_CO2sus_tp100=np.c_[np.zeros([4,100]), scale_CO2sus_tp100]; scale_CO2sus_tp100=scale_CO2sus_100yr-scale_CO2sus_tp100
scale_CH4sus_tp100 = np.array(fun_tCH4sustained_Uncertainty(np.arange(nYear-100))); scale_CH4sus_tp100=np.c_[np.zeros([4,100]), scale_CH4sus_tp100]; scale_CH4sus_tp100=scale_CH4sus_100yr-scale_CH4sus_tp100
scale_H2sus_tp100 = np.array(fun_tH2sustained_Uncertainty(np.arange(nYear-100)));   scale_H2sus_tp100=np.c_[np.zeros([4,100]), scale_H2sus_tp100];   scale_H2sus_tp100=scale_H2sus_100yr-scale_H2sus_tp100

scale_CO2_mid = scale_CO2_100yr[0]; scale_CO2_max = np.max(scale_CO2_100yr, axis=0); scale_CO2_min = np.min(scale_CO2_100yr, axis=0)
scale_CH4_mid = scale_CH4_100yr[0]; scale_CH4_max = np.max(scale_CH4_100yr, axis=0); scale_CH4_min = np.min(scale_CH4_100yr, axis=0)
scale_H2_mid  = scale_H2_100yr[0];  scale_H2_max  = np.max(scale_H2_100yr, axis=0);  scale_H2_min  = np.min(scale_H2_100yr, axis=0)
scale_CO2sus_mid = scale_CO2sus_100yr[0]; scale_CO2sus_max = np.max(scale_CO2sus_100yr, axis=0); scale_CO2sus_min = np.min(scale_CO2sus_100yr, axis=0)
scale_CH4sus_mid = scale_CH4sus_100yr[0]; scale_CH4sus_max = np.max(scale_CH4sus_100yr, axis=0); scale_CH4sus_min = np.min(scale_CH4sus_100yr, axis=0)
scale_H2sus_mid  = scale_H2sus_100yr[0];  scale_H2sus_max  = np.max(scale_H2sus_100yr, axis=0);  scale_H2sus_min  = np.min(scale_H2sus_100yr, axis=0)
scale_CO2sus_tp100_mid = scale_CO2sus_tp100[0]; scale_CO2sus_tp100_max = np.max(scale_CO2sus_tp100, axis=0); scale_CO2sus_tp100_min = np.min(scale_CO2sus_tp100, axis=0)
scale_CH4sus_tp100_mid = scale_CH4sus_tp100[0]; scale_CH4sus_tp100_max = np.max(scale_CH4sus_tp100, axis=0); scale_CH4sus_tp100_min = np.min(scale_CH4sus_tp100, axis=0)
scale_H2sus_tp100_mid  = scale_H2sus_tp100[0];  scale_H2sus_tp100_max  = np.max(scale_H2sus_tp100, axis=0);  scale_H2sus_tp100_min  = np.min(scale_H2sus_tp100, axis=0)

H2Ele, H2Ock, CH4Bu = np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear])
H2Ele2, H2Ock2, CH4Bu2 = np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear])
H2Ele3, H2Ock3, CH4Bu3 = np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear])
for idx in range(len(emissions_dic)):
    H2Ele[idx][0] = scale_CO2_mid * emissions_dic[idx][0, 0] + scale_CH4_mid * emissions_dic[idx][0, 1] + scale_H2_mid * emissions_dic[idx][0, 2]
    H2Ele[idx][1] = scale_CO2_max * emissions_dic[idx][0, 0] + scale_CH4_max * emissions_dic[idx][0, 1] + scale_H2_max * emissions_dic[idx][0, 2]
    H2Ele[idx][2] = scale_CO2_min * emissions_dic[idx][0, 0] + scale_CH4_min * emissions_dic[idx][0, 1] + scale_H2_min * emissions_dic[idx][0, 2]
    H2Ock[idx][0] = scale_CO2_mid * emissions_dic[idx][1, 0] + scale_CH4_mid * emissions_dic[idx][1, 1] + scale_H2_mid * emissions_dic[idx][1, 2]
    H2Ock[idx][1] = scale_CO2_max * emissions_dic[idx][1, 0] + scale_CH4_max * emissions_dic[idx][1, 1] + scale_H2_max * emissions_dic[idx][1, 2]
    H2Ock[idx][2] = scale_CO2_min * emissions_dic[idx][1, 0] + scale_CH4_min * emissions_dic[idx][1, 1] + scale_H2_min * emissions_dic[idx][1, 2]
    CH4Bu[idx][0] = scale_CO2_mid * emissions_dic[idx][3, 0] # + scale_CH4_mid * emissions_dic[idx][3, 1] + scale_H2_mid * emissions_dic[idx][3, 2]
    CH4Bu[idx][1] = scale_CO2_max * emissions_dic[idx][3, 0] # + scale_CH4_max * emissions_dic[idx][3, 1] + scale_H2_max * emissions_dic[idx][3, 2]
    CH4Bu[idx][2] = scale_CO2_min * emissions_dic[idx][3, 0] # + scale_CH4_min * emissions_dic[idx][3, 1] + scale_H2_min * emissions_dic[idx][3, 2]
    H2Ele2[idx][0] = scale_CO2sus_mid * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_mid * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_mid * emissions_dic[idx][0, 2]*0.01
    H2Ele2[idx][1] = scale_CO2sus_max * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_max * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_max * emissions_dic[idx][0, 2]*0.01
    H2Ele2[idx][2] = scale_CO2sus_min * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_min * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_min * emissions_dic[idx][0, 2]*0.01
    H2Ock2[idx][0] = scale_CO2sus_mid * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_mid * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_mid * emissions_dic[idx][1, 2]*0.01
    H2Ock2[idx][1] = scale_CO2sus_max * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_max * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_max * emissions_dic[idx][1, 2]*0.01
    H2Ock2[idx][2] = scale_CO2sus_min * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_min * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_min * emissions_dic[idx][1, 2]*0.01
    CH4Bu2[idx][0] = scale_CO2sus_mid * emissions_dic[idx][3, 0]*0.01 # + scale_CH4sus_mid * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_mid * emissions_dic[idx][3, 2]*0.01
    CH4Bu2[idx][1] = scale_CO2sus_max * emissions_dic[idx][3, 0]*0.01 # + scale_CH4sus_max * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_max * emissions_dic[idx][3, 2]*0.01
    CH4Bu2[idx][2] = scale_CO2sus_min * emissions_dic[idx][3, 0]*0.01 # + scale_CH4sus_min * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_min * emissions_dic[idx][3, 2]*0.01
    H2Ele3[idx][0] = scale_CO2sus_tp100_mid * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_tp100_mid * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_tp100_mid * emissions_dic[idx][0, 2]*0.01
    H2Ele3[idx][1] = scale_CO2sus_tp100_max * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_tp100_max * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_tp100_max * emissions_dic[idx][0, 2]*0.01
    H2Ele3[idx][2] = scale_CO2sus_tp100_min * emissions_dic[idx][0, 0]*0.01 + scale_CH4sus_tp100_min * emissions_dic[idx][0, 1]*0.01 + scale_H2sus_tp100_min * emissions_dic[idx][0, 2]*0.01
    H2Ock3[idx][0] = scale_CO2sus_tp100_mid * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_tp100_mid * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_tp100_mid * emissions_dic[idx][1, 2]*0.01
    H2Ock3[idx][1] = scale_CO2sus_tp100_max * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_tp100_max * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_tp100_max * emissions_dic[idx][1, 2]*0.01
    H2Ock3[idx][2] = scale_CO2sus_tp100_min * emissions_dic[idx][1, 0]*0.01 + scale_CH4sus_tp100_min * emissions_dic[idx][1, 1]*0.01 + scale_H2sus_tp100_min * emissions_dic[idx][1, 2]*0.01
    CH4Bu3[idx][0] = scale_CO2sus_tp100_mid * emissions_dic[idx][3, 0]*0.01 # + scale_CH4sus_tp100_mid * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_tp100_mid * emissions_dic[idx][3, 2]*0.01
    CH4Bu3[idx][1] = scale_CO2sus_tp100_max * emissions_dic[idx][3, 0]*0.01 # + scale_CH4sus_tp100_max * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_tp100_max * emissions_dic[idx][3, 2]*0.01
    CH4Bu3[idx][2] = scale_CO2sus_tp100_min * emissions_dic[idx][3, 0]*0.01 # + scale_CH4sus_tp100_min * emissions_dic[idx][3, 1]*0.01 + scale_H2sus_tp100_min * emissions_dic[idx][3, 2]*0.01


plt.plot(np.arange(nYear), H2Ele[0][0], color='green',  linestyle='-')
plt.plot(np.arange(nYear), H2Ock[0][0], color='blue',    linestyle='-')
plt.plot(np.arange(nYear), CH4Bu[0][0], color='purple', linestyle='-')
plt.fill_between(np.arange(nYear), H2Ele[0][1], H2Ele[0][2], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock[0][1], H2Ock[0][2], facecolor='blue', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), CH4Bu[0][1], CH4Bu[0][2], facecolor='purple', edgecolor='none', alpha=0.3)
plt.xlim(0, nYear-1)
plt.ylim(0, 1.2e-14)
# plt.show()
plt.savefig('FigSX1.ps')
plt.clf() 
plt.plot(np.arange(nYear), H2Ele[1][0], color='green',  linestyle='-')
plt.plot(np.arange(nYear), H2Ock[1][0], color='blue',    linestyle='-')
plt.plot(np.arange(nYear), CH4Bu[1][0], color='purple', linestyle='-')
plt.fill_between(np.arange(nYear), H2Ele[1][1], H2Ele[1][2], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock[1][1], H2Ock[1][2], facecolor='blue', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), CH4Bu[1][1], CH4Bu[1][2], facecolor='purple', edgecolor='none', alpha=0.3)
plt.xlim(0, nYear-1)
plt.ylim(0, 1.2e-14)
# plt.show()
plt.savefig('FigSX2.ps')
plt.clf() 


plt.plot(np.arange(nYear), H2Ele2[0][0], color='green',  linestyle='-')
plt.plot(np.arange(nYear), H2Ock2[0][0], color='blue',    linestyle='-')
plt.plot(np.arange(nYear), CH4Bu2[0][0], color='purple', linestyle='-')
plt.fill_between(np.arange(nYear), H2Ele2[0][1], H2Ele2[0][2], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock2[0][1], H2Ock2[0][2], facecolor='blue', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), CH4Bu2[0][1], CH4Bu2[0][2], facecolor='purple', edgecolor='none', alpha=0.3)
plt.xlim(0, nYear-1)
plt.ylim(0, 3.6e-14)
# plt.show()
plt.savefig('FigSX3.ps')
plt.clf() 
plt.plot(np.arange(nYear), H2Ele2[1][0], color='green',  linestyle='-')
plt.plot(np.arange(nYear), H2Ock2[1][0], color='blue',    linestyle='-')
plt.plot(np.arange(nYear), CH4Bu2[1][0], color='purple', linestyle='-')
plt.fill_between(np.arange(nYear), H2Ele2[1][1], H2Ele2[1][2], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock2[1][1], H2Ock2[1][2], facecolor='blue', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), CH4Bu2[1][1], CH4Bu2[1][2], facecolor='purple', edgecolor='none', alpha=0.3)
plt.xlim(0, nYear-1)
plt.ylim(0, 3.6e-14)
# plt.show()
plt.savefig('FigSX4.ps')
plt.clf() 


plt.plot(np.arange(nYear), H2Ele3[0][0], color='green',  linestyle='-')
plt.plot(np.arange(nYear), H2Ock3[0][0], color='blue',    linestyle='-')
plt.plot(np.arange(nYear), CH4Bu3[0][0], color='purple', linestyle='-')
plt.fill_between(np.arange(nYear), H2Ele3[0][1], H2Ele3[0][2], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock3[0][1], H2Ock3[0][2], facecolor='blue', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), CH4Bu3[0][1], CH4Bu3[0][2], facecolor='purple', edgecolor='none', alpha=0.3)
plt.xlim(0, nYear-1)
plt.ylim(0, 0.85e-14)
# plt.show()
plt.savefig('FigSX5.ps')
plt.clf() 
plt.plot(np.arange(nYear), H2Ele3[1][0], color='green',  linestyle='-')
plt.plot(np.arange(nYear), H2Ock3[1][0], color='blue',    linestyle='-')
plt.plot(np.arange(nYear), CH4Bu3[1][0], color='purple', linestyle='-')
plt.fill_between(np.arange(nYear), H2Ele3[1][1], H2Ele3[1][2], facecolor='green', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), H2Ock3[1][1], H2Ock3[1][2], facecolor='blue', edgecolor='none', alpha=0.3)
plt.fill_between(np.arange(nYear), CH4Bu3[1][1], CH4Bu3[1][2], facecolor='purple', edgecolor='none', alpha=0.3)
plt.xlim(0, nYear-1)
plt.ylim(0, 0.85e-14)
# plt.show()
plt.savefig('FigSX6.ps')
plt.clf() 
# """






############################################################################################################################################
"""
### Contributions from different species
nYear = 501
# scale_CO2_100yr, scale_CH4_100yr, scale_H2_100yr = np.array(fun_rfCO2(np.arange(nYear))), np.array(fun_rfCH4(np.arange(nYear))), np.array(fun_rfH2(np.arange(nYear)))
scale_CO2_100yr, scale_CH4_100yr, scale_H2_100yr = np.array(fun_tCO2(np.arange(nYear))), np.array(fun_tCH4(np.arange(nYear))), np.array(fun_tH2(np.arange(nYear)))
rf_H2Ele, rf_H2Ock, rf_CH4Bu = np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear])
for idx in range(len(emissions_dic)):
    rf_H2Ele[idx, 0], rf_H2Ele[idx, 1], rf_H2Ele[idx, 2] = scale_CO2_100yr * emissions_dic[idx][0, 0], scale_CH4_100yr * emissions_dic[idx][0, 1], scale_H2_100yr * emissions_dic[idx][0, 2]
    rf_H2Ock[idx, 0], rf_H2Ock[idx, 1], rf_H2Ock[idx, 2] = scale_CO2_100yr * emissions_dic[idx][1, 0], scale_CH4_100yr * emissions_dic[idx][1, 1], scale_H2_100yr * emissions_dic[idx][1, 2]
    rf_CH4Bu[idx, 0], rf_CH4Bu[idx, 1], rf_CH4Bu[idx, 2] = scale_CO2_100yr * emissions_dic[idx][3, 0], scale_CH4_100yr * emissions_dic[idx][3, 1], scale_H2_100yr * emissions_dic[idx][3, 2]

# scale_CO2_100yr, scale_CH4_100yr, scale_H2_100yr = np.array(fun_rfCO2sustained(np.arange(nYear))), np.array(fun_rfCH4sustained(np.arange(nYear))), np.array(fun_rfH2sustained(np.arange(nYear)))
scale_CO2_100yr, scale_CH4_100yr, scale_H2_100yr = np.array(fun_tCO2sustained(np.arange(nYear))), np.array(fun_tCH4sustained(np.arange(nYear))), np.array(fun_tH2sustained(np.arange(nYear)))
rf_H2Ele2, rf_H2Ock2, rf_CH4Bu2 = np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear])
for idx in range(len(emissions_dic)):
    rf_H2Ele2[idx, 0], rf_H2Ele2[idx, 1], rf_H2Ele2[idx, 2] = scale_CO2_100yr * emissions_dic[idx][0, 0]*0.01, scale_CH4_100yr * emissions_dic[idx][0, 1]*0.01, scale_H2_100yr * emissions_dic[idx][0, 2]*0.01
    rf_H2Ock2[idx, 0], rf_H2Ock2[idx, 1], rf_H2Ock2[idx, 2] = scale_CO2_100yr * emissions_dic[idx][1, 0]*0.01, scale_CH4_100yr * emissions_dic[idx][1, 1]*0.01, scale_H2_100yr * emissions_dic[idx][1, 2]*0.01
    rf_CH4Bu2[idx, 0], rf_CH4Bu2[idx, 1], rf_CH4Bu2[idx, 2] = scale_CO2_100yr * emissions_dic[idx][3, 0]*0.01, scale_CH4_100yr * emissions_dic[idx][3, 1]*0.01, scale_H2_100yr * emissions_dic[idx][3, 2]*0.01

# scale_CO2_100yrTp100, scale_CH4_100yrTp100, scale_H2_100yrTp100 = np.array(fun_rfCO2sustained(np.arange(nYear-100))), np.array(fun_rfCH4sustained(np.arange(nYear-100))), np.array(fun_rfH2sustained(np.arange(nYear-100)))
scale_CO2_100yrTp100, scale_CH4_100yrTp100, scale_H2_100yrTp100 = np.array(fun_tCO2sustained(np.arange(nYear-100))), np.array(fun_tCH4sustained(np.arange(nYear-100))), np.array(fun_tH2sustained(np.arange(nYear-100)))
scale_CO2_100yrTp100 = np.r_[np.zeros(100), scale_CO2_100yrTp100];      scale_CO2_100yrNew = scale_CO2_100yr - scale_CO2_100yrTp100
scale_CH4_100yrTp100 = np.r_[np.zeros(100), scale_CH4_100yrTp100];      scale_CH4_100yrNew = scale_CH4_100yr - scale_CH4_100yrTp100
scale_H2_100yrTp100  = np.r_[np.zeros(100), scale_H2_100yrTp100];       scale_H2_100yrNew  = scale_H2_100yr - scale_H2_100yrTp100
rf_H2Ele3, rf_H2Ock3, rf_CH4Bu3 = np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear]), np.zeros([2, 3, nYear]) 
for idx in range(len(emissions_dic)):
    rf_H2Ele3[idx, 0], rf_H2Ele3[idx, 1], rf_H2Ele3[idx, 2] = scale_CO2_100yrNew * emissions_dic[idx][0, 0]*0.01, scale_CH4_100yrNew * emissions_dic[idx][0, 1]*0.01, scale_H2_100yrNew * emissions_dic[idx][0, 2]*0.01
    rf_H2Ock3[idx, 0], rf_H2Ock3[idx, 1], rf_H2Ock3[idx, 2] = scale_CO2_100yrNew * emissions_dic[idx][1, 0]*0.01, scale_CH4_100yrNew * emissions_dic[idx][1, 1]*0.01, scale_H2_100yrNew * emissions_dic[idx][1, 2]*0.01
    rf_CH4Bu3[idx, 0], rf_CH4Bu3[idx, 1], rf_CH4Bu3[idx, 2] = scale_CO2_100yrNew * emissions_dic[idx][3, 0]*0.01, scale_CH4_100yrNew * emissions_dic[idx][3, 1]*0.01, scale_H2_100yrNew * emissions_dic[idx][3, 2]*0.01




plt.stackplot(np.arange(nYear), [rf_H2Ock[1][2] - rf_H2Ock[0][2], rf_H2Ock[1][1] - rf_H2Ock[0][1]], colors=['green', 'orange'])
# plt.plot(np.arange(nYear), rf_H2Ock[1][2] - rf_H2Ock[0][2], color='green')
# plt.plot(np.arange(nYear), rf_H2Ock[1][1] - rf_H2Ock[0][1], color='blue')
plt.xlim(0, nYear-1)
plt.ylim(0, 0.8e-14)
plt.show() 
# plt.savefig('FigSX4.ps')
plt.clf() 

stop 


plt.plot(np.arange(nYear), rf_H2Ock[1][2] - rf_H2Ock[0][2], color='green')
plt.plot(np.arange(nYear), rf_H2Ock[1][1] - rf_H2Ock[0][1], color='blue')
plt.xlim(0, nYear-1)
plt.ylim(0, 0.5e-14)
# plt.show() 
plt.savefig('FigSX4.ps')
plt.clf() 
plt.plot(np.arange(nYear), rf_H2Ock2[1][2] - rf_H2Ock2[0][2], color='green')
plt.plot(np.arange(nYear), rf_H2Ock2[1][1] - rf_H2Ock2[0][1], color='blue')
plt.xlim(0, nYear-1)
plt.ylim(0, 0.5e-14)
# plt.show() 
plt.savefig('FigSX5.ps')
plt.clf() 
plt.plot(np.arange(nYear), rf_H2Ock3[1][2] - rf_H2Ock3[0][2], color='green')
plt.plot(np.arange(nYear), rf_H2Ock3[1][1] - rf_H2Ock3[0][1], color='blue')
plt.xlim(0, nYear-1)
plt.ylim(0, 0.5e-14)
# plt.show() 
plt.savefig('FigSX6.ps')
plt.clf() 
# """