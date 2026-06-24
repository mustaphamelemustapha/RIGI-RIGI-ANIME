# Seed Data for Anime Movie Download Platform

MOCK_MOVIES = [
    {
        "movie_id": 1,
        "title": "Cyber City: 2099",
        "synopsis": "A lone character stands under neon cyan and purple lights in a rainy futuristic alley, dodging cybernetic security patrols.",
        "release_date": "2024-05-12",
        "poster_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuA5OP-PTtW5CRPBaHmVy4ghuRxTYvAn2vZrvhNdRGZxyveXIu9olvfWabzs58gaJd34VXC4YCcojWlSMeM-LwPfT5g-kp1uoYoxfH5GKojSsDmIJJ1a2fq4nfsbPC-TFnq0wS0FnJ-bTrae7ePv7xJ5moZF3-rEOyamxIhBNITNe0A5c_s5a9VjsnSlmu2oupy08nZUjmiLTAuD3aLex1wOSnLIM7Nr7flcUghkyjfQ3BzIYdgGdo7IhyQPoqVPEB3AovOaF-9tW3Ii",
        "genres": ["Cyberpunk", "Sci-Fi", "Action"],
        "rating": 8.9,
        "downloads_count": "1.2k",
        "technical_specs": {
            "file_size": "12.4 GB",
            "audio_tracks": "Japanese (Original TrueHD 7.1), English (DTS-HD)",
            "subtitle_tracks": "English, Spanish, French, German",
            "video_codec": "HEVC x265 (10-bit)",
            "avg_bitrate": "18.5 Mbps",
        },
        "mirrors": [
            {
                "mirror_name": "AnimeCloud Fast",
                "resolution": "2160p (4K)",
                "file_size": "12.4 GB",
                "link_url": "https://animecloud.fast/download/cybercity2160p",
                "video_quality_badge": "Ultra HD",
                "mirror_status": "Online",
                "is_active": True
            },
            {
                "mirror_name": "Vault CDN",
                "resolution": "1080p",
                "file_size": "4.2 GB",
                "link_url": "https://cdn.vault/download/cybercity1080p",
                "video_quality_badge": "Full HD",
                "mirror_status": "Slow",
                "is_active": True
            }
        ]
    },
    {
        "movie_id": 2,
        "title": "Jujutsu Kaisen 0",
        "synopsis": "Yuta Okkotsu, a high schooler who gains control of an extremely powerful cursed spirit, enrolls in Tokyo Prefectural Jujutsu High School.",
        "release_date": "2021-12-24",
        "poster_url": "https://lh3.googleusercontent.com/aida-public/AB6AXuBrsCeLH5ndrgxUz3pOnaj6-Qj8SLG-dhvWcWYtoiNq5UKBDHfqjpZ1kOKu7PIp9ch7Hztbrs3JMU1gAq1X9ZPE9AG3TGJ5hsEXQ3vbMKX9s7omEGiRqOuCBl9lC_tkuJJcoO8hDgkdFb8Caqk1FIbg52RYSUZkjwE-sGMAAj1dETGTOpZ3IzgNc772OgZqI6PNIX7jpkSmgYE3Jv5nnZAAV3IVDncK6d8jNIu6blp5t7IbugU3ILEE3f3vumzOfVDe6GU6VAQJVKRZ",
        "genres": ["Action", "Supernatural", "Fantasy"],
        "rating": 8.9,
        "downloads_count": "3.5k",
        "technical_specs": {
            "file_size": "4.2 GB",
            "audio_tracks": "Japanese (Original), English",
            "subtitle_tracks": "English, Spanish, French",
            "video_codec": "HEVC x265",
            "avg_bitrate": "12.2 Mbps",
        },
        "mirrors": [
            {
                "mirror_name": "Vault CDN",
                "resolution": "1080p",
                "file_size": "4.2 GB",
                "link_url": "https://cdn.vault/download/jjk0_1080p",
                "video_quality_badge": "Full HD",
                "mirror_status": "Slow",
                "is_active": True
            },
            {
                "mirror_name": "Nexus Drive",
                "resolution": "1080p",
                "file_size": "4.2 GB",
                "link_url": "https://nexus.drive/download/jjk0_1080p",
                "video_quality_badge": "Full HD",
                "mirror_status": "Online",
                "is_active": True
            }
        ]
    }
]
