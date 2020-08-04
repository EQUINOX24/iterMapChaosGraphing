import imageio
images = []
for k in range(1000):
    try:
        filename = './frames/frame ' + str(k) + '.png'
        images.append(imageio.imread(filename))
        print(k)
    except:
        pass
imageio.mimsave('movie.gif', images)
