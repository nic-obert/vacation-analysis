from typing import List
import cv2
import os


def get_all_charts() -> List[str]:
    charts = []
    for file in os.listdir('.'):
        if file.endswith('.png'):
            charts.append(file)
    return charts


def fill_background(chart: str) -> None:
    # Fill the transparent background with blue
    im = cv2.imread(chart, cv2.IMREAD_UNCHANGED)

    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if tuple(im[i, j]) == tuple([0, 0, 0, 0]):
                im[i, j] = [100, 0, 0, 255]

    cv2.imwrite(chart, im)


def main() -> None:
    
    charts = get_all_charts()
    for chart in charts:
        print(f'Filling background for {chart}')
        fill_background(chart)
    


if __name__ == '__main__':
    main()

