import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'prj_name_fleet_adapter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['config.yaml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.xml')),
    ],
    install_requires=['setuptools', 'fastapi>=0.79.0', 'uvicorn>=0.18.2'],
    zip_safe=True,
    maintainer='josiah',
    maintainer_email='josiahbrough@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fleet_adapter=prj_name_fleet_adapter.fleet_adapter:main',
            'fleet_manager=prj_name_fleet_adapter.fleet_manager:main',
        ],
    },
)
