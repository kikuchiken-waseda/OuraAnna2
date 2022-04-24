from csv import DictReader
import cv2
#from checkers import util

COLORMAP = {
    # CSS: #ffff8d
    "tng": (255, 255, 141),
    # CSS: #ff8a80
    "ulp": (255, 138, 128),
    # CSS: #ff80ab
    "llp": (255, 128, 171),
    # CSS: #80d8ff
    "plt": (128, 216, 255),
    # CSS: #ccff90
    "upw": (204, 255, 144),
    # CSS: #b9f6ca
    "atw": (185, 246, 202),
}


def get_color(label):
    rgb = COLORMAP[label[0:3]]
    return (rgb[2], rgb[1], rgb[0])


def parse(line):
    return (
        ((line["tng1x"], line["tng1y"]), get_color("tng")),
        ((line["tng2x"], line["tng2y"]), get_color("tng")),
        ((line["tng3x"], line["tng3y"]), get_color("tng")),
        ((line["tng4x"], line["tng4y"]), get_color("tng")),
        ((line["tng5x"], line["tng5y"]), get_color("tng")),
        ((line["tng6x"], line["tng6y"]), get_color("tng")),
        ((line["tng7x"], line["tng7y"]), get_color("tng")),
        ((line["tng8x"], line["tng8y"]), get_color("tng")),
        ((line["tng9x"], line["tng9y"]), get_color("tng")),
        ((line["tng10x"], line["tng10y"]), get_color("tng")),
        ((line["tng11x"], line["tng11y"]), get_color("tng")),
        ((line["tng12x"], line["tng12y"]), get_color("tng")),
        ((line["tng13x"], line["tng13y"]), get_color("tng")),
        ((line["tng14x"], line["tng14y"]), get_color("tng")),
        ((line["tng15x"], line["tng15y"]), get_color("tng")),
        ((line["tng16x"], line["tng16y"]), get_color("tng")),
        ((line["tng17x"], line["tng17y"]), get_color("tng")),
        ((line["tng18x"], line["tng18y"]), get_color("tng")),
        ((line["tng19x"], line["tng19y"]), get_color("tng")),
        ((line["tng20x"], line["tng20y"]), get_color("tng")),
        ((line["tng21x"], line["tng21y"]), get_color("tng")),
        ((line["tng22x"], line["tng22y"]), get_color("tng")),
        ((line["tng23x"], line["tng23y"]), get_color("tng")),
        ((line["tng24x"], line["tng24y"]), get_color("tng")),
        ((line["tng25x"], line["tng25y"]), get_color("tng")),
        ((line["tng26x"], line["tng26y"]), get_color("tng")),
        ((line["tng27x"], line["tng27y"]), get_color("tng")),
        ((line["tng28x"], line["tng28y"]), get_color("tng")),
        ((line["tng29x"], line["tng29y"]), get_color("tng")),
        ((line["tng30x"], line["tng30y"]), get_color("tng")),
        ((line["tng31x"], line["tng31y"]), get_color("tng")),
        ((line["tng32x"], line["tng32y"]), get_color("tng")),
        ((line["tng33x"], line["tng33y"]), get_color("tng")),
        ((line["tng34x"], line["tng34y"]), get_color("tng")),
        ((line["tng35x"], line["tng35y"]), get_color("tng")),
        ((line["tng36x"], line["tng36y"]), get_color("tng")),
        ((line["tng37x"], line["tng37y"]), get_color("tng")),
        ((line["tng38x"], line["tng38y"]), get_color("tng")),
        ((line["tng39x"], line["tng39y"]), get_color("tng")),
        ((line["tng40x"], line["tng40y"]), get_color("tng")),
        ((line["ulp1x"], line["ulp1y"]), get_color("ulp")),
        ((line["ulp2x"], line["ulp2y"]), get_color("ulp")),
        ((line["ulp3x"], line["ulp3y"]), get_color("ulp")),
        ((line["ulp4x"], line["ulp4y"]), get_color("ulp")),
        ((line["ulp5x"], line["ulp5y"]), get_color("ulp")),
        ((line["ulp6x"], line["ulp6y"]), get_color("ulp")),
        ((line["ulp7x"], line["ulp7y"]), get_color("ulp")),
        ((line["ulp8x"], line["ulp8y"]), get_color("ulp")),
        ((line["ulp9x"], line["ulp9y"]), get_color("ulp")),
        ((line["ulp10x"], line["ulp10y"]), get_color("ulp")),
        ((line["ulp11x"], line["ulp11y"]), get_color("ulp")),
        ((line["ulp12x"], line["ulp12y"]), get_color("ulp")),
        ((line["ulp13x"], line["ulp13y"]), get_color("ulp")),
        ((line["ulp14x"], line["ulp14y"]), get_color("ulp")),
        ((line["ulp15x"], line["ulp15y"]), get_color("ulp")),
        ((line["llp1x"], line["llp1y"]), get_color("llp")),
        ((line["llp2x"], line["llp2y"]), get_color("llp")),
        ((line["llp3x"], line["llp3y"]), get_color("llp")),
        ((line["llp4x"], line["llp4y"]), get_color("llp")),
        ((line["llp5x"], line["llp5y"]), get_color("llp")),
        ((line["llp6x"], line["llp6y"]), get_color("llp")),
        ((line["llp7x"], line["llp7y"]), get_color("llp")),
        ((line["llp8x"], line["llp8y"]), get_color("llp")),
        ((line["llp9x"], line["llp9y"]), get_color("llp")),
        ((line["llp10x"], line["llp10y"]), get_color("llp")),
        ((line["llp11x"], line["llp11y"]), get_color("llp")),
        ((line["llp12x"], line["llp12y"]), get_color("llp")),
        ((line["llp13x"], line["llp13y"]), get_color("llp")),
        ((line["llp14x"], line["llp14y"]), get_color("llp")),
        ((line["llp15x"], line["llp15y"]), get_color("llp")),
        ((line["llp16x"], line["llp16y"]), get_color("llp")),
        ((line["llp17x"], line["llp17y"]), get_color("llp")),
        ((line["llp18x"], line["llp18y"]), get_color("llp")),
        ((line["llp19x"], line["llp19y"]), get_color("llp")),
        ((line["llp20x"], line["llp20y"]), get_color("llp")),
        ((line["llp21x"], line["llp21y"]), get_color("llp")),
        ((line["llp22x"], line["llp22y"]), get_color("llp")),
        ((line["llp23x"], line["llp23y"]), get_color("llp")),
        ((line["llp24x"], line["llp24y"]), get_color("llp")),
        ((line["llp25x"], line["llp25y"]), get_color("llp")),
        ((line["plt1x"], line["plt1y"]), get_color("plt")),
        ((line["plt2x"], line["plt2y"]), get_color("plt")),
        ((line["plt3x"], line["plt3y"]), get_color("plt")),
        ((line["plt4x"], line["plt4y"]), get_color("plt")),
        ((line["plt5x"], line["plt5y"]), get_color("plt")),
        ((line["plt6x"], line["plt6y"]), get_color("plt")),
        ((line["plt7x"], line["plt7y"]), get_color("plt")),
        ((line["plt8x"], line["plt8y"]), get_color("plt")),
        ((line["plt9x"], line["plt9y"]), get_color("plt")),
        ((line["plt10x"], line["plt10y"]), get_color("plt")),
        ((line["plt11x"], line["plt11y"]), get_color("plt")),
        ((line["plt12x"], line["plt12y"]), get_color("plt")),
        ((line["plt13x"], line["plt13y"]), get_color("plt")),
        ((line["plt14x"], line["plt14y"]), get_color("plt")),
        ((line["plt15x"], line["plt15y"]), get_color("plt")),
        ((line["plt16x"], line["plt16y"]), get_color("plt")),
        ((line["plt17x"], line["plt17y"]), get_color("plt")),
        ((line["plt18x"], line["plt18y"]), get_color("plt")),
        ((line["plt19x"], line["plt19y"]), get_color("plt")),
        ((line["plt20x"], line["plt20y"]), get_color("plt")),
        ((line["plt21x"], line["plt21y"]), get_color("plt")),
        ((line["plt22x"], line["plt22y"]), get_color("plt")),
        ((line["plt23x"], line["plt23y"]), get_color("plt")),
        ((line["plt24x"], line["plt24y"]), get_color("plt")),
        ((line["plt25x"], line["plt25y"]), get_color("plt")),
        ((line["plt26x"], line["plt26y"]), get_color("plt")),
        ((line["plt27x"], line["plt27y"]), get_color("plt")),
        ((line["plt28x"], line["plt28y"]), get_color("plt")),
        ((line["plt29x"], line["plt29y"]), get_color("plt")),
        ((line["plt30x"], line["plt30y"]), get_color("plt")),
        ((line["upw1x"], line["upw1y"]), get_color("upw")),
        ((line["upw2x"], line["upw2y"]), get_color("upw")),
        ((line["upw3x"], line["upw3y"]), get_color("upw")),
        ((line["upw4x"], line["upw4y"]), get_color("upw")),
        ((line["upw5x"], line["upw5y"]), get_color("upw")),
        ((line["upw6x"], line["upw6y"]), get_color("upw")),
        ((line["upw7x"], line["upw7y"]), get_color("upw")),
        ((line["upw8x"], line["upw8y"]), get_color("upw")),
        ((line["upw9x"], line["upw9y"]), get_color("upw")),
        ((line["upw10x"], line["upw10y"]), get_color("upw")),
        ((line["upw11x"], line["upw11y"]), get_color("upw")),
        ((line["upw12x"], line["upw12y"]), get_color("upw")),
        ((line["upw13x"], line["upw13y"]), get_color("upw")),
        ((line["upw14x"], line["upw14y"]), get_color("upw")),
        ((line["upw15x"], line["upw15y"]), get_color("upw")),
        ((line["upw16x"], line["upw16y"]), get_color("upw")),
        ((line["upw17x"], line["upw17y"]), get_color("upw")),
        ((line["upw18x"], line["upw18y"]), get_color("upw")),
        ((line["upw19x"], line["upw19y"]), get_color("upw")),
        ((line["upw20x"], line["upw20y"]), get_color("upw")),
        ((line["upw21x"], line["upw21y"]), get_color("upw")),
        ((line["upw22x"], line["upw22y"]), get_color("upw")),
        ((line["upw23x"], line["upw23y"]), get_color("upw")),
        ((line["upw24x"], line["upw24y"]), get_color("upw")),
        ((line["upw25x"], line["upw25y"]), get_color("upw")),
        ((line["upw26x"], line["upw26y"]), get_color("upw")),
        ((line["upw27x"], line["upw27y"]), get_color("upw")),
        ((line["upw28x"], line["upw28y"]), get_color("upw")),
        ((line["atw1x"], line["atw1y"]), get_color("atw")),
        ((line["atw2x"], line["atw2y"]), get_color("atw")),
        ((line["atw3x"], line["atw3y"]), get_color("atw")),
        ((line["atw4x"], line["atw4y"]), get_color("atw")),
        ((line["atw5x"], line["atw5y"]), get_color("atw")),
        ((line["atw6x"], line["atw6y"]), get_color("atw")),
        ((line["atw7x"], line["atw7y"]), get_color("atw")),
        ((line["atw8x"], line["atw8y"]), get_color("atw")),
        ((line["atw9x"], line["atw9y"]), get_color("atw")),
        ((line["atw10x"], line["atw10y"]), get_color("atw")),
        ((line["atw11x"], line["atw11y"]), get_color("atw")),
        ((line["atw12x"], line["atw12y"]), get_color("atw")),
        ((line["atw13x"], line["atw13y"]), get_color("atw")),
        ((line["atw14x"], line["atw14y"]), get_color("atw")),
        ((line["atw15x"], line["atw15y"]), get_color("atw")),
        ((line["atw16x"], line["atw16y"]), get_color("atw")),
        ((line["atw17x"], line["atw17y"]), get_color("atw")),
        ((line["atw18x"], line["atw18y"]), get_color("atw")),
        ((line["atw19x"], line["atw19y"]), get_color("atw")),
        ((line["atw20x"], line["atw20y"]), get_color("atw")),
        ((line["atw21x"], line["atw21y"]), get_color("atw")),
        ((line["atw22x"], line["atw22y"]), get_color("atw")),
        ((line["atw23x"], line["atw23y"]), get_color("atw")),
        ((line["atw24x"], line["atw24y"]), get_color("atw")),
        ((line["atw25x"], line["atw25y"]), get_color("atw")),
        ((line["atw26x"], line["atw26y"]), get_color("atw")),
        ((line["atw27x"], line["atw27y"]), get_color("atw")),
        ((line["atw28x"], line["atw28y"]), get_color("atw")),
        ((line["atw29x"], line["atw29y"]), get_color("atw")),
        ((line["atw30x"], line["atw30y"]), get_color("atw")),
    )


def addPoint(src, row, dist):
    im = src.copy()
    for x in row:
        center = (int(x[0][0]), int(x[0][1]))
        color = x[1]
        cv2.circle(
            im,
            center,
            1,
            color,
            thickness=1,
            lineType=cv2.LINE_8,
            shift=0
        )
    cv2.imwrite(str(dist), im)


def load_csv(src):
    with open(src, 'r', encoding="utf-8_sig") as f:
        rows = [parse(row) for row in DictReader(f)]
    return rows


def load_image(date, subject, dicom_id, i):
    #conf = util.loadConf()
    #root = conf.get("CORPORA")
    work_dir = root.joinpath(str(date), str(subject))
    png_dir = work_dir.joinpath("png")
    input_dir = png_dir.joinpath("luminance_numbered")
    fname = "{}_{}.png".format(dicom_id, str(i).zfill(4))
    src = input_dir.joinpath(dicom_id, fname)
    if src.exists():
        output_dir = png_dir.joinpath(
            "luminance_numbered_pointed", dicom_id
        )
        output_dir.mkdir(parents=True, exist_ok=True)
        dist = output_dir.joinpath(fname)
        return cv2.imread(str(src)), dist
    else:
        print("該当のファイルは存在しません: {}".format(src))


if __name__ == "__main__":
    from argparse import ArgumentParser
    from tqdm import tqdm

    """
    parser = ArgumentParser()
    parser.add_argument(
        "-d", '--day', help='収録日', type=str, required=True
    )
    parser.add_argument(
        "-u", '--user', help='収録対象', type=str, required=True
    )
    args = parser.parse_args()
    date = args.day  # "20171110"
    subject = args.user  # "Maekawa"

    conf = util.loadConf()
    root = conf.get("CORPORA") """

    csv_file = './data/20171110/Maekawa/xy/s1_4.xy'
    png_dir = './data/20171110/Maekawa/png/luminance/4/'

    work_dir = root.joinpath(str(date), str(subject))
    xy_dir = work_dir.joinpath("xy")
    for xy in tqdm(xy_dir.glob("*.xy")):
        dicom_id = xy.stem
        for i, x in enumerate(load_csv(xy)):
            src, dist = load_image(date, subject, dicom_id, i) # 日付、被験者名、xyのディレクトリの拡張子？、フレーム
            addPoint(src, x, dist)
