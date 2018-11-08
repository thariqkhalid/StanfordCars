from keras import optimizers
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator

NUM_CLASSES = 10
INPUT_WIDTH = 150
INPUT_HEIGHT = 150
NUM_EPOCHS = 50

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(INPUT_HEIGHT, INPUT_WIDTH, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('softmax'))

adam = optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)

model.compile(loss='sparse_categorical_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])

batch_size = 8

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1./255)

# this is a generator that will read pictures found in
# subfolers of 'data/train', and indefinitely generate
# batches of augmented image data
train_generator = train_datagen.flow_from_directory(
        '/home/thariq/StanfordCars/data/train',  # this is the target directory
        target_size=(INPUT_HEIGHT, INPUT_WIDTH),  # all images will be resized to 150x150
        batch_size=batch_size,
        class_mode='sparse')  # since we use binary_crossentropy loss, we need binary labels

# this is a similar generator, for validation data
validation_generator = test_datagen.flow_from_directory(
        '/home/thariq/StanfordCars/data/val',
        target_size=(INPUT_HEIGHT, INPUT_WIDTH),
        batch_size=batch_size,
        class_mode='sparse')

history = model.fit_generator(
        train_generator,
        steps_per_epoch=2000 // batch_size,
        epochs=NUM_EPOCHS,
        verbose=1,
        workers=4,
        validation_data=validation_generator,
        validation_steps=800 // batch_size)

model.save_weights('first_try.h5')  # always save your weights after training or during training

with open('model_architecture.json','w') as f:
        f.write(model.to_json())