from setuptools import setup

with open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='hikvision-recover',
    version='1.0',
    url='https://github.com/spyoungtech/hikvision-recover/',
    license='MIT',
    author='Spencer Young',
    author_email='spencer.young@spyoung.com',
    description='Command-line tool for generating recovery codes for Hikvision IP Cameras',
    long_description=readme,
    packages=['hikvision_recover'],
    platforms='any',
    install_requires=[],
    entry_points={
        'console_scripts': ['hikvision-recover = hikvision_recover.__init__:main']
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)