import collisions
import data
import vector_math
import math


def distance(point1, point2):
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2 + (point2.z - point1.z) ** 2)


def cast_ray(ray, sphere_list):
    inter_pts = collisions.find_intersection_points(sphere_list, ray)
    # returns a tuple of the intersection points ordering closest to the ray
    color = data.Color(1, 1, 1)
    closest = math.inf

    if inter_pts:
        for sphere_data in inter_pts:
            sphere = sphere_data[0]
            inter_pt = sphere_data[1]

            ray_dist = distance(ray.pt, inter_pt)

            if ray_dist < closest:
                closest = ray_dist
                color = sphere.color

        return str(color.r * 255) + ' ' + str(color.g * 255) + ' ' + str(color.b * 255)
    else:
        return '255 255 255'


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    print("P3")
    print(width)
    print(height)
    print(255)

    step_x = (max_x - min_x) / width
    step_y = (max_y - min_y) / height

    for i in range(height):
        for j in range(width):
            x = min_x + j * step_x
            y = max_y - i * step_y
            pt = data.Point(x, y, 0)
            ray = data.Ray(eye_point, vector_math.vector_from_to(eye_point, pt))
            print(cast_ray(ray, sphere_list))
