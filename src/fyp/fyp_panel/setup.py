from glob import glob
import sys

from setuptools import setup

package_name = 'fyp_panel'
py_version = '.'.join(map(str, sys.version_info[:2]))
site_pkgs_path = 'lib/python' + py_version + '/site-packages/fyp_panel'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (site_pkgs_path + '/templates', glob(package_name + '/templates/*')),
        (
            site_pkgs_path + '/static/dist',
            glob(package_name + '/static/dist/*.*'),
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='josiah',
    maintainer_email='josiahbrough@gmail.com',
    description='fyp web based panel',
    license='MIT-0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_api_server=fyp_panel.simple_api_server:main',
        ],
    },
)
