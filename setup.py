import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="gist_control",
    version="0.1",
    author="Gaëtan Hérault",
    author_email="gaetan.hrlt+dev@gmail.com",
    description="Control your Github Gists!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ghrlt/gist-control",
    project_urls={
    	"Developer website": "https://ghr.lt?f=gist-control",
        "Bug Tracker": "https://github.com/ghrlt/gist-control/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "gist_control"},
    packages=setuptools.find_packages(where="gist_control"),
    python_requires=">=3.6",
)