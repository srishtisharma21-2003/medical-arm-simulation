from setuptools import setup

package_name = 'my_medical_ai'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='srishti',
    maintainer_email='srishti@todo.todo',
    description='Medical AI detection for hemorrhage simulation',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'detector = my_medical_ai.detector:main',
            'scan_controller = my_medical_ai.scan_controller:main',
        ],
    },
)
