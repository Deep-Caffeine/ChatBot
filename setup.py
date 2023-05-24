from importlib.machinery import SourceFileLoader
import setuptools

version = SourceFileLoader("chatbot_server.version", "src/chatbot_server/version.py").load_module()

required_packages = []
with open("requirements.txt", "r", encoding="utf-8") as f:
    required_packages.extend(f.read().splitlines())

setuptools.setup(
    name=version.package_name,
    version=version.version,
    author="cardroid",
    author_email="number1dh@gmail.com",
    description="ChatBot Server",
    install_requires=required_packages,
    license="MIT",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "chatbot_server=chatbot_server.main:main",
        ]
    },
)
