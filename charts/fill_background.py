from typing import List
from PIL import Image
import os


def get_all_charts() -> List[str]:
    charts = []
    for file in os.listdir('.'):
        if file.endswith('.png'):
            charts.append(file)
    return charts


def fill_background(chart: str) -> None:
    # Fill the transparent background with blue

    im = Image.open(chart)

    for x in range(im.width):
        for y in range(im.height):
            pixel = im.getpixel((x, y))

            # If pixel is transparent and black, fill with blue
            if pixel == (0, 0, 0, 0):
                im.putpixel((x, y), (0, 0, 70, 255))
            
            # If pixel is white and somewhat transparent
            elif pixel[:3] == (255, 255, 255):
                alpha = pixel[3]

                if alpha > 150:
                    im.putpixel((x, y), (255, 255, 255, 255))

                elif alpha > 110:
                    im.putpixel((x, y), (0, 0, 70, 255 - pixel[3]))

                else:
                    im.putpixel((x, y), (0, 0, 70, 255))
            

    im.save(chart, format='png')

    # im = cv2.imread(chart, cv2.IMREAD_UNCHANGED)

    # for i in range(im.shape[0]):
    #     for j in range(im.shape[1]):
    #         if tuple(im[i, j]) == tuple([0, 0, 0, 0]):
    #             im[i, j] = [70, 0, 0, 255]

    # # Save the image with alpha channel
    # cv2.imwrite(chart, im, [cv2.IMWRITE_PNG_COMPRESSION, 0])


def main() -> None:
    
    charts = get_all_charts()
    for chart in charts:
        print(f'Filling background for {chart}')
        fill_background(chart)
    


if __name__ == '__main__':
    main()

