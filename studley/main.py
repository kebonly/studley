import string_sum
import matplotlib.pyplot as plt

# print(string_sum.sum_as_string(3, 5))
# print(string_sum.simulate_diffusion(1.0, 3.5, 100))


# print(type(res))
for i in range(5):
    res = string_sum.simulate_diffusion(1.0, 0, 1000)
    plt.plot(res)
plt.show()