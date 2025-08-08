import imageio.v3 as iio

filenames = ['team-pic1.png', 'team-pic2.png']
images=[]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('output.gif', images, duration=0.5)


'''git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/GAMEDEV-STB/Image-to-gif.git
git push -u origin main
''' 