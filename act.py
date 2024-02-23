import xml.etree.ElementTree as ET
import os
from PIL import Image

# Путь к XML-файлу
xml_file = 'annotations.xml'
# Путь к папке с фотографиями
photos_folder = 'photos'

# Парсим XML-файл
tree = ET.parse(xml_file)
root = tree.getroot()

# Проходим по всем элементам image
for image in root.findall('image'):
    image_name = image.get('name')
    image_path = os.path.join(photos_folder, image_name)

    # Если фото найдено
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.convert('RGB')

        # Проходим по всем элементам box
        for box in image.findall('box'):
            label = box.get('label')
            xtl = float(box.get('xtl'))
            ytl = float(box.get('ytl'))
            xbr = float(box.get('xbr'))
            ybr = float(box.get('ybr'))

            # Вырезаем и сохраняем изображение
            box_img = img.crop((xtl, ytl, xbr, ybr))
            save_path = os.path.join('output', label)
            os.makedirs(save_path, exist_ok=True)
            box_img.save(os.path.join(save_path, f'{label}_{image_name.replace(".jpg", "")}.jpg'))

print('Вырезанные изображения сохранены успешно.')