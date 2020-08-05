def get_slider_offset(image_url, image_url_bg, css):

　　image_file = io.BytesIO(requests.get(image_url).content)

　　im = Image.open(image_file)

　　image_file_bg = io.BytesIO(requests.get(image_url_bg).content)

　　im_bg = Image.open(image_file_bg)

　　# 10*58 26/row => background image size = 260*116

　　captcha = Image.new('RGB', (260, 116))

　　captcha_bg = Image.new('RGB', (260, 116))

　　for i, px in enumerate(css):

  　　offset = convert_css_to_offset(px)

  　　region = im.crop(offset)

  　　region_bg = im_bg.crop(offset)

  　　offset = convert_index_to_offset(i)

  　　captcha.paste(region, offset)

  　　captcha_bg.paste(region_bg, offset)

　　diff = ImageChops.difference(captcha, captcha_bg)

　　return get_slider_offset_from_diff_image(diff)