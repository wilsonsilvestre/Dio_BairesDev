from PIL import Image

# Carregar a imagem
imagem = Image.open("C:\Users\teste.jpg")

# Converter para níveis de cinza
imagem_cinza = imagem.convert('L')

# Salvar a imagem convertida
imagem_cinza.save('imagem_cinza.jpg')
