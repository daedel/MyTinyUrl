from django.shortcuts import redirect
from MyTinyUrl.settings import CONFIG


def ensure_https_prefix(url: str) -> str:
    if not url.startswith('http'):
        url = f'https://{url}'
    return url


def redirect_to_url(url: str):
    url = ensure_https_prefix(url)
    return redirect(url)


def generate_url_for_redirection(code: str) -> str:
    return f"{CONFIG.HOST} / {code}"
