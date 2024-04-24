import matplotlib.pyplot as plt


def main():
    #img = plt.imread("files/img0.png")[:, :, 0]
    #img = plt.imread("files/img1.png")[:, :, 0]
    img = plt.imread("files/img2.png")[:, :, 0]

    # img = floodfill(img, 0, 0)
    print(img)
    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(1)
    plt.clf()

    flood_fill(img, 0, 0)

def flood_fill(img , x ,y):
    if x > img.shape[0]-1 or y > img.shape[1]-1 or x<0 or y<0:

        return img

    if img[x ,y ] == 1:
        img[x,y] =2
        plt.imshow(img, cmap="gray")
        plt.show(block=False)
        plt.pause(0.01)
        plt.clf()
        img = flood_fill(img , x+1,y)
        img = flood_fill(img, x - 1, y)
        img = flood_fill(img, x , y+1)
        img = flood_fill(img, x , y-1)

        print(img)
        return img
    else:
        return img




if __name__ == "__main__":
    main()
