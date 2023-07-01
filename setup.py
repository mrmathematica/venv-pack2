from setuptools import setup

setup(name='venv-pack2',
      version='0.6.2',
      url='https://github.com/mrmathematica/venv-pack',
      project_urls={"Source Code": "https://github.com/mrmathematica/venv-pack"},
      maintainer='mrmathematica',
      maintainer_email='mrmathematica@yahoo.com',
      keywords='venv packaging',
      classifiers=["Development Status :: 4 - Beta",
                   "License :: OSI Approved :: BSD License",
                   "Programming Language :: Python :: 3",
                   "Topic :: System :: Archiving :: Packaging",
                   "Topic :: System :: Software Distribution",
                   "Topic :: Software Development :: Build Tools"],
      license='BSD',
      description='Package virtual environments for redistribution',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      packages=['venv_pack'],
      package_data={'venv_pack': ['scripts/*',
                                  'scripts/common/*',
                                  'scripts/nt/*']},
      entry_points='''
        [console_scripts]
        venv-pack=venv_pack.__main__:main
      ''',
      zip_safe=False)
