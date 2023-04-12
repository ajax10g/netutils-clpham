from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Useful network utilities'
LONG_DESCRIPTION = 'Useful network utilities'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="netutils_clpham",
    version=VERSION,
    author="clpham",
    author_email="<youremail@email.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['netifaces', 'ipaddress'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=['python', 'clpham'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Private",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
