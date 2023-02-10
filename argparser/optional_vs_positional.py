import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Optional vs Positional",
        description="Esto es una CLI de ejemplo",
    )

    parser.add_argument("subcomando")
    parser.add_argument("--verbosity", help="Indica el nivel de verbosidad")
    args = parser.parse_args()
