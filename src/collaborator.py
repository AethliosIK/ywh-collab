# -*- coding: utf-8 -*-
# Author: Aethlios <tom.chambaretaud@protonmail.com>.

import requests

from src.constants import (
    YWH_URL,
    YWH_PROGRAMS_PATH,
    YWH_CHECK_PATH,
    YWH_LOGIN_PATH,
    YWH_TOTP_PATH,
    PAGE_PARAMETER,
    TOTP_TOKEN_PARAMETER,
    TOTP_CODE_PARAMETER,
    PID_FIELD,
    PROGRAM_SLUG_FIELD,
    PROGRAMS_FIELD,
    PAGINATION_FIELD,
    PAGES_FIELD,
    JWT_FIELD,
    TOTP_FIELD,
    UNAUTHENTICATED_STATUS_CODE,
)


class AuthenticationFail(Exception):
    pass


def extract_pid_from_programs(j: dict) -> dict:
    program_pids = {}
    for e in j[PROGRAMS_FIELD]:
        if PID_FIELD in e and e[PID_FIELD]:
            program_pids.update({e[PID_FIELD]: e[PROGRAM_SLUG_FIELD]})
    return program_pids


class YWHCollaborator:
    def __init__(self, jwt: str = None) -> None:
        self.program_pids = {}
        if jwt and not self.check_jwt(jwt):
            raise AuthenticationFail("Not logged")
        self.jwt = jwt

    @staticmethod
    def check_jwt(jwt: str) -> bool:
        r = requests.get(
            YWH_URL + YWH_CHECK_PATH,
            headers={"Authorization": f"Bearer {jwt}"},
        )
        return r and r.ok

    def login(self, email: str, password: str) -> str:
        r = requests.post(
            YWH_URL + YWH_LOGIN_PATH, json={"email": email, "password": password}
        )
        if r and r.ok and JWT_FIELD in r.json():
            self.jwt = r.json()[JWT_FIELD]
            return None
        if r and r.ok and TOTP_FIELD in r.json():
            return r.json()[TOTP_FIELD]
        raise AuthenticationFail("Invalid password")

    def login_totp(self, token: str, code: str) -> None:
        r = requests.post(
            YWH_URL + YWH_TOTP_PATH,
            json={TOTP_CODE_PARAMETER: code, TOTP_TOKEN_PARAMETER: token},
        )
        if not r or not r.ok:
            raise AuthenticationFail("Totp invalid")
        self.jwt = r.json()[JWT_FIELD]

    def get_programs_from_api(self, page: int = 1) -> dict:
        r = requests.get(
            YWH_URL + YWH_PROGRAMS_PATH,
            params={PAGE_PARAMETER: page},
            headers={"Authorization": f"Bearer {self.jwt}"},
        )
        if r and r.ok:
            return r.json()
        if r.status_code == UNAUTHENTICATED_STATUS_CODE:
            raise AuthenticationFail("JWT expired")
        return None

    def get_program_pids(self) -> dict:
        if len(self.program_pids) != 0:
            return self.program_pids

        j = self.get_programs_from_api()
        if not j:
            return {}
        self.program_pids.update(extract_pid_from_programs(j))

        l = j[PAGINATION_FIELD][PAGES_FIELD]
        for page in range(2, l + 1):
            j = self.get_programs_from_api(page=page)
            if not j:
                return self.program_pids
            self.program_pids.update(extract_pid_from_programs(j))

        return self.program_pids

    def extract_pids(self) -> list:
        program_pids = self.get_program_pids()
        if not program_pids:
            return []
        return program_pids.keys()

    def get_program_by_pid(self, pid: str) -> str:
        program_pids = self.get_program_pids()
        if pid in program_pids:
            return program_pids[pid]
        return None

    def compare(self, filename: str) -> list:
        with open(filename, "r") as f:
            for l in f.readlines():
                pid = l[:-1]
                program = self.get_program_by_pid(pid)
                if program:
                    yield program

    def export(self, filename: str) -> int:
        programs = self.extract_pids()
        with open(filename, "w") as f:
            for program in programs:
                f.write(f"{program}\n")
        return len(programs)
