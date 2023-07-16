import glob
import os
import re
from .ts import compact_ts, convert_ts, dowload_ts_playlist
from .utils import get_m3u8, parse_string, sort_array_by_other

REG_SUB = "#[a-zA-Z:\-0-9.,]*(\n){0,1}"
REG_X_KEY = '#EXT-X-KEY:METHOD=AES-128,URI="(.*)",IV=(.*)\s.*\s(.*)\n'

async def start(args, m3u8_url, key_url, output_folder):
    iv_val = None
    m3u8_url = parse_string(m3u8_url)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)

    data = get_m3u8(m3u8_url)

    if m3u8_url["type"] == "url" and args.save_m3u8 == True:
        m3u8_file_path = os.path.join(output_folder, "playlist.m3u8")

        with open(m3u8_file_path, "w") as f:
            f.write(data)

    if key_url != None:
        data_split = re.findall(REG_X_KEY, data)[0]
        iv_val = data_split[1][2:]
        key_url = parse_string(key_url)

    urls = re.sub(REG_SUB, "", data)
    urls = [url for url in urls.split("\n") if re.match('((https)||(http)):.*', url)]

    print(iv_val)
#    with Progress() as progress:
#        task1 = progress.add_task("[red]Downloading...", total=len(urls))

    dowload_ts_playlist(args, key_url, output_folder, iv_val, urls)
    print("Success downloading playlist")

    ts_files = glob.glob("{}/*.ts".format(output_folder))
    output_ts_path = os.path.join(output_folder, "output.ts")
    output_mp4_path = output_ts_path.replace(".ts", ".mp4")

    ts_indexs = [os.path.basename(ts).split("-")[0] for ts in ts_files]
    print(ts_indexs)

    ts_files = sort_array_by_other(ts_files, ts_indexs)
    compact_ts(ts_files, output_ts_path)
    convert_ts(args, output_folder, output_ts_path, output_mp4_path)
