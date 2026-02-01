import math
import random

def generate_trig_values():
    # 1. Generate a random angle in degrees (0 to 360)
    # uniform() gives us a float for better precision
    angle_deg = random.uniform(0, 360)

    # 2. Convert the angle to radians 
    # Python's math functions (sin, cos, tan) strictly use radians
    angle_rad = math.radians(angle_deg)

    # 3. Calculate trigonometric values
    s_val = math.sin(angle_rad)
    c_val = math.cos(angle_rad)
    
    # Tangent can be undefined at 90 or 270 degrees, 
    # but math.tan will return a very large number instead
    t_val = math.tan(angle_rad)

    # --- OUTPUT ---
    print(f"--- Trig Results ---")
    print(f"Random Angle (Deg): {angle_deg:.2f}°")
    print(f"Random Angle (Rad): {angle_rad:.4f} rad")
    print("-" * 20)
    print(f"Sine:    {s_val:.4f}")
    print(f"Cosine:  {c_val:.4f}")
    print(f"Tangent: {t_val:.4f}")

# Execute the function
if __name__ == "__main__":
    generate_trig_values()