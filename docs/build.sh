#!/usr/bin/env bash

echo "[o] Started to build docs..."
pandoc ./src/API_CHEATSHEET.md -o ./pdf/API.pdf
echo "[:)] Done building pdfs, see them in ./pdf"
pandoc ./src/API_CHEATSHEET.md -o ./html/API.html
echo "[:)] Done building html, see them in ./html"
