# calculator.py

def add(a, b):
    """
    Return the sum of a and b.
    """
    return a + b

def main():
    import argparse

    parser = argparse.ArgumentParser(description="A simple calculator")
    parser.add_argument("a", type=int, help="First number")
    parser.add_argument("b", type=int, help="Second number")
    args = parser.parse_args()

    result = add(args.a, args.b)
    print(f"The sum of {args.a} and {args.b} is {result}")


if __name__ == "__main__":
    main()
    
    
    
