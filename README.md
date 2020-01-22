# Image-Manipulation-Using-Quadtrees
Storing image in form of quadtree and retrieval of image.

To retrieve the image, i created a list with size n (n output pixels) and initialized it with 1 to n and stored in a seperate quadtree now i traversed quadtree in DFS. And got another sequence and again stored that sequence into another quadtree, and repeated process untill i got the sequence 0,1,4,5..... call it ListX. And again traversed image quadtree with DFS, and stored in a ListY and retrieved same sequence of pixels by simply accessing ListY[ListX[i]].

To reduce overhead, i hardcoded the sequences of index into genSeq.py
genSeq.py is required in order to get that sequence.

  
