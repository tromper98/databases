from typing import Dict
from dataclasses import dataclass, asdict


@dataclass
class Department:
    department_id: int
    city: str
    street: str
    house: str
    employee_count: int

    def to_dict(self) -> Dict:
        return {k: str(v) for k, v in asdict(self).items()}
