from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    license='MIT',
    description='An example package, EDSA - mathematical',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/AlfredAMens/mypackage',
    author='Alfred Adjei-Mensah',
    author_email='amensahalf@gmail.com'
)