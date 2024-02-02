import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


def root():
    return Path(__file__).parent.resolve()


def extract_cmake_properties(file: Path):
    if not file.exists():
        return {}
    info = {}
    with file.open() as f:
        for line in [re.search("set\\((\\w+)\\s+(\\S+)\\)", line)
                     for line in f.readlines()]:
            if line is not None:
                info[line.group(1)] = line.group(2)
    return info


def extract_ledger_version():
    vers = extract_cmake_properties(root().joinpath("doc", "LedgerVersion.cmake"))
    return (
        f"{vers.get('Ledger_VERSION_MAJOR')}"
        f".{vers.get('Ledger_VERSION_MINOR')}"
        f".{vers.get('Ledger_VERSION_PATCH')}"
    )


def extract_min_python():
    info = extract_cmake_properties(root().joinpath("CMakeLists.txt"))
    return info.get("Required_Python_Version")


def library_name():
    if platform.system() == "Windows":
        file = "ledger.pyd"
    elif platform.system() == "Darwin":
        file = "ledger.dylib"
    else:
        file = "ledger.so"
    return file


ledger_version = extract_ledger_version()
min_python_ver = extract_min_python()


def glob_sources(sourcedir: str):
    root = Path(sourcedir).resolve()
    sources = []
    for child in root.glob("*"):
        if child.is_dir():
            if child.name in ["cmake", "contrib", "doc", "lib", "src", "test", "tools"]:
                sources.extend(str(f.relative_to(root)) for f in child.glob("**/*"))
        else:
            sources.append(str(child.relative_to(root)))
    return sources


class CMakeExtension(Extension):
    def __init__(self, name: str, sourcedir: str = "") -> None:
        super().__init__(name, sources=glob_sources(sourcedir))
        self.sourcedir = os.fspath(Path(sourcedir).resolve())


class CMakeBuild(build_ext):
    def replace_cmake_python_requirement(self, sourcedir: str, revert=False):
        """Don't try to link to Python libraries since there might be none."""
        file = Path(sourcedir).joinpath("CMakeLists.txt")
        with file.open("r") as f:
            lines = f.readlines()
        python_package_line = 0
        for i, line in enumerate(lines):
            if "find_package(Python" in line:
                python_package_line = 2
            if python_package_line > 0:
                if revert:
                    lines[i] = line.replace("Development.Module", "Development")
                elif "Development.Module" not in line:
                    lines[i] = line.replace("Development", "Development.Module")
                python_package_line -= 1
        with file.open("w") as f:
            f.writelines(lines)

    def build_extension(self, ext: CMakeExtension) -> None:
        ext_fullpath = Path.cwd() / self.get_ext_fullpath(ext.name)
        extdir = ext_fullpath.parent.resolve()
        self.replace_cmake_python_requirement(ext.sourcedir)
        cmake_generator = os.environ.get("CMAKE_GENERATOR", "")
        cmake_args = [
            # Older CMake versions might have trouble with newer Boost versions
            "-DBoost_NO_BOOST_CMAKE=ON",
            "-DBoost_NO_WARN_NEW_VERSIONS=ON",
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE={extdir}{os.sep}",
            f"-DUSE_PYTHON=ON",
        ]
        build_args = ["-j12"]
        build_temp = Path(self.build_temp) / ext.name
        if not build_temp.exists():
            build_temp.mkdir(parents=True)
        subprocess.run(
            ["cmake", ext.sourcedir, *cmake_args], cwd=build_temp, check=True,
        )
        subprocess.run(
            ["cmake", "--build", ".", "--target", "libledger", *build_args], cwd=build_temp, check=True,
        )
        self.replace_cmake_python_requirement(ext.sourcedir, True)
        lib = extdir.joinpath("lib" + library_name())
        if lib.exists():
            shutil.move(str(lib), str(extdir.joinpath(library_name())))
        if lib.exists():
            lib.unlink()


setup(
    name="ledger",
    version=ledger_version,
    description="Python interface to the Ledger double-entry accounting system",
    url="https://ledger-cli.org/",
    python_requires=">=" + min_python_ver,
    license="BSD-3-Clause",
    ext_modules=[CMakeExtension("ledger")],
    cmdclass={"build_ext": CMakeBuild},
)
