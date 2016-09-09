from setuptools import find_packages, setup

import ___pkg___

setup(
        name='___pkg___',
        version=___pkg___.version,
        install_requires=['cliez'],
        packages=find_packages(exclude=["tests"]),
        url='https://github.com/___github___',
        download_url='https://github.com/___github___/tarball/master',
        license='MIT',
        test_suite="tests",
        author='___author___',
        zip_safe=False,
        author_email='___email___',
        description='___description___',
        keywords='___keywords___',
        entry_points={
            'console_scripts': [
                '___cmd___ = ___pkg___.main:main'
            ]
        },
)
