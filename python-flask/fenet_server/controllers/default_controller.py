import connexion
import six

from fenet_server import util


def fecontent_get_sc_image(scParameters, range=None):  # noqa: E501
    """Gets security content image

    Takes in the Product Name, Product Version, Channel and SC Channel to provide the image to download # noqa: E501

    :param scParameters: The Product Name, Product Version, Channel and SC Channel
    :type scParameters: str
    :param range: range header for partial downloads
    :type range: str

    :rtype: None
    """
    return 'do some magic!'


def femeta_get_meta_data(metaParameters, range=None):  # noqa: E501
    """Gets Meta Data

    Takes in the Product Name, Product Version, zfenet Channel and Model Number to provide the meta Data # noqa: E501

    :param metaParameters: The Product Name, Product Version, Fenet Channel and Model Number
    :type metaParameters: str
    :param range: range header for partial downloads
    :type range: str

    :rtype: object
    """
    return 'do some magic!'
