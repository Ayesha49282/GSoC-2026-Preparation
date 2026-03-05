# Physics Script: Calculating Gravitational Force
# This script is a part of my GSoC 2026 preparation.

def calculate_gravitational_force(mass1, mass2, distance):
    """
    Calculates the force between two masses based on Newton's Law.
    Formula: F = G * (m1 * m2) / r^2
    """
    G = 6.67430e-11  # Universal Gravitational Constant
    
    force = (G * mass1 * mass2) / (distance**2)
    return force

# Example Data: Force between Earth and Moon
earth_mass = 5.972e24    # kg
moon_mass = 7.348e22     # kg
avg_distance = 3.844e8   # meters

# Calculation
force_result = calculate_gravitational_force(earth_mass, moon_mass, avg_distance)

# Output the result
print(f"Object 1 Mass: {earth_mass} kg")
print(f"Object 2 Mass: {moon_mass} kg")
print(f"Distance: {avg_distance} m")
print("-" * 30)
print(f"The Gravitational Force is: {force_result:.2f} Newtons")
