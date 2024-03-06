.PHONY: build run
.SILENT:

build:
	pyinstaller --onefile main.py --distpath ./build/app

run: build
	./build/app/main
