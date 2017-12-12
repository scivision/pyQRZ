from setuptools import setup, find_packages

install_requires = ['requests', 'xmltodict', 'six']
versionstr = '0.1.0'

setup(
    name='pyQRZ',
    version=versionstr,
    author='Zeb Palmer',
    author_email='zeb@zebpalmer.com',
    package_dir={'qrz': 'qrz'},
    url='http://github.com/zebpalmer/pyQRZ',
    license='MIT',
    description='Query QRZ.com Ham Radio License API',
    long_description=open('README.rst', 'rt').read(),
    install_requires=install_requires,
    packages=find_packages(),
    python_requires='>2.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications :: Ham Radio',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
