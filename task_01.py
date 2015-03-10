#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setting a default value."""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal(273.15)


def fahrenheit_to_celsius(degrees):

    """A function that will convert degrees from Fahreheit to Celsius

    Arg:
        degree(int): value that will be used to convert from F to C

    Return:
        Convert the temperature from F to C

    Example:
        >>>fahrenheit_to_celsius(212)
        Decimal('100')
    """
    return (decimal.Decimal(degrees - 32) * 5) / 9


def celsius_to_kelvin(degrees):

    """A function that will convert degrees from Celsius to Kelvin

    Arg:
        degree(int): value that will be used to convert from C to K

    Return:
        Convert the temperature from C to K

    Example:
        >>>celsius_to_kelvin(100)
        Decimal('373.15')
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))


def fahrenheit_to_kelvin(degrees):

    """A function that will convert degrees from Fahrenheit to Kelvin

    Arg:
        degree(int): value that will be used to convert from F to K

    Return:
        Convert the temperature from F to K

    Example:
        >>>fahrenheit_to_kelvin(212)
        Decimal('373.15')
        """
    return fahrenheit_to_celsius(degrees) + ABSOLUTE_DIFFERENCE

F_TO_K = fahrenheit_to_kelvin(212) + ABSOLUTE_DIFFERENCE
print F_TO_K
