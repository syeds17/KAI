from pathlib import Path

HOME = Path.home()

FOLDERS = {
    "downloads": {
        "name": "Downloads",
        "path": str(HOME / "Downloads"),
        "aliases": ["downloads", "download"]
    },

    "documents": {
        "name": "Documents",
        "path": str(HOME / "Documents"),
        "aliases": ["documents", "document"]
    },

    "desktop": {
        "name": "Desktop",
        "path": str(HOME / "Desktop"),
        "aliases": ["desktop"]
    },

    "pictures": {
        "name": "Pictures",
        "path": str(HOME / "Pictures"),
        "aliases": ["pictures", "photos"]
    },

    "videos": {
        "name": "Videos",
        "path": str(HOME / "Videos"),
        "aliases": ["videos", "video"]
    },

    "music": {
        "name": "Music",
        "path": str(HOME / "Music"),
        "aliases": ["music", "songs"]
    }
}