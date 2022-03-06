def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights = sorted(redShirtHeights, reverse=True)
    blueShirtHeights = sorted(blueShirtHeights, reverse=True)
    if blueShirtHeights[0] == redShirtHeights[0]:
        return False
    sign = blueShirtHeights[0] > redShirtHeights[0]
    for i in range(1, len(redShirtHeights)):
        if blueShirtHeights[i] == redShirtHeights[i] or (blueShirtHeights[i] > redShirtHeights[i]) != sign:
            return False
    return True

