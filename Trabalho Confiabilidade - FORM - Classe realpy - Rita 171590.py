from realpy import *
from scipy.stats import norm

def gfunction(x, d):
    fy = x[0]
    Z = x[1]
    Msw = x[2]
    Mw = x[3]

    g = (fy * Z) * 1000 - Msw - Mw  
    return g

xvar = [
    {'varname': 'fy', 'vardist': 'lognormal', 'varmean': 305, 'varcov': 0.05},
    {'varname': 'Z', 'vardist': 'lognormal', 'varmean': 1.2, 'varcov': 0.07},
    {'varname': 'Msw', 'vardist': 'normal', 'varmean': 20_000, 'varcov': 0.26},
    {'varname': 'Mw', 'vardist': 'gumbel', 'varmean': 40_000, 'varcov': 0.87}
]

dvar = [
    {'varname': 'factor1', 'varvalue': 1.00},
    {'varname': 'factor2', 'varvalue': 1.00},
    {'varname': 'factor3', 'varvalue': 1.00},
    {'varname': 'factor4', 'varvalue': 1.00}
]

beam = Reliability(xvar, dvar, gfunction)

result = beam.form(iHLRF=True, toler=1.e-6)

try:
    beta = result[0]
    
    pf = norm.cdf(-beta)

    print(f"Reliability Index (Beta) = {beta:.4f}")
except Exception as e:
    print(f"Erro ao calcular os resultados: {e}")