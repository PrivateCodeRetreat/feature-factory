import re
from pathlib import Path

from setuptools import setup, find_packages

HERE = Path(__file__).parent
# _version_file_contents = (HERE / "project" / "version.py").read_text()
# matched = re.search(r'"(.*)"', _version_file_contents)
# VERSION = matched.group(1) if matched is not None else "UNKNOWN VERSION"
VERSION = 1

setup(
    name="approvaltests.startup",
    version=VERSION,
    description="Assertion/verification library to aid testing",
    author="ApprovalTests Contributors",
    author_email="",
    url="https://github.com/approvals/ApprovalTests.Python.starterproject",
    python_requires=">=3.6.1",
    packages=find_packages(exclude=["tests*"]),
    package_data={"approvaltests": ["reporters/reporters.json"]},
    install_requires=["pyperclip==1.8.2", "pytest"],
    long_description=(HERE / "README.md").read_text(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)
