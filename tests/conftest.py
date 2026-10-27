import sys
import os

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
src_dir = os.path.join(pkg_root, "src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
if pkg_root not in sys.path:
    sys.path.insert(1, pkg_root)
