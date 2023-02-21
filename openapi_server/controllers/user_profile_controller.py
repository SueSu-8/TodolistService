import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.user_profile import UserProfile  # noqa: E501
from openapi_server import util


def create_user_profile(user_profile=None):  # noqa: E501
    """Create a new user-profile

    This can only be done once by a new user # noqa: E501

    :param user_profile: 
    :type user_profile: dict | bytes

    :rtype: Union[UserProfile, Tuple[UserProfile, int], Tuple[UserProfile, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        user_profile = UserProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user_profile():  # noqa: E501
    """Delete the current user-profile. Note this is permanent!

    This can only be done by a logged in user and will use the auth token # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def describe_user_profile():  # noqa: E501
    """Read the current user-profile

    This can only be done by a logged in user and will use the auth token # noqa: E501


    :rtype: Union[UserProfile, Tuple[UserProfile, int], Tuple[UserProfile, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_user_profile(user_profile=None):  # noqa: E501
    """Update the current user-profile

    This can only be done by a logged in user and will use the auth token # noqa: E501

    :param user_profile: 
    :type user_profile: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        user_profile = UserProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
