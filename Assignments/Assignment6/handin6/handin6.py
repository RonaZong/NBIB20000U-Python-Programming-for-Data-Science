import numpy as np
import matplotlib.pyplot as plt

def read_mnist_csv(filename):
    '''Test read_mnist_csv function'''
    data = np.genfromtxt(filename, delimiter=',')
    np_array = np.array(data[1:])
    return np_array

def group_by_label(np_array):
    '''Test group_by_label function'''
    groups = []
    for i in range(10):
        indices = np.where(np_array[:, 0] == i)
        groups.append(np_array[indices])
    return groups

def convert_to_images(np_array):
    '''Test the convert_to_images function'''
    grouped_images = []
    for i in np_array:
        grouped_images.append(np.reshape(i[:,1:], (-1, 28, 28)))
    return grouped_images

def draw_image(np_array):
    '''Test the draw_image function'''
    plt.imshow(np_array, cmap='gray', interpolation='nearest')
    # plt.axis('off')

def draw_image_row(np_array):
    '''Test the draw_image_row function'''
    fig, axs =plt.subplots(1, len(np_array))
    axs[0].imshow(np_array[0][0])

def calc_group_averages(np_array):
    '''Test the calc_group_averages function'''
    group_averages = []
    for group in np_array:
        average = np.average(group, axis=0)
        group_averages.append(np.reshape(average, (1, 28, 28)))
    return group_averages