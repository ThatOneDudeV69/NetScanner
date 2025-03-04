from setuptools import setup, find_packages

setup(
    name="NetScanner",
    version="1.0",
    author="ThatOneDudeV69",
    description="A Python tool for port scanning, network scanning, and MAC spoofing.",
    packages=find_packages(),
    install_requires=[
        "scapy"
    ],
    entry_points={
        "console_scripts": [
            "network-tool=network_tool.main:main"
        ]
    },
)
