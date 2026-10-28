
import json

from sdc.tile import Tile


def write_sdc_tileset(path: str, tileset: dict) -> None:
    with open(path, "w") as f:
        json.dump(tileset, f, indent = 4, cls = TileEncoder)

def read_sdc_tileset(path: str) -> dict:
    with open(path, "r") as f:
        loaded = json.load(f, object_hook = sdc_decoder)

    return {int(key): loaded[key] for key in loaded.keys()}



def sdc_decoder(obj):
    if "__classname__" in obj:
        if obj["__classname__"] == "Tile":
            obj.pop("__classname__")
            if "layout" in obj:
                obj["layout"] = tuple(obj["layout"])
            return Tile(**obj)
    return obj



class TileEncoder(json.JSONEncoder):

    def default(self, o):
        d = dict(o.__dict__)
        for k in o.__dict__.keys():
            if k.startswith("_"):
                d.pop(k)
        d["__classname__"] = "Tile"
        return d
