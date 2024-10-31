from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Books-Recommender-System on desktop app"
AUTHOR_USER_NAME = "Abhijit"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = [ 'numpy']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Abhijit Maharana",
    description="A small package for book Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/abhijit0905/book_recomendation_system",
    author_email="abhijitmaharana2580@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)