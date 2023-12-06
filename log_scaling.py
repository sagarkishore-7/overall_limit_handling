import math
import random
import matplotlib.pyplot as plt

# Generate hypothetical 5-minute bucket limits for 7 days of data
buckets_per_day = 24 * 12  # 5-minute buckets in a day
total_buckets_7_days = 7 * buckets_per_day
total_buckets_3_days = 3 * buckets_per_day

# Generate 5-minute bucket limits
limits_7_days = [random.randint(50, 200) for _ in range(total_buckets_7_days)]
limits_3_days = [random.randint(50, 200) for _ in range(total_buckets_3_days)]

# Apply logarithmic scaling to calculate the overall limits
overall_limit_7_days = sum([math.log(limit) for limit in limits_7_days])
overall_limit_3_days = sum([math.log(limit) for limit in limits_3_days])

# Transform the overall limits back to linear scale using a scaling factor
scaling_factor = max(overall_limit_7_days, overall_limit_3_days) / 5  # Adjust 500 to an appropriate value
overall_limit_7_days = math.exp(overall_limit_7_days / scaling_factor)
overall_limit_3_days = math.exp(overall_limit_3_days / scaling_factor)

print(limits_7_days)
print(limits_3_days)

print(f"Overall Limit for 7 Days of Data: {overall_limit_7_days:.2f} emails")
print(f"Overall Limit for 3 Days of Data: {overall_limit_3_days:.2f} emails")

# Create two subplots
plt.figure(figsize=(12, 6))

# Subplot for 7-day limits
plt.subplot(1, 2, 1)
plt.plot(limits_7_days, label='7-day limits')
plt.axhline(y=overall_limit_7_days, color='r', linestyle='--', label='Overall Limit')
plt.title('7-day Limits')
plt.legend()

# Subplot for 3-day limits
plt.subplot(1, 2, 2)
plt.plot(limits_3_days, label='3-day limits')
plt.axhline(y=overall_limit_3_days, color='r', linestyle='--', label='Overall Limit')
plt.title('3-day Limits')
plt.legend()

plt.tight_layout()

# Show the graphs
plt.show()