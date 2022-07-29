from setuptools import setup

# Get the long description from the README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

# Get version from __init__.py
with open('xmas-tree/__init__.py', encoding='utf-8') as f:
    version = f.read().split('__version__ = ')[1].split('\n')[0]

if __name__=="__main__":
    # Setup
    setup(
        name='xmas-tree',
        version=version,
        description='A Christmas tree generator',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/Blotz/3d-xmas-tree',
        author='Ferdinand Theil',
        author_email='f.p.theil@gmail.com',
        license='GNU General Public License v3.0',
        classifiers=[
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.10',
        ],
        packages=['xmas-tree'],
        install_requires=[
            'numpy',
            'opencv-python',
        ]
    )
