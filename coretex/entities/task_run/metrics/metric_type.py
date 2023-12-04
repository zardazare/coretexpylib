#     Copyright (C) 2023  Coretex LLC

#     This file is part of Coretex.ai

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.

#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from enum import IntEnum


class MetricType(IntEnum):

    """
        List of supported metric types
    """

    int = 1
    float = 2
    timestamp = 3
    interval = 4
    bytes = 5
    percent = 6


def createMetricType(index: int) -> MetricType:
    if index == 1:
        return MetricType.int

    if index == 2:
        return MetricType.float

    if index == 3:
        return MetricType.timestamp

    if index == 4:
        return MetricType.interval

    if index == 5:
        return MetricType.bytes

    if index == 6:
        return MetricType.percent

    raise ValueError(f"[Coretex] Enum index does not exist ({index}). Max: 6")
