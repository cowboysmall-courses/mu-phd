
import json
import importlib

from typing import List

# from sdc.tile import Tile
# from sdc.builders import TileSetBuilder


C_NAME = "__classname__"
M_NAME = "__modulename__"


def write_sdc_tileset(path: str, tileset: List) -> None:
    with open(path, "w") as f:
        json.dump(tileset, f, indent = 4, cls = SDCEncoder)

def read_sdc_tileset(path: str) -> List:
    with open(path, "r") as f:
        loaded = json.load(f, object_hook = sdc_decoder)
    return loaded



def sdc_decoder(obj):
    if C_NAME in obj and M_NAME in obj:
        if "layout" in obj:
            obj["layout"] = tuple(obj["layout"])

        m = importlib.import_module(obj.pop(M_NAME))
        c = getattr(m, obj.pop(C_NAME))

        return c(**obj)

    return obj



class SDCEncoder(json.JSONEncoder):

    def default(self, o):
        d = dict(o.__dict__)

        for k in o.__dict__.keys():
            if k.startswith("_"):
                d.pop(k)

        d[C_NAME] = o.__class__.__name__
        d[M_NAME] = o.__class__.__module__

        return d
