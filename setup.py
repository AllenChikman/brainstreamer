from setuptools import setup, find_packages

setup(
    name='brain-computer-interface',
    version='0.1.0',
    author='Allen Chikman',
    description='Imaginary hardware , that can read minds, and upload snapshots of cognitions',
    packages=find_packages(),
    install_requires=['click', 'flask'],
    tests_require=['pytest', 'pytest-cov'],
)
