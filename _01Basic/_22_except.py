try:
    n1 = 10
    n2 = 'o'
    result = n1 / n2
    print("Result:", result)
except Exception as e:
    print("An error occurred:", e)
else:
    print("Division successful.")
finally:
    print("Execution completed.")