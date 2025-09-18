from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sosgaza_theme/__init__.py
from sosgaza_theme import __version__ as version

setup(
	name="sosgaza_theme",
	version=version,
	description="multi themes for frappe & erpnext apps",
	author="AmeerBaathar",
	author_email="ameerbaathar18@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
