"""qkx setup script"""
import imp
import os.path as pt
from setuptools import setup


def get_version():
    """Get version & version_info without importing qkx.__init__"""
    path = pt.join(pt.dirname(__file__), 'qkx', '__version__.py')
    mod = imp.load_source('qkx_version', path)
    return mod.VERSION, mod.VERSION_INFO


def get_description():
    """Get the description"""
    sm = 'Remote manager to execute commands over ssh.'
    lg = open(pt.join(pt.dirname(__file__), 'README.rst')).read()
    lg += open(pt.join(pt.dirname(__file__), 'HISTORY.rst')).read()
    return sm, lg


def get_dev_status(ver_info):
    """Get the development status"""
    dev_status_map = {
        'pre': '2 - Pre-Alpha',
        'alpha': '3 - Alpha',
        'beta': '4 - Beta',
        'rc': '4 - Beta',
        'final': '5 - Production/Stable'
    }
    pre_alpha = ver_info[3] == 'alpha' and ver_info[4] == 0
    status_key = 'pre' if pre_alpha else ver_info[3]
    return dev_status_map[status_key]


VERSION, VER_INFO = get_version()
DESCRIPTION, LONG_DESCRIPTION = get_description()
DEV_STATUS = get_dev_status(VER_INFO)


setup(name='qkx',
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      keywords='ssh git transfer files collaborate access',
      author='Manuel Lopez',
      author_email='jmlopez.rod@gmail.com',
      url='http://qkx.rtfd.org/',
      license='BSD License',
      packages=[
          'qkx',
          'qkx.command',
          'qkx.core',
          ],
      platforms=['Darwin', 'Linux'],
      scripts=['bin/qkx'],
      install_requires=[
          'pysftp>=0.2.8',
          'rsa>=3.1.4',
          'pycrypto>=2.6.1',
          'ecdsa>=0.11',
          'python-dateutil>=2.2',
          ],
      package_data={
          'qkx.scaffold': [
              'gitignore.tpl',
              'latex/*',
              'python/*',
              ],
          },
      include_package_data=True,
      classifiers=[
          'Development Status :: %s' % DEV_STATUS,
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Communications :: File Sharing',
          'Topic :: Software Development :: Version Control',
          ],
      )
