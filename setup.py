from setuptools import setup

try:
    desc = file.read(open('README.md'))
except StandardError:
    desc = "See README.md"

setup(
    name='nose-gae-index',
    version='1.0',
    description="Updates the GAE index.yaml with datastore queries used in tests.",
    long_description=desc,
    author='Joachim Krebs',
    author_email='joachim@jkrebs.com',
    url='http://github.com/jkrebs/nose-gae-index/',
    license='BSD',
    py_modules = ['plugin'],
    zip_safe=True,
    install_requires=['nose'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        'nose.plugins': ['gae-index = plugin:GAEIndex']
    },
)
