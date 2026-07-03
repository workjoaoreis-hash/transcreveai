#!/bin/bash

set -e

echo "🧹 Limpando builds antigos..."
rm -rf build dist *.spec

echo "📦 Gerando TranscreveAI.app..."
pyinstaller \
  --windowed \
  --name TranscreveAI \
  main.py

echo "✅ App criado em:"
echo "dist/TranscreveAI.app"

