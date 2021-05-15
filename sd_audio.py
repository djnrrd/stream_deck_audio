import argparse
from pydub import AudioSegment
from pydub.playback import play


def add_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', choices=['crumbs', 'deejay', 'dr_who',
                                         'fanceee', 'victory',
                                         'glitter_attack', 'horny_jail',
                                         'i_alone', 'princess', 'taps',
                                         'that_doesnt', 'yikes_forever'])
    return parser


def play_file(file_name):
    mp3_path = f"res/{file_name}.mp3"
    file_sound = AudioSegment.from_mp3(mp3_path)
    file_sound = file_sound
    play(file_sound)


def main():
    parser = add_args()
    arg = parser.parse_args()
    play_file(arg.file)


if __name__ == '__main__':
    main()
