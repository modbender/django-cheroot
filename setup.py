import setuptools

README = open('README.md').read()

setuptools.setup(
    name='django-cheroot',
    version='1.0.0',
    url='https://github.com/modbender/django-cheroot',
    description='Django Cheroot provides a bridge to use Cheroot which is the high-performance, pure-Python HTTP server used by CherryPy',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Yashas H R',
    author_email='rameshmamathayashas@gmail.com',
    install_requires=[
        'django>=2.2.24',
        'cheroot>=8.2.1',
    ],
    python_requires='>=3.5',
    platforms=['any'],
    packages=setuptools.find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
