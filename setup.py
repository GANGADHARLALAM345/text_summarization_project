import setuptools
from pathlib import Path

# Read long description from README.md
HERE = Path(__file__).parent
long_description = (HERE / "README.md").read_text(encoding="utf-8")

__version__ = "1.0.0"

REPO_NAME = "text_summarization_project"
AUTHOR_USER_NAME = "GANGADHARLALAM345"
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = "s210267@rguktsklm.ac.in"


def read_requirements(path: str = "requirements.txt") -> list:
    reqs = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or line.startswith("-e"):
                    continue
                reqs.append(line)
    except FileNotFoundError:
        pass
    return reqs

# Filter requirements to avoid installing packages that require platform-specific
# build-time tools during normal package installation (e.g., `notebook` may pull
# `pywinpty` on Windows which triggers rust/extra build backends). The full
# development dependencies remain available as extras.
base_reqs = read_requirements()
blocked = {"notebook", "pywinpty"}
install_requires = [r for r in base_reqs if r.split("==")[0].lower() not in blocked]

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package / NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        "dev": [r for r in base_reqs if r.split("==")[0].lower() in blocked] + [
            "pytest", "black"
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

 
    
