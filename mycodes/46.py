# 练习 46：项目骨架
# 这节基本都在建目录、装环境，能敲的 Python 就这个 setup.py。
# 这台机器用 py -m venv 建环境，测试从 ex47 起用 pytest，别照书装 nose 了。

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description': 'My Project',
'author': 'My Name',
'url': 'URL to get it at.' ,
'download_url': 'Where to download it.' ,
'author_email': 'My email.',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['NAME'],
'scripts': [],
'name': 'projectname'
}

setup(**config)
