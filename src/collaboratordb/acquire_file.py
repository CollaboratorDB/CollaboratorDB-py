from dolomite_base import acquire_file, acquire_metadata
import urllib 
import requests
import json
import os


class _CollaboratorDbHandler:
    def __init__(self, project: str, version: str):
        self.project = project
        self.version = version


base_url = "https://demodb.api.artifactdb.io"
cache_dir = "~/.cache/CollaboratorDB"


@acquire_metadata.register
def _acquire_metadata_collaboratordb(project: _CollaboratorDbHandler, path: str):
    aid = project.project + ":" + path + "@" + project.version
    full_url = base_url + "/files/" + urllib.parse.quote(aid, safe='') + "/metadata"
    fpath = os.path.join(cache_dir, urllib.parse.quote(full_url, safe=''))

    if not os.path.exists(fpath):
        resp = requests.get(full_url, verify=False)
        if resp.status_code >= 300:
            raise ValueError("failed to get metadata for '" + aid + "' from the CollaboratorDB REST API")

        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        with open(fpath, 'wb') as fd:
            fd.write(resp.content)
        payload = resp.json()
    else: 
        with open(fpath, 'r') as fd:
            payload = json.load(fd)


    if "$schema" not in payload and "_extra" in payload:
        payload["$schema"] = payload["_extra"]["$schema"]
    if payload["$schema"].startswith("redirection/"):
        payload = _acquire_metadata_collaboratordb(project, payload["redirection"]["targets"][0]["location"])

    return payload


@acquire_file.register
def _acquire_file_collaboratordb(project: _CollaboratorDbHandler, path: str):
    aid = project.project + ":" + path + "@" + project.version
    full_url = base_url + "/files/" + urllib.parse.quote(aid, safe='')
    fpath = os.path.join(cache_dir, urllib.parse.quote(full_url, safe=''))

    if not os.path.exists(fpath):
        resp = requests.get(full_url, verify=False)
        if resp.status_code >= 300:
            raise ValueError("failed to get file for '" + aid + "' from the CollaboratorDB REST API")

        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        with open(fpath, 'wb') as fd:
            fd.write(resp.content)

    return fpath
