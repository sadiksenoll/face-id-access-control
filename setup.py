from setuptools import setup, find_packages

setup(
    name="yuz-tanima-projesi",
    version="1.0.0",
    description="PyQt6 tabanlı modern yüz tanıma uygulaması",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="[Your Name]",
    author_email="[your.email@example.com]",
    url="https://github.com/[your-username]/yuz-tanima-projesi",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.4.0",
        "opencv-python>=4.7.0",
        "numpy>=1.21.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "yuz-tanima=yuz_tanima:main",
        ],
    },
)
