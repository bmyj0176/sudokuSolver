import time

start_time = time.time()

# Run the check once or a small number of times
for _ in range(100000000):  # Run a smaller test
    # Insert your check logic here
    pass

end_time = time.time()

# Estimate the time for 13,797 checks
time_per_1000 = (end_time - start_time) / 1000
estimated_time = time_per_1000 * 13797

print(f"Estimated time for 13,797 checks: {estimated_time} seconds")