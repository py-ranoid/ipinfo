from setuptools import setup

setup(name='ipinfo',
      version='0.1',
      description='Module to fetch information about user using IP address',
      url='https://salsa.debian.org/comfortablydumb-guest/Hello-from-the-Debian-side',
      author='Vishal Gupta',
      author_email='vishalg8897@gmail.com',
      license='GNU',
      package_data={'ipinfo': ['country_names.json']},
      include_package_data=True,
      install_requires=[
          'argparse',
          'urllib3'
      ],
      packages=['ipinfo'],
      zip_safe=False)
