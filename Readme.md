# WOB-RPM Graph with BG Constraint

Tool for visualizing Weight on Bit (WOB) and RPM relationships with Bit Grade (BG) constraints in drilling operations.

## Features

- Contour plot showing BG constraint regions
- WOB-RPM boundary curve at maximum allowable BG
- Interactive visualization with matplotlib
- High resolution PNG output

## Installation

1. Create virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
# Usage
Run:
```bash
python BGConstraint.py
```
Generates:
- Contour plot (BG_Constraint_WOB_RPM2.png)
- WOB-RPM boundary curve (BG_Constraint_WOB_RPM.png)

## Parameters
- @param DeltaBGmax: Maximum allowable BG (5e-3)
- @param C_a: Coefficient (1.6e-7)
- @param c3: RPM exponent (1)
- @param c4: WOB exponent (1.019)
- @param sigma: MSE (6000/12000)

## Equation
${\Delta}{BG}={C_a}({RPM}^{c3} \cdot {WOB}^{c4}(\frac{\sigma}{1000})x_i)$

## Range
- RPM: 0-300
- WOB: 0-100 kips

## Dependencies
- matplotlib
- numpy

## Files
- BGConstraint.py: Main script
- (Generated) BG_Constraint_WOB_RPM.png: WOB-RPM boundary curve
- (Generated) BG_Constraint_WOB_RPM2.png: Contour plot
- .gitignore: Files to ignore