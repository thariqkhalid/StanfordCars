from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

img = load_img(os.path.join(TRAIN_IMG_DIR,"1/00163.jpg"))

x = img_to_array(img)

x = x.reshape((1,) + x.shape)

i = 0
for batch in datagen.flow(x, batch_size=3,
                         save_to_dir='preview', save_prefix=classes[72], save_format='jpeg'):
    i += 1
    if i > 29:
        break