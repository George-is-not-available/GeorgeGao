class PowerCalculator:
    def calculate_power(self, x, n):
        return x ** n


# Create an instance of the PowerCalculator class
calculator = PowerCalculator()

# Calculate 7 to the power of 7
result = calculator.calculate_power(7, 7)

# Print the result
print(result)
