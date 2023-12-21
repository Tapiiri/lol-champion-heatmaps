def rotate_centerpoints(centerpoints, image_size):
   rotated_centerpoints = [(y, image_size[0] - x) for x, y in centerpoints]

   return rotated_centerpoints