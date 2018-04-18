from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


class FX:

    def BS_Analytics_Currency(self, Y_t, K, t, T, r_d, r_f, v_y, selector):
        d1 = (np.log(Y_t / K) + (r_d - r_f + 0.5 * np.power(v_y, 2.0)) * (T - t)) / (v_y * np.sqrt(T - t))
        d2 = d1 - v_y * np.sqrt(T - t)
        if selector == 1:
            P = Y_t * np.exp(-r_f * (T - t)) * norm.cdf(d1) - K * np.exp(-r_d * (T - t)) * norm.cdf(d2)
            return P
        elif selector == 2:
            P = -Y_t * np.exp(-r_f * (T - t)) * norm.cdf(-d1) + K * np.exp(-r_d * (T - t)) * norm.cdf(-d2)
            return P
        else:
            print("Wrong input inserted, the program is now closing" + "\n")
            exit()

    def BS_Analytics_Foreign(self, Sf_t, Y_t, K_sf, t, T, r_f, v_sf, selector):
        d1 = (np.log(Sf_t / K_sf) + (r_f + 0.5 * np.power(v_sf, 2.0)) * (T - t)) / (v_sf * np.sqrt(T - t))
        d2 = d1 - v_sf * np.sqrt(T - t)
        if selector == 1:
            P = Y_t * (Sf_t * norm.cdf(d1) - K_sf * np.exp(-r_f * (T - t)) * norm.cdf(d2))
            return P
        elif(selector == 2):
            P = Y_t * (-Sf_t * norm.cdf(-d1) + K_sf * np.exp(-r_f * (T - t)) * norm.cdf(-d2))
            return P
        else:
            print("Wrong input inserted, the program is now closing" + "\n")
            exit()

    def BS_Analytics_Struck(self, Sf_t, Y_t, K_sd, t, T, r_d, v_sf, v_y, selector):
        d1 = (np.log(Sf_t * Y_t / K_sd) + (r_d + 0.5 * np.power(v_sf + v_y, 2.0)) * (T - t)) / ((v_sf + v_y) * np.sqrt(T - t))
        d2 = d1 - (v_sf + v_y) * np.sqrt(T - t);
        if selector == 1:
            P = Y_t * Sf_t * norm.cdf(d1) - K_sd * np.exp(-r_d * (T - t)) * norm.cdf(d2)
            return P
        elif selector == 2:
            P = -Y_t * Sf_t * norm.cdf(-d1) + K_sd * np.exp(-r_d * (T - t)) * norm.cdf(-d2)
            return P
        else:
            print("Wrong input inserted, the program is now closing" + "\n")
            exit()

    def BS_Analytics_Quanto(self, Y, Sf_t, K_sf, t, T, r_d, r_f, v_sf, v_y, selector):
        d1 = (np.log(Sf_t / K_sf) + (r_f - v_sf * v_y + 0.5 * np.power(v_sf, 2.0)) * (T - t)) / ((v_sf) * np.sqrt(T - t))
        d2 = d1 - (v_sf) * np.sqrt(T - t)
        if selector == 1:
            P = Y * np.exp(-r_d * (T - t)) * (Sf_t * np.exp((r_f - v_y * v_sf) * (T - t)) * norm.cdf(d1) - K_sf * norm.cdf(d2))
            return P
        elif selector == 2:
            P = Y * np.exp(-r_d * (T - t)) * (-Sf_t * np.exp((r_f - v_y * v_sf) * (T - t)) * norm.cdf(-d1) + K_sf * norm.cdf(-d2))
            return P
        else:
            print("Wrong input inserted, the program is now closing" + "\n")
            exit()

    def BS_Analytics_EquityLinked(self, Sf_t, Y_t, K, t, T, r_d, r_f, v_sf, v_y, selector):
        d1 = (np.log(Y_t / K) + (r_d - r_f + v_sf * v_y + 0.5 * np.power(v_y, 2.0)) * (T - t)) / ((v_y) * np.sqrt(T - t))
        d2 = d1 - (v_sf) * np.sqrt(T - t)
        if selector == 1:
            P = Sf_t * (Y_t * norm.cdf(d1) - K * np.exp((r_f - r_d - v_y * v_sf) * (T - t)) * norm.cdf(d2))
            return P
        elif selector == 2:
            P = Sf_t * (- Y_t * norm.cdf(-d1) + K * np.exp((r_f - r_d - v_y * v_sf) * (T - t)) * norm.cdf(-d2))
            return P
        else:
            print("Wrong input inserted, the program is now closing" + "\n")
            exit()


# Use this console for changing the inputs
Sd_t = 100.0 #Domestic asset present value
Sf_t = 100.0 #Foreign asset present value
Y_t = 1.0 #Exchange rate present value
t = 0.0 #Evaluation date
T = 1.0 #Maturity
r_d = 0.03 #Domestic risk-free rate
r_f = 0.025 #Foreign risk-free rate
Y = 1.10 #Quanto Constant
v_y = 0.05 #Exchange rate process volatility
v_sf = 0.2 #Foreign asset volatility
K = 1.0 #Exchange Rate Strike
K_sf = 100.0 #Foreign Strike
K_sd = 100.0 #Domestic Strike

if Sd_t < 0.0 or Sf_t < 0.0 or Y_t <= 0.0 or K < 0.0 or K_sf < 0.0 or K_sd < 0.0 or Y < 0.0 or t < 0.0 or t > T or r_d < 0.0 or r_f < 0.0 or v_y <= 0.0 or v_sf <= 0.0:
    print("Wrong input inserted, the program is now closing" + "\n")
    exit()

print("Choose the FX options you wish to evaluate: " + "\n" + "1 - Currency Options" + "\n" + "2 - Foreign Vanilla Options" + "\n" + "3 - Struck Options" + "\n" + "4 - Quanto Options" + "\n" + "5 - Equity Linked Options" + "\n")
selector = int(input("\n" + "Insert the number associated with your product: "))
print(selector)

print("\n" + "What is the type of your option? " + "\n" + "1 - Call" + "\n" + "2 - Put" + "\n")
selector2 = int(input("Insert the number associated with the type of your option: "))
print(type(selector2))

if selector2 != 1 and selector2 != 2:
    print("Wrong input inserted, the program is now closing" + "\n")
    exit()

if selector == 1:
    p = FX().BS_Analytics_Currency(Y_t, K, t, T, r_d, r_f, v_y, selector2)
elif selector == 2:
    p = FX().BS_Analytics_Foreign(Sf_t, Y_t, K_sf, t, T, r_f, v_sf, selector2)
elif selector == 3:
    p = FX().BS_Analytics_Struck(Sf_t, Y_t, K_sd, t, T, r_d, v_sf, v_y, selector2)
elif selector == 4:
    p = FX().BS_Analytics_Quanto(Y, Sf_t, K_sf, t, T, r_d, r_f, v_sf, v_y, selector2)
elif selector == 5:
    p = FX().BS_Analytics_EquityLinked(Sf_t, Y_t, K, t, T, r_d, r_f, v_sf, v_y, selector2)
else:
    print("Wrong inputs, the program is now closing" + "\n")
    exit()
print("\n" + "The price of your FX option is: " + str(round(p,3)) + " $" + "\n")

Maturities = np.arange(0.00000001, 10, 0.5)
if selector == 1 or selector == 5:
    S = np.arange(0.000000001, Y_t * 2, 0.1)
else:
    S = np.arange(0.000000001, Sf_t * 2, 1)
fig = plt.figure()
ax = fig.gca(projection='3d')
S, Maturities = np.meshgrid(S, Maturities)
if selector == 1:
    Z = np.array(FX().BS_Analytics_Currency(S, K, t, Maturities, r_d, r_f, v_y, selector2))
elif selector == 2:
    Z = np.array(FX().BS_Analytics_Foreign(S, Y_t, K_sf, t, Maturities, r_f, v_sf, selector2))
elif selector == 3:
    Z = np.array(FX().BS_Analytics_Struck(S, Y_t, K_sd, t, Maturities, r_d, v_sf, v_y, selector2))
elif selector == 4:
    Z = np.array(FX().BS_Analytics_Quanto(Y, S, K_sf, t, Maturities, r_d, r_f, v_sf, v_y, selector2))
else:
    Z = np.array(FX().BS_Analytics_EquityLinked(Sf_t, S, K, t, Maturities, r_d, r_f, v_sf, v_y, selector2))
surf = ax.plot_surface(S, Maturities, Z, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=False)
ax.set_zlim(0.0, np.max(Z))
if selector == 1 or selector == 5:
    ax.set_xlabel("Y", fontsize=12)
else:
    ax.set_xlabel("S", fontsize=12)
ax.set_zlabel("Price", fontsize=12)
ax.set_ylabel("T", fontsize=12)
ax.set_title("Price Surface - FX Options", fontsize=14)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
