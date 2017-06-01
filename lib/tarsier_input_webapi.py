import tarsier
import json
from typing import Union, List, Any

import requests



def dict2list(d: Union[dict, str]):
    if type(d) != dict:
        return [d]
    l = []
    append = l.append
    extend = l.extend
    for k, v in d.items():
        append(k)
        extend(dict2list(v))
    return l


def get_nest(d: dict, k: List[str]) -> Any:
    for i in k:
        d = d.get(i, {})
    return d


class TarsierInputWebapi(tarsier.TarsierInputPlugin):
    def parse_config(self, config: dict) -> dict:
        config["method"] = config.get("method", "get").lower()
        config["field"] = dict2list(config["field"])
        if "basic_auth" in config:
            config["basic_auth"] = list(config["basic_auth"].items())[0]

        return config

    def init_plugin(self, url: str, method="get", params=None, basic_auth=None, field=None, headers=None):
        self._url = url
        self._method = method
        self._field = field
        self._basic_auth = basic_auth
        self._params = params or {}
        self._headers = headers or {'content-type': 'application/json'}

    def load(self):
        if self._method == "get":
            r = requests.get(self._url, params=self._params, headers=self._headers, auth=self._basic_auth)
        elif self._method == "delete":
            r = requests.delete(self._url, headers=self._headers, auth=self._basic_auth)
        else:
            data = self._params
            if self._headers.get('content-type', '') == 'application/json':
                data = json.dumps(data)
            r = getattr(requests, self._method)(self._url, data=data, headers=self._headers, auth=self._basic_auth)

        if r.status_code < 400:
            # success
            ret = r.json()
            if self._field:
                ret = get_nest(ret, self._field)
            if type(ret) != list:
                ret = [ret]
            return ret
        else:
            return []

