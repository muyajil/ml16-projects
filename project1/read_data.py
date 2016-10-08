import os
import numpy as np
import nibabel as nib

root_dir = os.path.dirname(os.path.realpath(__file__))

test_dir = "set_test"
train_dir = "set_train"

file_prefix_train = "train_"
file_prefix_test = "test_"

file_suffix = ".nii"

targets_file = "targets.csv"
targets = []

with open(targets_file, "r") as file:
	targets = file.readlines()

Y_train = map(int, targets)
X_train = []

for i in range(278):
	image = nib.load(os.path.join(root_dir, train_dir, file_prefix_train + str(i+1) + file_suffix))	
	(height, width, depth, values) = image.shape
	data = image.get_data()
	X = []
	for a in range(height):
		for b in range(width):
			for c in range(depth):
				X.append(data[a][b][c])
				
	X_train.append(X)
	print "Finished file " + str(i+1)

print "Finished"
print X_train.shape