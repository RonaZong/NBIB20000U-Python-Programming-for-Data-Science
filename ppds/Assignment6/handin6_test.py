import handin6
import matplotlib.pyplot as plt
import numpy as np

data = handin6.read_mnist_csv('mnist_test_200.csv')
assert data.shape == (200, 785)

groups = handin6.group_by_label(data)
# Check that there are 10 groups
assert len(groups) == 10
# Check dimensions of group members
for group in groups:
    assert group.shape[0] > 0
    assert group.shape[1] == 785

grouped_images = handin6.convert_to_images(groups)
# Check that there are 10 groups
assert len(grouped_images) == 10
# Check dimensions of group members
for group in grouped_images:
    assert len(group.shape) == 3
    assert group.shape[0] > 0
    assert group.shape[1] == 28
    assert group.shape[2] == 28

# Call drawing function
handin6.draw_image(grouped_images[0][0])
# Check how many images have been plotted
assert len(plt.gcf().get_axes()) >= 1
# plt.show()

# Call drawing function
handin6.draw_image_row(grouped_images)
# Check how many images have been plotted
assert len(plt.gcf().get_axes()) == 10
# plt.show()

# Call function
group_averages = handin6.calc_group_averages(grouped_images)
# Check dimensions
assert len(group_averages) == 10
for group in group_averages:
    assert len(group.shape) == 3
    assert group.shape[0] == 1
    assert group.shape[1] == 28
    assert group.shape[2] == 28
# Check that we can call draw_image_row
handin6.draw_image_row(group_averages)