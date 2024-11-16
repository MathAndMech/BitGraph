import matplotlib
matplotlib.use('TkAgg')  # Set backend before importing pyplot
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
DeltaBGmax = 5e-3
C_a = 1.6e-7
C_3 = 1
C_4 = 1.019
sigma = 6000

def calculate_delta_bg(rpm, wob):
    return C_a * (rpm**C_3) * (wob**C_4) * (sigma / 1000)

# Define the range of RPM and WOB with new ranges
rpm = np.linspace(0, 300, 400)  # 0-300 RPM
wob = np.linspace(0, 90, 400)   # 0-90 kips

# Create a meshgrid
RPM, WOB = np.meshgrid(rpm, wob)

# Calculate values
delta_bg_values = calculate_delta_bg(RPM, WOB)

# Create better visualization
levels = np.linspace(0, DeltaBGmax, 20)

# Calculate figure size for 16:9 ratio
width = 16
height = 9
plt.figure(figsize=(width, height))

# Create filled contour
contour = plt.contourf(RPM, WOB, delta_bg_values, levels=levels, cmap='Blues')

# Create red contour line with label
cs = plt.contour(RPM, WOB, delta_bg_values, levels=[DeltaBGmax], colors='red', linewidths=2)
# Place label at coordinates (x=250, y=80) with some offset
plt.text(100, 55, (r'$\Delta BG_{{x_i}max}$' + f' = {DeltaBGmax:.0e}'), 
         color='black',
         fontsize=15,
         bbox=dict(facecolor='white', edgecolor='white', alpha=0.7))

plt.colorbar(contour, label='ΔBG')
plt.xlabel('RPM')
plt.ylabel('WOB (kips)')
plt.title(r'$\Delta BG_{x_i} = C_a \left[ RPM^{C_3} \cdot WOB^{C_4} \cdot \left( \frac{\sigma}{1000} \right) x_i \right]$', pad=20)
plt.grid(True)

# Save the plot as a high-resolution PNG file
plt.savefig('BG_Constraint_WOB_RPM2.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()

# Calculate RPM values for given WOB points where ΔBG = ΔBG_max
def calculate_rpm_at_max_bg(wob):
    # Solve for RPM from the equation: DeltaBGmax = C_a * RPM^C_3 * wob^C_4 * (sigma/1000)
    rpm = (DeltaBGmax / (C_a * wob**C_4 * sigma/1000))**(1/C_3)
    return rpm

# Create evenly spaced WOB points
wob_points = np.linspace(5, 85, 40)  # 40 points from 5 to 85 kips
rpm_points = [calculate_rpm_at_max_bg(w) for w in wob_points]

# Create new figure
plt.figure(figsize=(width, height))
plt.plot(rpm_points, wob_points, 'k-o', linewidth=2, markersize=6)
plt.grid(True)
plt.xlabel('N (RPM)')
plt.ylabel('WOB (kips)')
plt.title('Bit Wear Performance Analysis')

# Add text labels above and below curve
mid_index = len(rpm_points) // 2
plt.text(rpm_points[mid_index] + 20, 45, 
         'Bit Wear > Maximum Allowable Wear', 
         fontsize=12, color='black')
plt.text(rpm_points[mid_index] + 20, 8,
         'Bit Wear < Maximum Allowable Wear', 
         fontsize=12, color='black')

plt.savefig('BG_Constraint_WOB_RPM.png', dpi=300, bbox_inches='tight')
plt.show()
