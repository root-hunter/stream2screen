# Stream2Screen (s2s)
Stream2Screen (s2s) is a Python library that allows you to download and process .ts MPEG files and .m3u8 playlists. It provides functionality to handle encrypted .ts files using AES encryption. With this library, you can easily download all associated .ts files from a given link or .m3u8 file, merge them, and export them as a single video using FFmpeg.

## Usage Example
1) Install ffmpeg -> (https://ffmpeg.org/)
2) Install Python -> (https://python.org/)
3) Install Python Dependencies
```
pip install -r requirements.txt
```
4a) Build s2s to executable
```
make build
```
4b) Build + Test build (Optional)
```
make test-build
```
5) Use it and enjoy! ;)
```
./s2s -i (M3U8 FILE_PATH/URL) -o (OUTPUT_DIR_PATH) -k [DECRYPT_KEY FILE_PATH/URL (Optional)] 
```

# Download Any Content Using .m3u8
Stream2Screen (s2s) provides a powerful feature that enables you to download virtually any content that utilizes .m3u8 playlists, even if it is typically behind a paywall or requires a subscription. By leveraging the functionality of s2s, you can access and download the media files associated with the .m3u8 playlist.

With s2s, you can bypass restrictions and limitations, allowing you to download content such as live streams, TV shows, movies, and more. By providing the link to the .m3u8 playlist, s2s will download all the associated .ts files and merge them seamlessly, creating a complete video file that you can save and enjoy offline.

Please note that it is essential to respect copyright laws and the terms of service of the content providers. Make sure you have the necessary rights and permissions to download and use the content. Stream2Screen (s2s) is designed to provide a convenient way to handle and process media files within the boundaries of legal and authorized usage.

Always use s2s responsibly and in compliance with applicable laws and regulations.

## What are .ts MPEG Files?

.ts files, also known as MPEG transport stream files, are a container format used for storing and transmitting audio, video, and other data. They are commonly used for streaming media content over the internet. Each .ts file contains a small segment of the audio or video stream.

## Naming Convention for .ts Files
Stream2Screen (s2s) currently assumes that the .ts files associated with the content follow a specific naming convention. Each .ts file is expected to be named in the format XXXX-YYYY.ts, where X represents the sequence number, and YYYY represents the count or quantity of frames within each .ts file.

The sequence number (XXXX) indicates the order in which the .ts files should be merged, ensuring that they are combined in the correct sequence. The frame count (YYYY) represents the total number of frames contained within each .ts file.

This naming convention allows s2s to accurately identify and merge the .ts files in the correct order, ensuring a seamless and complete video output. It's important to note that if your .ts files do not follow this naming convention, you may need to modify the code in Stream2Screen (s2s) accordingly to accommodate your specific file naming scheme.

As the project evolves, future versions of Stream2Screen (s2s) may include additional flexibility in handling file naming conventions, providing more customization options to support different naming schemes.
## What are .m3u8 Playlists?

.m3u8 is a file format used for playlists in HTTP Live Streaming (HLS). It is an adaptive streaming protocol that breaks the media content into smaller chunks, typically in .ts format. The .m3u8 playlist file contains a list of URLs pointing to the individual .ts files.

## AES-Encrypted .ts Files

AES encryption is a common method used to protect media content. Some .ts files may be encrypted with AES for security reasons. Stream2Screen (s2s) provides functionality to handle AES-encrypted .ts files, allowing you to decrypt and process them seamlessly.

## Library Features

- Download and process .ts MPEG files and .m3u8 playlists
- Support for AES-encrypted .ts files
- Seamless merging of downloaded .ts files
- Export merged files as a single video using FFmpeg
