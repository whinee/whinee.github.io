import json

import click
import httpx
import yaml

GH_INFO = {
    "desc": "description",
    "forks": None,
    "issues": "open_issues_count",
    "stars": "stargazers_count",
    "watching": "subscribers_count",
}

@click.command()
@click.argument('kv')
def main(kv):
    op = []

    with open("repos.yml", "r") as f:
        RYML = yaml.safe_load(f)

    for k, v in RYML["users"].items():
        for vk, vv in v.items():
            repo = f'github.com/{k}/{vk}'
            rl = vv.get("links", {})
            links = {"repo": f'https://{repo}', **rl}
            resp = httpx.get(f'https://api.github.com/repos/{k}/{vk}').json()

            info = {}

            for ghk, ghv in GH_INFO.items():
                info[ghk] = resp[ghv if ghv else ghk]
            if rl:
                dll = rl.get("dl")
                if dll:
                    links["dl"] = dll
                else:
                    if vv["release"]:
                        links["dl"] = f'{repo}/releases'

            op.append({
                "name": vk,
                "links": links,
                "tags": vv.get("topics", []) + resp["topics"],
                **info
            })

    httpx.post(f'https://{kv}.whi-ne.workers.dev', json={"wh_projects": json.dumps(op, indent=None)})

if __name__ == '__main__':
    main()