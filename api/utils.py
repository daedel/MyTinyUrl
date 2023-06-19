from django.shortcuts import redirect


def ensure_https_prefix(url: str) -> str:
    if not url.startswith('http'):
        url = f'https://{url}'
    return url


def redirect_to_url(url: str):
    url = ensure_https_prefix(url)
    return redirect(url)
