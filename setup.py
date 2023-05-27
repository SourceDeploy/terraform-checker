"""Setup script"""
from setuptools import find_packages
from setuptools import setup


# main_ns = {}
# with open("version.py", encoding="utf-8") as f:
#     exec(f.read(), main_ns)

setup(
  name="terraform_checker",
  #version=main_ns["__version__"],
  version="1.0",
  packages=find_packages(),
  include_package_data=True,
  install_requires=["azure-identity", "azure-mgmt-resource", "importlib-resources"]
)
