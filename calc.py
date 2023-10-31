def add(x: int,y: int) -> int:
     return x + y
 
def sub(x: int,y: int) -> int:
     return x - y
 
def prod(x: int,y: int) -> int:
    return x * y
 
def div(x: int,y: int) -> int:
    return x // y


if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"Result: {add(x, y)}")