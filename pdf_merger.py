import os

from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def merge_images_to_pdf(image_folder, pdf_output_path):
    image_files = sorted([os.path.join(image_folder, file) for file in os.listdir(image_folder) if
                          file.endswith(('.jpg', '.jpeg', '.png'))], key=lambda x: int(''.join(filter(str.isdigit, x))))

    if not image_files:
        print(f"Nenhuma imagem encontrada no diretório '{image_folder}'.")
        return

    c = canvas.Canvas(pdf_output_path, pagesize=letter)
    page_width, page_height = letter

    for image_file in image_files:
        image = Image.open(image_file)
        img_width, img_height = image.size
        scale_x = page_width / img_width
        scale_y = page_height / img_height
        scale = min(scale_x, scale_y)
        new_width = img_width * scale
        new_height = img_height * scale
        x_offset = (page_width - new_width) / 2
        y_offset = (page_height - new_height) / 2
        c.drawImage(image_file, x_offset, y_offset, width=new_width, height=new_height)
        c.showPage()

    c.save()

    print(f"PDF criado com sucesso em '{pdf_output_path}'.")
