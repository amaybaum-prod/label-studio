from setuptools import setup, find_packages
import os

# Read version from package
def get_version():
    version_file = os.path.join(os.path.dirname(__file__), "src", "label_studio_converter", "__init__.py")
    with open(version_file) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip("\"'")
    return "0.0.59"

setup(
    name="label-studio-converter",
    version=get_version(),
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "nltk>=3.10.3",
        "label-studio-sdk>=0.0.41",
    ],
    extras_require={
        "test": [
            "pytest",
            "coverage",
        ]
    },
    python_requires=">=3.8",
)
