from setuptools import setup, find_packages


setup(
    name='backport_ipaddress',
    version='0.1',
    description='Backport of Python 3\'s ipaddress module',
    long_description=open('README.rst').read(),
    maintainer='Sebastian Kreft',
    url='http://github.com/sk-/backport_ipaddress',
    py_modules=['backport_ipaddress'],
    tests_require=['unittest2'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=True,
)