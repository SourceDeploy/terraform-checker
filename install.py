"""Environment install script"""
#!/usr/bin/env python

import argparse
import subprocess


def main(environment):
    """Install script"""
    print("Upgrading pip...")
    subprocess.call("python -m pip install --upgrade pip", shell=True)
    subprocess.call("python -m pip install wheel", shell=True)
    if environment == "dist":
        subprocess.call("pip install .", shell=True)
    else:
        subprocess.call("pip install -e .", shell=True)
        subprocess.call("pip install pre-commit pylint", shell=True)
        subprocess.call("pre-commit install", shell=True)
        subprocess.call("pre-commit run --all-files", shell=True)



if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()

    PARSER.add_argument(
      "-e",
      "--env",
      help="Environment to configure",
      default="local",
      choices=["dist", "local", "test"]
    )

    ARGS = PARSER.parse_args()
    main(ARGS.env)
