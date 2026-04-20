from setuptools import setup, find_packages

setup(
    name="datavalue_theme_free",
    version="1.0.0",
    description="Free theme for Frappe",
    author="Abdo Hamoud",
    author_email="abdo.host@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "frappe>=15.0.0 <16.0.0"
    ]
)
