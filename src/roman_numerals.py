import argparse


def roman_numerals(num):
    
    result = "I" * num
    

    roman_dict = {
        "IIIII": "V",
        "IIII":"IV",
        "IIIIIIIIII":"X",
        "XXXX":"XL",
        "XXXXX":"L",
        "CCCCC":"D",
        "DD":"M"
    }


    for key,value in roman_dict.items:
        result = result.replace(key, value)
        return result
