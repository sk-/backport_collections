from setuptools import setup, find_packages


setup(
    name='backport_collections',
    version='0.1',
    description='Backport of Python 2.7\'s collections module',
    long_description=open('README.rst').read(),
    maintainer='Sebastian Kreft',
    url='http://github.com/sk-/backport_collections',
    py_modules=['backport_collections', 'backport_abcoll'],
    tests_require=['unittest2', 'nose'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python :: 2.6',
    ],
    zip_safe=True,
)
