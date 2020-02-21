from scipy.stats.kde import gaussian_kde
from numpy import linspace


def ApproxGaussienne(L):

    kde = gaussian_kde(L)
    interv_definition = linspace(min(L), max(L), 200)
    y = kde(interv_definition)
    fig = plt.figure()
    plt.plot( interv_definition, y )
    return interv_definition, y

def IntervConfiance95_1(L):
    y = ApproxGaussienne(L)[1]
    I_conf = []
    for i in range(len(y)):
        if y[i] <= 0.025:
            y.pop(i)
    
    I_conf.append(min(y))
    I_conf.append(max(y))

    return I_conf

def var(L):
    m = np.mean(L)
    L_ecart = np.add(L, -m)
    L_ecart = np.square(L_ecart)
    var = np.mean(L_ecart)

    return var

def IntervConfiance95_2(L):
    m, V = np.mean(L), var(L)
    n = len(L)
    sigma = np.sqrt(V)
    I_conf = [m - 2*(sigma/np.sqrt(n)), m + 2*(sigma/np.sqrt(n))]

    return I_conf








