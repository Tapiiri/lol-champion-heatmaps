def rotate_centerpoints(centerpoints, image_size):
   rotated_centerpoints = [(image_size[1] - y, x) for x, y in centerpoints]

   return rotated_centerpoints