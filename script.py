import os
import shutil
import yaml
import markdown
from bs4 import BeautifulSoup

def read_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        frontmatter = []
        in_frontmatter = False

        for line in lines:
            if line.strip() == '---':
                if in_frontmatter:
                    break
                in_frontmatter = True
            elif in_frontmatter:
                frontmatter.append(line)

        if frontmatter:
            return yaml.safe_load(''.join(frontmatter))
        return {}

def copy_files_with_tag(source_dir, target_dir, tag):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                frontmatter = read_frontmatter(file_path)
                if frontmatter and 'tags' in frontmatter:
                    tags = frontmatter['tags']
                    if isinstance(tags, list) and tag in tags:
                        shutil.copy(file_path, os.path.join(target_dir, file))
                        print(f"Copied: {file_path} to {target_dir}")
                    elif isinstance(tags, str) and tags == tag:
                        shutil.copy(file_path, os.path.join(target_dir, file))
                        print(f"Copied: {file_path} to {target_dir}")

def send_images_folder(md_source_dir, img_source_dir, img_target_dir):
    if not os.path.exists(img_target_dir):
        os.makedirs(img_target_dir)

    image_files = set()

    for root, _, files in os.walk(md_source_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    html = markdown.markdown(f.read())
                soup = BeautifulSoup(html, 'html.parser')
                for img_tag in soup.find_all('img'):
                    img_src = img_tag.get('src')
                    if img_src:
                        # Handle relative paths
                        img_path = os.path.join(root, img_src)
                        if os.path.exists(img_path):
                            image_files.add(img_path)
                        else:
                            # Try to find the image in the img_source_dir
                            img_path = os.path.join(img_source_dir, img_src)
                            if os.path.exists(img_path):
                                image_files.add(img_path)
                            else:
                                print(f"Warning: Image not found {img_path}")

    print("Image files found:", image_files)
    return image_files

def copy_images(image_files, img_target_dir):
    for img_file in image_files:
        if os.path.exists(img_file):
            shutil.copy(img_file, os.path.join(img_target_dir, os.path.basename(img_file)))
            print(f"Copied: {img_file} to {img_target_dir}")
        else:
            print(f"Warning: Image file does not exist {img_file}")

if __name__ == "__main__":
    source_directory = 'input'
    target_directory = 'output'
    tag_to_check = 'données_recherche'
    img_source_directory = 'input/images'
    img_target_directory = 'output/images'

    copy_files_with_tag(source_directory, target_directory, tag_to_check)

    image_files = send_images_folder(source_directory, img_source_directory, img_target_directory)
    copy_images(image_files, img_target_directory)

