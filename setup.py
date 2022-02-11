import setuptools

setuptools.setup(
    name="neispy",
    version="4.0.1",
    license="MIT",
    author="Ryu ju heon",
    author_email="saidbysolo@gmail.com",
    description="Provably fair for Python",
    long_description=open("README.md", "rt", encoding="UTF8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SaidBySolo/provablyfair",
    package_data={"provablyfair": ["py.typed"]},
    packages=setuptools.find_packages(),
    platforms="any",
    classifiers=[
        # 패키지에 대한 태그
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
