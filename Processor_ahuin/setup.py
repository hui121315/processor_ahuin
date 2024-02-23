from setuptools import setup, find_packages

setup(
    name="Processor_ahuin",
    version="0.1.0",
    author="ahuin",
    author_email="z1156273305@gmail.com",
    description="从JSON文件提取数据并保存到CSV文件的工具",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hui121315/DataProcessor",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas>=1.1.5",
    ],
)
