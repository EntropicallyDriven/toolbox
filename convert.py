# All conversion factors in the form A_B:
# If you have a quantity in unit A and want to convert it
# to unit B, multiply it by A_B.

################ L E N G T H ################

in_m    = 0.0254
mil_m   = 2.54e-5
nm_m    = 1e-9
um_m    = 1e-6
mm_m    = 0.001
cm_m    = 0.01
km_m    = 1000.0
mi_m    = 1609.34
au_m    = 149597870700
ly_m    = 9.4605284e15

mil_mm  = 0.0254
mil_um  = 25.4

m_in = 1.0/in_m
m_mil = 1.0/mil_m
m_nm  = 1e9
m_um  = 1e6
m_mm = 1000
m_cm = 100
m_km = 0.001
m_mi    = 1.0/mi_m
m_au = 1.0/au_m
m_ly = 1.0/ly_m

mm_mil = 1.0/mil_mm
um_mil = 1.0/mil_um

############## V O L U M E ##################
cc_l = 1e-3
l_cc = 1e3
l_m3 = 0.001
gal_l = 3.78541
m3_l = 1000
l_gal = 1.0/gal_l

################ M A S S  ###################
lb_kg = 0.453592
lb_g = 453.592
oz_kg = 0.0283495
oz_g  = 28.3495
g_kg = 0.001

kg_lb = 1.0/lb_kg
g_lb  = 1.0/lb_g
kg_oz = 1.0/oz_kg
g_oz = 1.0/oz_g
kg_g = 1.0/g_kg

############## E N E R G Y ##################
ev_j    = 1.60217662e-19
hz_j    = 6.62607004e-34
j_hz    = 1.0/hz_j
j_ev    = 1.0/ev_j
hz_ev   = hz_j * j_ev
ev_hz   = 1.0/hz_ev

############ P R E S S U R E ################
atm_torr = 760.0
atm_pa   = 101325.0
atm_bar  = 1.01325
atm_mbar = 1013.25
pa_torr = 0.00750061683
mbar_torr = 0.750061683

torr_atm  = 1.0/atm_torr
pa_atm    = 1.0/atm_pa
bar_atm   = 1.0/atm_bar
mbar_atm  = 1.0/atm_mbar
torr_pa   = 1.0/pa_torr
torr_mbar = 1.0/mbar_torr

######## M A G N E T I C   F I E L D ########
t_g       = 10000.0
g_t       = 1.0/t_g

########### T E M P E R A T U R E ###########
def f_k(tf):
    return (5.0 * (tf + 459.67) /9.0)
def f_c(tf):
    return (5.0 * (tf -32) / 9.0)
def k_f(tk):
    return (1.8 * tk - 459.67)
def c_f(tc):
    return (1.8 * tc + 32)
def c_k(tc):
    return tc + 273.15
def k_c(tk):
    return tk - 273.15
