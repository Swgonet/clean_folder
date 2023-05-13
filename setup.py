from setuptools import setup, find_namespace_packages

setup(
    name="Clean folder",
    version=1.0,
    description="This is a clean_folder для дз Goit",
    url="https://github.com/Swgonet/goit-homework-01",
    author="Swgonet",
    author_email="599xxd@gmail.com",
    license="Have liscense)",
    packages=find_namespace_packages(),
    entry_point={'console_scripts': ['ddd=clean_code.clean:sort']}
)