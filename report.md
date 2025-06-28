# 🌟 5-Pointed Star Pattern Generation Using Complex Numbers 
## A Mathematical and Computational Approach 

### Abstract 
This project presents a method to generate a **perfect 5-pointed star (pentagram)** using **complex number theory** and **ASCII art**. By leveraging the geometric properties of complex numbers on the unit circle, we compute vertex positions and connect them with Bresenham’s line algorithm to produce a symmetric star pattern in the terminal. This approach demonstrates the application of abstract mathematics to visual pattern generation.

---

## 🧮 1. Mathematical Foundations 

### 1.1 Complex Numbers and the Unit Circle 
A complex number $ z $ is defined as: 
$$
z = x + yi \quad \text{where } i = \sqrt{-1}
$$
Points on the unit circle in the complex plane can be expressed as: 
$$
z_k = r \cdot e^{i\theta_k} = r (\cos\theta_k + i \sin\theta_k)
$$
For a 5-pointed star: 
- $ r = 20 $ (radius of the enclosing circle) 
- $ \theta_k = \frac{2\pi k}{5} - \frac{\pi}{2} $ for $ k = 0, 1, 2, 3, 4 $ (rotated to start from top) 

### 1.2 Pentagram Geometry 
The pentagram is constructed by connecting every second vertex of a regular pentagon. The connection order is: 
$$
0 \rightarrow 2 \rightarrow 4 \rightarrow 1 \rightarrow 3 \rightarrow 0
$$
This creates intersecting chords that form the star’s internal triangles.

---

## 🛠️ 2. Implementation Details 

### 2.1 Coordinate Conversion 
To map complex coordinates to a 2D ASCII grid: 
$$
x_{\text{grid}} = \text{round}(x \cdot 1.3 + \frac{\text{grid\_width}}{2}) \\
y_{\text{grid}} = \text{round}(-y \cdot 0.7 + \frac{\text{grid\_height}}{2})
$$
- **X-axis scaling (1.3):** Prevents horizontal compression. 
- **Y-axis scaling (0.7):** Compensates for taller ASCII characters. 

### 2.2 Line Drawing Algorithm 
Bresenham’s Line Algorithm is used to draw smooth lines between vertices: 
```python
def draw_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        grid[y0][x0] = '*'  # Plot pixel
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy