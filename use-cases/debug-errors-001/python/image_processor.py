
# image_processor.py
# Exercise: debug-errors-001
# Fixed by exercise participant:
# - Reduced memory usage by processing images one at a time
# - Avoided storing large image arrays in memory

from PIL import Image
import os
import time

def load_and_process(image_path):
    # Load the image
    img = Image.open(image_path)

    # Simulate processing without creating huge arrays
    img = img.resize((256, 256))
    time.sleep(0.1)  # Simulate processing time

    return img.size


def process_images(image_files):
    results = []

    for image_file in image_files:
        result = load_and_process(image_file)
        results.append(result)

    return results


def main():
    image_directory = "sample_images"
    image_files = [
        os.path.join(image_directory, f)
        for f in os.listdir(image_directory)
        if f.endswith(".jpg")
    ]

    processed_data = process_images(image_files)

    print(f"Processed {len(processed_data)} images successfully")


if __name__ == "__main__":
    main()
