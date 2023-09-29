from dolomite_base import acquire_metadata, load_object
from .acquire_file import _CollaboratorDbHandler


def fetch_object(id: str):
    p1 = id.find(":")
    p2 = id.rfind("@")
    project = id[:p1]
    path = id[p1 + 1:p2]
    version = id[p2 + 1:]

    handler = _CollaboratorDbHandler(project, version)
    meta = acquire_metadata(handler, path)
    return load_object(meta, handler)
