def scale(toponym):
    toponym_boounbed_by = toponym["boundedBy"]["Envelope"]
    lowerCorner = list(map(float, toponym_boounbed_by["lowerCorner"].split()))
    upperCorner = list(map(float, toponym_boounbed_by["upperCorner"].split()))
    return max(abs(lowerCorner[0] - upperCorner[0]), abs(lowerCorner[1] - upperCorner[1])) / 2