import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='hyta',
    version='0.1.4',
    author='Toygar Aksoy',
    author_email='toygar.aksoy@gmail.com',
    description='Indicators for Hypance Project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Hypance/HypanceDataAnalysis',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/Hypance/HypanceDataAnalysis/issues"
    # },
    license='MIT',
    packages=['hyta'],
    install_requires=['pandas', 'numpy'],
)
