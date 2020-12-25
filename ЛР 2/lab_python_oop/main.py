from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Square("голубого", 3)
    c = Circle("зеленого", 7)
    s = Square("красного", 8)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()