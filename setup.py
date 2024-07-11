try:
    from setuptools import setup
    has_setuptools = True
except:
    from distutils.core import setup
    has_setuptools = False

extra_args = {}
if has_setuptools:
    extra_args['install_requires'] = ['pygments', 'colorama; os_name == "nt"']

setup(
    name='colored-traceback',
    version='0.4.0',
    description='Automatically color uncaught exception tracebacks',
    long_description=open("README.rst").read(),
    author='Anton Backer',
    author_email='olegov@gmail.com',
    url='http://www.github.com/staticshock/colored-traceback.py',
    packages=['colored_traceback', 'colored_traceback.auto', 'colored_traceback.always'],
    license='ISC',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ),
    **extra_args
)
