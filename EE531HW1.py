"""
EE531 Homework 1

Sources
https://openai.com/

Author: ChatGPT 5.2

Modified: Jeff Dinsmore
"""
# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
"""
# ----------------------------
# 1) Transformer nameplate -> base current (HV side)
# ----------------------------
S_kVA = 3 * 333.0        # total 3-ph kVA
V_HV_LL = 13_800.0       # volts

I_HV_nom = (S_kVA * 1000) / (np.sqrt(3) * V_HV_LL)
print(f"Transformer HV rated current = {I_HV_nom:.2f} A")

# Inrush point (given assumption)
I_inrush_A = 12.0 * I_HV_nom
t_inrush_s = 0.1
I_inrush_pu = I_inrush_A / I_HV_nom  # should be 12
print(f"Inrush point: {I_inrush_A:.1f} A, {I_inrush_pu:.1f} pu at {t_inrush_s} s")

# ----------------------------
# 2) Enter curve data (READ FROM YOUR PLOTS)
#    Use either per-unit (recommended) or amps.
# ----------------------------
USE_PER_UNIT_XAXIS = True

# ---- Transformer damage curve points (from the Canvas plot)
# Put x as per-unit (I/Im) and y as seconds.
# Example placeholder points (REPLACE THESE with your readings):
xfmr_I_pu = np.array([2, 3, 5, 10, 20, 50, 100, 200, 500, 1000], dtype=float)
xfmr_t_s  = np.array([1e4, 2e3, 3e2, 3e1, 6, 0.8, 0.2, 0.08, 0.03, 0.02], dtype=float)

# ---- Fuse curve points (Type T, chosen size e.g., 25T)
# You should enter BOTH minimum-melt and total-clearing curves.
# Typical fuse plots are in AMPS on x-axis. You can enter them in amps here.
# Example placeholder points (REPLACE THESE with your readings):
fuse_I_A_melt = np.array([50, 55, 57, 60, 75, 100, 130, 160, 250, 450, 650, 750, 900, 1600, 2000], dtype=float)
fuse_t_s_melt = np.array([300, 100, 50, 30, 10, 5, 3, 2, .7, 0.2, 0.1, 0.07, 0.05, 0.02, .01], dtype=float)

fuse_I_A_clear = np.array([50, 80, 120, 200, 300, 500, 800, 1200], dtype=float)
fuse_t_s_clear = np.array([300, 60, 15, 2.2, 0.7, 0.18, 0.06, 0.03], dtype=float)

# Convert fuse curves to per-unit if we’re using per-unit x-axis
if USE_PER_UNIT_XAXIS:
    fuse_I_x_melt  = fuse_I_A_melt  / I_HV_nom
    fuse_I_x_clear = fuse_I_A_clear / I_HV_nom
    x_label = r"Current (per-unit of transformer rated current, $I/I_m$)"
    inrush_x = I_inrush_pu
else:
    fuse_I_x_melt  = fuse_I_A_melt
    fuse_I_x_clear = fuse_I_A_clear
    # Convert transformer damage curve to amps if needed
    xfmr_I_pu_to_A = xfmr_I_pu * I_HV_nom
    xfmr_I_x = xfmr_I_pu_to_A
    x_label = "Current (A)"
    inrush_x = I_inrush_A

# If per-unit x-axis, transformer curve already uses xfmr_I_pu
xfmr_I_x = xfmr_I_pu if USE_PER_UNIT_XAXIS else xfmr_I_x

# ----------------------------
# 3) Plot
# ----------------------------
plt.figure()
plt.loglog(xfmr_I_x, xfmr_t_s, linewidth=2, label="Transformer damage curve")

plt.loglog(fuse_I_x_melt, fuse_t_s_melt, "--", linewidth=2, label="Fuse min-melt (Type T, size ???)")
plt.loglog(fuse_I_x_clear, fuse_t_s_clear, "-",  linewidth=2, label="Fuse total-clearing (Type T, size ???)")

plt.loglog([inrush_x], [t_inrush_s], marker="x", markersize=10, linestyle="None",
           label=f"Inrush point (12 pu, 0.1 s)")

plt.grid(True, which="both")
plt.xlabel(x_label)
plt.ylabel("Time (s)")
plt.title("TCC Overlay: Transformer Damage vs Fuse Curves + Inrush Point")
plt.legend()
plt.show()

# %%
"""

# -------------------------------------------------
# 1) Transformer nameplate data
# -------------------------------------------------
S_kVA = 3 * 333.0        # total 3-phase kVA
V_HV_LL = 13_800.0       # volts (HV side)

I_HV_nom = (S_kVA * 1000) / (np.sqrt(3) * V_HV_LL)
print(f"Transformer HV rated current = {I_HV_nom:.2f} A")

# Inrush assumption (given)
I_inrush_A = 12.0 * I_HV_nom
t_inrush_s = 0.1

# -------------------------------------------------
# 2) Transformer damage curve (READ FROM PDF)
#    Original curve is in per-unit -> convert to amps
# -------------------------------------------------
# Example digitized points (REPLACE with your readings)
xfmr_I_pu = np.array([2, 3, 5, 10, 20, 50, 100, 200, 500, 1000], dtype=float)
xfmr_t_s  = np.array([1e4, 2e3, 3e2, 3e1, 6, 0.8, 0.2, 0.08, 0.03, 0.02], dtype=float)

# Convert per-unit current to amps
xfmr_I_A = xfmr_I_pu * I_HV_nom

# -------------------------------------------------
# 3) Fuse curves (Type T, 25T) — from manufacturer plot
# -------------------------------------------------
# Minimum-melt curve (example placeholders)
fuse_I_A_melt = np.array([49, 52, 57, 60, 75, 100, 130, 160, 250, 450, 650, 750, 900, 1600, 2000], dtype=float)
fuse_t_s_melt = np.array([300, 100, 50, 30, 10, 5, 3, 2, .7, 0.2, 0.1, 0.07, 0.05, 0.02, .01], dtype=float)

#fuse_I_A_melt = np.array([50, 80, 120, 200, 300, 500, 800, 1200], dtype=float)
#fuse_t_s_melt = np.array([200, 40, 10, 1.5, 0.5, 0.12, 0.04, 0.02], dtype=float)

# Total-clearing curve
fuse_I_A_clear = np.array([55, 65, 90, 170, 250, 550, 900, 1500, 2500, 10000], dtype=float)
fuse_t_s_clear = np.array([300, 50, 10, 2, 0.7, 0.2, 0.1, 0.05, 0.03, 0.01], dtype=float)

# -------------------------------------------------
# 4) Plot TCC
# -------------------------------------------------
plt.figure()

plt.loglog(xfmr_I_A, xfmr_t_s, linewidth=2,
    label="Transformer damage curve")

plt.loglog(fuse_I_A_melt, fuse_t_s_melt, "--", linewidth=2,
    label="Fuse min-melt (Type T, 25T)")

plt.loglog(fuse_I_A_clear, fuse_t_s_clear, "-", linewidth=2,
    label="Fuse total-clearing (Type T, 25T)")

# Inrush point
plt.loglog([I_inrush_A], [t_inrush_s], marker="x", markersize=10,
    linestyle="None", label="Inrush (12×In, 0.1 s)")

plt.grid(True, which="both")
plt.xlabel("Current (A)")
plt.ylabel("Time (s)")
plt.title("Time–Current Coordination (Amps Scale)")
plt.legend()

plt.show()
