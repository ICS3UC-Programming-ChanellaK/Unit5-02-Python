#!/usr/bin/env python3
# Created By: Chanella
# Date: May 06, 2025
# This program calculates the area of a triangle.


def calculate_area(base, height):

    area = (base * height) / 2
    print("The area is {0} cm²".format(area))


def main():
    # this function gets the base and the height of a triangle
    try:
        user_base = float(input("Enter the base of the triangle(cm):"))
        user_height = float(input("Enter the height of the triangle(cm):"))
        print("")

        if user_base <= 0 or user_height <= 0:
            print("Enter a positive number")
        else:
            # call the function to calculate the area
            calculate_area(user_base, user_height)
    except:
        print("Invalid input,please enter a valid base and height")


if __name__ == "__main__":
    main()
