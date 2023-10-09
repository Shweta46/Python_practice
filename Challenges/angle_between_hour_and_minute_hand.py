# Function to compute the angle between the hour and minute hand
def findAngle(hh, mm):
    # handle 24-hour notation
    hh = hh % 12

    # find the position of the hour's hand
    h = (hh * 360) // 12 + (mm * 360) // (12 * 60)

    # find the position of the minute's hand
    m = (mm * 360) // 60

    # calculate the angle difference
    angle = abs(h - m)
    # abs is used to only get positive value

    # consider the shorter angle and return it
    if angle > 180:
        angle = 360 - angle

    return angle


# Clock Angle Problem
if __name__ == '__main__':
    hh = 5
    mm = 30

    print(findAngle(hh, mm))