import os
import subprocess
import threading
from Crypto.Cipher import AES
from .utils import divide_chunks, get_binary, get_key

def decrypt_ts(data, key, iv):
    # Decrypts TS data using AES encryption
    decryptor = AES.new(key, AES.MODE_CBC, IV=iv)
    return decryptor.decrypt(data)


def convert_ts(args, output_folder, output_ts_path, output_mp4_path):
    log_file_path = os.path.join(output_folder, "convert.log")

    ffmpeg_command = [
        "ffmpeg",
        "-hwaccel",
        args.hwaccel,
        # "-threads", "32",
        "-i",
        output_ts_path,
        "-c:v",
        args.codec,
        output_mp4_path,
    ]
    with open(log_file_path, "w") as log_out:
        # Run ffmpeg command to convert TS to MP4
        result = subprocess.run(ffmpeg_command, stdout=log_out, text=True)
        print("Result code: {}".format(result))
    log_out.close()
    os.remove(output_ts_path)


def compact_ts(ts_files, output_file_path):
    with open(output_file_path, "wb") as output:
        for ts_file_path in ts_files:
            # Concatenate TS files into a single output file
            # print(ts_file_path)
            ts_file = open(ts_file_path, "rb")
            ts_data = ts_file.read()

            output.write(ts_data)

            ts_file.close()
            os.remove(ts_file_path)
    output.close()


def dowload_ts(args, key_path, output_folder, iv_val, urls):
    for url in urls:
        file_name = os.path.basename(url).split("?")[0]
        print('Downloading "%s"' % file_name)
        enc_data = get_binary(url)

        iv = None
        key_data = None

        if iv_val != None:
            key_data = get_key(key_path)
            if key_path["type"] == 'url' and args.save_key == True:
                key_file_path = os.path.join(output_folder, "enc.key")
                with open(key_file_path, "wb") as f:
                    f.write(key_data)
                    f.close()
            iv = bytes.fromhex(iv_val)

        out_file = os.path.join(output_folder, "%s" % file_name)
        with open(out_file, "wb") as output:
            if iv != None and key_data != None:
                dec_data = decrypt_ts(enc_data, key_data, iv)
                output.write(dec_data)
            else:
                output.write(enc_data)


def dowload_ts_playlist(args, key_path, output_folder, iv_val, urls):
    n = len(urls) // args.dthreads
    ds = divide_chunks(urls, n)

    threads = []

    for chunk in ds:
        thread = threading.Thread(
            target=dowload_ts, args=(args, key_path, output_folder, iv_val, chunk)
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()