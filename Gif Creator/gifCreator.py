import imageio

image = imageio.imread('bestFlag.jpg')
image_list = [image]
output_file = 'bestFlag.gif'
imageio.mimsave(output_file, image_list, duration=0.5)
print(f'GIF dosyası oluşturuldu: {output_file}')

