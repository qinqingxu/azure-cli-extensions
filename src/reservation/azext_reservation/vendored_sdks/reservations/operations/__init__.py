# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._reservation_operations import ReservationOperations
from ._azure_reservation_api_operations import AzureReservationAPIOperationsMixin
from ._reservation_order_operations import ReservationOrderOperations
from ._operation_operations import OperationOperations
from ._calculate_refund_operations import CalculateRefundOperations
from ._return_operations_operations import ReturnOperations
from ._calculate_exchange_operations import CalculateExchangeOperations
from ._exchange_operations import ExchangeOperations
from ._quota_operations import QuotaOperations
from ._quota_request_status_operations import QuotaRequestStatusOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ReservationOperations",
    "AzureReservationAPIOperationsMixin",
    "ReservationOrderOperations",
    "OperationOperations",
    "CalculateRefundOperations",
    "ReturnOperations",
    "CalculateExchangeOperations",
    "ExchangeOperations",
    "QuotaOperations",
    "QuotaRequestStatusOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()