def data_recovery(data):
	
    PNG = b'\x89PNG\r\n\x1a\n'      # PNG header
    JPEG = b'\xff\xd8\xff'           # JPEG header
    BMP = b'\x42\x4d'               # BMP header
    TIFF = b'\x49\x49\x2a\x00'       # TIFF header
    GIF = b'\x47\x49\x46\x38'       # GIF header
    ZIP = b'\x50\x4b\x03\x04'       # ZIP header
    ELF = b'\x7fELF'                # ELF header
    PDF = b'\x25\x50\x44\x46'       # PDF header
    MP3 = b'\x49\x44\x33'           # MP3 header
    MPEG = b'\xff\xfb'              # MPEG header
    PDDF = b'\x00\x00\x01\x00'      # PDDF header
    ICO = b'\x00\x01\x00\x00'      # ICO header
    result_list = []
    if PNG in data:
        result_list.append('PNG')
    if JPEG in data:
        result_list.append('JPEG')
    if BMP in data:
        result_list.append('BMP')
    if TIFF in data:
        result_list.append('TIFF')
    if GIF in data:
        result_list.append('GIF')
    if ZIP in data:
        result_list.append('ZIP')
    if ELF in data:
        result_list.append('ELF')
    if PDF in data:
        result_list.append('PDF')
    if MP3 in data:
        result_list.append('MP3')
    if MPEG in data:
        result_list.append('MPEG')
    if PDDF in data:
        result_list.append('PDDF')
    if ICO in data:
        result_list.append('ICO')

    return result_list

