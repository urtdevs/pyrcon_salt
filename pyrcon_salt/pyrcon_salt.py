# -*- coding: utf-8 -*-
"""
Use pyrcon as a Pillar source.
"""

# Import python libs
import logging

# Import third party libs
try:
    from pyrcon.rcon import RConnection
    HAS_LIBS = True
except ImportError:
    HAS_LIBS = False


__virtualname__ = "pyrcon"
__opts__ = {
    "pyrcon.host": None,
    "pyrcon.port": 27960,
    "pyrcon.password": None
}


# Set up Logging
log = logging.getLogger(__name__)


def __virtual__():
    """
    Only return if pyrcon is installed.
    """
    return __virtualname__ if HAS_LIBS else False


def ext_pillar(minion_id, pillar):
    """
    Execute pyrcon and return data.
    """
    host = __opts__["pyrcon.host"]
    port = __opts__["pyrcon.port"]
    password = __opts__["pyrcon.password"]

    log.info("Querying {0}:{1} with pyrcon for information for {2}.".format(host, port, minion_id))
    try:
        rcon = RConnection(host, port, password)
    except:
        log.exception("Could not connect to {0}.".format(host))
        return {}
