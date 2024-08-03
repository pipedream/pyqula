
# functions to compute the electronic density directly from the 
# moments of the KPM LDOS


import numpy as np
from .momenttoprofile import generate_profile
from .ldos import moments_local_dos

def get_density(m_in,scale=10.,x=None,fermi=0.,
        kernel="jackson",**kwargs):
  """Return the electronic density"""
  if npol is None: npol = ne
  mus = moments_local_dos(m_in/scale,**kwargs) # get coefficients
  return get_density_from_mus(mus,fermi) # obtain the density directly



def get_density_from_mus(mus,fermi):
    N = len(mus)  # Number of moments
    # Function to compute G_n(E) for n >= 1
    def G_n(n):
        if n == 0:
            return np.arccos(-fermi)
        else:
            return np.sin(n * np.arccos(fermi)) / n
    # Compute electronic density
    rho = (mu[0] * G_n(0) + 2 * np.sum(mus[n]*G_n(n) for n in range(1, N))) / np.pi
    
    return rho

