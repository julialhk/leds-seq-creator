# leds-seq-creator

## Time Selection

### multiple episodes

select episodes 3 and 4.
```python
episodes(3, 5)
``` 

select the first half of episode 3
```python
episodes(3, 3.5)
``` 

### single episode
select a single, full episode
```python
episode(4)
``` 







## Elements Selection

### single element
apply the follwoing actions to element flower1
```python
elements(flower1)
``` 

### pre defined group
apply to a group of elements of type flower
```python
elements(flowers)
``` 

### all objects
apply to all the elements in the scene
```python
elements(all)
``` 

### custom group
create a custom group of elements, name it `my_elements_name` (you can choose your own name), and use it later like other groups
```python
my_elements_name = [flower1, cabbage1]
elements(my_elements_name)
``` 

### sub-element
select a single stick from a `sticks` object. following actions will apply to this stick only
```python
elements(sticks1.stick(3))
``` 

### mixing
you can freely mix elements of any type (groups, objects, custom-groups, sub-elements). examples:
```python
elements(sticks1.stick(0), sticks1.stick(2), sticks1.stick(4))
elements(flowers, sticks1.stick(0))
elements(flower1, cabbage1)
```

## Cycle Definition
define number of beats which forms a unit that repeat itself
```python
cycle(beats=2)
```
apply the following actions in units of 2 beats. for example: for blink animation, the blink rate will be 2 beats

## Coloring
apply a static coloring to on the during the time frame set directly above it, and to the elements set directly above it

### uniform
set the color to be uniform (same color on the whole element)
```python
color.uniform(red)
```
or you can create your own custom color in hsv format
```python
color.uniform((0.2, 0.85, 0.6))
```
where hue is 0.2 (between red and green), saturation is 0.85 (mostely color, but with a bit white), and brightness 0.6 (not very bright, but not dark)

### alternate
color the object in two colors, and change between then every few pixels
```python
color.alternate(red, pink)
```
choose how many pixels to paint in each color
```python
color.alternate(red, coral, number_of_pixels=10)
```

### gradient
color with gradient from one hue to the other (passing all the hues in the middle)
```python
color.gradient(0.0, 0.2)
```
- if you choose close numbers (difference of up to 0.2), you will get about the same color
- if you choose far away numbers, you will get a colorful coloring
- if you your colors are 1.0 aprat `color.gradient(0.0, 1.0)` you will get a full rainbow with all the colors
- if the diff is >> 1.0, the colors will appear many times




