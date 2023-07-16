import argparse
import os


def get_args():
    parser = argparse.ArgumentParser(
        description="Download .ts file from m3u8 file and export to video with ffmpeg."
    )

    parser.usage = "python3 download.py -i ./griffin.m3u8 -o ./griffin_mp4 -k ./enc.key"

    parser.add_argument(
        "-i", "--input", help="Input m3u8 file/URL", required=True, type=str
    )
    parser.add_argument(
        "-o", "--output-dir", help="Output dir", required=True, type=str
    )
    parser.add_argument(
        "-ha",
        "--hwaccel",
        help="ffmpeg hardware acceleration setting",
        default="auto",
        type=str,
    )

    parser.add_argument(
        "-dT",
        "--dthreads",
        help="Number of threads for parallel dowloads",
        type=int,
        default=os.cpu_count(),
    )
    parser.add_argument("-k", "--key", help="Encryption key file/URL", type=str)
    parser.add_argument(
        "-c", "--codec", help="Output ffmpeg video codec", type=str, default="libx264"
    )

    parser.add_argument(
        "-sM", "--save-m3u8", help="Save m3u8 file if download it from URL", 
        type=bool, default=False
    )

    parser.add_argument(
        "-sK", "--save-key", help="Save key file if download it from URL",
        type=bool, default=False
    )

    args = parser.parse_args()
    print(args.save_m3u8)

    return args
