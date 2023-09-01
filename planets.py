import cv2
import numpy as np
# Load the image of the planets
planets = cv2.imread('PRO-104-Project-Image-main/solar-system.jpg')
# Get the size of the image
(h, w) = planets.shape[:2]
# Create a new image to display the planets and their names
planets_with_names = np.zeros((h, w, 3), dtype=np.uint8)
# Add the planets to the new image
planets_with_names[0:h, 0:w] = planets
# Add the names of the planets to the new image
cv2.putText(planets_with_names, 'Mercury', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(planets_with_names, 'Venus', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(planets_with_names, 'Earth', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(planets_with_names, 'Mars', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(planets_with_names, 'Jupiter', (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(planets_with_names, 'Saturn', (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(planets_with_names, 'Uranus', (10, 210), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv2.imshow("output",planets)

cv2.waitKey(0)