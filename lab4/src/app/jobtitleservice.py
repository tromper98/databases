from typing import List

from src.app.model import JobTitle


class JobTitleProvider:

    def get_job_titles(self) -> List[JobTitle]:
        ...


class JobTitleService:
    _provider: JobTitleProvider

    def __init__(self, provider: JobTitleProvider) -> None:
        self._provider = provider

    def get_job_titles(self) -> List[JobTitle]:
        return self._provider.get_job_titles()
