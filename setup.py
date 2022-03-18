import setuptools

with open("README.md", "r", encoding="utf8") as f:
    LONG_DESCRIPTION = f.read()

setuptools.setup(
    name="STACC-Data-Engineering-API",
    author="Rauno Arike",
    description="A web API for the STACC data engineering test task",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/RaunoArike/STACC-Data-Engineering-API",
    packages=setuptools.find_packages(exclude=("tests")),
    install_requires="flask",
    python_requires=">=3.7"
)
