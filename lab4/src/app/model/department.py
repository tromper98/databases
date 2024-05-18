from typing import Dict, Optional
from dataclasses import dataclass, asdict


@dataclass
class Department:
    department_id: Optional[int]
    city: str
    street: str
    house: str
    employee_count: Optional[int] = None

    def to_dict(self) -> Dict:
        return {k: str(v) for k, v in asdict(self).items()}

    @staticmethod
    def from_dict(dt: Dict):
        if 'department_id' in dt.keys():
            department_id = dt['department_id']
        else:
            department_id = None
        return Department(department_id=department_id, city=dt['city'], street=dt['street'], house=dt['house'])
