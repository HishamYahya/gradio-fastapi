from setuptools import setup, find_packages

version = "0.1.0"

with open("README.md") as f:
    long_description = f.read()

setup(
    name="gradio-fastapi",
    version=version,
    author="Hisham Alyahya",
    author_email="Hishamaalyahya@gmail.com",
    license="MIT",
    description="Easily Share and Demo Your FastAPI Apps using Gradio Public URL Tunneling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "Gradio",
        "Deployment",
        "FastAPI",
        "Server",
        "Demoing",
        "Backend",
        "Frontend",
        "Serving",
    ],
    packages=find_packages(),
    url="https://github.com/HishamYahya/gradio-fastapi",
    install_requires=["fastapi"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)