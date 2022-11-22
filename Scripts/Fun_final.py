import numpy as np 

### These parameters are currently from Ken's analysis before
### Should be replaced by their numbers once available 
ppbperkgH2 = 3.5 * 1e-9  # ppb/kg
molwtH2 = 0.002016; molwtCH4 = 0.01604246; molwtCO2 = 0.04401 # kg/mol
ppbpermol = ppbperkgH2 * molwtH2  # ppb/mol
ppbpermol = 7.056*1e-12
ppbperkgCH4 = ppbpermol / molwtCH4
ppbperkgCO2 = ppbpermol / molwtCO2


def final_emissions(leakCH4, leakH2, avoided=11):

    emissionArray = np.zeros([5, 3])  

    # Hydrogen electrolysis, green hydrogen from Ocko and Hamburg (2022)
    # Let's assume per 1 kg hydrogen consumption 
    H2ElectrolysisKg = 1 # kg 
    H2ElectrolysisMolar = H2ElectrolysisKg / molwtH2
    H2ElectrolysisMolarTotal = H2ElectrolysisMolar / (1-leakH2)
    H2ElectrolysisMolarLeak = H2ElectrolysisMolarTotal - H2ElectrolysisMolar
    emissionArray[0, 0] = 0 
    emissionArray[0, 1] = 0 
    emissionArray[0, 2] = H2ElectrolysisMolarLeak

    # Steam methane reforming, blue hydrogen from Ocko and Hamburg (2022)
    # Consumption of 1kg of hydrogen requires 3kg of methane
    H2SmrOckoMolar = H2ElectrolysisMolar
    H2SmrOckoMolarTotal = H2SmrOckoMolar / (1-leakH2)
    H2SmrOckoMolarLeak = H2SmrOckoMolarTotal - H2SmrOckoMolar
    Ch4SmrOckoKg = H2ElectrolysisKg * 3
    Ch4SmrOckoMolar = Ch4SmrOckoKg / molwtCH4
    Ch4SmrOckoMolarTotal = Ch4SmrOckoMolar / (1-leakCH4)
    Ch4SmrOckoMolarLeak = Ch4SmrOckoMolarTotal - Ch4SmrOckoMolar
    emissionArray[1, 0] = 0 
    emissionArray[1, 1] = Ch4SmrOckoMolarLeak 
    emissionArray[1, 2] = H2SmrOckoMolarLeak 

    # Methane pyrolysis
    # H2 + 1/2 O2 --> H2O deltaH = 286 kJ/mol
    # CH4 --> C + 2 H2 deltaH = -74.8 kJ/mol 
    effH2 = 1
    h2deltaH = 286
    pyrolysisDeltaH = -74.8
    effPyrolysis = 0.58
    EnergyProduced1KgH2 = H2ElectrolysisMolar * effH2 * h2deltaH # KJ, 100% efficacy 
    H2PyrolysisMolar = EnergyProduced1KgH2 / (effH2 * (h2deltaH + pyrolysisDeltaH/2)) 
    H2PyrolysisMolarTotal = H2PyrolysisMolar / (1-leakH2)
    H2PyrolysisMolarLeak = H2PyrolysisMolarTotal - H2PyrolysisMolar
    CH4PyrolysisMolar = H2PyrolysisMolarTotal / (2 * effPyrolysis) 
    CH4PyrolysisMolarTotal = CH4PyrolysisMolar / (1-leakCH4)
    CH4PyrolysisMolarLeak = CH4PyrolysisMolarTotal - CH4PyrolysisMolar
    emissionArray[2, 0] = 0 
    emissionArray[2, 1] = CH4PyrolysisMolarLeak 
    emissionArray[2, 2] = H2PyrolysisMolarLeak 

    # Methane combustion with Ocko and Hamburg assumption 
    # Consumption of 1kg of hydrogen avoid 11 kg of CO2
    # CH4 + 2O2  --> CO2 + 2H2O  deltaH = 890 kJ/mol
    Co2Kg = H2ElectrolysisKg * avoided 
    Co2Molar = Co2Kg / molwtCO2
    Ch4Molar = Co2Molar
    Ch4MolarTotal = Ch4Molar / (1-leakCH4)
    Ch4MolarLeak = Ch4MolarTotal - Ch4Molar
    emissionArray[3, 0] = Co2Molar 
    emissionArray[3, 1] = Ch4MolarLeak 
    emissionArray[3, 2] = 0 

    scale = 1  # 1 kg hydrogen consumption 
    # scale = 600 * 1e15 / EnergyProduced1KgH2 # X kg hydrogen to provide all energy

    # print ()
    # print ()
    # print (emissionArray[1, 1] * molwtCH4)
    # print (emissionArray[3, 1] * molwtCH4)
    # print ('-----')

    return emissionArray * ppbpermol * scale





# def test():
#     # H2 + 1/2 O2 --> H2O deltaH = 286 kJ/mol
#     # CH4 + 2O2  --> CO2 + 2H2O  deltaH = 890 kJ/mol 
#     H2Kg = 1 / (286) * molwtH2 
#     CH4Kg = 1 / (890*1) * molwtCH4
#     CO2Kg = 1 / (890*1) * molwtCO2
#     print () 
#     print () 
#     print (H2Kg, CH4Kg, CO2Kg) 
#     print (H2Kg/H2Kg, CH4Kg/H2Kg, CO2Kg/H2Kg) 
# test()
# stop 





####################################################################################################################################################################################
####################################################################################################################################################################################
####################################################################################################################################################################################

def fun_rfCO2(t):
    rfCO2 = 0.0000133*(0.2173 + 0.2763*np.exp(-0.232342*t) + 0.282*np.exp(-0.0273673*t) + 0.224*np.exp(-0.0025355*t))
    return rfCO2
def fun_rfCH4(t):
    rfCH4 = 0.000572688*np.exp(-0.0847458*t)
    return rfCH4
def fun_rfH2(t):
    rfH2 = 0.0000166868*(-np.exp(-14.2857*t) + np.exp(-0.526316*t)) - 0.0000104656*(np.exp(-0.526316*t) - np.exp(-t/8)) + 0.0000189353*(-np.exp(-0.526316*t) + np.exp(-0.0847458*t))
    return rfH2

def fun_rfCO2sustained(t):
    rfCO2sustained = 0.00132786 - 0.0000158163*np.exp(-0.232342*t) - 0.000137047*np.exp(-0.0273673*t) - 0.001175*np.exp(-0.0025355*t) + 2.89009*1e-6*t
    return rfCO2sustained
def fun_rfCH4sustained(t):
    rfCH4sustained = 0.00675772 - 0.00675772*np.exp(-0.0847458*t)
    return rfCH4sustained
def fun_rfH2sustained(t):
    rfH2sustained = 0.000281836 + 1.16807*1e-6*np.exp(-14.2857*t) + 0.0000241567*np.exp(-0.526316*t) - 0.0000837246*np.exp(-0.125*t) - 0.000223436*np.exp(-0.0847458*t)
    return rfH2sustained


def fun_rfH2_lifetime14(t):
    rfCO2 = -0.0000169179*np.exp(-14.2857*t) - 3.49089*1e-6*np.exp(-0.714286*t) + 7.12727*1e-6*np.exp(-0.125*t) + 0.0000132815*np.exp(-0.0847458*t)
    return rfCO2
def fun_rfH2_lifetime25(t):
    rfCO2 = -0.000016535*np.exp(-14.2857*t) - 0.00002526*np.exp(-0.4*t) + 0.0000152727*np.exp(-0.125*t) + 0.0000265222*np.exp(-0.0847458*t)
    return rfCO2

def fun_rfH2sustained_lifetime14(t):
    rfCO2 = 0.000207669 + 1.18425*1e-6*np.exp(-14.2857*t) + 4.88725*1e-6*np.exp(-0.714286*t) - 0.0000570182*np.exp(-0.125*t) - 0.000156722*np.exp(-0.0847458*t)
    return rfCO2
def fun_rfH2sustained_lifetime25(t):
    rfCO2 = 0.000370837 + 1.15745*1e-6*np.exp(-14.2857*t) + 0.0000631499*np.exp(-0.4*t) - 0.000122182*np.exp(-0.125*t) - 0.000312962*np.exp(-0.0847458*t)
    return rfCO2


def fun_rfCH4_addCO2(t):
    rfCH4 = 2.89009*1e-6 - 2.10996*1e-6*np.exp(-0.232342*t) + 0.000563297*np.exp(-0.0847458*t) + 5.53949*1e-6*np.exp(-0.0273673*t) + 3.07108*1e-6*np.exp(-0.0025355*t)
    return rfCH4
def fun_rfCH4sustained_addCO2(t):
    rfCH4 = 0.00805148 + 9.08129*1e-6*np.exp(-0.232342*t) - 0.00664691*np.exp(-0.0847458*t) - 0.000202413*np.exp(-0.0273673*t) - 0.00121124*np.exp(-0.0025355*t) + 2.89009*1e-6*t
    return rfCH4





def fun_agwpCO2(H):
    agwpCO2 = 0.00132786 - 0.0000158163 * np.exp(-0.232342 * H) - 0.000137047 * np.exp(-0.0273673 * H) - 0.001175 * np.exp(-0.0025355 * H) + 2.89009*1e-6 * H
    return agwpCO2
def fun_agwpCH4(H):
    agwpCH4 = 0.00675772 - 0.00675772 * np.exp(-0.0847458 * H)
    return agwpCH4
def fun_agwpH2(H):
    agwpH2 = 0.000281836 + 1.16807*1e-6 * np.exp(-14.2857 * H) + 0.0000241567 * np.exp(-0.526316 * H) - 0.0000837246 *  np.exp(-0.125 * H) - 0.000223436 * np.exp(-0.0847458 * H)
    return agwpH2

def fun_agwpCO2sustained(H):
    agwpCO2sustained = -0.468494 + 0.0000680733 * np.exp(-0.232342 * H) + 0.00500769 * np.exp(-0.0273673 * H) + 0.463419 * np.exp(-0.0025355 * H) + 0.00132786 * H + 1.44505*1e-6 * H**2
    return agwpCO2sustained
def fun_agwpCH4sustained(H):
    agwpCH4sustained = -0.0797411 + 0.0797411 * np.exp(-0.0847458 * H) + 0.00675772 * H
    return agwpCH4sustained
def fun_agwpH2sustained(H):
    agwpH2sustained = -0.00326036 - 8.17652*1e-8 * np.exp(-14.2857 * H) - 0.0000458978 * np.exp(-0.526316 * H) + 0.000669797 * np.exp(-0.125 * H) + 0.00263655 * np.exp(-0.0847458 * H) + 0.000281836 * H
    return agwpH2sustained








def fun_tCO2(H):
    tCO2 = -0.0000455369 * np.exp(-0.243902 * H) + 0.0000402533 * np.exp(-0.232342 * H) + 1.9589*1e-6 * np.exp(-0.0273673 * H) - 3.75064*1e-6 * np.exp(-0.00401606 * H) + 4.51763*1e-6 * np.exp(-0.0025355 * H) + 2.55773*1e-6 * np.exp(-2.22045*1e-16 * H)
    return tCO2 
def fun_tCH4(H):
    tCH4 = -0.000455922 * np.exp(-0.243902 * H) + 0.000445509 * np.exp(-0.0847458 * H) + 0.0000104131 * np.exp(-0.00401606 * H)
    return tCH4 
def fun_tH2(H):
    tH2 = 1.52288*1e-7 * np.exp(-14.2857 * H) + 5.73996*1e-6 * np.exp(-0.526316 * H) - 0.0000320818 * np.exp(-0.243902 * H) + 0.0000110255 * np.exp(-0.125 * H) + 0.0000147302 * np.exp(-0.0847458 * H) + 4.33827*1e-7 * np.exp(-0.00401606 * H)
    return tH2 

def fun_tCO2sustained(H):
    tCO2sustained = 0.000186701 * np.exp(-0.243902 * H) - 0.00017325 * np.exp(-0.232342 * H) - 0.0000715784 * np.exp(-0.0273673 * H) + 0.00093391 * np.exp(-0.00401606 * H) - 0.00178175 * np.exp(-0.0025355 * H) + np.exp(-2.22045*1e-16 * H) * (0.000905971 + 2.55773*1e-6 * H)
    return tCO2sustained 
def fun_tCH4sustained(H):
    tCH4sustained = 0.00598058 + 0.00186928 * np.exp(-0.243902 * H) - 0.00525701 * np.exp(-0.0847458 * H) - 0.000122874 * np.exp(-0.00401606 * H) - 0.00246998 * np.exp(-H/249)
    return tCH4sustained 
def fun_tH2sustained(H):
    tH2sustained = 0.000249425 - 1.06602*1e-8 * np.exp(-14.2857 * H) - 0.0000109059 * np.exp(-0.526316 * H) + 0.000131535 * np.exp(-0.243902 * H) - 0.0000882037 * np.exp(-0.125 * H) - 0.000173817 * np.exp(-0.0847458 * H) - 0.000108023 * np.exp(-0.00401606 * H)
    return tH2sustained 


def fun_tH2_lifetime14(H):
    tCO2 = 1.54397*1e-7*np.exp(-14.2857*H) + 9.47549*1e-7*np.exp(-0.714286*H) - 0.0000192616*np.exp(-0.243902*H) + 7.50857*1e-6*np.exp(-0.125*H) + 0.000010332*np.exp(-0.0847458*H) + 3.19017*1e-7*np.exp(-0.00401606*H)
    return tCO2 
def fun_tH2_lifetime25(H):
    tCO2 = 1.50903*1e-7*np.exp(-14.2857*H) + 0.0000205974*np.exp(-0.4*H) - 0.0000580427*np.exp(-0.243902*H) + 0.0000160898*np.exp(-0.125*H) + 0.0000206323*np.exp(-0.0847458*H) + 5.72215*1e-7*np.exp(-0.00401606*H)
    return tCO2 
def fun_tH2sustained_lifetime14(H):
    tCO2 = 0.000183787 - 1.08078*1e-8*np.exp(-14.2857*H) - 1.32657*1e-6*np.exp(-0.714286*H) + 0.0000789724*np.exp(-0.243902*H) - 0.0000600685*np.exp(-0.125*H) - 0.000121918*np.exp(-0.0847458*H) - 0.0000794351*np.exp(-0.00401606*H)
    return tCO2 
def fun_tH2sustained_lifetime25(H):
    tCO2 = 0.00032819 - 1.05632*1e-8*np.exp(-14.2857*H) - 0.0000514936*np.exp(-0.4*H) + 0.000237975*np.exp(-0.243902*H) - 0.000128718*np.exp(-0.125*H) - 0.000243462*np.exp(-0.0847458*H) - 0.000142481*np.exp(-0.00401606*H)
    return tCO2 


def fun_tCH4_addCO2(H):
    rfCH4 = -0.000431675*np.exp(-0.243902*H) - 0.0000231123*np.exp(-0.232342*H) + 0.000438204*np.exp(-0.0847458*H) + 2.89322*1e-6*np.exp(-0.0273673*H) + 6.47584*1e-6*np.exp(-0.00401606*H) + 4.65696*1e-6*np.exp(-0.0025355*H) + 2.55773*1e-6*np.exp(2.22045*1e-16*H)
    return rfCH4
def fun_tCH4sustained_addCO2(H):
    rfCH4 = 0.00176987*np.exp(-0.243902*H) + 0.0000994755*np.exp(-0.232342*H) - 0.00517081*np.exp(-0.0847458*H) - 0.000105718*np.exp(-0.0273673*H) - 0.00161248*np.exp(-0.00401606*H) - 0.00183671*np.exp(-0.0025355*H) + np.exp(2.22045*1e-16*H)*(0.00685637 + 2.55773*1e-6*H)
    return rfCH4




def fun_tCO2_Uncertainty(H):
    tCO2_G2013 = -0.0000455369*np.exp(-0.243902*H) + 0.0000402533*np.exp(-0.232342*H) + 1.9589*1e-6*np.exp(-0.0273673*H) - 3.75064*1e-6*np.exp(-0.00401606*H) + 4.51763*1e-6*np.exp(-0.0025355*H) + 2.55773*1e-6*np.exp(-2.22045*1e-16*H)
    tCO2_BR2008 = -2.45214*1e-6*np.exp(-0.232342*H) - 4.37889*1e-6*np.exp(-0.119048*H) + 2.91387*1e-6*np.exp(-0.0273673*H) - 0.0000314858*np.exp(-0.0025355*H) + 0.0000323395*np.exp(-0.002442*H) + 3.0635*1e-6*np.exp(1.11022*1e-16*H)
    tCO2_O22 = 2.46236*1e-6 - 0.0000144819*np.exp(-0.285714*H) + 9.55137*1e-6*np.exp(-0.232342*H) + 1.63543*1e-6*np.exp(-0.0273673*H) - 2.50815*1e-6*np.exp(-0.0060241*H) + 3.34086*1e-6*np.exp(-0.0025355*H)
    tCO2_CM2013 = 2.85178*1e-6 - 0.0000180416*np.exp(-0.276243*H) + 0.0000125394*np.exp(-0.232342*H) + 1.93065*1e-6*np.exp(-0.0273673*H) - 3.883*1e-6*np.exp(-0.00456621*H) + 4.60275*1e-6*np.exp(-0.0025355*H)
    outputs = np.zeros([4, len(H)])
    outputs[0] = tCO2_G2013
    outputs[1] = tCO2_BR2008
    outputs[2] = tCO2_O22
    outputs[3] = tCO2_CM2013
    return outputs
def fun_tCH4_Uncertainty(H):
    tCH4_G2013 = -0.000455922*np.exp(-0.243902*H) + 0.000445509*np.exp(-0.0847458*H) + 0.0000104131*np.exp(-0.00401606*H)
    tCH4_BR2008 = -0.00125356*np.exp(-0.119048*H) + 0.00124626*np.exp(-0.0847458*H) + 7.29467*1e-6*np.exp(-0.002442*H)
    tCH4_O22 = -0.000396787*np.exp(-0.285714*H) + 0.000380806*np.exp(-0.0847458*H) + 0.0000159808*np.exp(-0.0060241*H)
    tCH4_CM2013 = -0.000449162*np.exp(-0.276243*H) + 0.000434713*np.exp(-0.0847458*H) + 0.0000144498*np.exp(-0.00456621*H)
    outputs = np.zeros([4, len(H)])
    outputs[0] = tCH4_G2013
    outputs[1] = tCH4_BR2008
    outputs[2] = tCH4_O22
    outputs[3] = tCH4_CM2013
    return outputs
def fun_tH2_Uncertainty(H):
    tH2_G2013 = 1.52288*1e-7*np.exp(-14.2857*H) + 5.73996*1e-6*np.exp(-0.526316*H) - 0.0000320818*np.exp(-0.243902*H) + 0.0000110255*np.exp(-0.125*H) + 0.0000147302*np.exp(-0.0847458*H) + 4.33827*1e-7*np.exp(-0.00401606*H)
    tH2_BR2008 = 8.96647*1e-8*np.exp(-14.2857*H) + 2.36939*1e-6*np.exp(-0.526316*H) - 0.000132102*np.exp(-0.125*H) + 0.000088133*np.exp(-0.119048*H) + 0.0000412062*np.exp(-0.0847458*H) + 3.04044*1e-7*np.exp(-0.002442*H)
    tH2_O22 = 1.6853*1e-7*np.exp(-14.2857*H) + 7.41157*1e-6*np.exp(-0.526316*H) - 0.0000297104*np.exp(-0.285714*H) + 8.87403*1e-6*np.exp(-0.125*H) + 0.0000125909*np.exp(-0.0847458*H) + 6.65372*1e-7*np.exp(-0.0060241*H)
    tH2_CM2013 = 1.81259*1e-7*np.exp(-14.2857*H) + 7.6853*1e-6*np.exp(-0.526316*H) - 0.0000330588*np.exp(-0.276243*H) + 0.0000102171*np.exp(-0.125*H) + 0.0000143733*np.exp(-0.0847458*H) + 6.01905*1e-7*np.exp(-0.00456621*H)
    outputs = np.zeros([4, len(H)])
    outputs[0] = tH2_G2013
    outputs[1] = tH2_BR2008
    outputs[2] = tH2_O22
    outputs[3] = tH2_CM2013
    return outputs

def fun_tCO2sustained_Uncertainty(H):
    tCO2sustained_G2013 = 0.000186701*np.exp(-0.243902*H) - 0.00017325*np.exp(-0.232342*H) - 0.0000715784*np.exp(-0.0273673*H) + 0.00093391*np.exp(-0.00401606*H) - 0.00178175*np.exp(-0.0025355*H) + np.exp(-2.22045*1e-16*H)*(0.000905971 + 2.55773*1e-6*H)
    tCO2sustained_BR2008 = 0.000010554*np.exp(-0.232342*H) + 0.0000367827*np.exp(-0.119048*H) - 0.000106473*np.exp(-0.0273673*H) + 0.012418*np.exp(-0.0025355*H) - 0.013243*np.exp(-0.002442*H) + np.exp(1.11022*1e-16*H)*(0.000884147 + 3.0635*1e-6*H)
    tCO2sustained_O22 = 0.000951461 + 0.0000506865*np.exp(-0.285714*H) - 0.0000411091*np.exp(-0.232342*H) - 0.0000597587*np.exp(-0.0273673*H) + 0.000416354*np.exp(-0.0060241*H) - 0.00131763*np.exp(-0.0025355*H) + 2.46236*1e-6*H
    tCO2sustained_CM2013 = 0.00102415 + 0.0000653105*np.exp(-0.276243*H) - 0.0000539695*np.exp(-0.232342*H) - 0.0000705459*np.exp(-0.0273673*H) + 0.000850376*np.exp(-0.00456621*H) - 0.00181532*np.exp(-0.0025355*H) + 2.85178*1e-6*H
    outputs = np.zeros([4, len(H)])
    outputs[0] = tCO2sustained_G2013
    outputs[1] = tCO2sustained_BR2008
    outputs[2] = tCO2sustained_O22
    outputs[3] = tCO2sustained_CM2013
    return outputs
def fun_tCH4sustained_Uncertainty(H):
    tCH4sustained_G2013 = 0.00598058 + 0.00186928*np.exp(-0.243902*H) - 0.00525701*np.exp(-0.0847458*H) - 0.000122874*np.exp(-0.00401606*H) - 0.00246998*np.exp(-H/249)
    tCH4sustained_BR2008 = 0.00716318 + 0.0105299*np.exp(-0.119048*H) - 0.0147059*np.exp(-0.0847458*H) - 0.00298717*np.exp(-0.002442*H)
    tCH4sustained_O22 = 0.00575758 + 0.00138876*np.exp(-0.285714*H) - 0.00449351*np.exp(-0.0847458*H) - 0.000188574*np.exp(-0.0060241*H) - 0.00246424*np.exp(-H/166)
    tCH4sustained_CM2013 = 0.00666815 + 0.00162597*np.exp(-0.276243*H) - 0.00512961*np.exp(-0.0847458*H) - 0.00316451*np.exp(-0.00456621*H)
    outputs = np.zeros([4, len(H)])
    outputs[0] = tCH4sustained_G2013
    outputs[1] = tCH4sustained_BR2008
    outputs[2] = tCH4sustained_O22
    outputs[3] = tCH4sustained_CM2013
    return outputs
def fun_tH2sustained_Uncertainty(H):
    tH2sustained_G2013 = 0.000249425 - 1.06602*1e-8*np.exp(-14.2857*H) - 0.0000109059*np.exp(-0.526316*H) + 0.000131535*np.exp(-0.243902*H) - 0.0000882037*np.exp(-0.125*H) - 0.000173817*np.exp(-0.0847458*H) - 0.000108023*np.exp(-0.00401606*H)
    tH2sustained_BR2008 = 0.000298746 - 6.27653*1e-9*np.exp(-14.2857*H) - 4.50184*1e-6*np.exp(-0.526316*H) + 0.00105682*np.exp(-0.125*H) - 0.000740317*np.exp(-0.119048*H) - 0.000486233*np.exp(-0.0847458*H) - 0.000124506*np.exp(-0.002442*H)
    tH2sustained_O22 = 0.000240124 - 1.17971*1e-8*np.exp(-14.2857*H) - 0.000014082*np.exp(-0.526316*H) + 0.000103986*np.exp(-0.285714*H) - 0.0000709922*np.exp(-0.125*H) - 0.000148573*np.exp(-0.0847458*H) - 0.000110452*np.exp(-0.0060241*H)
    tH2sustained_CM2013 = 0.0002781 - 1.26881*1e-8*np.exp(-14.2857*H) - 0.0000146021*np.exp(-0.526316*H) + 0.000119673*np.exp(-0.276243*H) - 0.0000817366*np.exp(-0.125*H) - 0.000169605*np.exp(-0.0847458*H) - 0.000131817*np.exp(-0.00456621*H)
    outputs = np.zeros([4, len(H)])
    outputs[0] = tH2sustained_G2013
    outputs[1] = tH2sustained_BR2008
    outputs[2] = tH2sustained_O22
    outputs[3] = tH2sustained_CM2013
    return outputs




if __name__ == '__main__':
    final_emissions(0.01, 0.01)
    final_emissions(0.1, 0.03)