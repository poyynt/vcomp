import setuptools
import vcomp

with open("README.md") as f:
    long_desc = f.read()


setuptools.setup(
        name="vcomp",
        version=vcomp.version,
        description="Video Compressor (VComp)",
        long_description=long_desc,
        long_description_content_type="text/markdown",
        url="https://github.com/poyynt/vcomp/",
        author="Parsa Torbati",
        author_email="parsa@programmer.net",
        packages=setuptools.find_packages(),
        python_requires=">=3.2",
        install_requires=[
            "moviepy",
            ],
        entry_points={
            "console_scripts": [
                "vcomp=vcomp.main:run",
                ],
            },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apple Public Source License",
            "Operating System :: OS Independent",
            "Development Status :: 5 - Production/Stable",
            "Natural Language :: English",
            "Topic :: Utilities",
            ],
        )
