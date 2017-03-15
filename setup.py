from setuptools import setup

setup(
    name='flaskr',
    packages=['flaskr'],
    include_package_data=True,
    install_requires=[
        'flask',
        'coverage',
        'pytest',
        'pytest-cov',
        'pytest-runner',
    ],
)
