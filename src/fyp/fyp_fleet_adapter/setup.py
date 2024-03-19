from glob import glob
import os

from setuptools import find_packages, setup

package_name = 'fyp_fleet_adapter'

setup(
    name=package_name,
    version='2.2.3',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['config.yaml']),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.xml'),
        ),
    ],
    install_requires=['setuptools', 'fastapi>=0.79.0', 'uvicorn>=0.18.2'],
    zip_safe=True,
    maintainer='ohettiar',
    maintainer_email='oshhettiarachchi@gmail.com',
    description='Fleet adapters for interfacing with the FYP fleet',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fleet_adapter=fyp_fleet_adapter.fleet_adapter:main',
            'fleet_manager=fyp_fleet_adapter.fleet_manager:main',
        ],
    },
)
