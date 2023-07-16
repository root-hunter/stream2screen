BUILD_DIR = "dist"

TEST_M3U8_URL = "https://vixcloud.co/v2/playlist/124299?type=video&rendition=720p&token=Les0O0Egv7RoPKvrlutuvg&expires=1694711932&canCast=1&n=1"
TEST_KEY_URL = "https://vixcloud.co/storage/enc.key"
TEST_OUTPUT_DIR = ./downloads/griffin
S2S_TEST_COMMAND = s2s -i ${TEST_M3U8_URL} -o ${TEST_OUTPUT_DIR} -k ${TEST_KEY_URL}

build:
	pyinstaller --onefile s2s/__main__.py -n s2s --clean --specpath specs

test-build: build
	./${BUILD_DIR}/${S2S_TEST_COMMAND}
	
test:
	python3 ${S2S_TEST_COMMAND}


