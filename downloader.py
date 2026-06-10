import re
import time
import instaloader

from utils import (
    load_completed,
    save_completed,
    save_failed
)

L = instaloader.Instaloader(
    download_videos=True,
    download_video_thumbnails=False,
    download_geotags=False,
    download_comments=False,
    save_metadata=False,
    post_metadata_txt_pattern=""
)

completed = load_completed()

with open("urls.txt", "r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

total = len(urls)

for index, url in enumerate(urls, start=1):

    if url in completed:
        continue

    try:

        print(f"[{index}/{total}] Processing")

        shortcode = re.search(
            r"/(?:reel|p)/([^/]+)/",
            url
        ).group(1)

        post = instaloader.Post.from_shortcode(
            L.context,
            shortcode
        )

        L.download_post(
            post,
            target="instagram_bulk"
        )

        save_completed(url)

        print(
            f"[{index}/{total}] Downloaded"
        )

        time.sleep(5)

    except Exception as e:

        print(
            f"[{index}/{total}] Failed"
        )

        print(e)

        save_failed(url)

        if "429" in str(e):
            print(
                "Rate limit detected. Sleeping for 1 hour."
            )
            time.sleep(3600)
        else:
            time.sleep(10)

print("Download Process Complete")
