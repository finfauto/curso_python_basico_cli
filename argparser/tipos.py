import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Programa de prueba",
        description="Esto es una CLI de ejemplo",
    )

    parser.add_argument("subcomando")
    parser.add_argument("año", type=int)

    args = parser.parse_args()
    print(type(args.año))
