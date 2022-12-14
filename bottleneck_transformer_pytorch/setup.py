from setuptools import setup, find_packages

setup(
  name = 'bottleneck-transformer-pytorch_repo',
  packages = find_packages(),
  version = '0.1.4',
  license='MIT',
  description = 'Bottleneck Transformer - Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/bottleneck-transformer-pytorch',
  keywords = [
    'artificial intelligence',
    'attention mechanism',
    'transformers',
    'image classification',
    'vision'
  ],
  install_requires=[
    'einops>=0.3',
    'torch>=1.6'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
