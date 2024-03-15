import math

def potrubi_cal(a, x1, y1, z1, x2, y2, z2):
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)


def main():
    try:
        a = int(input("délka strany místnosti: "))
        x1, y1, z1 = map(int, input("souřadnice 1. bodu (x1 y1 z1): ").split())
        x2, y2, z2 = map(int, input("souřadnice 2. bodu (x2 y2 z2): ").split())

        if a <= 0:
            raise ValueError("velikost místnosti nesmí být záporná")

        potrubi = potrubi_cal(a, x1, y1, z1, x2, y2, z2)

        print(f"min délka potrubí: {potrubi}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
