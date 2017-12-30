# -* encoding: utf-8 *-
import logging
from typing import Optional, NamedTuple

_log = logging.getLogger(__name__)


class ErrorMessage(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


CertContents = NamedTuple(
    'CertContents', [
    ("countryName", str),
    ("localityName", str),
    ("organizationName", str),
    ("organizationalUnitName", str),
    ("commonName", str),
    ("emailAddress", str),
    ("title", str),
    ("unstructuredName", str),
])


class CA:
    def __init__(self, name, pathlen: Optional[int]=None, parent: 'CA'=None) -> None:
        self.name = name
        self.pathlen = pathlen
        self.parent = parent
        if pathlen is None and parent is not None:
            if parent.pathlen is not None:
                if parent.pathlen > 0:
                    self.pathlen = parent.pathlen - 1
                    _log.info("[%s] Selected pathlen from parent \"%s\". pathlen=%s", self.name, parent.name,
                              self.pathlen)
                else:
                    raise ErrorMessage("[%s] Parent %s has pathlen == 0.", self.name, parent.name)

    def create(self) -> str:
        pass

    def issue(self, contents: CertContents) -> str:
        pass
