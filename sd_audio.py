import argparse
from pydub import AudioSegment
from pydub.playback import play
import os
import random


def add_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        choices=[
            "crumbs",
            "deejay",
            "dr_who",
            "fanceee",
            "victory",
            "glitter_attack",
            "horny_jail",
            "a_chicken",
            "princess",
            "f",
            "that_doesnt",
            "yikes_forever",
            "wrestling",
        ],
    )
    return parser


def get_random_file(file_path):
    base_path = os.path.dirname(__file__)
    print(base_path)
    dir_files = os.listdir(f"{base_path}/res/{file_path}")
    ret_file = random.choice(dir_files)[:-4]
    return f"{file_path}/{ret_file}"


def play_file(file_name):
    if file_name == "wrestling":
        if random.randint(1, 141) == 1:
            file_name = f"wrestling/steiner_maths/steiner_maths"
        else:
            file_name = get_random_file(file_name)
    if file_name in ("wrestling", "dr_who"):
        file_name = get_random_file(file_name)
    if file_name == "deejay":
        if random.randint(1, 5) == 1:
            file_name = "fucks_sake_dj"
        else:
            file_name = "deejay2"
    base_path = os.path.dirname(__file__)
    mp3_path = f"{base_path}/res/{file_name}.mp3"
    file_sound = AudioSegment.from_mp3(mp3_path)
    file_sound = file_sound
    play(file_sound)


def main():
    parser = add_args()
    arg = parser.parse_args()
    play_file(arg.file)


if __name__ == "__main__":
    main()
