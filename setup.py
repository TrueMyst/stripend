import setuptools
from setuptools import setup


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries",
]

setup(
    name="stripend",
    version="0.1.1",
    description="A Python module that includes utility methods for making your code shorter, more flexible, and smarter.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TrueMyst/stripend",
    project_urls={"Issue tracker": "https://github.com/TrueMyst/stripend/issues"},
    author="TrueMyst",
    license="MIT",
    classifiers=classifiers,
    keywords=["utilities", "utils", "python", "code", ""],
    packages=setuptools.find_packages(),
)
