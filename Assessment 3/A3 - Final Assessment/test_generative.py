from __future__ import annotations
import unittest
from generative import flatten_image, unflatten_image, check_adjacent_for_one, pixel_flip, write_image, generate_new_images
from ai import read_image


class TestGenerative(unittest.TestCase):
    """Unit tests for the module generative.py"""

    def test_flatten_image(self) -> None:
        print("\n-----------------------------")
        print("TEST CASES - test_flatten_image")
        """
        Verify output of flatten_image for at least three different sizes of images.
        """
        # Case 1: 2x2 image
        img_2x2 = [
            [1, 2],
            [3, 4]
        ]
        expected_flat_img_2x2 = [1, 2, 3, 4]
        self.assertEqual(flatten_image(img_2x2), expected_flat_img_2x2)
        print("Case 1 - Pass")

        # Case 2: 3x3 image
        img_3x3 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_flat_img_3x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(flatten_image(img_3x3), expected_flat_img_3x3)
        print("Case 2 - Pass")

        # Case 3: 4x4 image
        img_4x4 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        expected_flat_img_4x4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(flatten_image(img_4x4), expected_flat_img_4x4)
        print("Case 3 - Pass")
       
    def test_unflatten_image(self) -> None:
        print("\n-----------------------------")
        print("TEST CASES - test_unflatten_image")
        """
        Verify output of unflatten_image for at least three different sizes of flattened images.
        """
         # Case 1: 2x2 image
        img_2x2 = [
            [1, 2],
            [3, 4]
        ]
        expected_unflat_img_2x2 = [1, 2, 3, 4]
        self.assertEqual(flatten_image(img_2x2), expected_unflat_img_2x2)
        print("Case 4 - Pass")

        # Case 2: 3x3 image
        img_3x3 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_unflat_img_3x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(flatten_image(img_3x3), expected_unflat_img_3x3)
        print("Case 5 - Pass")

        # Case 3: 4x4 image
        img_4x4 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        expected_unflat_img_4x4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(flatten_image(img_4x4), expected_unflat_img_4x4)
        print("Case 6 - Pass")


    def test_check_adjacent_for_one(self) -> None:
        print("\n-----------------------------")
        print("TEST CASES - test_check_adjacent_for_one")
        """
        Verify output of check_adjacent_for_one for three different pixel indexes of an image representing different scenarios.
        """
        img_1 = [
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 1, 1, 1]
        ]
        flat_img = []
        for row in img_1:
            for pixel in row:
                flat_img.append(pixel)
        pixel_index_1 = 19
        self.assertTrue(check_adjacent_for_one(flat_img, pixel_index_1))
        print("Case 7 - Pass")
        
        img_2 = [
            [0, 1, 1, 0, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1],
        ]
        flat_img = []
        for row in img_2:
            for pixel in row:
                flat_img.append(pixel)
        pixel_index_2 = 5
        self.assertTrue(check_adjacent_for_one(flat_img, pixel_index_2))
        print("Case 8 - Pass")

        img_3 = [
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1]
        ]
        flat_img = []
        for row in img_3:
            for pixel in row:
                flat_img.append(pixel)
        pixel_index_3 = 21
        self.assertTrue(check_adjacent_for_one(flat_img, pixel_index_3))
        print("Case 9 - Pass")

    def test_pixel_flip(self) -> None:
        """
        Verify output of pixel_flip for a 5x5 image with a budget of 2.
        """
        image = [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1]
        ]
        flat_image = flatten_image(image)
        budget = 2
        flipped_possibilities = []
        pixel_flip(flat_image, flat_image, budget, flipped_possibilities)

        # # Check the number of flipped possibilities
        self.assertEqual(len(flipped_possibilities), 8)
        

    # def test_generate_new_images(self) -> None:
        print("\n-----------------------------")
        print("Test_generate_new_images")
        print("Incomplete")
        """
        Verify generate_new_images with image.txt and for each image of the generated images verify that:
        - image is of size 28x28,
        - all values in the generated image are either 1s or 0s,
        - the number of pixels flipped from original image are within budget,
        - all pixels flipped from the original image had an adjacent value of 1.
         """
         
        original_image = read_image("image.txt")
        budget = 2
        generated_images = generate_new_images(original_image, budget)

        for image in generated_images:
            # 1. Image is of size 28x28
            self.assertEqual(len(generated_images), 28)         #checks 28 rows
            self.assertEqual(len(generated_images[0]), 28)      #checks 28 elements in first row 

            for row in generated_images:
                #  2. all values in the generated image are either 1s or 0s,
                for pixel in row:
                    self.assertIn(pixel, [0, 1])   

            # 3. the number of pixels flipped from original image are within budget,
            flipped_pixels_counter = 0
            for row in image:
                for pixel in row:
                    if (pixel == 1):
                        flipped_pixels_counter += 1    

        

if __name__ == "__main__":
    unittest.main()