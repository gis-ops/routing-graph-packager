import json

from .router_base import RouterBase


class Valhalla(RouterBase):
    """Valhalla implementation"""
    def name(self):
        return 'valhalla'

    def build_graph(self):
        config = {"mjolnir": {"tile_dir": self._docker_graph_dir}}

        cmd = f"valhalla_build_tiles --inline-config '{json.dumps(config)}'" \
              f" {self._docker_pbf_path}"
        return self._exec_docker(cmd)