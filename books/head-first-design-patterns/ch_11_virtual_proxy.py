class Icon:
    @property
    def width(self) -> int:
        raise NotImplementedError

    @property
    def height(self) -> int:
        raise NotImplementedError

    def paint_icon(self) -> None:
        raise NotImplementedError


class ImageIcon(Icon):
    @property
    def width(self) -> int:
        return 1280

    @property
    def height(self) -> int:
        return 720

    def paint_icon(self) -> None:
        print(":)")


class ImageProxy(Icon):
    def __init__(self, url: str):
        self._image_icon = None
        self._url = url

    # Following 'if' statements can be reworked to use The State Pattern: ImageNotLoaded and ImageLoaded
    @property
    def width(self) -> int:
        return self._image_icon.width if self._image_icon else 600

    @property
    def height(self) -> int:
        return self._image_icon.height if self._image_icon else 800

    def paint_icon(self) -> None:
        if not self._image_icon:
            # Download image from the internet
            print(f"Downloading the image from '{self._url}'")
            self._image_icon = ImageIcon()
        self._image_icon.paint_icon()


image = ImageProxy("whatever://image")
image.paint_icon()
