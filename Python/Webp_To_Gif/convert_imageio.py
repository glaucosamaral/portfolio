import os
import imageio
from tqdm import tqdm
import shutil

# Função para converter uma imagem animada .webp para .gif com duração máxima de 10 segundos
def convert_webp_to_gif(image_path, output_path):
    images = imageio.mimread(image_path)
    duration = 0.1  # Duração entre frames, ajustável conforme necessário
    max_duration = 10  # Duração máxima de 10 segundos

    # Calcula o número máximo de frames com base na duração
    max_frames = int(max_duration / duration)

    if len(images) <= max_frames:
        # Se a duração for menor ou igual a 10 segundos, salva sem renomear
        output_file = os.path.join(output_path, f"{os.path.splitext(os.path.basename(image_path))[0]}.gif")
        imageio.mimsave(output_file, images, format='GIF', duration=duration)
    else:
        # Se a duração for maior que 10 segundos, divide em partes
        for i in range(0, len(images), max_frames):
            segment = images[i:i + max_frames]
            output_file = os.path.join(output_path, f"{os.path.splitext(os.path.basename(image_path))[0]}_{i // max_frames + 1}.gif")
            imageio.mimsave(output_file, segment, format='GIF', duration=duration)

# Função para mover arquivos para suas respectivas pastas temáticas em 'converted_files'
def move_file_to_theme_folder(file_path, theme_folder):
    theme_dest_folder = os.path.join(converted_folder, theme_folder)
    os.makedirs(theme_dest_folder, exist_ok=True)  # Cria a pasta do tema se não existir
    shutil.move(file_path, theme_dest_folder)

# Função para limpar as pastas dentro de input_files sem remover as pastas
def clear_input_folders(input_folder):
    for theme_folder in os.listdir(input_folder):
        theme_path = os.path.join(input_folder, theme_folder)
        if os.path.isdir(theme_path):
            for filename in os.listdir(theme_path):
                file_path = os.path.join(theme_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Erro ao apagar o arquivo {file_path}: {e}")

# Pastas principais
input_folder = "input_files"
output_folder = "output_files"
converted_folder = "converted_files"

# Verifica e cria as pastas de saída, se não existirem
os.makedirs(output_folder, exist_ok=True)
os.makedirs(converted_folder, exist_ok=True)

# Processa os arquivos .webp nas subpastas temáticas
for theme_folder in tqdm(os.listdir(input_folder), desc="Verificando pastas temáticas"):
    theme_path = os.path.join(input_folder, theme_folder)
    
    if os.path.isdir(theme_path):  # Verifica se é uma subpasta
        # Cria uma pasta correspondente em output_files
        output_theme_folder = os.path.join(output_folder, theme_folder)
        os.makedirs(output_theme_folder, exist_ok=True)
        
        for filename in tqdm(os.listdir(theme_path), desc=f"Convertendo arquivos da pasta {theme_folder}"):
            file_path = os.path.join(theme_path, filename)
            
            try:
                if filename.lower().endswith('.webp'):
                    convert_webp_to_gif(file_path, output_theme_folder)
                    move_file_to_theme_folder(file_path, theme_folder)
                else:
                    print(f"Formato de arquivo não suportado: {filename}")
            
            except Exception as e:
                print(f"Falha na conversão do arquivo {filename}: {e}")

# Após a conversão, limpar as pastas em input_files sem removê-las
clear_input_folders(input_folder)

print("Conversão e limpeza concluídas.")