#
# Magic to get version number from git repository tag, regardless of whether the package has been installed or
# just checked out.
#
from pkg_resources import get_distribution
try:
    __version__ = get_distribution(__name__).version
except:
    # package is not installed

    try:
        from setuptools_scm import get_version
        __version__ = get_version(root='../..', relative_to=__file__) + '.notinst'
    except Exception as e:
        __version__ = 'unknown_{}'.format(str(e).replace(' ', '_'))

