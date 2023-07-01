#!/usr/bin/env python3

import requests

def main() -> None:
    print(f"requests=={requests.__version__} installed")

    try:
        import numpy
        print(f"numpy=={numpy.__version__} installed")
    except:
        print("numpy not installed")

if __name__ == "__main__":
    main()