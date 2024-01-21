def TravelTime(dis):
    if dis <= 1:
        return 1
    return 1 + TravelTime(dis*1/2)

if __name__ == "__main__":
    distance = float(input("Enter the distance: "))
    time = TravelTime(distance)
    print(f"Time to travel {distance} meters is: {time}")w