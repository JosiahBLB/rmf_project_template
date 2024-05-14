from setuptools import setup

package_name = 'prj_name_tasks'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='josiah',
    maintainer_email='josiahbrough@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'request_loop = prj_name_tasks.request_loop:main',
          'request_lift = prj_name_tasks.request_lift:main',
          'cancel_task = prj_name_tasks.cancel_task:main',
          'dispatch_loop = prj_name_tasks.dispatch_loop:main',
          'dispatch_action = prj_name_tasks.dispatch_action:main',
          'dispatch_patrol = prj_name_tasks.dispatch_patrol:main',
          'dispatch_delivery = prj_name_tasks.dispatch_delivery:main',
          'dispatch_clean = prj_name_tasks.dispatch_clean:main',
          'dispatch_go_to_place = prj_name_tasks.dispatch_go_to_place:main',
          'mock_docker = prj_name_tasks.mock_docker:main',
          'teleop_robot = prj_name_tasks.teleop_robot:main',
        ],
    },
)
