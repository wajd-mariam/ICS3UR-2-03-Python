#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: September 2019
# This program calculates the circumference of a circle using τ (tau)

import constants


def main():

    # input
    radius = int(input("Enter the radius of the circle (mm):"))

    # process
    circumference = constants.TAU * radius

    # output
    print("")
    print("Circumference is: {} mm".format(circumference))


if __name__ == "__main__":
    main()
