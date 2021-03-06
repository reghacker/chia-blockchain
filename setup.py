from setuptools import setup


dependencies = [
    "aiter==0.13.20191203",  # Used for async generator tools
    "blspy==0.1.16",  # Signature library
    "cbor2==5.0.1",  # Used for network wire format
    "clvm==0.4",  # contract language
    "PyYAML==5.3",  # Used for config file format
    "aiosqlite==0.11.0",  # asyncio wrapper for sqlite, to store blocks
    "aiohttp==3.6.2",  # HTTP server for full node rpc
    "colorlog==4.1.0",  # Adds color to logs
    "chiavdf==0.12.3",  # timelord and vdf verification
    "chiabip158==0.12",  # bip158-style wallet filters
    "chiapos==0.12.4",  # proof of space
    "sortedcontainers==2.1.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "clvm-tools==0.1.1",  # clvm compiler tools
]

upnp_dependencies = [
    "miniupnpc==2.0.2",  # Allows users to open ports on their router
]
dev_dependencies = [
    "pytest",
    "flake8",
    "mypy",
    "isort",
    "autoflake",
    "black",
    "pytest-asyncio",
]

kwargs = dict(
    name="chia-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@chia.net",
    description="Chia proof of space plotting, proving, and verifying (wraps C++)",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="chia blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"], dev=dev_dependencies, upnp=upnp_dependencies,
    ),
    packages=[
        "src",
        "src.cmds",
        "src.consensus",
        "src.full_node",
        "src.protocols",
        "src.rpc",
        "src.server",
        "src.simulator",
        "src.types",
        "src.util",
        "src.wallet",
        "src.wallet.puzzles",
        "src.wallet.rl_wallet",
        "src.wallet.util",
    ],
    scripts=[
        "scripts/_chia-common",
        "scripts/_chia-stop-wallet",
        "scripts/chia-drop-db",
        "scripts/chia-start-all",
        "scripts/chia-start-farmer",
        "scripts/chia-restart-harvester",
        "scripts/chia-start-introducer",
        "scripts/chia-start-node",
        "scripts/chia-start-sim",
        "scripts/chia-start-timelord",
        "scripts/chia-start-wallet-gui",
        "scripts/chia-start-wallet-server",
        "scripts/chia-stop-all",
    ],
    entry_points={
        "console_scripts": [
            "chia = src.cmds.cli:main",
            "chia-check-plots = src.cmds.check_plots:main",
            "chia-create-plots = src.cmds.create_plots:main",
            "chia-generate-keys = src.cmds.generate_keys:main",
            "chia-websocket-server = src.wallet.websocket_server:main",
        ]
    },
    package_data={
        "src.util": ["initial-*.yaml"],
        "src.server": ["dummy.crt", "dummy.key"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
