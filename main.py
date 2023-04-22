import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


# PART 1
def lorenz(x, y, z, r, s=10, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


dt = 0.01
num_steps = 10000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (50, 45, 40)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
# Plots 1st r-value

r = int(input("Enter an r-value: "))
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r)
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

# Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

# Displays plots and increments j
plt.show()


# PART 2

# Part 2 Question 1.1
# Data points
x = [1, 3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 10, 12.41, 12.82, 13.28, 14.65, 15]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Create scatter plot
plt.scatter(x, y)
# Set labels and title
plt.xlabel('Arrival Time (min)')
plt.ylabel('Service Start Time (min)')
plt.title('Arrival Time vs. Service Start Time')
# Show plot
plt.show()

# Part 2 Question 1.2
# Data points
x = [3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 10, 12.41, 12.82, 13.28, 14.65, 15, 15.27]

# Create scatter plot
plt.scatter(x, y)
# Set labels and title
plt.xlabel('Arrival Time (min)')
plt.ylabel('Service End Time (min)')
plt.title('Arrival Time vs. Service End Time')
# Show plot
plt.show()

# Part 2 Question 1.3
# Data points
x = [0, 1.22, 1.98, 3.11, 2.25, 2.01, 1.71, 1.18, 0.4, 0, 1.41, 0.82, 0.28, 0.65, 0]

# Create scatter plot
plt.scatter(x, y)
# Set labels and title
plt.xlabel('Arrival Time (min)')
plt.ylabel('Time in Queue (min)')
plt.title('Arrival Time vs. Time in Queue')
# Show plot
plt.show()

# Part 2 Question 1.4
# Data points
x = [0, 1, 2, 2, 2, 3, 4, 3, 2, 0, 1, 2, 1, 1, 0]

# Create scatter plot
plt.scatter(x, y)
# Set labels and title
plt.xlabel('Arrival Time (min)')
plt.ylabel('Number of People in System')
plt.title('Arrival Time vs. Number of People in System')
# Show plot
plt.show()

# Part 2 Question 1.5
# Data points
x = [0, 0, 1, 1, 1, 2, 3, 2, 1, 0, 0, 1, 0, 0, 0]

# Create scatter plot
plt.scatter(x, y)
# Set labels and title
plt.xlabel('Arrival Time (min)')
plt.ylabel('Number of People in Queue')
plt.title('Arrival Time vs. Number of People in Queue')
# Show plot
plt.show()


# Part 2 Question 3a
# creates constants for lamda and mew
lamda = 10
mew = 20
# creates constant k for values between 1 and 20
k = np.linspace(1, 20)
# sets utilization (p) equal to equation for p where both lamda and mew are multiplied by k
p = (k * lamda)/(k * mew)

# plots graph
plt.plot(k, p)
plt.xlabel("k")
plt.ylabel("p")
plt.title('Utilization vs. k')
plt.show()

# Part 2 Question 3b
# sets throughput (X) equal to mew * k
X = k * mew

# plots graph
plt.plot(k, X)
plt.xlabel("k")
plt.ylabel("X")
plt.title('Throughput vs. k')
plt.show()

# Part 2 Question 3c
# sets mean number in the system E_n equal to the equation for E_n
E_n = (p**2)/(1 - p)

# plots graph
plt.plot(k, E_n)
plt.xlabel("k")
plt.ylabel("E_n")
plt.title('Mean Number in the System vs. k')
plt.show()

# Part 2 Question 3d
# sets mean time in the system E_t equal to the equation for E_t where both lamda and mew are multiplied by k
E_t = 1/((k**2) * ((mew**2) - (mew * lamda)))

# plots graph
plt.plot(k, E_t)
plt.xlabel("k")
plt.ylabel("E_t")
plt.title('Mean Time in the System vs. k')
plt.show()
