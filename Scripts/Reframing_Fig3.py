import numpy as np 
import matplotlib.pyplot as plt 
from Fun_final import fun_agwpH2sustained
from Fun_final import fun_agwpCO2sustained

ppbperkgH2 = 3.5 * 1e-9  # ppb/kg
molwtH2 = 0.002016; molwtCH4 = 0.01604246; molwtCO2 = 0.04401 # kg/mol
ppbpermol = ppbperkgH2 * molwtH2  # ppb/mol
ppbpermol = 7.056*1e-12
ppbperkgCH4 = ppbpermol / molwtCH4
ppbperkgCO2 = ppbpermol / molwtCO2

A_CO2 = 1.33*1e-5                                                   # W/m2/ppb
a0 = 0.2173; a1 = 0.224; a2 = 0.2824; a3 = 0.2763                   # 1
tau1_CO2 = 394.4; tau2_CO2 = 36.54; tau3_CO2 = 4.304                # Years 

A_CH4 = 3.88*1e-4                                                   # W/m2/ppb
f1 = 0.37; f2 = 0.106                                               # 1
tau_CH4 = 11.8                                                      # Years

C = 3.5 * 1e-9                                                      # ppb/kg
f1 = 0.37; f2 = 0.106                                               # 1

horizon = 501

def sub_components(A_i, a_i, tau_i, tau_H2, tp, H):
    AGWP1_H2_i = A_i*a_i*tau_i*tau_H2*C*(tp - tau_i*(1-np.exp(-tp/tau_i)) - (tau_H2/(tau_H2-tau_i)) * (tau_H2*(1-np.exp(-tp/tau_H2))-tau_i*(1-np.exp(-tp/tau_i)))) 
    AGWP2_H2_i = (A_i*a_i*tau_i*(tau_H2**2)*C*(1-np.exp(-tp/tau_H2))) / (tau_H2-tau_i) * (tau_H2*(np.exp(-tp/tau_H2)-np.exp(-H/tau_H2))-tau_i*(np.exp(-tp/tau_i)-np.exp(-H/tau_i)))
    AGWP3_H2_i = A_i*a_i*(tau_i**2)*tau_H2*C*((1-np.exp(-tp/tau_i))-(tau_H2/(tau_H2-tau_i))*(np.exp(-tp/tau_H2)-np.exp(-tp/tau_i)))*(np.exp(-tp/tau_i)-np.exp(-H/tau_i))
    return AGWP1_H2_i, AGWP2_H2_i, AGWP3_H2_i
agwp1_ch4, agwp2_ch4, agwp3_ch4 = sub_components(3.88*1e-4, 1.46*1e-2, 11.8, 1.9, 1, np.arange(horizon))
agwp1_o3,  agwp2_o3,  agwp3_o3  = sub_components(0.042, 0.0056, 0.07, 1.9, 1, np.arange(horizon))
agwp1_h2o, agwp2_h2o, agwp3_h2o = sub_components(1e-4, 0.042, 8, 1.9, 1, np.arange(horizon))
agwp_ch4 = (agwp1_ch4 + agwp2_ch4 + agwp3_ch4) * (1+f1+f2)
agwp_o3 = agwp1_o3 + agwp2_o3 + agwp3_o3
agwp_h2o = agwp1_h2o + agwp2_h2o + agwp3_h2o
agwp_H2 = agwp_ch4 + agwp_o3 + agwp_h2o
agwp_H2_cont = np.zeros(horizon)
for i in range(horizon):
    agwp_H2_cont = agwp_H2_cont + np.r_[np.zeros(i), agwp_H2[i:]]

rfH2sus = fun_agwpH2sustained(np.arange(horizon)) * C
rfH2tp1 = fun_agwpH2sustained(np.arange(horizon-1)) * C
rfH2tp1 = np.r_[np.zeros(1), rfH2tp1]
rfH2tp1 = rfH2sus - rfH2tp1
rfH2tp1 = rfH2tp1


# # HH = 501
# HH = 31

# plt.plot(np.arange(HH), agwp_H2[:HH], color='purple')
# plt.plot(np.arange(HH), rfH2tp1[:HH], color='green')
# plt.xlim(0, HH)
# plt.ylim(0, 1.1e-12)
# plt.show()
# # plt.savefig('testtest1.ps')
# plt.clf() 

# plt.plot(np.arange(HH), agwp_H2_cont[:HH], color='purple')
# plt.plot(np.arange(HH), rfH2sus[:HH], color='green')
# plt.xlim(0, HH)
# plt.ylim(0, 5e-10)
# plt.show()
# # plt.savefig('testtest2.ps')
# plt.clf() 





def sub_agwpCO2Ocko(H):
    agwpOnly = A_CO2 * (a0*H + a1*tau1_CO2*(1-np.exp(-H/tau1_CO2))+ a2*tau2_CO2*(1-np.exp(-H/tau2_CO2))+ a3*tau3_CO2*(1-np.exp(-H/tau3_CO2))) 
    return agwpOnly * ppbperkgCO2
agwp_CO2 = sub_agwpCO2Ocko(np.arange(horizon))

rfCO2sus = fun_agwpCO2sustained(np.arange(horizon))
rfCO2tp1 = fun_agwpCO2sustained(np.arange(horizon-1)) 
rfCO2tp1 = np.r_[np.zeros(1), rfCO2tp1]
rfCO2tp1 = rfCO2sus - rfCO2tp1
rfCO2tp1 = rfCO2tp1 * ppbperkgCO2



ratio1 = agwp_H2/agwp_CO2
ratio2 = rfH2tp1/rfCO2tp1


# HH = 501
HH = 31

# plt.plot(np.arange(HH), agwp_CO2[:HH], color='purple')
# plt.plot(np.arange(HH), rfCO2tp1[:HH], color='green')
# plt.show()
# plt.clf() 

plt.plot(np.arange(HH), ratio1[:HH], color='purple')
plt.plot(np.arange(HH), ratio2[:HH], color='green')
plt.show()
plt.clf() 
