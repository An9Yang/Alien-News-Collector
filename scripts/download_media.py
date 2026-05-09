#!/usr/bin/env python3
"""Download a remote image/media file and save it with a sensible extension.

Usage:
    python3 scripts/download_media.py <url> <dest_path_without_ext>

The extension is chosen from the response Content-Type, falling back to the
URL suffix. Prints the final saved path on stdout, or an error line starting
with "ERROR:" on stderr (and exits non-zero) so the calling Routine can keep
going without aborting the whole run.
"""

from __future__ import annotations

import mimetypes
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = (
    "Mozilla/5.0 (compatible; AlienNewsCollector/1.0; "
    "+https://github.com/An9Yang/Alien-News-Collector)"
)

# Content-Type -> extension overrides where mimetypes is unhelpful.
EXT_OVERRIDES = {
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/svg+xml": ".svg",
    "image/avif": ".avif",
    "video/mp4": ".mp4",
    "video/webm": ".webm",
    "audio/mpeg": ".mp3",
}


def pick_extension(content_type: str | None, url: str) -> str:
    if content_type:
        primary = content_type.split(";", 1)[0].strip().lower()
        if primary in EXT_OVERRIDES:
            return EXT_OVERRIDES[primary]
        guessed = mimetypes.guess_extension(primary)
        if guessed:
            return guessed
    # Fall back to URL suffix.
    path = urllib.parse.urlparse(url).path
    _, ext = os.path.splitext(path)
    if ext and len(ext) <= 6:
        return ext.lower()
    return ".bin"


def download(url: str, dest_no_ext: str, timeout: float = 30.0) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        ext = pick_extension(resp.headers.get("Content-Type"), url)
        dest = dest_no_ext + ext
        os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
        with open(dest, "wb") as out:
            while True:
                chunk = resp.read(64 * 1024)
                if not chunk:
                    break
                out.write(chunk)
        return dest


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        sys.stderr.write(
            "usage: download_media.py <url> <dest_path_without_ext>\n"
        )
        return 2
    url, dest_no_ext = argv[1], argv[2]
    try:
        path = download(url, dest_no_ext)
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as e:
        sys.stderr.write(f"ERROR: download failed for {url}: {e}\n")
        return 1
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
