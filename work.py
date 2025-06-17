def bmi(height, weight):
    return weight / (height/100.0) ** 2

def main():
    import math
    x = 10
    y = 3
    z = math.sqrt(2)
    x += 10
    print(bmi(x * y, z))


if __name__ == "__main__":
    main()
