from scipy.integrate import quad

def proba_depasse(L, lmax):
    m, V = np.mean(L), var(L)
    sigma = np.sqrt(V)

    def f(l):
        return ( 1/(sigma * np.sqrt(2*np.pi)) ) * np.exp(-0.5 * ( (l - m)/sigma )**2 )
    
    P = quad(f, lmax, np.inf)

    return P