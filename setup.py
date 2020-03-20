"""
slovo
~~~~~
slovo's propose is mainly for making words.
"""

from setuptools import setup, find_packages

setup(
    name="slovo",
    version=__import__("slovo").__version__,
    description="Making words",
    author="Oleg Butuzov",
    author_email="butuzov@made.ua",
    platforms=["OS Independent"],
    keywords=["words", "dictionalies"],
    python_requires='>=3.6',
    packages=find_packages(exclude=['tests']),
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
