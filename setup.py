import setuptools

setuptools.setup(
    name="django-miglean",
    version="0.0.1",
    url="https://github.com/borntyping/cookiecutter-pypackage-minimal",

    author="Eugen Massini",
    author_email="eugen.massini@gmail.com",

    description="Django development command to remove the existing migrations.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
