import sys
import re

new_markers = [
    # Terrain
    { 'name': 'Thái Hành Sơn', 'vi': 'Thái Hành Sơn Mạch', 'coords': [113.8, 37.1], 'type': 'terrain' },
    { 'name': 'Hoàng Thổ cao nguyên', 'vi': 'Cao nguyên Hoàng Thổ', 'coords': [108.5, 36.2], 'type': 'terrain' },
    { 'name': 'Tần Lĩnh', 'vi': 'Tần Lĩnh Sơn Mạch', 'coords': [107.8, 33.7], 'type': 'terrain' },
    { 'name': 'Thanh Tạng cao nguyên', 'vi': 'Thanh Tạng Cao Nguyên', 'coords': [94.0, 33.0], 'type': 'terrain' },
    { 'name': 'Trường Giang', 'vi': 'Sông Trường Giang', 'coords': [112.5, 29.8], 'type': 'terrain' },
    { 'name': 'Bồn địa Tứ Xuyên', 'vi': 'Bồn Địa Tứ Xuyên', 'coords': [105.5, 30.5], 'type': 'terrain' },
    { 'name': 'Thảo nguyên Mông Cổ', 'vi': 'Thảo nguyên Mạc Bắc', 'coords': [102.0, 48.0], 'type': 'terrain' },
    { 'name': 'Gobi', 'vi': 'Sa mạc Qua Bi', 'coords': [105.0, 43.0], 'type': 'terrain' },
    { 'name': 'Hoa Bắc bình nguyên', 'vi': 'Hoa Bắc Bình Nguyên', 'coords': [115.0, 37.0], 'type': 'terrain' },
    
    # Missing from lore
    { 'name': 'Hào Châu', 'vi': 'Hào Châu (Phượng Dương)', 'coords': [117.5, 32.9], 'type': 'city', 'faction': 'tianwan' },
    { 'name': 'Kiến Khang', 'vi': 'Kiến Khang (Trực Lệ)', 'coords': [118.78, 32.04], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Nam Xương', 'vi': 'Hồng Châu (Nam Xương)', 'coords': [115.89, 28.67], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Hán Khẩu', 'vi': 'Hán Dương/Hán Khẩu', 'coords': [114.28, 30.58], 'type': 'city', 'faction': 'tianwan' },
    { 'name': 'Lộ Châu', 'vi': 'Lộ Châu (Sơn Tây)', 'coords': [113.11, 36.19], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Quỳ Châu', 'vi': 'Quỳ Châu (Tứ Xuyên)', 'coords': [109.5, 31.0], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Thuận Khánh', 'vi': 'Thuận Khánh Phủ', 'coords': [106.0, 30.8], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Gia Định', 'vi': 'Gia Định Châu', 'coords': [103.7, 29.5], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Uy Sở', 'vi': 'Uy Sở (Vân Nam)', 'coords': [101.5, 25.0], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Bá Châu', 'vi': 'Bá Châu (Tứ Xuyên)', 'coords': [106.7, 31.8], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Cát Lâm', 'vi': 'Cát Lâm (Đông Bắc)', 'coords': [126.54, 43.83], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Đông Kinh', 'vi': 'Đông Kinh (Cao Ly)', 'coords': [129.2, 35.8], 'type': 'city', 'faction': 'goryeo' },
    { 'name': 'Tây Kinh', 'vi': 'Tây Kinh (Sơn Tây)', 'coords': [113.2, 40.0], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Sơn Hải Quan', 'vi': 'Sơn Hải Quan', 'coords': [119.7, 40.0], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Bờ sông Hoàng Hà', 'vi': 'Hà Nam Tây Bộ', 'coords': [110.0, 34.5], 'type': 'terrain'},

    # Screenshots: Hà Nam Giang Bắc
    { 'name': 'Lư Châu', 'vi': 'Lư Châu Lộ', 'coords': [117.28, 31.86], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'An Phong', 'vi': 'An Phong Lộ', 'coords': [116.71, 32.55], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Kỳ Châu', 'vi': 'Kỳ Châu', 'coords': [115.38, 30.23], 'type': 'city', 'faction': 'tianwan' },
    { 'name': 'Hoàng Châu', 'vi': 'Hoàng Châu Lộ', 'coords': [114.92, 30.45], 'type': 'city', 'faction': 'tianwan' },
    { 'name': 'Tín Dương', 'vi': 'Tín Dương Châu', 'coords': [114.07, 32.13], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Tương Dương', 'vi': 'Tương Dương Lộ', 'coords': [112.14, 32.04], 'type': 'city', 'faction': 'yuan' },

    # Screenshots: Giang Triết
    { 'name': 'Gia Hưng', 'vi': 'Gia Hưng Lộ', 'coords': [120.75, 30.76], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Thường Châu', 'vi': 'Thường Châu Lộ', 'coords': [119.97, 31.81], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Nhuận Châu', 'vi': 'Trấn Giang Lộ (Nhuận Châu)', 'coords': [119.46, 32.20], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Ninh Quốc', 'vi': 'Ninh Quốc Lộ', 'coords': [118.75, 30.95], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Huy Châu', 'vi': 'Huy Châu Lộ', 'coords': [118.33, 29.86], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Thai Châu', 'vi': 'Thai Châu Lộ', 'coords': [121.14, 28.89], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Ôn Châu', 'vi': 'Ôn Châu Lộ', 'coords': [120.69, 28.00], 'type': 'city', 'faction': 'yuan' },

    # Screenshots: Giang Tây
    { 'name': 'Cửu Giang', 'vi': 'Giang Châu Lộ (Cửu Giang)', 'coords': [115.99, 29.71], 'type': 'city', 'faction': 'tianwan' },
    { 'name': 'Nam Khang', 'vi': 'Nam Khang Lộ', 'coords': [116.03, 29.43], 'type': 'city', 'faction': 'tianwan' },
    { 'name': 'Lâm Giang', 'vi': 'Lâm Giang Lộ', 'coords': [115.54, 28.06], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Kiến Xương', 'vi': 'Kiến Xương Lộ', 'coords': [116.61, 27.56], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Phủ Châu', 'vi': 'Phủ Châu Lộ', 'coords': [116.35, 27.94], 'type': 'city', 'faction': 'yuan' },

    # Screenshots: Hồ Quảng
    { 'name': 'Nhạc Châu', 'vi': 'Nhạc Châu Lộ', 'coords': [113.12, 29.35], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Lễ Châu', 'vi': 'Lễ Châu Lộ', 'coords': [111.75, 29.63], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Đạo Châu', 'vi': 'Đạo Châu Lộ', 'coords': [111.57, 25.53], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Vĩnh Châu', 'vi': 'Vĩnh Châu Lộ', 'coords': [111.60, 26.22], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Toàn Châu', 'vi': 'Toàn Châu Lộ', 'coords': [111.07, 25.93], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Nam Ninh', 'vi': 'Vũ Duyên Xuyên (Nam Ninh)', 'coords': [108.31, 22.81], 'type': 'city', 'faction': 'yuan' },

    # Screenshots: Tứ Xuyên
    { 'name': 'Đồng Xuyên', 'vi': 'Đồng Xuyên Châu', 'coords': [105.08, 31.09], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Mã Hồ', 'vi': 'Mã Hồ Lộ', 'coords': [104.05, 28.61], 'type': 'city', 'faction': 'yuan' },

    # Screenshots: Vân Nam
    { 'name': 'Lâm An', 'vi': 'Lâm An Lộ', 'coords': [102.82, 23.63], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Sở Hùng', 'vi': 'Sở Hùng Lộ', 'coords': [101.52, 25.04], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Đằng Xung', 'vi': 'Đằng Xung Phủ', 'coords': [98.49, 25.02], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Lệ Giang', 'vi': 'Lệ Giang Lộ', 'coords': [100.22, 26.87], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Hạc Khánh', 'vi': 'Hạc Khánh Lộ', 'coords': [100.17, 26.55], 'type': 'city', 'faction': 'yuan' },

    # Screenshots: Thiểm Tây / Cam Túc / Sơn Tây
    { 'name': 'Củng Xương', 'vi': 'Củng Xương Lộ', 'coords': [104.61, 34.61], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Phượng Tường', 'vi': 'Phượng Tường Phủ', 'coords': [107.39, 34.52], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Bình Lương', 'vi': 'Bình Lương Phủ', 'coords': [106.68, 35.54], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Trạch Châu', 'vi': 'Trạch Châu Lộ', 'coords': [112.85, 35.50], 'type': 'city', 'faction': 'yuan' },

    # Screenshots: Hà Bắc / Sơn Đông
    { 'name': 'Đông Bình', 'vi': 'Đông Bình Lộ', 'coords': [116.30, 35.93], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Thái An', 'vi': 'Thái An Châu', 'coords': [117.12, 36.19], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Duyện Châu', 'vi': 'Duyện Châu', 'coords': [116.82, 35.53], 'type': 'city', 'faction': 'yuan' },
]

def update_test_html():
    with open('test.html', 'r', encoding='utf-8') as f:
        html = f.read()

    marker_strs = []
    for m in new_markers:
        faction_str = f", faction:'{m.get('faction', '')}'" if 'faction' in m else ""
        marker_strs.append(f"  {{ name:'{m['name']}', vi:'{m['vi']}', coords:[{m['coords'][0]},{m['coords'][1]}], type:'{m['type']}'{faction_str} }},\\n")

    insert_str = "\\n  // === Bổ Sung Thành Trì Vừa/Nhỏ & Địa Hình (Theo Screenshot) ===\\n" + "".join(marker_strs)

    # Find the Sukhothai line and array closing bracket
    idx = html.find('];')
    if idx != -1:
        # Search backwards safely from ]; finding the actual MARKERS end
        idx_markers_end = html.rfind(']', 0, idx+2)
        if idx_markers_end != -1:
            # wait, it's just `];` after the MARKERS list.
            match = re.search(r'}[\s\n]*];(?:\s*// Generative helpers)?', html)
            if match:
                idx_real = match.end() - len('];') - (len('// Generative helpers') if '// Generative helpers' in match.group() else 0) - (2 if match.group().endswith('];') else 0)
                # Actually, easier to simply replace ];\n\n// Generative helpers
                idx_gen = html.find('// Generative helpers')
                if idx_gen != -1:
                    insert_point = html.rfind(']', 0, idx_gen)
                    new_html = html[:insert_point] + insert_str + html[insert_point:]
                    with open('test.html', 'w', encoding='utf-8') as f:
                        f.write(new_html)
                    print('Injected markers to test.html successfully.')
                    return
        print('FAILED to precisely inject.')

def update_lore_js():
    with open('lore_1351.js', 'r', encoding='utf-8') as f:
        js = f.read()

    lorekeys = [x.strip() for x in re.findall(r'^\s*\'(.*?)\':', js, re.MULTILINE)]
    
    lore_entries = []
    for m in new_markers:
        name = m['name']
        if name in lorekeys:
            continue
        if m['type'] == 'city':
            lore = f"Thành trì quan trọng tại {m['vi'].split(' ')[0]}. Trong thời kỳ cuối Nguyên, nơi đây là trung tâm giao thương và quân sự cấp địa phương, đóng vai trò bản lề trên các trục giao thông chính."
        elif m['type'] == 'terrain':
            lore = f"Địa hình quan trọng, tạo thành phòng tuyến tự nhiên, ảnh hưởng lớn đến việc di chuyển quân đội và phân bổ lãnh thổ."
        lore_entries.append(f"    '{name}': {{\\n        desc: '{lore}',\\n        event: 'Chưa có sự kiện nổi bật trong năm 1351.'\\n    }},\\n")

    if lore_entries:
        insert_str = "\\n    // --- Bổ Sung Dữ Liệu Lore ---\\n" + "".join(lore_entries)
        idx = js.rfind('};')
        if idx != -1:
            new_js = js[:idx] + insert_str + js[idx:]
            with open('lore_1351.js', 'w', encoding='utf-8') as f:
                f.write(new_js)
            print('Injected lore to lore_1351.js successfully.')

update_test_html()
update_lore_js()
