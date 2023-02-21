import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.task import Task  # noqa: E501
from openapi_server import util


def create_task(task_id, task=None):  # noqa: E501
    """Create a new task

     # noqa: E501

    :param task_id: uuid for task
    :type task_id: str
    :param task: 
    :type task: dict | bytes

    :rtype: Union[Task, Tuple[Task, int], Tuple[Task, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        task = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_task(task_id):  # noqa: E501
    """Delete a task

     # noqa: E501

    :param task_id: uuid for task
    :type task_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_task():  # noqa: E501
    """Lists all tasks belonging to the user

    (no filtering yet; no pagination yet) # noqa: E501


    :rtype: Union[List[Task], Tuple[List[Task], int], Tuple[List[Task], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_task(task_id, task=None):  # noqa: E501
    """Update a task

     # noqa: E501

    :param task_id: uuid for task
    :type task_id: str
    :param task: 
    :type task: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        task = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
