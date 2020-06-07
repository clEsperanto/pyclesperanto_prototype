import clesperanto as cle
import numpy as np


test = cle.push(np.asarray([
[1, 1, 1],
[1, 2, 1],
[1, 1, 1]
]))

test2 = cle.create(test)
cle.maximum_sphere(test, test2, 1, 1, 1)

#print("B test")
#print(cle.pull(test))

#print("B test2")
#print(cle.pull(test2))

a = cle.pull(test2)
assert (np.min(a) == 1)
assert (np.max(a) == 2)


cle.set(test, 5)
#print(test)
#print(cle.pull(test))

a = cle.pull(test)
assert (np.min(a) == 5)
assert (np.max(a) == 5)
assert (np.mean(a) == 5)

print ("ok maximum sphere")

test = cle.push(np.asarray([
    [1, -1],
    [1, -1]
]))

test2 = cle.create(test)
cle.absolute(test, test2)

print(test2)

a = cle.pull(test2)
assert (np.min(a) == 1)
assert (np.max(a) == 1)
assert (np.mean(a) == 1)
print ("ok absolute")




test = cle.push(np.asarray([
    [1, 0],
    [1, 0]
]))

test1 = cle.push(np.asarray([
    [1, 1],
    [0, 0]
]))

test2 = cle.create(test)
cle.binary_and(test, test1, test2)

print(test2)

a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.25)
print ("ok binary_and")




test1 = cle.push(np.asarray([
    [1, 1],
    [1, 0]
]))

test2 = cle.create(test1)
cle.binary_not(test1, test2)

print(test2)
a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.25)
print ("ok binary_not")






test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
]))

test2 = cle.create(test1)
cle.binary_edge_detection(test1, test2)

print(test2)
a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) - 12 / 36 < 0.001)
print ("ok binary_edge_detection")













test = cle.push(np.asarray([
    [1, 0],
    [1, 0]
]))

test1 = cle.push(np.asarray([
    [1, 1],
    [0, 0]
]))

test2 = cle.create(test)
cle.binary_or(test, test1, test2)

print(test2)

a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.75)
print ("ok binary_or")









test = cle.push(np.asarray([
    [1, 0],
    [1, 0]
]))

test1 = cle.push(np.asarray([
    [1, 1],
    [0, 0]
]))

test2 = cle.create(test)
cle.binary_subtract(test, test1, test2)

print(test2)

a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.25)
print ("ok binary_subtract")


test = cle.push(np.asarray([
    [1, 0],
    [1, 0]
]))

test1 = cle.push(np.asarray([
    [1, 1],
    [0, 0]
]))

test2 = cle.create(test)
cle.binary_xor(test, test1, test2)

print(test2)

a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.5)
print ("ok binary_xor")




test = cle.push(np.asarray([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))

test1 = cle.push(np.asarray([
    [0, 1, 0],
    [1, 2, 1],
    [0, 1, 0]
]))

test2 = cle.create(test)
cle.convolve(test, test1, test2)

print(test2)

a = cle.pull(test1)
b = cle.pull(test2)
assert (np.min(a) == np.min(b))
assert (np.max(a) == np.max(b))
assert (np.mean(a) == np.mean(b))
print ("ok convolve")












test1 = cle.push(np.asarray([
    [1, 1],
    [1, 0]
]))

test2 = cle.create(test1)
cle.copy(test1, test2)

print(test2)
a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.75)
print ("ok copy")




test1 = cle.push(np.asarray([
    [
        [1, 4],
        [0, 4]
    ],
    [
        [1, 3],
        [1, 2]
    ]
]))

test2 = cle.create((2, 2))
cle.copy_slice(test1, test2, 0)

print(test2)
a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.75)
print ("ok copy slice from 3d")



test1 = cle.push(np.asarray([
        [4, 4],
        [4, 4]
]))

test2 = cle.create((2, 2, 2))
cle.set(test2, 0)
cle.copy_slice(test1, test2, 0)

print(test2)
a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 4)
assert (np.mean(a) == 2)
print ("ok copy slice to 3d")





test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test)
cle.dilate_box(test, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok dilate_box")





test = cle.push_zyx(np.asarray([
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
]))

reference = cle.push_zyx(np.asarray([
    [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
]))

result = cle.create(test)
cle.dilate_box_slice_by_slice(test, result)


a = cle.pull_zyx(result)
b = cle.pull_zyx(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok dilate_box_slice_by_slice")




test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test)
cle.dilate_sphere(test, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok dilate_sphere")









test = cle.push_zyx(np.asarray([
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
]))

reference = cle.push_zyx(np.asarray([
    [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
]))

result = cle.create(test)
cle.dilate_sphere_slice_by_slice(test, result)


a = cle.pull_zyx(result)
b = cle.pull_zyx(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok dilate_sphere_slice_by_slice")











test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 4, 6, 8, 0],
    [0, 4, 6, 8, 0],
    [0, 4, 6, 8, 0],
    [0, 0, 0, 0, 0]
]))

test2 = cle.push(np.asarray([
    [1, 1, 1, 1, 1],
    [1, 2, 3, 2, 1],
    [1, 2, 3, 2, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 2, 2, 4, 0],
    [0, 2, 2, 4, 0],
    [0, 4, 6, 8, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.divide_images(test1, test2, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok divide_images")









reference = cle.push_zyx(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 2, 2, 2, 0],
    [0, 2, 2, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create((5, 5))
cle.set(result, 0)
cle.draw_box(result, 1, 1, 0, 2, 1, 1, 2)

print(result)

a = cle.pull(result)
b = cle.pull(reference)

assert (np.array_equal(a, b))
print ("ok draw_box")



reference = cle.push_zyx(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 2, 2, 2, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create((5, 5))
cle.set(result, 0)
cle.draw_sphere(result, 2, 2, 0, 1, 1, 0, 2)

print(result)

a = cle.pull(result)
b = cle.pull(reference)

assert (np.array_equal(a, b))
print ("ok draw_sphere")







reference = cle.push_zyx(np.asarray([
    [2, 2, 0, 0, 0],
    [2, 2, 2, 0, 0],
    [0, 2, 2, 2, 0],
    [0, 0, 2, 2, 2],
    [0, 0, 0, 2, 2]
]))

result = cle.create((5, 5))
cle.set(result, 0)
cle.draw_line(result, 1, 1, 0, 4, 4, 0, 1, 2)

print(result)

a = cle.pull(result)
b = cle.pull(reference)

assert (np.array_equal(a, b))
print ("ok draw_line")




test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 2, 3, 4, 0],
    [0, 3, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))

test2 = cle.push(np.asarray([
    [1, 1, 1, 1, 1],
    [1, 5, 4, 3, 1],
    [1, 4, 3, 2, 1],
    [1, 3, 4, 1, 1],
    [1, 1, 1, 1, 1]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.equal(test1, test2, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok equal")



test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 2, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.equal_constant(test1, result, 4)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok equal_constant")





test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test)
cle.erode_box(test, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok erode_box")






test = cle.push_zyx(np.asarray([
    [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
]))

reference = cle.push_zyx(np.asarray([
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
]))

result = cle.create(test)
cle.erode_box_slice_by_slice(test, result)


a = cle.pull_zyx(result)
b = cle.pull_zyx(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok erode_box_slice_by_slice")





test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test)
cle.erode_sphere(test, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok erode_sphere")






test = cle.push_zyx(np.asarray([
    [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
]))

reference = cle.push_zyx(np.asarray([
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
]))

result = cle.create(test)
cle.erode_sphere_slice_by_slice(test, result)


a = cle.pull_zyx(result)
b = cle.pull_zyx(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok erode_sphere_slice_by_slice")








test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 2, 0],
    [0, 2, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [1, 1, 1, 1, 1],
    [1,  2.7182817, 2.7182817, 7.389056, 1],
    [1,  7.389056, 7.389056, 20.085537, 1],
    [1, 20.085537, 20.085537, 54.59815, 1],
    [1, 1, 1, 1, 1]
]))

result = cle.create(test)
cle.exponential(test, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, atol=0.00001))
print ("ok exponential")






test = cle.push_zyx(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 0, 0],
    [0, 1, 2, 0, 0],
    [0, 1, 3, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push_zyx(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 2, 1, 0],
    [0, 0, 2, 1, 0],
    [0, 0, 3, 1, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test)
cle.flip(test, result, True, False, False)

print(result)

a = cle.pull_zyx(result)
b = cle.pull_zyx(reference)
assert (np.array_equal(a, b))
print ("ok flip")





test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 100, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test)
cle.gaussian_blur(test, result, 1, 1, 0)

print(result)

a = cle.pull(result)
assert (np.min(a) > 0)
assert (np.max(a) > 15.9)
assert (np.max(a) < 16)

print ("ok gaussian_blur")





test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 0, 0],
    [0, 1, 2, 0, 0],
    [0, 1, 3, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 1, 2, 0, 0],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, -1, -2, 0, 0],
    [0, -1, -3, 0, 0]
]))

result = cle.create(test)
cle.gradient_x(test, result)


a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok gradient_x")






test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 0, 0],
    [0, 1, 2, 0, 0],
    [0, 1, 3, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [1, 2, -1, -2, 0],
    [1, 2, -1, -2, 0],
    [1, 3, -1, -3, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test)
cle.gradient_y(test, result)


a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok gradient_y")





test = cle.push_zyx(np.asarray([
    [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
]))

reference = cle.push_zyx(np.asarray([
    [
        [0, 0, 0, 0, 0],
        [1, 0, 0, -1, 0],
        [1, 0, 0, -1, 0],
        [1, 0, 0, -1, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],[
        [0, 0, 0, 0, 0],
        [-1, 0, 0, 1, 0],
        [-1, 0, 0, 1, 0],
        [-1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
]))

result = cle.create(test)
cle.gradient_z(test, result)


a = cle.pull_zyx(result)
b = cle.pull_zyx(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok gradient_z")







test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))
test2 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 3, 3, 3, 0],
    [0, 3, 3, 3, 0],
    [0, 3, 3, 3, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.greater(test1, test2, result)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok greater")









test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 2, 3, 4, 0],
    [0, 4, 5, 5, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.greater_constant(test1, result, 4)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok greater_constant")







test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))
test2 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 3, 3, 3, 0],
    [0, 3, 3, 3, 0],
    [0, 3, 3, 3, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]))

result = cle.create(test1)
cle.greater_or_equal(test1, test2, result)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok greater_or_equal")







test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 2, 3, 4, 0],
    [0, 4, 5, 5, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.greater_or_equal_constant(test1, result, 4)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok greater_or_equal_constant")








test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, -1, -1, -1, 0],
    [0, -1, 8, -1, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.laplace_box(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok laplace_box")







test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, -1, 0, 0],
    [0, -1, 4, -1, 0],
    [0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.laplace_diamond(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok laplace_diamond")





test1 = cle.push(np.asarray([
    [1, 10],
    [1000, 100]
]))

reference = cle.push(np.asarray([
    [0, 2.3026],
    [6.9078, 4.6052]
]))

result = cle.create(test1)
cle.logarithm(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)
print(b)

assert (np.allclose(a, b, 0.01))
print ("ok logarithm")







test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))
test2 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 3, 0, 0],
    [0, 4, 4, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.mask(test1, test2, result)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok mask")




test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))
test2 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 2, 1, 3, 0],
    [0, 2, 1, 3, 0],
    [0, 1, 1, 3, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 3, 0, 0],
    [0, 4, 4, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.mask_label(test1, test2, result, 1)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok mask_label")












test1 = cle.push(np.asarray([
    [0, 3, 4, 5, 0],
    [0, 2, 1, 6, 0],
    [0, 0, 8, 7, 0]
]))

reference = cle.push(np.asarray([
    [2, 3, 4, 5, 2],
    [2, 2, 2, 6, 2],
    [2, 2, 8, 7, 2]
]))

result = cle.create(test1)
cle.maximum_image_and_scalar(test1, result, 2)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok maximum_image_and_scalar")








test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))
test2 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 2, 1, 3, 0],
    [0, 2, 1, 3, 0],
    [0, 1, 1, 3, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 2, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.maximum_images(test1, test2, result)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok maximum_images")










test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.maximum_box(test1, result, 1, 1, 0)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok maximum_box")






test1 = cle.push(np.asarray([
    [
        [1, 0, 0, 0, 9],
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [1, 0, 0, 0, 9],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [5, 0, 6, 0, 10]
    ],[
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [0, 2, 0, 8, 0],
        [5, 0, 6, 0, 10]
    ]
]))

reference = cle.push(np.asarray([
    [1, 3, 3, 3, 5],
    [2, 4, 4, 4, 0],
    [0, 1, 1, 1, 6],
    [8, 8, 7, 8, 0],
    [9, 10, 10, 10, 10]
]))

result = cle.create(reference)
cle.maximum_x_projection(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok maximum_x_projection")







test1 = cle.push(np.asarray([
    [
        [1, 0, 0, 0, 9],
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [1, 0, 0, 0, 9],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [5, 0, 6, 0, 10]
    ],[
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [0, 2, 0, 8, 0],
        [5, 0, 6, 0, 10]
    ]
]))

reference = cle.push(np.asarray([
    [5, 4, 6, 8, 10],
    [5, 4, 6, 8, 10],
    [5, 4, 6, 8, 10],
    [5, 4, 6, 8, 10],
    [5, 4, 6, 8, 10]
]))

result = cle.create(reference)
cle.maximum_y_projection(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok maximum_y_projection")







test1 = cle.push(np.asarray([
    [
        [1, 0, 0, 0, 9],
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [1, 0, 0, 0, 9],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [5, 0, 6, 0, 10]
    ],[
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [0, 2, 0, 8, 0],
        [5, 0, 6, 0, 10]
    ]
]))

reference = cle.push(np.asarray([
    [9, 8, 10, 7, 10],
    [8, 9, 10, 7, 10],
    [8, 10, 7, 9, 10],
    [8, 9, 7, 10, 10],
    [9, 7, 10, 8, 10]
]))

result = cle.create(reference)
cle.maximum_z_projection(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok maximum_z_projection")





test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.mean_box(test1, result, 1, 1, 0)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok mean_box")






test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 1.8, 0, 0],
    [0, 1.8, 1.8, 1.8, 0],
    [0, 0, 1.8, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.mean_sphere(test1, result, 1, 1, 0)


a = cle.pull(result)
b = cle.pull(reference)

print(a)
print(b)

assert (np.allclose(a, b, 0.0001))
print ("ok mean_sphere")







test1 = cle.push(np.asarray([
    [
        [1, 0, 0, 0, 9],
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [1, 0, 0, 0, 9],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [5, 0, 6, 0, 10]
    ],[
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [0, 2, 0, 8, 0],
        [5, 0, 6, 0, 10]
    ]
]))

reference = cle.push(np.asarray([
    [2, 2,   2.8, 2.2, 4.2],
    [2, 2,   2.8, 2.2, 4.2],
    [2, 2.8, 2.2, 2, 4.2],
    [2, 2,   2.2, 2.8, 4.2],
    [2, 2.2, 2.8, 2, 4.2]
]))

result = cle.create(reference)
cle.mean_z_projection(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.allclose(a, b, 0.001))
print ("ok mean_z_projection")








test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))
test2 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 2, 1, 3, 0],
    [0, 2, 1, 3, 0],
    [0, 1, 1, 3, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 3, 0],
    [0, 2, 1, 3, 0],
    [0, 1, 1, 3, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.minimum_images(test1, test2, result)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok minimum_images")














test1 = cle.push(np.asarray([
    [0, 3, 4, 5, 0],
    [0, 2, 1, 6, 0],
    [0, 0, 8, 7, 0]
]))

reference = cle.push(np.asarray([
    [0, 2, 2, 2, 0],
    [0, 2, 1, 2, 0],
    [0, 0, 2, 2, 0]
]))

result = cle.create(test1)
cle.minimum_image_and_scalar(test1, result, 2)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok minimum_image_and_scalar")






test1 = cle.push(np.asarray([
    [
        [1, 0, 0, 0, 1],
        [0, 2, 0, 8, 1],
        [3, 0, 1, 0, 1],
        [0, 4, 0, 7, 1],
        [1, 1, 1, 1, 1]
    ],[
        [0, 2, 0, 8, 1],
        [1, 0, 0, 0, 1],
        [3, 0, 1, 0, 1],
        [0, 4, 0, 7, 1],
        [1, 1, 1, 1, 1]
    ],[
        [0, 2, 0, 8, 1],
        [3, 0, 1, 0, 1],
        [0, 4, 0, 7, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ],[
        [0, 2, 0, 8, 1],
        [1, 0, 0, 0, 1],
        [0, 4, 0, 7, 1],
        [3, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ],[
        [1, 0, 0, 0, 1],
        [0, 4, 0, 7, 1],
        [3, 0, 1, 0, 1],
        [0, 2, 0, 8, 1],
        [1, 1, 1, 1, 1]
    ]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
]))

result = cle.create(reference)
cle.minimum_z_projection(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.allclose(a, b, 0.001))
print ("ok minimum_z_projection")






test1 = cle.push_zyx(np.asarray([
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2]
]))

reference = cle.push_zyx(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4],
    [0, 2, 4, 6, 8]
]))

result = cle.create(test1)
cle.multiply_image_and_coordinate(test1, result, 0)


a = cle.pull_zyx(result)
b = cle.pull_zyx(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok multiply_image_and_coordinate")



test1 = cle.push_zyx(np.asarray([
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2]
]))

reference = cle.push_zyx(np.asarray([
    [0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2],
    [4, 4, 4, 4, 4]
]))

result = cle.create(test1)
cle.multiply_image_and_scalar(test1, result, 2)


a = cle.pull_zyx(result)
b = cle.pull_zyx(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok multiply_image_and_scalar")






test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 4, 5, 6, 0],
    [0, 7, 8, 9, 0],
    [0, 0, 0, 0, 0]
]))
test2 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 2, 2, 2, 0],
    [0, 1, 1, 1, 0],
    [0, 3, 3, 3, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 2, 4, 6, 0],
    [0, 4, 5, 6, 0],
    [0, 21, 24, 27, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.multiply_images(test1, test2, result)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok multiply_images")









test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.minimum_box(test1, result, 1, 1, 0)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok minimum_box")








test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 2, 0],
    [0, 2, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 2, 3, 3, 0],
    [0, 3, 4, 4, 0],
    [0, 3, 4, 4, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test)
flag = cle.create((1,1,1))
cle.nonzero_maximum_box(test, flag, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, atol=0.00001))
print ("ok nonzero_maximum_box")








test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 2, 0],
    [0, 2, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 2, 2, 2, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test)
flag = cle.create((1,1,1))
cle.nonzero_minimum_box(test, flag, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, atol=0.00001))
print ("ok nonzero_minimum_box")






test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 2, 0],
    [0, 2, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 2, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 3, 4, 4, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test)
flag = cle.create((1,1,1))
cle.nonzero_maximum_diamond(test, flag, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, atol=0.00001))
print ("ok nonzero_maximum_diamond")







test = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 2, 0],
    [0, 2, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 2, 0],
    [0, 2, 2, 3, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test)
flag = cle.create((1,1,1))
cle.nonzero_minimum_diamond(test, flag, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, atol=0.00001))
print ("ok nonzero_minimum_diamond")






test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 4, 5, 6, 0],
    [0, 7, 8, 9, 0],
    [0, 0, 0, 0, 0]
]))
test2 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 2, 2, 2, 0],
    [0, 1, 1, 1, 0],
    [0, 3, 3, 3, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.not_equal(test1, test2, result)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok not_equal")

test1 = cle.push_zyx(np.asarray([
    [0, 0, 0, 1],
    [0, 0, 3, 1],
    [0, 0, 3, 1],
    [1, 1, 1, 1]
]))
# crop width, height
crop_x = 3
crop_y = 3

reference = cle.push_zyx(np.asarray([
    [0, 0, 0],
    [0, 0, 3],
    [0, 0, 3]
]))

result = cle.create((crop_x, crop_y))
cle.crop(test1, result, 0, 0)

a = cle.pull(result)
b = cle.pull(reference)

print(a)
print(b)
assert (np.array_equal(a, b))
print("ok crop")



test1 = cle.push_zyx(np.asarray([
    [0, 0, 0, 1],
    [0, 0, 3, 1],
    [0, 0, 3, 1],
    [1, 1, 1, 1]
]))
test2 = cle.push_zyx(np.asarray([
    [1, 2],
]))

reference = cle.push_zyx(np.asarray([
    [0, 0, 0, 1],
    [0, 0, 3, 1],
    [0, 1, 2, 1],
    [1, 1, 1, 1]
]))

result = cle.create(test1)
cle.copy(test1, result)

cle.paste(test2, result, 1, 2, 0)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok paste")






test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 2, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [1, 2, 3, 3, 3],
    [2, 1, 2, 3, 4],
    [4, 2, 3, 4, 5],
    [4, 4, 4, 5, 5],
    [4, 4, 5, 5, 5]
]))

result = cle.create(test1)
flag = cle.create((1, 1, 1))
cle.onlyzero_overwrite_maximum_box(test1, flag, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok onlyzero_overwrite_maximum_box")







test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 2, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 1, 2, 3, 0],
    [1, 1, 2, 3, 3],
    [2, 2, 3, 4, 4],
    [4, 4, 4, 5, 5],
    [0, 4, 4, 5, 0]
]))

result = cle.create(test1)
flag = cle.create((1, 1, 1))
cle.onlyzero_overwrite_maximum_diamond(test1, flag, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok onlyzero_overwrite_maximum_diamond")









test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 2, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 4, 9, 0],
    [0, 4, 9, 16, 0],
    [0, 16, 16, 25, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.power(test1, result, 2)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, 0.001))
print ("ok power")









test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 4, 5, 6, 0],
    [0, 7, 8, 9, 0],
    [0, 0, 0, 0, 0]
]))
test2 = cle.push(np.asarray([
    [1, 0, 0, 0, 0],
    [1, 1, 2, 3, 0],
    [1, 1, 2, 3, 0],
    [1, 1, 2, 3, 0],
    [1, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 1, 1, 1, 1],
    [0, 1, 4, 27, 1],
    [0, 4, 25, 216, 1],
    [0, 7, 64, 729, 1],
    [0, 1, 1, 1, 1]
]))

result = cle.create(test1)
cle.power_images(test1, test2, result)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.allclose(a, b, 0.0001))
print ("ok power_images")










test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 2, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))

test2 = cle.push_zyx(np.asarray([
    [0, 9, 8, 7, 6, 5]
]))


reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 9, 8, 7, 0],
    [0, 8, 7, 6, 0],
    [0, 6, 6, 5, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.replace_intensities(test1, test2, result)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, 0.001))
print ("ok replace_intensities")










test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 2, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 8, 3, 0],
    [0, 8, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.replace_intensity(test1, result, 2, 8)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, 0.001))
print ("ok replace_intensity")









result = cle.create((5, 5))

reference = cle.push(np.asarray([
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3]
]))

cle.set(result, 3)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, 0.001))
print ("ok set")




result = cle.push(np.asarray([
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3]
]))

reference = cle.push(np.asarray([
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
    [3, 3, 3, 3, 3]
]))

cle.set_column(result, 3, 4)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, 0.001))
print ("ok set_column")






result = cle.push(np.asarray([
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3]
]))

reference = cle.push(np.asarray([
    [4, 4, 4, 4, 4],
    [4, 3, 3, 3, 4],
    [4, 3, 3, 3, 4],
    [4, 3, 3, 3, 4],
    [4, 4, 4, 4, 4]
]))

cle.set_image_borders(result, 4)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, 0.001))
print ("ok set_image_borders")






result = cle.push(np.asarray([
    [
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3]
        ],[
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3]
        ]
]))

reference = cle.push(np.asarray([
    [
        [3, 4, 3, 3, 3],
        [3, 4, 3, 3, 3],
        [3, 4, 3, 3, 3],
        [3, 4, 3, 3, 3],
        [3, 4, 3, 3, 3]
    ], [
        [3, 4, 3, 3, 3],
        [3, 4, 3, 3, 3],
        [3, 4, 3, 3, 3],
        [3, 4, 3, 3, 3],
        [3, 4, 3, 3, 3]
    ]
]))

cle.set_plane(result, 1, 4)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, 0.001))
print ("ok set_plane")





result = cle.push(np.asarray([
    [
        [0, 0, 0],
        [3, 4, 3],
        [3, 4, 3]
    ],[
        [3, 4, 3],
        [3, 4, 3],
        [3, 4, 3]
    ]
]))

reference = cle.push(np.asarray([
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ], [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
]))

cle.set_ramp_x(result)

a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.allclose(a, b, 0.001))
print ("ok set_ramp_x")







result = cle.push(np.asarray([
    [
        [0, 0, 0],
        [3, 4, 3],
        [3, 4, 3]
    ],[
        [3, 4, 3],
        [3, 4, 3],
        [3, 4, 3]
    ]
]))

reference = cle.push(np.asarray([
    [
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
    ], [
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
    ]
]))

cle.set_ramp_y(result)

a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.allclose(a, b, 0.001))
print ("ok set_ramp_y")










result = cle.push(np.asarray([
    [
        [0, 0, 0],
        [3, 4, 3],
        [3, 4, 3]
    ],[
        [3, 4, 3],
        [3, 4, 3],
        [3, 4, 3]
    ]
]))

reference = cle.push(np.asarray([
    [
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2]
    ], [
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2]
    ]
]))

cle.set_ramp_z(result)

a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.allclose(a, b, 0.001))
print ("ok set_ramp_z")






result = cle.push(np.asarray([
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3]
]))

reference = cle.push(np.asarray([
    [3, 3, 3, 4, 3],
    [3, 3, 3, 4, 3],
    [3, 3, 3, 4, 3],
    [3, 3, 3, 4, 3],
    [3, 3, 3, 4, 3]
]))

cle.set_row(result, 3, 4)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.allclose(a, b, 0.001))
print ("ok set_row")













test1 = cle.push_zyx(np.asarray([
    [0, 0, 0, 1],
    [0, 0, 3, 1],
    [0, 0, 3, 1],
    [1, 1, 1, 1]
]))

reference = cle.push_zyx(np.asarray([
    [0, 0, 0, 12],
    [0, 0, 9, 13],
    [0, 0, 10, 14],
    [3, 7, 11, 15]
]))

result = cle.create(test1)
cle.set_nonzero_pixels_to_pixelindex(test1, result)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok set_nonzero_pixels_to_pixelindex")






result = cle.push(np.asarray([
    [0, 0, 0, 1],
    [0, 0, 3, 1],
    [0, 0, 3, 1],
    [1, 1, 1, 1]
]))

reference = cle.push(np.asarray([
    [3, 0, 0, 1],
    [0, 3, 3, 1],
    [0, 0, 3, 1],
    [1, 1, 1, 3]
]))

cle.set_where_x_equals_y(result, 3)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok set_where_x_equals_y")






result = cle.push(np.asarray([
    [0, 0, 0, 1],
    [0, 0, 3, 1],
    [0, 0, 3, 1],
    [1, 1, 1, 1]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 1],
    [3, 0, 3, 1],
    [3, 3, 3, 1],
    [3, 3, 3, 1]
]))

cle.set_where_x_greater_than_y(result, 3)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok set_where_x_greater_than_y")





result = cle.push(np.asarray([
    [0, 0, 0, 1],
    [0, 0, 3, 1],
    [0, 0, 3, 1],
    [1, 1, 1, 1]
]))

reference = cle.push(np.asarray([
    [0, 3, 3, 3],
    [0, 0, 3, 3],
    [0, 0, 3, 3],
    [1, 1, 1, 1]
]))

cle.set_where_x_smaller_than_y(result, 3)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok set_where_x_smaller_than_y")








test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))
test2 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 3, 3, 3, 0],
    [0, 3, 3, 3, 0],
    [0, 3, 3, 3, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

result = cle.create(test1)
cle.smaller(test1, test2, result)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok smaller")




test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 2, 3, 4, 0],
    [0, 4, 5, 5, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]))

result = cle.create(test1)
cle.smaller_constant(test1, result, 4)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok smaller_constant")













test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 3, 3, 4, 0],
    [0, 4, 4, 5, 0],
    [0, 0, 0, 0, 0]
]))
test2 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 3, 3, 3, 0],
    [0, 3, 3, 3, 0],
    [0, 3, 3, 3, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]))

result = cle.create(test1)
cle.smaller_or_equal(test1, test2, result)

a = cle.pull(result)
b = cle.pull(reference)
print(a)

assert (np.array_equal(a, b))
print ("ok smaller_or_equal")









test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 0],
    [0, 2, 3, 4, 0],
    [0, 4, 5, 5, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]))

result = cle.create(test1)
cle.smaller_constant(test1, result, 4)

print(result)

a = cle.pull(result)
b = cle.pull(reference)
assert (np.array_equal(a, b))
print ("ok smaller_or_equal_constant")






test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]))

reference = cle.push(np.asarray([
    [0, 0, 0, 0, 0],
    [0, 1.41, 2, 1.41, 0],
    [0, 3.16, 2, 3.16, 0],
    [0, 3.16, 2, 3.16, 0],
    [0, 1.41, 2, 1.41, 0]
]))

result = cle.create(test1)
cle.sobel(test1, result)
a = cle.pull(result)
print(a)

b = cle.pull(reference)
assert (np.allclose(a, b, 0.01))
print ("ok sobel")











test1 = cle.push(np.asarray([
    [
        [1, 0, 0, 0, 9],
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [1, 0, 0, 0, 9],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [5, 0, 6, 0, 10]
    ],[
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [0, 2, 0, 8, 0],
        [5, 0, 6, 0, 10]
    ]
]))

reference = cle.push(np.asarray([
    [3.94, 3.46, 4.21, 3.19, 4.27],
    [3.46, 3.94, 4.21, 3.19, 4.27],
    [3.46, 4.21, 3.19, 3.94, 4.27],
    [3.46, 3.94, 3.19, 4.21, 4.27],
    [3.94, 3.19, 4.21, 3.46, 4.27]
]))

result = cle.create(reference)
cle.standard_deviation_z_projection(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.allclose(a, b, 0.01))
print ("ok standard_deviation_z_projection")








test1 = cle.push_zyx(np.asarray([
    [0, 0],
    [1, 1],
    [2, 2]
]))

reference = cle.push_zyx(np.asarray([
    [5, 5],
    [4, 4],
    [3, 3]
]))

result = cle.create(test1)
cle.subtract_image_from_scalar(test1, result, 5)


a = cle.pull_zyx(result)
b = cle.pull_zyx(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok subtract_image_from_scalar")








test1 = cle.push(np.asarray([
    [
        [1, 0, 0, 0, 9],
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [1, 0, 0, 0, 9],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [5, 0, 6, 0, 10]
    ],[
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [0, 2, 0, 8, 0],
        [5, 0, 6, 0, 10]
    ]
]))

reference = cle.push(np.asarray([
    [2, 5, 9, 4, 25],
    [6, 6, 8, 10, 0],
    [0, 1, 3, 1, 30],
    [24, 15, 14, 22, 0],
    [18, 28, 30, 19, 50]
]))

result = cle.create(reference)
cle.sum_x_projection(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.allclose(a, b, 0.01))
print ("ok sum_x_projection")








test1 = cle.push(np.asarray([
    [
        [1, 0, 0, 0, 9],
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [1, 0, 0, 0, 9],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [5, 0, 6, 0, 10]
    ],[
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [0, 2, 0, 8, 0],
        [5, 0, 6, 0, 10]
    ]
]))

reference = cle.push(np.asarray([
    [9, 6, 7, 15, 29],
    [9, 6, 7, 15, 29],
    [9, 6, 7, 15, 29],
    [9, 6, 7, 15, 29],
    [9, 6, 7, 15, 29]
]))

result = cle.create(reference)
cle.sum_y_projection(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.allclose(a, b, 0.01))
print ("ok sum_y_projection")







test1 = cle.push(np.asarray([
    [
        [1, 0, 0, 0, 9],
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [3, 0, 1, 0, 10],
        [0, 4, 0, 7, 0],
        [1, 0, 0, 0, 9],
        [5, 0, 6, 0, 10]
    ],[
        [0, 2, 0, 8, 0],
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [5, 0, 6, 0, 10]
    ],[
        [1, 0, 0, 0, 9],
        [0, 4, 0, 7, 0],
        [3, 0, 1, 0, 10],
        [0, 2, 0, 8, 0],
        [5, 0, 6, 0, 10]
    ]
]))

reference = cle.push(np.asarray([
    [10, 10, 14, 11, 21],
    [10, 10, 14, 11, 21],
    [10, 14, 11, 10, 21],
    [10, 10, 11, 14, 21],
    [10, 11, 14, 10, 21]
]))

result = cle.create(reference)
cle.sum_z_projection(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.allclose(a, b, 0.01))
print ("ok sum_z_projection")








test1 = cle.push(np.asarray([
    [
        [0, 1],
        [2, 3]
    ],[
        [4, 5],
        [6, 7]
    ]
]))

reference = cle.push(np.asarray([
    [
        [0, 1],
        [4, 5]
    ], [
        [2, 3],
        [6, 7]
    ]
]))

result = cle.create(test1)
cle.transpose_xy(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok transpose_xy")







test1 = cle.push(np.asarray([
    [
        [0, 1],
        [2, 3]
    ],[
        [4, 5],
        [6, 7]
    ]
]))

reference = cle.push(np.asarray([
    [
        [0, 4],
        [2, 6]
    ], [
        [1, 5],
        [3, 7]
    ]
]))

result = cle.create(test1)
cle.transpose_xz(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok transpose_xz")





test1 = cle.push(np.asarray([
    [
        [0, 1],
        [2, 3]
    ],[
        [4, 5],
        [6, 7]
    ]
]))

reference = cle.push(np.asarray([
    [
        [0, 2],
        [1, 3]
    ], [
        [4, 6],
        [5, 7]
    ]
]))

result = cle.create(test1)
cle.transpose_yz(test1, result)


a = cle.pull(result)
b = cle.pull(reference)

print(a)

assert (np.array_equal(a, b))
print ("ok transpose_yz")


