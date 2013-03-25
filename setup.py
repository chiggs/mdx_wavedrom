from distutils.core import setup
setup(
  name='markdown_wavedrom',
  version='0.0.1.a',
  maintainer="Chris Higgs",
  maintainer_email="chiggs.99@gmail.com",
  url="github.com/chiggs/mdx_wavedrom",
  py_modules=[
    'mdx_wavedrom',
    'mdx_wavedrom.extension',
  ],
  license='LICENSE.md',
  description='A markdown extension to insert wavedrom into the HTML output.',
  long_description=open('README.md').read(),
)

