#!/bin/bash

# Define the URL and output file

URL="https://zenodo.org/records/14655645/files/tsrepair.zip?download=1"
OUTPUT_ZIP="tsrepair_datasets.zip"
BASE_DIR="repair/data"
OUTPUT_DIR="$BASE_DIR/test/"

# Download the ZIP file
echo "Downloading the ZIP file from $URL..."
wget -O "$OUTPUT_ZIP" "$URL"

# Check if the download was successful
if [ $? -eq 0 ]; then
    echo "Download successful. File saved as $OUTPUT_ZIP."
else
    echo "Failed to download the file. Exiting."
    exit 1
fi

# Create output directories if they don't exist
if [ ! -d "$BASE_DIR" ]; then
    mkdir -p "$BASE_DIR"
    echo "Created base directory: $BASE_DIR"
fi

if [ ! -d "$OUTPUT_DIR" ]; then
    mkdir -p "$OUTPUT_DIR"
    echo "Created directory: $OUTPUT_DIR"
fi

# Decompress the ZIP file
echo "Decompressing $OUTPUT_ZIP into $OUTPUT_DIR..."
unzip -q "$OUTPUT_ZIP" -d "$OUTPUT_DIR"

# Check if the decompression was successful
if [ $? -eq 0 ]; then
    echo "Decompression successful. Files extracted to $OUTPUT_DIR."
else
    echo "Failed to decompress the ZIP file. Exiting."
    exit 1
fi

# Optional: Clean up the ZIP file after decompression
echo "Cleaning up..."
rm "$OUTPUT_ZIP"
echo "Temporary ZIP file removed."

echo "All tasks completed successfully!"
