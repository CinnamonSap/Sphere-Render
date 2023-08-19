import data
import utility
import vector_math


def sphere_intersection_point(ray, sphere):
# get the values from the quadratic equations, both the negative and positive parts

    a = vector_math.dot_vector(ray.direction, ray.direction)

    b = 2 * vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), ray.direction)

    c = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center),
                                vector_math.difference_point(ray.pt, sphere.center)) - sphere.rad ** 2

    if b ** 2 - 4 * a * c < 0:
        return None

    neg_t = utility.quadratic_neg([c, b, a])
    pos_t = utility.quadratic_pos([c, b, a])

    # this is to sort out the double neg, single pos single neg, and double pos values

    if neg_t < 0 and pos_t < 0:
        return None
    elif neg_t > 0 or pos_t > 0:
        if neg_t > pos_t:
            g = pos_t
        else:
            g = neg_t
    else:
        if neg_t > pos_t:
            g = pos_t
        else:
            g = neg_t

    return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.direction, g))


def find_intersection_points(sphere_list, ray):
    res = []
    for sphere in sphere_list:
        if sphere_intersection_point(ray, sphere) is not None:
            res.append((data.Sphere(sphere.center, sphere.rad, sphere.color), sphere_intersection_point(ray, sphere)))
    return res


def sphere_normal_at_point(sphere, point):
    return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))
