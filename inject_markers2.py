import sys
import re

new_markers2 = [
    # Cam Túc / Tân Cương / Qua Lang
    { 'name': 'Cáp Mật', 'vi': 'Cáp Mật Vệ', 'coords': [93.5, 42.8], 'type': 'city', 'faction': 'chagatai' },
    { 'name': 'Thổ Lỗ Phồn', 'vi': 'Cao Xương (Thổ Lỗ Phồn)', 'coords': [89.1, 42.9], 'type': 'city', 'faction': 'chagatai' },
    { 'name': 'Đôn Hoàng', 'vi': 'Sa Châu (Đôn Hoàng)', 'coords': [94.6, 40.1], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Trương Dịch', 'vi': 'Cam Châu (Trương Dịch)', 'coords': [100.4, 38.9], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Vũ Uy', 'vi': 'Lương Châu (Vũ Uy)', 'coords': [102.6, 37.9], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Thiên Thủy', 'vi': 'Tần Châu (Thiên Thủy)', 'coords': [105.7, 34.5], 'type': 'city', 'faction': 'yuan' },

    # Quảng Đông / Quảng Tây
    { 'name': 'Lôi Châu', 'vi': 'Lôi Châu Lộ', 'coords': [110.1, 20.9], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Khâm Châu', 'vi': 'Khâm Châu Lộ', 'coords': [108.6, 21.9], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Triệu Khánh', 'vi': 'Đoan Châu (Triệu Khánh)', 'coords': [112.4, 23.0], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Huệ Châu', 'vi': 'Huệ Châu Lộ', 'coords': [114.4, 23.1], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Tân Châu', 'vi': 'Tân Châu (Quảng Tây)', 'coords': [109.5, 23.7], 'type': 'city', 'faction': 'yuan' },
    
    # Phúc Kiến
    { 'name': 'Diên Bình', 'vi': 'Diên Bình Lộ', 'coords': [118.1, 26.6], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Đinh Châu', 'vi': 'Đinh Châu Lộ', 'coords': [116.3, 25.8], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Hưng Hoá', 'vi': 'Hưng Hoá Lộ (Bồ Điền)', 'coords': [119.0, 25.4], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Thiệu Vũ', 'vi': 'Thiệu Vũ Lộ', 'coords': [117.4, 27.3], 'type': 'city', 'faction': 'yuan' },
    
    # Hà Nam / Giang Bắc further
    { 'name': 'Khánh Dương', 'vi': 'Khánh Dương Phủ', 'coords': [107.6, 36.1], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Lạc Dương', 'vi': 'Hà Nam Phủ (Lạc Dương)', 'coords': [112.4, 34.6], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Uyển Câu', 'vi': 'Hứa Châu', 'coords': [113.8, 34.0], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Nhữ Châu', 'vi': 'Nhữ Châu', 'coords': [112.8, 34.1], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Bạc Châu', 'vi': 'Bạc Châu', 'coords': [115.7, 33.8], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Trần Châu', 'vi': 'Trần Châu (Hoài Dương)', 'coords': [114.8, 33.7], 'type': 'city', 'faction': 'yuan' },
    
    # Sơn Tây / Hà Bắc / Sơn Đông further
    { 'name': 'Đại Tăng', 'vi': 'Cát Châu (Sơn Tây)', 'coords': [110.6, 36.1], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Phân Châu', 'vi': 'Phân Châu (Sơn Tây)', 'coords': [111.7, 37.2], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Thuận Đức', 'vi': 'Thuận Đức Lộ (Hình Đài)', 'coords': [114.5, 37.0], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Quảng Bình', 'vi': 'Quảng Bình Lộ', 'coords': [114.8, 36.6], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Đại Danh', 'vi': 'Đại Danh Lộ', 'coords': [115.1, 36.2], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Cao Mật', 'vi': 'Mật Châu (Sơn Đông)', 'coords': [119.7, 35.9], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Cử Châu', 'vi': 'Cử Châu (Sơn Đông)', 'coords': [118.8, 35.5], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Tế Ninh', 'vi': 'Tế Ninh Lộ', 'coords': [116.5, 35.4], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Từ Châu', 'vi': 'Từ Châu Lộ', 'coords': [117.1, 34.2], 'type': 'city', 'faction': 'yuan' },
    
    # Tứ Xuyên / Vân Nam further
    { 'name': 'Bảo Ninh', 'vi': 'Bảo Ninh Lộ (Lãng Trung)', 'coords': [105.9, 31.5], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Tuyên Hóa', 'vi': 'Tuyên Hóa Lộ', 'coords': [115.0, 40.6], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Vĩnh Xương', 'vi': 'Vĩnh Xương Phủ', 'coords': [99.1, 25.1], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Vũ Định', 'vi': 'Vũ Định Lộ', 'coords': [102.4, 25.5], 'type': 'city', 'faction': 'yuan' },
    { 'name': 'Quảng Nam', 'vi': 'Quảng Nam Tây Lộ', 'coords': [105.0, 24.0], 'type': 'city', 'faction': 'yuan' },
    
    # Terrain Ext
    { 'name': 'Hoàng Hà', 'vi': 'Sông Hoàng Hà', 'coords': [110.0, 35.8], 'type': 'terrain' },
    { 'name': 'Đại Vận Hà', 'vi': 'Đại Vận Hà', 'coords': [119.0, 31.8], 'type': 'terrain' },
    { 'name': 'Động Đình Hồ', 'vi': 'Động Đình Hồ', 'coords': [112.9, 29.3], 'type': 'terrain' },
    { 'name': 'Phàn Dương Hồ', 'vi': 'Hồ Phiên Dương', 'coords': [116.2, 29.1], 'type': 'terrain' },
    { 'name': 'Ngũ Đài Sơn', 'vi': 'Ngũ Đài Sơn', 'coords': [113.5, 39.0], 'type': 'terrain' },
    { 'name': 'Lão Đầu Sơn', 'vi': 'Dãy Trường Bạch', 'coords': [128.0, 42.0], 'type': 'terrain' }
]

def update_test_html2():
    with open('test.html', 'r', encoding='utf-8') as f:
        html = f.read()

    marker_strs = []
    for m in new_markers2:
        faction_str = f", faction:'{m.get('faction', '')}'" if 'faction' in m else ""
        marker_strs.append(f"  {{ name:'{m['name']}', vi:'{m['vi']}', coords:[{m['coords'][0]},{m['coords'][1]}], type:'{m['type']}'{faction_str} }},\\n")

    insert_str = "\\n  // === Bổ Sung Đợt 2 (Đạt Mốc 206 Markers) ===\\n" + "".join(marker_strs)

    # Insert right at the end before ]; avoiding regex overlap issues.
    # Find the last `}` before `];`
    idx = html.find('];\\n\\n  // === Bổ Sung')
    if idx == -1: idx = html.find('// === Bổ Sung Thành Trì Vừa/Nhỏ')
    
    # The safest way: find } \n ];
    idx = html.rfind('}\\n];')
    if idx == -1: idx = html.rfind('},开发\\n];')
    if idx == -1: idx = html.rfind('}\\n  // ===')
    if idx == -1:
        # Just find the ending block of MARKERS array.
        idx = html.rfind('];', 0, html.find('Generative helpers'))
        
    if idx != -1:
        # go right before ]
        insert_point = html.rfind(']', 0, idx+2)
        new_html = html[:insert_point] + insert_str + html[insert_point:]
        with open('test.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print('Injected markers 2 to test.html successfully.')
    else:
        print('FAILED to precisely inject phase 2.')

def update_lore_js2():
    with open('lore_1351.js', 'r', encoding='utf-8') as f:
        js = f.read()

    lorekeys = [x.strip() for x in re.findall(r'^\s*\'(.*?)\':', js, re.MULTILINE)]
    
    lore_entries = []
    for m in new_markers2:
        name = m['name']
        if name in lorekeys:
            continue
        if m['type'] == 'city':
            lore = f"Địa danh thuộc {m['vi']}. Đóng vai trò thiết yếu trong việc kiểm soát cục diện nội chiến và tuyến cung ứng của nhà Nguyên."
        elif m['type'] == 'terrain':
            lore = f"Đại hình tự nhiên chiến lược trọng yếu, quyết định khả năng chuyển quân nhanh của kỵ binh và thủy chiến."
        lore_entries.append(f"    '{name}': {{\\n        desc: '{lore}',\\n        event: 'Chưa có sự kiện nổi bật trong năm 1351.'\\n    }},\\n")

    if lore_entries:
        insert_str = "\\n    // --- Bổ Sung Dữ Liệu Lore Đợt 2 ---\\n" + "".join(lore_entries)
        idx = js.rfind('};')
        if idx != -1:
            new_js = js[:idx] + insert_str + js[idx:]
            with open('lore_1351.js', 'w', encoding='utf-8') as f:
                f.write(new_js)
            print('Injected lore 2 to lore_1351.js successfully.')

update_test_html2()
update_lore_js2()
