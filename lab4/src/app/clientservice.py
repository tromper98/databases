from typing import Protocol, List

from model.clientmodel import ClientModel


class ClientProvider(Protocol):
    def get_clients_by_department(self, department_id: int) -> List:
        ...

    def get_client_by_id(self, client_id: int) -> ClientModel:
        ...

    def update_client(self, client: ClientModel) -> None:
        ...


class ClientService:
    _provider: ClientProvider
    _client: ClientModel

    def __init__(self, client_id: int) -> None:
        self._provider = ClientProvider()
        self._client = self._provider.get_client_by_id(client_id)

    def update_client_data(self, new_client_data: ClientModel) -> None:
        self._client = new_client_data
        self._save_client_data()

    def update_client_department(self, new_department_id: int) -> None:
        self._client.department_id = new_department_id
        self._provider.update_client(self._client)

    def _save_client_data(self) -> None:
        self._provider.update_client(self._client)
