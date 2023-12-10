from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="ecs-rollback",
    version="1.0.0",
    author="Venkatesh Deore",
    author_email="deore.venkatesh@gmail.com",
    license="MIT",
    description="A simple CLI tool for triggering AWS ECS rollbacks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codebreaker343/ecs-rollback",
    py_modules=["ecs_rollback", "app"],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["ecs-rollback=ecs_rollback:cli"]},
)
