from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme_description = fh.read()

runtime_dependencies = [
]

development_dependencies = [
    "wheel == 0.37.0",
    "black == 21.9b0",
    "mccabe == 0.6.1",
    "mypy-extensions == 0.4.3",
    "pycodestyle == 2.7.0",
    "pyflakes == 2.3.1",
    "build == 0.7.0",
]

test_dependencies = [
    "tox >= 3.24",
    "nose2 >= 0.10.0",
    "coverage >= 6.0",
    "flake8 >= 3.9",
    "flake8-docstrings == 1.6.0",
    "flake8-fixme == 1.1.1",
    "flake8-eradicate == 1.1.0",
    "flake8-assertive == 1.3.0",
    "eradicate<3.0,>=2.0",
]

setup(
    name="initiator",
    version="0.0.1",
    long_description=readme_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="initiator", exclude="tests"),
    package_dir={"": "src"},
    install_requires=runtime_dependencies,
    setup_requires=development_dependencies,
    tests_require=test_dependencies,
    entry_points={
        "console_scripts": [
            "initiator = initiator.cli:run_cli",
        ]
    },
    extras_require={
        "test": test_dependencies,
        "dev": development_dependencies,
        "all": test_dependencies + development_dependencies,
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)