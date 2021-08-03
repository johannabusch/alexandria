from setuptools import find_packages, setup

setup(
	name='alexandria',
	packages=find_packages(include=['alexandria', 'alexandria_tests']),
	version='0.1.9',
	description='Collection of scripts to analyse molecular dynamics simulations.',
	author='Jan Neumann',
	license='GPL-3.0',
        install_requires=[
            'numpy>=1.20.0',
            'scipy>=1.4.0',
            'MDAnalysis==1.1.1',
            ],
        package_data={
            "alexandria_tests": ["water_testsim/*.xtc", "water_testsim/*.tpr", "data/*.dat"],
            "doc": ["doc.pdf"],
            },
        test_suite='alexandria_tests',
)
