from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='meeseeks',
    version='0.1',
    description='Existance is pain',
    url='http://github.com/anoopkcn/meeseeks',
    author='Anoop Chandran',
    author_email='anoopkcn@gmail.com',
    license='MIT',
    packages=['meeseeks'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
