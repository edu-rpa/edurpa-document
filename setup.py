import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="EduRPA",
    version="0.0.1",
    author="david",
    author_email="davidhuynh0222@gmail.com",
    description="education librabry for RPA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edu-rpa/edu-rpa-library",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
