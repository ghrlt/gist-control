import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
	name='gist-control',
	version='0.1',
	scripts=['gist.py'],
	author="Gaëtan Hérault",
	author_email="gaetan.hrlt+dev@gmail.com",
	description="Use this package to automate your Gists!",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/ghrlt/gist-control",
	packages=setuptools.find_packages(),

	install_requires=[
		"requests"
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
 )