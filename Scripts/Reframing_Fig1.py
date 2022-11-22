from Fun_final import final_emissions
from Fun_final import fun_rfCO2, fun_rfCH4, fun_rfH2
from Fun_final import fun_tCO2, fun_tCH4, fun_tH2
from Fun_final import fun_rfCO2sustained, fun_rfCH4sustained, fun_rfH2sustained
from Fun_final import fun_tCO2sustained, fun_tCH4sustained, fun_tH2sustained
from Fun_final import fun_agwpCO2sustained, fun_agwpCH4sustained, fun_agwpH2sustained
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



### Figure 1
### Time horizon of radiative forcing and temperature change for a unit pulse and constant emission 
### of 1kg H2, CH4, CO2

ppbperkgH2 = 3.5 * 1e-9  # ppb/kg
molwtH2 = 0.002016; molwtCH4 = 0.01604246; molwtCO2 = 0.04401 # kg/mol
ppbpermol = ppbperkgH2 * molwtH2  # ppb/mol
ppbpermol = 7.056*1e-12
ppbperkgCH4 = ppbpermol / molwtCH4
ppbperkgCO2 = ppbpermol / molwtCO2

# print ()
# print () 
# print (ppbperkgCO2, ppbperkgCH4, ppbperkgH2) 
# print (ppbperkgCO2/ppbperkgH2, ppbperkgCH4/ppbperkgH2, ppbperkgH2/ppbperkgH2) 
# print () 
# stop 




############################################################################################################################################
# """
# Absolute
horizon = 500

# # rfCO2 = fun_rfCO2(np.arange(horizon+1)) * ppbperkgCO2
# # rfCO2sus = fun_rfCO2sustained(np.arange(horizon+1)) * ppbperkgCO2 * 0.01
# # rfCO2tp100 = fun_rfCO2sustained(np.arange(horizon-100+1)) * ppbperkgCO2 * 0.01
# rfCO2 = fun_rfCO2(np.arange(horizon+1))    # Per ppb increase
# rfCO2sus = fun_rfCO2sustained(np.arange(horizon+1)) * 0.01
# rfCO2tp100 = fun_rfCO2sustained(np.arange(horizon-100+1)) * 0.01
# rfCO2tp100 = np.r_[np.zeros(100), rfCO2tp100]
# rfCO2tp100 = rfCO2sus - rfCO2tp100
# plt.plot(np.arange(horizon+1), rfCO2, color='purple')
# plt.plot(np.arange(horizon+1), rfCO2sus, color='purple', linestyle='--')
# plt.plot(np.arange(horizon+1), rfCO2tp100, color='purple', linestyle=':')
# plt.xlim(0, horizon)
# # plt.ylim(0, 4e-15)
# plt.ylim(0, 2.5e-5)
# # plt.ylim(0, 2)
# # plt.show() 
# plt.savefig('Fig1a.ps')
# plt.clf() 

# # rfCH4 = fun_rfCH4(np.arange(horizon+1)) * ppbperkgCH4
# # rfCH4sus = fun_rfCH4sustained(np.arange(horizon+1)) * ppbperkgCH4 * 0.01
# # rfCH4tp100 = fun_rfCH4sustained(np.arange(horizon-100+1)) * ppbperkgCH4 * 0.01
# rfCH4 = fun_rfCH4(np.arange(horizon+1))
# rfCH4sus = fun_rfCH4sustained(np.arange(horizon+1)) * 0.01
# rfCH4tp100 = fun_rfCH4sustained(np.arange(horizon-100+1)) * 0.01
# rfCH4tp100 = np.r_[np.zeros(100), rfCH4tp100]
# rfCH4tp100 = rfCH4sus - rfCH4tp100
# plt.plot(np.arange(horizon+1), rfCH4, color='orange')
# plt.plot(np.arange(horizon+1), rfCH4sus, color='orange', linestyle='--')
# plt.plot(np.arange(horizon+1), rfCH4tp100, color='orange', linestyle=':')
# plt.xlim(0, horizon)
# # plt.ylim(0, 2.4e-13)
# # plt.ylim(0, 2)
# plt.ylim(0, 6e-4)
# # plt.show() 
# plt.savefig('Fig1b.ps')
# plt.clf() 

# # rfH2 = fun_rfH2(np.arange(horizon+1)) * ppbperkgH2
# # rfH2sus = fun_rfH2sustained(np.arange(horizon+1)) * ppbperkgH2 * 0.01
# # rfH2tp100 = fun_rfH2sustained(np.arange(horizon-100+1)) * ppbperkgH2 * 0.01
# rfH2 = fun_rfH2(np.arange(horizon+1))
# rfH2sus = fun_rfH2sustained(np.arange(horizon+1)) * 0.01
# rfH2tp100 = fun_rfH2sustained(np.arange(horizon-100+1)) * 0.01
# rfH2tp100 = np.r_[np.zeros(100), rfH2tp100]
# rfH2tp100 = rfH2sus - rfH2tp100
# plt.plot(np.arange(horizon+1), rfH2, color='green')
# plt.plot(np.arange(horizon+1), rfH2sus, color='green', linestyle='--')
# plt.plot(np.arange(horizon+1), rfH2tp100, color='green', linestyle=':')
# plt.xlim(0, horizon)
# # plt.ylim(0, 7e-14)
# plt.ylim(0, 2.5e-5)
# # plt.ylim(0, 2)
# # plt.ylim(0, 2.4e-13)
# # plt.show() 
# plt.savefig('Fig1c.ps')
# plt.clf() 


# Text here 
# ratioCH4 = rfCH4/rfCO2
# ratioH2 = rfH2/rfCO2
# maxCO2 = np.max(rfCO2)
# print (ratioCH4[110]) 
# print (ratioH2[110]) 
# print (rfCO2[-1]/maxCO2*100)

# print (rfH2sus[50:100]/1e-15)


# rfCO2 = fun_tCO2(np.arange(horizon+1)) * ppbperkgCO2
# rfCO2sus = fun_tCO2sustained(np.arange(horizon+1)) * ppbperkgCO2 * 0.01
# rfCO2tp100 = fun_tCO2sustained(np.arange(horizon-100+1)) * ppbperkgCO2 * 0.01
rfCO2 = fun_tCO2(np.arange(horizon+1))
rfCO2sus = fun_tCO2sustained(np.arange(horizon+1)) * 0.01
rfCO2tp100 = fun_tCO2sustained(np.arange(horizon-100+1)) * 0.01
rfCO2tp100 = np.r_[np.zeros(100), rfCO2tp100]
rfCO2tp100 = rfCO2sus - rfCO2tp100
plt.plot(np.arange(horizon+1), rfCO2, color='purple')
plt.plot(np.arange(horizon+1), rfCO2sus, color='purple', linestyle='--')
plt.plot(np.arange(horizon+1), rfCO2tp100, color='purple', linestyle=':')
plt.xlim(0, horizon)
# plt.ylim(0, 3e-15)
plt.ylim(0, 2e-5)
# plt.show() 
plt.savefig('Fig1d.ps')
plt.clf() 

# rfCH4 = fun_tCH4(np.arange(horizon+1)) * ppbperkgCH4
# rfCH4sus = fun_tCH4sustained(np.arange(horizon+1)) * ppbperkgCH4 * 0.01
# rfCH4tp100 = fun_tCH4sustained(np.arange(horizon-100+1)) * ppbperkgCH4 * 0.01
rfCH4 = fun_tCH4(np.arange(horizon+1))
rfCH4sus = fun_tCH4sustained(np.arange(horizon+1)) * 0.01
rfCH4tp100 = fun_tCH4sustained(np.arange(horizon-100+1)) * 0.01
rfCH4tp100 = np.r_[np.zeros(100), rfCH4tp100]
rfCH4tp100 = rfCH4sus - rfCH4tp100
plt.plot(np.arange(horizon+1), rfCH4, color='orange')
plt.plot(np.arange(horizon+1), rfCH4sus, color='orange', linestyle='--')
plt.plot(np.arange(horizon+1), rfCH4tp100, color='orange', linestyle=':')
plt.xlim(0, horizon)
# plt.ylim(0, 0.8e-13)
# plt.ylim(0, 2e-4)
# plt.ylim(0, 1.8e-13)
plt.ylim(0, 4.8e-4)
# plt.show() 
plt.savefig('Fig1e.ps')
plt.clf() 

# rfH2 = fun_tH2(np.arange(horizon+1)) * ppbperkgH2
# rfH2sus = fun_tH2sustained(np.arange(horizon+1)) * ppbperkgH2 * 0.01
# rfH2tp100 = fun_tH2sustained(np.arange(horizon-100+1)) * ppbperkgH2 * 0.01
rfH2 = fun_tH2(np.arange(horizon+1))
rfH2sus = fun_tH2sustained(np.arange(horizon+1)) * 0.01
rfH2tp100 = fun_tH2sustained(np.arange(horizon-100+1)) * 0.01
rfH2tp100 = np.r_[np.zeros(100), rfH2tp100]
rfH2tp100 = rfH2sus - rfH2tp100
plt.plot(np.arange(horizon+1), rfH2, color='green')
plt.plot(np.arange(horizon+1), rfH2sus, color='green', linestyle='--')
plt.plot(np.arange(horizon+1), rfH2tp100, color='green', linestyle=':')
plt.xlim(0, horizon)
# plt.ylim(0, 3e-14)
plt.ylim(0, 2e-5)
# plt.ylim(0, 1.8e-13)
# plt.show() 
plt.savefig('Fig1f.ps')
plt.clf() 
# """


############################################################################################################################################
"""
# Ratios
# horizon = 500

# rfCO2 = fun_rfCO2(np.arange(horizon+1)) * ppbperkgCO2
# rfCO2sus = fun_rfCO2sustained(np.arange(horizon+1)) * ppbperkgCO2 * 0.01
# rfCO2tp100 = fun_rfCO2sustained(np.arange(horizon-100+1)) * ppbperkgCO2 * 0.01
# rfCO2tp100 = np.r_[np.zeros(100), rfCO2tp100]
# rfCO2tp100 = rfCO2sus - rfCO2tp100

# rfCH4 = fun_rfCH4(np.arange(horizon+1)) * ppbperkgCH4
# rfCH4sus = fun_rfCH4sustained(np.arange(horizon+1)) * ppbperkgCH4 * 0.01
# rfCH4tp100 = fun_rfCH4sustained(np.arange(horizon-100+1)) * ppbperkgCH4 * 0.01
# rfCH4tp100 = np.r_[np.zeros(100), rfCH4tp100]
# rfCH4tp100 = rfCH4sus - rfCH4tp100
# plt.plot(np.arange(horizon+1), rfCH4/rfCO2, color='orange')
# plt.plot(np.arange(horizon+1), rfCH4sus/rfCO2sus, color='orange', linestyle='--')
# plt.plot(np.arange(horizon+1), rfCH4tp100/rfCO2tp100, color='orange', linestyle=':')
# plt.xlim(0, horizon)
# plt.ylim(0, 120)
# # plt.show() 
# plt.savefig('Fig1b.ps')
# plt.clf() 

# rfH2 = fun_rfH2(np.arange(horizon+1)) * ppbperkgH2
# rfH2sus = fun_rfH2sustained(np.arange(horizon+1)) * ppbperkgH2 * 0.01
# rfH2tp100 = fun_rfH2sustained(np.arange(horizon-100+1)) * ppbperkgH2 * 0.01
# rfH2tp100 = np.r_[np.zeros(100), rfH2tp100]
# rfH2tp100 = rfH2sus - rfH2tp100
# plt.plot(np.arange(horizon+1), rfH2/rfCO2, color='green')
# plt.plot(np.arange(horizon+1), rfH2sus/rfCO2sus, color='green', linestyle='--')
# plt.plot(np.arange(horizon+1), rfH2tp100/rfCO2tp100, color='green', linestyle=':')
# plt.xlim(0, horizon)
# plt.ylim(0, 40)
# # plt.show() 
# plt.savefig('Fig1c.ps')
# plt.clf() 



# rfCO2 = fun_tCO2(np.arange(horizon+1)) * ppbperkgCO2
# rfCO2sus = fun_tCO2sustained(np.arange(horizon+1)) * ppbperkgCO2 * 0.01
# rfCO2tp100 = fun_tCO2sustained(np.arange(horizon-100+1)) * ppbperkgCO2 * 0.01
# rfCO2tp100 = np.r_[np.zeros(100), rfCO2tp100]
# rfCO2tp100 = rfCO2sus - rfCO2tp100

# rfCH4 = fun_tCH4(np.arange(horizon+1)) * ppbperkgCH4
# rfCH4sus = fun_tCH4sustained(np.arange(horizon+1)) * ppbperkgCH4 * 0.01
# rfCH4tp100 = fun_tCH4sustained(np.arange(horizon-100+1)) * ppbperkgCH4 * 0.01
# rfCH4tp100 = np.r_[np.zeros(100), rfCH4tp100]
# rfCH4tp100 = rfCH4sus - rfCH4tp100
# plt.plot(np.arange(horizon+1), rfCH4/rfCO2, color='orange')
# plt.plot(np.arange(horizon+1), rfCH4sus/rfCO2sus, color='orange', linestyle='--')
# plt.plot(np.arange(horizon+1), rfCH4tp100/rfCO2tp100, color='orange', linestyle=':')
# plt.xlim(0, horizon)
# plt.ylim(0, 120)
# # plt.show() 
# plt.savefig('Fig1e.ps')
# plt.clf() 

# rfH2 = fun_tH2(np.arange(horizon+1)) * ppbperkgH2
# rfH2sus = fun_tH2sustained(np.arange(horizon+1)) * ppbperkgH2 * 0.01
# rfH2tp100 = fun_tH2sustained(np.arange(horizon-100+1)) * ppbperkgH2 * 0.01
# rfH2tp100 = np.r_[np.zeros(100), rfH2tp100]
# rfH2tp100 = rfH2sus - rfH2tp100
# plt.plot(np.arange(horizon+1), rfH2/rfCO2, color='green')
# plt.plot(np.arange(horizon+1), rfH2sus/rfCO2sus, color='green', linestyle='--')
# plt.plot(np.arange(horizon+1), rfH2tp100/rfCO2tp100, color='green', linestyle=':')
# plt.xlim(0, horizon)
# plt.ylim(0, 40)
# # plt.show() 
# plt.savefig('Fig1f.ps')
# plt.clf() 
# """



############################################################################################################################################
"""
# Uncertainty in H2 lifetimes
horizon = 500


rfH2 = fun_rfH2(np.arange(horizon+1)) * ppbperkgH2
rfH2_lifetime14 = fun_rfH2_lifetime14(np.arange(horizon+1)) * ppbperkgH2
rfH2_lifetime25 = fun_rfH2_lifetime25(np.arange(horizon+1)) * ppbperkgH2
plt.plot(np.arange(horizon+1), rfH2, color='green')
plt.fill_between(np.arange(horizon+1), rfH2_lifetime14, rfH2_lifetime25, facecolor='green', edgecolor='none', alpha=0.3)
plt.xlim(0, horizon)
plt.ylim(0, 9e-14)
# plt.show()
plt.savefig('FigS1a.ps')
plt.clf()
rfH2sus = fun_rfH2sustained(np.arange(horizon+1))*ppbperkgH2*0.01
rfH2sus_lifetime14 = fun_rfH2sustained_lifetime14(np.arange(horizon+1))*ppbperkgH2*0.01
rfH2sus_lifetime25 = fun_rfH2sustained_lifetime25(np.arange(horizon+1))*ppbperkgH2*0.01
plt.plot(np.arange(horizon+1), rfH2sus, color='green')
plt.fill_between(np.arange(horizon+1), rfH2sus_lifetime14, rfH2sus_lifetime25, facecolor='green', edgecolor='none', alpha=0.3)
plt.xlim(0, horizon)
plt.ylim(0, 9e-14)
# plt.show()
plt.savefig('FigS1b.ps')
plt.clf()
rfH2tp100 = fun_rfH2sustained(np.arange(horizon-100+1))*ppbperkgH2*0.01; rfH2tp100 = np.r_[np.zeros(100), rfH2tp100]; rfH2tp100 = rfH2sus - rfH2tp100
rfH2tp100_lifetime14 = fun_rfH2sustained_lifetime14(np.arange(horizon-100+1))*ppbperkgH2*0.01; rfH2tp100_lifetime14 = np.r_[np.zeros(100), rfH2tp100_lifetime14]; rfH2tp100_lifetime14 = rfH2sus_lifetime14 - rfH2tp100_lifetime14
rfH2tp100_lifetime25 = fun_rfH2sustained_lifetime25(np.arange(horizon-100+1))*ppbperkgH2*0.01; rfH2tp100_lifetime25 = np.r_[np.zeros(100), rfH2tp100_lifetime25]; rfH2tp100_lifetime25 = rfH2sus_lifetime25 - rfH2tp100_lifetime25
plt.plot(np.arange(horizon+1), rfH2tp100, color='green')
plt.fill_between(np.arange(horizon+1), rfH2tp100_lifetime14, rfH2tp100_lifetime25, facecolor='green', edgecolor='none', alpha=0.3)
plt.xlim(0, horizon)
plt.ylim(0, 9e-14)
# plt.show()
plt.savefig('FigS1c.ps')
plt.clf()


rfH2 = fun_tH2(np.arange(horizon+1)) * ppbperkgH2
rfH2_lifetime14 = fun_tH2_lifetime14(np.arange(horizon+1)) * ppbperkgH2
rfH2_lifetime25 = fun_tH2_lifetime25(np.arange(horizon+1)) * ppbperkgH2
plt.plot(np.arange(horizon+1), rfH2, color='green')
plt.fill_between(np.arange(horizon+1), rfH2_lifetime14, rfH2_lifetime25, facecolor='green', edgecolor='none', alpha=0.3)
plt.xlim(0, horizon)
plt.ylim(0, 4e-14)
# plt.show()
plt.savefig('FigS1d.ps')
plt.clf()
rfH2sus = fun_tH2sustained(np.arange(horizon+1))*ppbperkgH2*0.01
rfH2sus_lifetime14 = fun_tH2sustained_lifetime14(np.arange(horizon+1))*ppbperkgH2*0.01
rfH2sus_lifetime25 = fun_tH2sustained_lifetime25(np.arange(horizon+1))*ppbperkgH2*0.01
plt.plot(np.arange(horizon+1), rfH2sus, color='green')
plt.fill_between(np.arange(horizon+1), rfH2sus_lifetime14, rfH2sus_lifetime25, facecolor='green', edgecolor='none', alpha=0.3)
plt.xlim(0, horizon)
plt.ylim(0, 4e-14)
# plt.show()
plt.savefig('FigS1e.ps')
plt.clf()
rfH2tp100 = fun_tH2sustained(np.arange(horizon-100+1))*ppbperkgH2*0.01; rfH2tp100 = np.r_[np.zeros(100), rfH2tp100]; rfH2tp100 = rfH2sus - rfH2tp100
rfH2tp100_lifetime14 = fun_tH2sustained_lifetime14(np.arange(horizon-100+1))*ppbperkgH2*0.01; rfH2tp100_lifetime14 = np.r_[np.zeros(100), rfH2tp100_lifetime14]; rfH2tp100_lifetime14 = rfH2sus_lifetime14 - rfH2tp100_lifetime14
rfH2tp100_lifetime25 = fun_tH2sustained_lifetime25(np.arange(horizon-100+1))*ppbperkgH2*0.01; rfH2tp100_lifetime25 = np.r_[np.zeros(100), rfH2tp100_lifetime25]; rfH2tp100_lifetime25 = rfH2sus_lifetime25 - rfH2tp100_lifetime25
plt.plot(np.arange(horizon+1), rfH2tp100, color='green')
plt.fill_between(np.arange(horizon+1), rfH2tp100_lifetime14, rfH2tp100_lifetime25, facecolor='green', edgecolor='none', alpha=0.3)
plt.xlim(0, horizon)
plt.ylim(0, 4e-14)
# plt.show()
plt.savefig('FigS1f.ps')
plt.clf()
# """



############################################################################################################################################
"""
# Considering CH4 converted to CO2 
horizon = 500

# rfCH4 = fun_rfCH4(np.arange(horizon+1)) * ppbperkgCH4
# rfCH4sus = fun_rfCH4sustained(np.arange(horizon+1)) * ppbperkgCH4 * 0.01
# rfCH4tp100 = fun_rfCH4sustained(np.arange(horizon-100+1)) * ppbperkgCH4 * 0.01
# rfCH4tp100 = np.r_[np.zeros(100), rfCH4tp100]
# rfCH4tp100 = rfCH4sus - rfCH4tp100
# rfCH4_addCO2 = fun_rfCH4_addCO2(np.arange(horizon+1)) * ppbperkgCH4
# rfCH4sus_addCO2 = fun_rfCH4sustained_addCO2(np.arange(horizon+1)) * ppbperkgCH4 * 0.01
# rfCH4tp100_addCO2 = fun_rfCH4sustained_addCO2(np.arange(horizon-100+1)) * ppbperkgCH4 * 0.01
# rfCH4tp100_addCO2 = np.r_[np.zeros(100), rfCH4tp100_addCO2]
# rfCH4tp100_addCO2 = rfCH4sus_addCO2 - rfCH4tp100_addCO2
# plt.plot(np.arange(horizon+1), rfCH4, color='orange')
# plt.plot(np.arange(horizon+1), rfCH4_addCO2, color='orange', linestyle='--')
# plt.xlim(0, horizon)
# plt.ylim(0, 2.5e-13)
# # plt.show() 
# plt.savefig('FigS3a.ps')
# plt.clf() 
# plt.plot(np.arange(horizon+1), rfCH4sus, color='orange')
# plt.plot(np.arange(horizon+1), rfCH4sus_addCO2, color='orange', linestyle='--')
# plt.xlim(0, horizon)
# plt.ylim(0, 2.5e-13)
# # plt.show() 
# plt.savefig('FigS3b.ps')
# plt.clf() 
# plt.plot(np.arange(horizon+1), rfCH4tp100, color='orange')
# plt.plot(np.arange(horizon+1), rfCH4tp100_addCO2, color='orange', linestyle='--')
# plt.xlim(0, horizon)
# plt.ylim(0, 2.5e-13)
# # plt.show() 
# plt.savefig('FigS3c.ps')
# plt.clf() 

# T
rfCH4 = fun_tCH4(np.arange(horizon+1)) * ppbperkgCH4
rfCH4sus = fun_tCH4sustained(np.arange(horizon+1)) * ppbperkgCH4 * 0.01
rfCH4tp100 = fun_tCH4sustained(np.arange(horizon-100+1)) * ppbperkgCH4 * 0.01
rfCH4tp100 = np.r_[np.zeros(100), rfCH4tp100]
rfCH4tp100 = rfCH4sus - rfCH4tp100
rfCH4_addCO2 = fun_tCH4_addCO2(np.arange(horizon+1)) * ppbperkgCH4
rfCH4sus_addCO2 = fun_tCH4sustained_addCO2(np.arange(horizon+1)) * ppbperkgCH4 * 0.01
rfCH4tp100_addCO2 = fun_tCH4sustained_addCO2(np.arange(horizon-100+1)) * ppbperkgCH4 * 0.01
rfCH4tp100_addCO2 = np.r_[np.zeros(100), rfCH4tp100_addCO2]
rfCH4tp100_addCO2 = rfCH4sus_addCO2 - rfCH4tp100_addCO2
plt.plot(np.arange(horizon+1), rfCH4, color='orange')
plt.plot(np.arange(horizon+1), rfCH4_addCO2, color='orange', linestyle='--')
plt.xlim(0, horizon)
plt.ylim(0, 0.8e-13)
# plt.show() 
plt.savefig('FigS3d.ps')
plt.clf() 
plt.plot(np.arange(horizon+1), rfCH4sus, color='orange')
plt.plot(np.arange(horizon+1), rfCH4sus_addCO2, color='orange', linestyle='--')
plt.xlim(0, horizon)
plt.ylim(0, 0.8e-13)
# plt.show() 
plt.savefig('FigS3e.ps')
plt.clf() 
plt.plot(np.arange(horizon+1), rfCH4tp100, color='orange')
plt.plot(np.arange(horizon+1), rfCH4tp100_addCO2, color='orange', linestyle='--')
plt.xlim(0, horizon)
plt.ylim(0, 0.8e-13)
# plt.show() 
plt.savefig('FigS3f.ps')
plt.clf() 
# """

