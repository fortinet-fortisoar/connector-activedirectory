""" Copyright start
  Copyright (C) 2008 - 2021 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import operations, _check_health

logger = get_logger("activedirectory")


class ActiveDirectory(Connector):
    def execute(self, config, operation, params, **kwargs):
        try:
            logger.info('In execute() Operation: {}'.format(operation))
            operation = operations.get(operation)
            return operation(config, params)
        except Exception as err:
            raise ConnectorError('{}'.format(str(err)))

    def check_health(self, config):
        try:
            return _check_health(config)
        except Exception as err:
            raise ConnectorError('{}'.format(str(err)))

