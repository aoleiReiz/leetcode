
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    n = len(redShirtSpeeds)
    totalSpeed = 0
    if fastest:
        redShirtSpeeds = sorted(redShirtSpeeds, reverse=True)
        blueShirtSpeeds = sorted(blueShirtSpeeds)
    else:
        redShirtSpeeds = sorted(redShirtSpeeds, reverse=True)
        blueShirtSpeeds = sorted(blueShirtSpeeds, reverse=True)
    for i in range(n):
        totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return totalSpeed
