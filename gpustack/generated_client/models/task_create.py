from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskCreate")


@_attrs_define
class TaskCreate:
    """
    Attributes:
        name (str):
        method_path (str):
        args (Union[List[Any], None, Unset]):
        node_id (Union[None, Unset, int]):
        pid (Union[None, Unset, int]):
        state (Union[None, Unset, str]):
    """

    name: str
    method_path: str
    args: Union[List[Any], None, Unset] = UNSET
    node_id: Union[None, Unset, int] = UNSET
    pid: Union[None, Unset, int] = UNSET
    state: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        method_path = self.method_path

        args: Union[List[Any], None, Unset]
        if isinstance(self.args, Unset):
            args = UNSET
        elif isinstance(self.args, list):
            args = self.args

        else:
            args = self.args

        node_id: Union[None, Unset, int]
        if isinstance(self.node_id, Unset):
            node_id = UNSET
        else:
            node_id = self.node_id

        pid: Union[None, Unset, int]
        if isinstance(self.pid, Unset):
            pid = UNSET
        else:
            pid = self.pid

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "method_path": method_path,
            }
        )
        if args is not UNSET:
            field_dict["args"] = args
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if pid is not UNSET:
            field_dict["pid"] = pid
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        method_path = d.pop("method_path")

        def _parse_args(data: object) -> Union[List[Any], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                args_type_0 = cast(List[Any], data)

                return args_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None, Unset], data)

        args = _parse_args(d.pop("args", UNSET))

        def _parse_node_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        node_id = _parse_node_id(d.pop("node_id", UNSET))

        def _parse_pid(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pid = _parse_pid(d.pop("pid", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        task_create = cls(
            name=name,
            method_path=method_path,
            args=args,
            node_id=node_id,
            pid=pid,
            state=state,
        )

        task_create.additional_properties = d
        return task_create

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
