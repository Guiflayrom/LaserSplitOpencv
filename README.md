
# Laser Split Image W/ OpenCV

Once upon a time, a little boy called Guilherme was looking the woman cutting mortadella at bakery and he just thought: is it fucking possible to automate this process?

And then, in a Monday, after work, for pure hobbie, I decided program this algorithm, 'cause the logic was not wanted get out my head >.<

So if u have some kindo difficult in math, feel free to use my logic as u want :D


## Usage/Examples

```python
FILE = 'mortadela.jpg'           #okay, filename, at moment nothing so special
WINDOW_TITLE = 'Scanner - GDA'   #feel free to change
SHOW_WINDOW = True               #alright we wanna see that

if FILE == 'mortadela.jpg':
```
    # With this config,
    # The code gonna split the image in two
```python
    WEIGHT = 1000  #1000 kg
    SPLITED = 500   #500 g
```
    # Depending the size of image, you have to
    # Increase or decrease these numbers
```python
    RESIZE = 180   #in my case, the image was small
    THICK = 2      #and the thick is about the line thickness
````
```
# And here is the point of the program, im use threshold to
# detect the object, feel free to edit and use yolo or other
# frameworks..
```
```python
    THRESH = 235
```

