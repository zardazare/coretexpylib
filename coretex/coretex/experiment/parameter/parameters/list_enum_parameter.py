from typing import Any, List, Optional, Tuple, Dict

from ..base_list_parameter import BaseListParameter
from ..utils import validateEnumStructure
from ....space import SpaceTask


class ListEnumParameter(BaseListParameter):

    @property
    def types(self) -> List[type]:
        return [str]

    @property
    def listTypes(self) -> List[type]:
        return [int]

    def validate(self) -> Tuple[bool, Optional[str]]:
        isValid, message = validateEnumStructure(self.name, self.value, self.required)
        if not isValid:
            return isValid, message

        # validateEnumStructure already checks if value is of correct type
        value: Dict[str, Any] = self.value  # type: ignore[assignment]

        selected = value["selected"]
        options = value["options"]

        if not isinstance(selected, list):
            return False, f"Enum list parameter \"{self.name}.selected\" has invalid type. Expected \"list[int]\", got \"{type(selected).__name__}\""

        if not all(isinstance(element, int) for element in selected):
            elementTypes = ", ".join({type(element).__name__ for element in selected})
            return False, f"Enum list parameter \"{self.name}.selected\" has invalid type. Expected \"list[int]\", got \"list[{elementTypes}]\""

        invalidIndxCount = len([element for element in selected if element >= len(options) or element < 0])
        if invalidIndxCount > 0:
            return False, f"Enum list parameter \"{self.name}.selected\" has out of range values"

        return True, None

    def parseValue(self, task: SpaceTask) -> Optional[Any]:
        if self.value is None:
            return self.value

        selected: List[int] = self.value["selected"]
        options: List[str] = self.value["options"]

        return [options[value] for value in selected]
