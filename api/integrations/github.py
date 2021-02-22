import os
import requests


class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    def get_organization(self, login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """
        return requests.get(
            f"{self.API_URL}/orgs/{login}",
            headers={"Authorization": f"{self.GITHUB_TOKEN}"},
        ).json()

    def get_organization_public_members(self, login: str) -> int:
        """Retorna a quantidade dos membros públicos de uma organização

        :login: login da organização no Github
        """
        return len(requests.get(f"{self.API_URL}/orgs/{login}/members").json())
