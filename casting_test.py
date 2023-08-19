import cast
import data

spheres = [data.Sphere(data.Point(1, 1, 0), 2, data.Color(0, 0, 1)), data.Sphere(data.Point(0.5, 1.5, -3), 0.5, data.Color(1, 0, 0))]

cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, data.Point(0, 0, -14), spheres)
