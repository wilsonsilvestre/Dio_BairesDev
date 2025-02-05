from PIL import Image

# Carregar a imagem
imagem = Image.open('C:\Users\teste.jpg')

# Converter para níveis de cinza
imagem_cinza = imagem.convert('L')

# Definir um limite para a binarização
limite = 128

# Aplicar a binarização
imagem_binaria = imagem_cinza.point(lambda p: 255 if p > limite else 0)

# Salvar a imagem convertida
imagem_binaria.save('imagem_binaria.jpg')
