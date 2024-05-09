import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from pdf_merger import merge_images_to_pdf
import config

def download_images_from_url(url, output_folder):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    div_found = False
    image_files = []

    for i in range(1, 51):
        page_id = f"page{i}"
        while True:
            page_div = soup.find("div", {"id": page_id})
            if page_div:
                div_found = True
                break
            else:
                time.sleep(5)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                if time.time() - start_time > 15:
                    print("Extração concluída. A div não foi encontrada.")
                    driver.quit()
                    return

        img_tags = page_div.find_all("img")
        for img_tag in img_tags:
            while True:
                img_url_src = img_tag.get('src')
                img_url_data_src = img_tag.get('data-src')
                if img_url_src and img_url_src != "about:blank":
                    img_url = img_url_src
                elif img_url_data_src and img_url_data_src != "about:blank":
                    img_url = img_url_data_src
                else:
                    img_url = None

                if img_url:
                    img_response = requests.get(img_url)
                    if img_response.status_code == 200:
                        img_name = f"{page_id}_image_{img_tags.index(img_tag) + 1}.jpg"
                        img_path = os.path.join(output_folder, img_name)
                        with open(img_path, 'wb') as img_file:
                            img_file.write(img_response.content)
                            print(f"Imagem {img_name} baixada com sucesso.")
                        image_files.append(img_path)
                        break
                    else:
                        print(f"Falha ao baixar a imagem {img_url} da div {page_id}")
                else:
                    print(f"Imagem em branco ou sem atributo 'src' ou 'data-src' encontrada na div {page_id}. Esperando 5 segundos e tentando novamente.")
                    time.sleep(5)
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')

    if not div_found:
        print("Extração concluída. A div não foi encontrada.")

    driver.quit()
    return image_files

def delete_files_in_folder(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Arquivo {file_path} excluído com sucesso.")
        except Exception as e:
            print(f"Falha ao excluir o arquivo {file_path}: {e}")

def check_and_rename_pdf(pdf_path, chapter_number):
    if os.path.exists(pdf_path):
        file_name, extension = os.path.splitext(pdf_path)
        index = 1
        while True:
            new_pdf_path = f"{file_name}_{chapter_number}_{index}{extension}"
            if not os.path.exists(new_pdf_path):
                return new_pdf_path
            index += 1
    return pdf_path

if __name__ == "__main__":
    start_time = time.time()

    for i in range(config.QUANTIDADE_CAPITULOS):
        url = f"{config.MANGA_URL}/c{config.CHAPTER_NUMBER + i}"
        output_folder = config.IMAGE_DIRECTORY

        try:
            image_files = download_images_from_url(url, output_folder)
            manga_name = config.MANGA_NAME
            pdf_output_path = check_and_rename_pdf(
                os.path.join(config.OUTPUT_DIRECTORY, f"{manga_name}_c{config.CHAPTER_NUMBER + i}.pdf"),
                config.CHAPTER_NUMBER + i
            )
            merge_images_to_pdf(output_folder, pdf_output_path)
            delete_files_in_folder(output_folder)
        except Exception as e:
            print(f"Erro durante a execução: {e}")
