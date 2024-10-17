from PIL import Image, ImageDraw, ImageFont

# Definições iniciais
largura, altura = 1280, 640
fundo_cor = (255, 240, 245)  # Cor de fundo rosa claro
texto_cor = (0, 0, 0)  # Cor do texto: preto
logo_cor = (0, 0, 0)  # Cor da logo GitHub: preto

# Cria a imagem
imagem = Image.new('RGB', (largura, altura), fundo_cor)
draw = ImageDraw.Draw(imagem)

# Fonte do texto (Você deve ter essa fonte em seu sistema ou mudar para uma disponível)
try:
    fonte = ImageFont.truetype("arial.ttf", 80)
except IOError:
    fonte = ImageFont.load_default()

# Texto centralizado
texto = "Eleições Virtuais"
bbox = draw.textbbox((0, 0), texto, font=fonte)
largura_texto = bbox[2] - bbox[0]
altura_texto = bbox[3] - bbox[1]

posicao_texto = ((largura - largura_texto) // 2, (altura - altura_texto) // 2)
draw.text(posicao_texto, texto, font=fonte, fill=texto_cor)

# Salvar imagem
imagem.save('eleicoes_virtual.png')
print("Imagem 'eleicoes_virtual.png' criada com sucesso!")
