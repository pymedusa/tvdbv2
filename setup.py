from setuptools import find_packages, setup


setup(
    name='tvdbapiv2',
    version='1.0.1',
    description='Swagger client for the TheTVDB.com public API v2',
    author='p0psicles',
    author_email='p0psicles@gmail.com',
    url='https://github.com/pymedusa/tvdbv2',
    packages=find_packages(),
    install_requires=[
        'python-dateutil >= 2.7.0',
        'requests >= 2.16.0',
        'six >= 1.9.0',
    ],
    license='GPLv3',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
    ],
)
