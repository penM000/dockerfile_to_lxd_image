from setuptools import setup, find_packages

setup(
    name="dockerfile2lxdimage",
    version='0.1',
    description='dockerfilelxd',
    author='penM000',
    author_email='none@gmail.com',
    url='https://github.com/penM000/dockerfile_to_lxd_image',
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      dockerfile2lxdimage = dockerfile2lxdimage.cli:execute
    """,
    install_requires=open('requirements.txt').read().splitlines(),
)
