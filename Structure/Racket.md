## images
2htdp/image library

| commands     | args                           |                                                                    |
| ------------ | ------------------------------ | ------------------------------------------------------------------ |
| circle       | number, string, string         | size, fill, color                                                  |
| rectangle    | number, number, string, string | width, height, fill, color                                         |
| image-width  | image                          |                                                                    |
| image-height | image                          |                                                                    |
| above        | image, image, ...              |                                                                    |
| beside       | image, image, ...              |                                                                    |
| overlay      | image, image, ...              |                                                                    |
| random       | int                            | random getal tussen 0 en input                                     |
| animate      | (lambda (time) image)          | animates an image by calling<br>the lambda with increasing numbers |
|              |                                |                                                                    |

R5RS --> Racket
cons --> ncons
car --> ncar
cdr --> mcdr

Racket/contract
