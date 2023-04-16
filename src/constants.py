# -*- coding: utf-8 -*-
# Author: Aethlios <tom.chambaretaud@protonmail.com>.

ASCII_ART = """\033[01;31m██╗   ██╗██╗    ██╗██╗  ██╗       ██████╗ ██████╗ ██╗     ██╗      █████╗ ██████╗ 
╚██╗ ██╔╝██║    ██║██║  ██║      ██╔════╝██╔═══██╗██║     ██║     ██╔══██╗██╔══██╗
 ╚████╔╝ ██║ █╗ ██║███████║█████╗██║     ██║   ██║██║     ██║     ███████║██████╔╝
  ╚██╔╝  ██║███╗██║██╔══██║╚════╝██║     ██║   ██║██║     ██║     ██╔══██║██╔══██╗
   ██║   ╚███╔███╔╝██║  ██║      ╚██████╗╚██████╔╝███████╗███████╗██║  ██║██████╔╝
   ╚═╝    ╚══╝╚══╝ ╚═╝  ╚═╝       ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝                                                                                  
\033[00m"""

DESCRIPTION = "Yes We Hack private program comparator for hunters collaboration by Aethlios."
WARNING = "\033[01;31m[!] Please note that if you share the list of anonymized programs publicly, it will be possible for all other members of the program to know that you are also invited!\033[00m"

ACTION_EXPORT = "export"
ACTION_COMPARE = "compare"

YWH_URL = "https://api.yeswehack.com"
YWH_PROGRAMS_PATH = "/programs"
YWH_CHECK_PATH = "/user"
YWH_LOGIN_PATH = "/login"
YWH_TOTP_PATH = "/account/totp"

PAGE_PARAMETER = "page"
TOTP_TOKEN_PARAMETER = "token"
TOTP_CODE_PARAMETER = "code"
PID_FIELD = "pid"
PROGRAM_SLUG_FIELD = "slug"
PROGRAMS_FIELD = "items"
PAGINATION_FIELD = "pagination"
PAGES_FIELD = "nb_pages"
JWT_FIELD = "token"
TOTP_FIELD = "totp_token"

UNAUTHENTICATED_STATUS_CODE = 401
