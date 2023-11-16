def assess_image_quality(image_url):
    try:
        response = requests.get(image_url)
        img_bytes = BytesIO(response.content)
        img_array = np.asarray(bytearray(img_bytes.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # Assess image blur
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur_value = cv2.Laplacian(gray, cv2.CV_64F).var()
        if blur_value < 100:
            img_quality = {"img":"blurry"}
            return img_quality
        else:
            img_quality = {"img":"ok"}
            return img_quality
async def mainDetect(url):
    try:
        quality = assess_image_quality(url)
        if quality["img"] == "ok":
            result = await detect_sequence(url)
        else:
            r = {"AI":"blurry image"}
            result = json.dumps(r)
        return result
    finally:
        torch.cuda.empty_cache()
        pass
