from setuptools import setup, find_packages

setup(
    name='meet',
    version='1.0',
    author='Jeffrey B. Daube',
    author_email='daubejb@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url="http://www.github.com/daubejb/meet",
    description='A simple cli utility to create a meeting notes document in \
    either a google doc on google drive or in markdown in your directory of \
    choice',
    keywords='meeting notes generator google docs markdown daube design',
    install_requires=[
        'apiclient',
        'oauth2client',
        'google-api-python-client',
        ],
    entry_points={
        'console_scripts': [
            'm=main:main',
        ],
        },
    )
