def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    twoSteps = 0
    if stairs >= 2:
        twoSteps = ways(stairs - 2)
    onestep = ways(stairs - 1)
    return twoSteps + onestep
stairs  = int(input("Enter number of steps"))
print("Number of ways to climb = ",ways(stairs))
