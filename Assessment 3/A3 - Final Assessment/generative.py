"""
This file is part of Assignment 3 of FIT1045, S1 2023.

It contains methods for generating new images from existing images.

@file generative.py
@author
@date
"""
from __future__ import annotations
from ai import predict_number, read_image

# Task 1: Flatten and unflatten images
def flatten_image(image: list[list[int]]) -> list[int]:
    """
    Flattens a 2D list into a 1D list.
    
    :param image: 2D list of integers representing an image.
    :return: 1D list of integers representing a flattened image.
    """
    # raise NotImplementedError
    return [pixel for row in image for pixel in row]
    
def unflatten_image(flat_image: list[int]) -> list[list[int]]:
    """
    Unflattens a 1D list into a 2D list.
        
    :param flat_image: 1D list of integers representing a flattened image.
    :return: 2D list of integers.
    """
    # raise NotImplementedError
    side_length = int(len(flat_image) ** 0.5)
    unflattened_image = []
    index = 0
    for i in range(side_length):
        row = []
        for i in range(side_length):
            row.append(flat_image[index])
            index += 1
        unflattened_image.append(row)
    return unflattened_image

# Task 2: Checking for an adjacent 1
def check_adjacent_for_one(flat_image: list[int], flat_pixel: int) -> bool:
    """
    Checks if a pixel has an adjacent pixel with the value of 1.
    
    :param flat_image: 1D list of integers representing a flattened image.
    :param flat_pixel: Integer representing the index of the pixel in question.
    :return: Boolean.
    """
    
    image_width = int(len(flat_image) ** 0.5) 
    image_height = image_width

    pixel_row = flat_pixel // image_width
    pixel_col = flat_pixel % image_width

    # Check if any adjacent pixels have a value of 1
    adjacent_indices = [(pixel_row + 1, pixel_col), (pixel_row - 1, pixel_col), (pixel_row, pixel_col + 1), (pixel_row, pixel_col - 1)]

    for row, col in adjacent_indices:
        if ((image_height > row >= 0) and (image_width > col >= 0)):     # Check if any adjacent pixels have a value of 1
            adjacent_pixel_index = (row * image_width) + col             
            if (flat_image[adjacent_pixel_index] == 1):
                return True

# Task 3: Recursively flipping pixels
def pixel_flip(lst: list[int], orig_lst: list[int], budget: int, results: list, i: int = 0) -> None:
    """
    Uses recursion to generate all possibilities of flipped arrays where
    a pixel was a 0 and there was an adjacent pixel with the value of 1.

    :param lst: 1D list of integers representing a flattened image.
    :param orig_lst: 1D list of integers representing the original flattened image.
    :param budget: Integer representing the number of pixels that can be flipped.
    :param results: List of 1D lists of integers representing all possibilities of flipped arrays, initially empty.
    :param ind: Integer representing the index of the pixel in question.
    :return: None.
    """
    if (budget < 0):
        return 

    if (i >= len(lst)):
        if (lst != orig_lst):
            results.append(lst)
        return

    if (lst[i] == 0 and check_adjacent_for_one(orig_lst, i)):
        new_list = lst[:]
        new_list[i] = 1
        pixel_flip(new_list, orig_lst, budget - 1, results, i + 1)

    pixel_flip(lst, orig_lst, budget, results, i + 1)

# Task 4: Writing images to a file
def write_image(orig_image: list[list[int]], new_image: list[list[int]], file_name: str) -> None:
    """
    Writes a newly generated image into a file where the modified pixels are marked as 'X'.
    
    :param orig_image: 2D list of integers representing the original image.
    :param new_image: 2D list of integers representing a newly generated image.
    :param file_name: String representing the name of the file.
    :return: None.
    """
    with open(file_name, 'w') as file:
        for orig_row, new_row in zip(orig_image, new_image):
            for orig_pixel, new_pixel in zip(orig_row, new_row):
                if (orig_pixel != new_pixel):
                    file.write('X')
                else:
                    file.write(str(orig_pixel))
            file.write('\n')

# Task 5: Generating new images 
def generate_new_images(image: list[list[int]], budget: int) -> list[list[list[int]]]:
    """
    Generates all possible new images that can be generated within the budget.
    
    :param image: 2D list of integers representing an image.
    :param budget: Integer representing the number of pixels that can be flipped.
    :return: List of 2D lists of integers representing all possible new images.
    """

    flat_image = flatten_image(image)
    predicted_no = predict_number(image)     #predicted_number(img) from the ai module
    generated_images = []

    flipped_possibilities = []
    pixel_flip(flat_image, flat_image, budget, flipped_possibilities)
    
    for possibility in flipped_possibilities:
        unflattened_possibility = unflatten_image(possibility)
        if (predict_number(unflattened_possibility) == predicted_no):
            generated_images.append(unflattened_possibility)

    return generated_images


if __name__ == "__main__":
    image = read_image("confusing_image.txt")
    new_images = generate_new_images(image, 2)
    print(f"Number of new images generated: {len(new_images)}")
    # Write first image to test generation
    write_image(image, new_images[0], "new_image_1.txt") 