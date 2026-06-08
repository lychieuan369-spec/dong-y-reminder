# -*- coding: utf-8 -*-
Q2 = [
    # ============================================================
    # SECTION 1: 14 KINH CHÍNH + HUYỆT ĐẶC BIỆT (40 câu)
    # ============================================================

    # Số huyệt mỗi kinh
    {"q": "Kinh Thủ Thái Âm Phế có bao nhiêu huyệt?", "opts": {"A": "9", "B": "11", "C": "21", "D": "27"}, "ans": "B"},
    {"q": "Kinh Thủ Dương Minh Đại Trường có bao nhiêu huyệt?", "opts": {"A": "18", "B": "20", "C": "22", "D": "27"}, "ans": "B"},
    {"q": "Kinh Túc Dương Minh Vị có bao nhiêu huyệt?", "opts": {"A": "36", "B": "42", "C": "45", "D": "48"}, "ans": "C"},
    {"q": "Kinh Túc Thái Âm Tỳ có bao nhiêu huyệt?", "opts": {"A": "19", "B": "21", "C": "25", "D": "27"}, "ans": "B"},
    {"q": "Kinh Thủ Thiếu Âm Tâm có bao nhiêu huyệt?", "opts": {"A": "7", "B": "9", "C": "11", "D": "13"}, "ans": "B"},
    {"q": "Kinh Thủ Thái Dương Tiểu Trường có bao nhiêu huyệt?", "opts": {"A": "17", "B": "19", "C": "21", "D": "23"}, "ans": "B"},
    {"q": "Kinh Túc Thái Dương Bàng Quang có bao nhiêu huyệt?", "opts": {"A": "54", "B": "60", "C": "63", "D": "67"}, "ans": "D"},
    {"q": "Kinh Túc Thiếu Âm Thận có bao nhiêu huyệt?", "opts": {"A": "25", "B": "27", "C": "29", "D": "31"}, "ans": "B"},
    {"q": "Kinh Thủ Quyết Âm Tâm Bào có bao nhiêu huyệt?", "opts": {"A": "7", "B": "9", "C": "11", "D": "13"}, "ans": "B"},
    {"q": "Kinh Thủ Thiếu Dương Tam Tiêu có bao nhiêu huyệt?", "opts": {"A": "21", "B": "23", "C": "25", "D": "27"}, "ans": "B"},
    {"q": "Kinh Túc Thiếu Dương Đởm có bao nhiêu huyệt?", "opts": {"A": "42", "B": "44", "C": "46", "D": "48"}, "ans": "B"},
    {"q": "Kinh Túc Quyết Âm Can có bao nhiêu huyệt?", "opts": {"A": "11", "B": "13", "C": "14", "D": "16"}, "ans": "C"},
    {"q": "Mạch Đốc có bao nhiêu huyệt?", "opts": {"A": "26", "B": "28", "C": "30", "D": "32"}, "ans": "B"},
    {"q": "Mạch Nhâm có bao nhiêu huyệt?", "opts": {"A": "22", "B": "24", "C": "26", "D": "28"}, "ans": "B"},
    {"q": "Tổng số huyệt của 14 kinh chính là bao nhiêu?", "opts": {"A": "309", "B": "349", "C": "361", "D": "365"}, "ans": "C"},

    # Huyệt quan trọng - đầu kinh, cuối kinh, đặc biệt
    {"q": "Huyệt đầu tiên của kinh Phế là huyệt nào?", "opts": {"A": "Thiếu Thương", "B": "Thái Uyên", "C": "Trung Phủ", "D": "Việt Tuyền"}, "ans": "C"},
    {"q": "Huyệt cuối cùng của kinh Phế là huyệt nào?", "opts": {"A": "Thiếu Thương", "B": "Kinh Cừ", "C": "Thái Uyên", "D": "Xích Trạch"}, "ans": "A"},
    {"q": "Huyệt Hợp Cốc thuộc kinh nào?", "opts": {"A": "Tam Tiêu", "B": "Đại Trường", "C": "Vị", "D": "Tiểu Trường"}, "ans": "B"},
    {"q": "Huyệt Túc Tam Lý thuộc kinh nào?", "opts": {"A": "Vị", "B": "Tỳ", "C": "Thận", "D": "Bàng Quang"}, "ans": "A"},
    {"q": "Huyệt Nội Quan thuộc kinh nào?", "opts": {"A": "Tâm Bào", "B": "Tam Tiêu", "C": "Tâm", "D": "Phế"}, "ans": "A"},
    {"q": "Huyệt Nghị Phong thuộc kinh nào?", "opts": {"A": "Đởm", "B": "Tam Tiêu", "C": "Bàng Quang", "D": "Vị"}, "ans": "B"},
    {"q": "Huyệt Bách Hội (GV20) có vị trí ở đâu?", "opts": {"A": "Giữa đỉnh đầu", "B": "Phía trước đỉnh đầu", "C": "Giữa trán", "D": "Sau chân mày"}, "ans": "A"},
    {"q": "Huyệt Quan Nguyên (CV4) thuộc kinh nào?", "opts": {"A": "Mạch Đốc", "B": "Mạch Nhâm", "C": "Kinh Tỳ", "D": "Kinh Thận"}, "ans": "B"},
    {"q": "Huyệt Nhân Trung (GV26) dùng trong trường hợp nào?", "opts": {"A": "Hô hấp", "B": "Cấp cứu hôn mê", "C": "Đau bụng", "D": "Đau khớp"}, "ans": "B"},
    {"q": "Huyệt Phong Thị (GB31) thuộc kinh nào?", "opts": {"A": "Bàng Quang", "B": "Đởm", "C": "Vị", "D": "Tỳ"}, "ans": "B"},
    {"q": "Huyệt nào là giao hội giữa Mạch Đốc và kinh Tỳ?", "opts": {"A": "Hội Âm", "B": "Trung Cực", "C": "Bách Hội", "D": "Trung Quản"}, "ans": "A"},
    {"q": "Huyệt dương giao hội chính của tam kinh dương tay là huyệt nào?", "opts": {"A": "Ngoại Quan", "B": "Đại Chùy", "C": "Phong Thị", "D": "Túc Tam Lý"}, "ans": "B"},
    {"q": "Huyệt Dương Lăng Tuyền (GB34) có đặc điểm gì đặc biệt?", "opts": {"A": "Hợp huyệt", "B": "Hội của Cân", "C": "Hội của Cơ", "D": "Cả A và C"}, "ans": "D"},
    {"q": "Huyệt Thái Khê thuộc kinh nào?", "opts": {"A": "Phế", "B": "Tỳ", "C": "Thận", "D": "Can"}, "ans": "C"},
    {"q": "Huyệt Thái Xung thuộc kinh nào?", "opts": {"A": "Tỳ", "B": "Đởm", "C": "Can", "D": "Vị"}, "ans": "C"},
    {"q": "Huyệt Niệu Quản (BL40) là huyệt gì của kinh Bàng Quang?", "opts": {"A": "Nguyên huyệt", "B": "Hợp huyệt", "C": "Kinh huyệt", "D": "Khích huyệt"}, "ans": "B"},
    {"q": "Huyệt Phong Long (ST40) là loại huyệt gì của kinh Vị?", "opts": {"A": "Lạc huyệt", "B": "Nguyên huyệt", "C": "Khích huyệt", "D": "Du huyệt"}, "ans": "A"},
    {"q": "Huyệt Tam Âm Giao (SP6) là giao điểm của những kinh nào?", "opts": {"A": "Tỳ, Thận, Can", "B": "Tỳ, Vị, Phế", "C": "Can, Đởm, Tỳ", "D": "Thận, Bàng Quang, Tâm"}, "ans": "A"},
    {"q": "Huyệt Hậu Khê (SI3) thông với mạch nào?", "opts": {"A": "Mạch Nhâm", "B": "Mạch Đốc", "C": "Đới Mạch", "D": "Âm Duy Mạch"}, "ans": "B"},
    {"q": "Huyệt Liệt Khuyết (LU7) thông với mạch nào?", "opts": {"A": "Mạch Đốc", "B": "Mạch Nhâm", "C": "Xung Mạch", "D": "Đới Mạch"}, "ans": "B"},
    {"q": "Huyệt Ấn Đường (EX-HN3) còn được gọi là gì?", "opts": {"A": "An Miên", "B": "Yin Tang", "C": "Si Zhu Kong", "D": "Tai Yang"}, "ans": "B"},

    # ============================================================
    # SECTION 2: NGŨ DU HUYỆT - TỈNH/HUỲNH/DU/KINH/HỢP (25 câu)
    # ============================================================

    {"q": "Ngũ du huyệt theo thứ tự từ đầu chi là?", "opts": {"A": "Tỉnh-Huỳnh-Du-Kinh-Hợp", "B": "Hợp-Kinh-Du-Huỳnh-Tỉnh", "C": "Tỉnh-Du-Huỳnh-Kinh-Hợp", "D": "Huỳnh-Tỉnh-Du-Kinh-Hợp"}, "ans": "A"},
    {"q": "Tỉnh huyệt là huyệt ở vị trí nào?", "opts": {"A": "Gần khớp khuỷu", "B": "Đầu ngón tay/chân", "C": "Giữa cánh tay", "D": "Cổ tay/cổ chân"}, "ans": "B"},
    {"q": "Tỉnh huyệt thuộc hành nào của kinh âm?", "opts": {"A": "Hành Mộc", "B": "Hành Hỏa", "C": "Hành Thổ", "D": "Hành Kim"}, "ans": "A"},
    {"q": "Tỉnh huyệt thuộc hành nào của kinh dương?", "opts": {"A": "Hành Mộc", "B": "Hành Hỏa", "C": "Hành Kim", "D": "Hành Thủy"}, "ans": "C"},
    {"q": "Huỳnh huyệt (Ying spring) dùng trị chứng gì chủ yếu?", "opts": {"A": "Bệnh mạn tính", "B": "Sốt nóng, bệnh ở phần", "C": "Hô hấp cấp", "D": "Đau xương khớp"}, "ans": "B"},
    {"q": "Du huyệt (Shu stream) dùng trị chứng gì chủ yếu?", "opts": {"A": "Chứng nặng, ẩm ướt đau khớp", "B": "Sốt cao", "C": "Bệnh mạn tính tạng phủ", "D": "Mất ngủ"}, "ans": "A"},
    {"q": "Kinh huyệt (Jing river) dùng trị chứng gì chủ yếu?", "opts": {"A": "Hô hấp, ho, khàn tiếng", "B": "Sốt nóng", "C": "Đau dạ dày bụng", "D": "Tiểu tiện"}, "ans": "A"},
    {"q": "Hợp huyệt (He sea) dùng trị chứng gì chủ yếu?", "opts": {"A": "Bệnh ngoại cảm", "B": "Bệnh ở các phủ tạng, phủ", "C": "Bệnh ở giao", "D": "Bệnh ở kinh mạch"}, "ans": "B"},
    {"q": "Tỉnh huyệt của kinh Phế là huyệt nào?", "opts": {"A": "Thiếu Thương", "B": "Ngư Tế", "C": "Thái Uyên", "D": "Kinh Cừ"}, "ans": "A"},
    {"q": "Huỳnh huyệt của kinh Phế là huyệt nào?", "opts": {"A": "Thiếu Thương", "B": "Ngư Tế", "C": "Thái Uyên", "D": "Kinh Cừ"}, "ans": "B"},
    {"q": "Hợp huyệt của kinh Tâm là huyệt nào?", "opts": {"A": "Thiếu Hải", "B": "Thiếu Phủ", "C": "Thần Môn", "D": "Thông Lý"}, "ans": "A"},
    {"q": "Hợp huyệt của kinh Đại Trường là huyệt nào?", "opts": {"A": "Hợp Cốc", "B": "Khúc Trì", "C": "Dũng Tuyền", "D": "Ngoại Quan"}, "ans": "B"},
    {"q": "Hợp huyệt của kinh Tiểu Trường là huyệt nào?", "opts": {"A": "Tiểu Hải", "B": "Hậu Khê", "C": "Nhân Tông", "D": "Yang Lao"}, "ans": "A"},
    {"q": "Tỉnh huyệt của kinh Thận là huyệt nào?", "opts": {"A": "Thái Khê", "B": "Dũng Tuyền", "C": "Phục Lưu", "D": "Âm Cốc"}, "ans": "B"},
    {"q": "Hợp huyệt của kinh Vị là huyệt nào?", "opts": {"A": "Nội Đình", "B": "Giải Khê", "C": "Túc Tam Lý", "D": "Phong Long"}, "ans": "C"},
    {"q": "Du huyệt của kinh Tâm Bào là huyệt nào?", "opts": {"A": "Lao Cung", "B": "Đại Lăng", "C": "Trung Xung", "D": "Nội Quan"}, "ans": "B"},
    {"q": "Hợp huyệt của kinh Đởm là huyệt nào?", "opts": {"A": "Dương Lăng Tuyền", "B": "Khâu Âm", "C": "Dương Bộ", "D": "Túc Lâm Khấp"}, "ans": "A"},
    {"q": "Tỉnh huyệt của kinh Can là huyệt nào?", "opts": {"A": "Thái Xung", "B": "Đại Đôn", "C": "Hành Gian", "D": "Khúc Tuyền"}, "ans": "B"},
    {"q": "Hợp huyệt của kinh Can là huyệt nào?", "opts": {"A": "Thái Xung", "B": "Hành Gian", "C": "Khúc Tuyền", "D": "Trung Phong"}, "ans": "C"},
    {"q": "Theo ngũ hành, hợp huyệt của kinh âm thuộc hành nào?", "opts": {"A": "Hành Kim", "B": "Hành Thủy", "C": "Hành Mộc", "D": "Hành Thổ"}, "ans": "B"},
    {"q": "Theo ngũ hành, hợp huyệt của kinh dương thuộc hành nào?", "opts": {"A": "Hành Thổ", "B": "Hành Mộc", "C": "Hành Kim", "D": "Hành Thủy"}, "ans": "A"},
    {"q": "Khi bệnh ở phủ nên chọn loại huyệt nào ưu tiên?", "opts": {"A": "Tỉnh huyệt", "B": "Huỳnh huyệt", "C": "Hợp hạ toàn huyệt", "D": "Khích huyệt"}, "ans": "C"},
    {"q": "Hợp hạ toàn huyệt (lower he-sea) có bao nhiêu huyệt?", "opts": {"A": "4", "B": "6", "C": "8", "D": "3"}, "ans": "B"},
    {"q": "Hợp hạ toàn huyệt của Vị là huyệt nào?", "opts": {"A": "Túc Tam Lý", "B": "Thượng Cự Hư", "C": "Phong Long", "D": "Liang Qiu"}, "ans": "B"},
    {"q": "Khi bệnh ở tỉnh thì nên châm huyệt gì?", "opts": {"A": "Tỉnh huyệt để tia máu", "B": "Huỳnh huyệt", "C": "Hợp huyệt", "D": "Nguyên huyệt"}, "ans": "A"},

    # ============================================================
    # SECTION 3: HUYỆT NGUYÊN, LẠC, KHÍCH, MỘ, DU LƯNG (25 câu)
    # ============================================================

    {"q": "Nguyên huyệt của kinh Phế là huyệt nào?", "opts": {"A": "Kinh Cừ", "B": "Ngư Tế", "C": "Thái Uyên", "D": "Xích Trạch"}, "ans": "C"},
    {"q": "Nguyên huyệt của kinh Đại Trường là huyệt nào?", "opts": {"A": "Hợp Cốc", "B": "Khúc Trì", "C": "Dương Khê", "D": "Ngoại Quan"}, "ans": "A"},
    {"q": "Nguyên huyệt của kinh Vị là huyệt nào?", "opts": {"A": "Túc Tam Lý", "B": "Giải Khê", "C": "Xung Dương", "D": "Phong Long"}, "ans": "C"},
    {"q": "Nguyên huyệt của kinh Tỳ là huyệt nào?", "opts": {"A": "Thái Bạch", "B": "Tam Âm Giao", "C": "Công Tôn", "D": "Âm Lăng Tuyền"}, "ans": "A"},
    {"q": "Nguyên huyệt của kinh Tâm là huyệt nào?", "opts": {"A": "Thiếu Phủ", "B": "Thần Môn", "C": "Thông Lý", "D": "Thiếu Hải"}, "ans": "B"},
    {"q": "Nguyên huyệt của kinh Tiểu Trường là huyệt nào?", "opts": {"A": "Hậu Khê", "B": "Wan Gu", "C": "Yang Lao", "D": "Zhi Zheng"}, "ans": "B"},
    {"q": "Nguyên huyệt của kinh Bàng Quang là huyệt nào?", "opts": {"A": "Niệu Quản", "B": "Jing Gu", "C": "Fei Yang", "D": "Kun Lun"}, "ans": "B"},
    {"q": "Nguyên huyệt của kinh Thận là huyệt nào?", "opts": {"A": "Dũng Tuyền", "B": "Thái Khê", "C": "Phục Lưu", "D": "Zhao Hai"}, "ans": "B"},
    {"q": "Nguyên huyệt của kinh Can là huyệt nào?", "opts": {"A": "Hành Gian", "B": "Thái Xung", "C": "Khúc Tuyền", "D": "Trung Phong"}, "ans": "B"},
    {"q": "Nguyên huyệt của kinh Đởm là huyệt nào?", "opts": {"A": "Dương Lăng Tuyền", "B": "Khâu Âm", "C": "Qiu Xu", "D": "Zu Lin Qi"}, "ans": "C"},
    {"q": "Lạc huyệt của kinh Phế là huyệt nào?", "opts": {"A": "Thái Uyên", "B": "Liệt Khuyết", "C": "Thiếu Thương", "D": "Ngư Tế"}, "ans": "B"},
    {"q": "Lạc huyệt của kinh Vị là huyệt nào?", "opts": {"A": "Túc Tam Lý", "B": "Phong Long", "C": "Nội Đình", "D": "Giải Khê"}, "ans": "B"},
    {"q": "Lạc huyệt của kinh Tỳ là huyệt nào?", "opts": {"A": "Thái Bạch", "B": "Tam Âm Giao", "C": "Công Tôn", "D": "Đại Bao"}, "ans": "C"},
    {"q": "Mộ huyệt của Phế là huyệt nào?", "opts": {"A": "Phong Môn", "B": "Trung Phủ", "C": "Đản Trung", "D": "Ri Yue"}, "ans": "B"},
    {"q": "Mộ huyệt của Tâm là huyệt nào?", "opts": {"A": "Đản Trung", "B": "Cự Khuyết", "C": "Trung Quản", "D": "Chương Môn"}, "ans": "B"},
    {"q": "Mộ huyệt của Vị là huyệt nào?", "opts": {"A": "Đản Trung", "B": "Trung Quản", "C": "Thiên Xu", "D": "Chương Môn"}, "ans": "B"},
    {"q": "Mộ huyệt của Đại Trường là huyệt nào?", "opts": {"A": "Trung Quản", "B": "Thiên Xu", "C": "Quan Nguyên", "D": "Khí Hải"}, "ans": "B"},
    {"q": "Mộ huyệt của Can là huyệt nào?", "opts": {"A": "Nhật Nguyệt", "B": "Chương Môn", "C": "Kỳ Môn", "D": "Trung Phủ"}, "ans": "C"},
    {"q": "Mộ huyệt của Đởm là huyệt nào?", "opts": {"A": "Kỳ Môn", "B": "Nhật Nguyệt", "C": "Chương Môn", "D": "Quan Nguyên"}, "ans": "B"},
    {"q": "Du lưng (back-shu) của Phế là huyệt nào?", "opts": {"A": "Phế Du BL13", "B": "Thận Du BL23", "C": "Tâm Du BL15", "D": "Tỳ Du BL20"}, "ans": "A"},
    {"q": "Du lưng của Thận là huyệt nào?", "opts": {"A": "Phế Du BL13", "B": "Cách Du BL17", "C": "Thận Du BL23", "D": "Đởm Du BL19"}, "ans": "C"},
    {"q": "Khích huyệt của kinh Phế là huyệt nào?", "opts": {"A": "Liệt Khuyết", "B": "Khổng Tối", "C": "Xích Trạch", "D": "Thái Uyên"}, "ans": "B"},
    {"q": "Khích huyệt của kinh Tâm là huyệt nào?", "opts": {"A": "Âm Khích", "B": "Thần Môn", "C": "Thông Lý", "D": "Thiếu Hải"}, "ans": "A"},
    {"q": "Khích huyệt dùng trong trường hợp nào?", "opts": {"A": "Bệnh mạn tính", "B": "Chứng cấp tính, đau cấp", "C": "Tăng bổ tinh khí", "D": "Giảm diệt phong tà"}, "ans": "B"},
    {"q": "Du lưng thường nằm ở đâu trên lưng?", "opts": {"A": "Đường kinh Tỳ", "B": "Đường kinh Bàng Quang 1.5 thốn cạnh cột sống", "C": "Mạch Đốc", "D": "Đường kinh Đởm"}, "ans": "B"},

    # ============================================================
    # SECTION 4: BỔ TẢ THỦ PHÁP (20 câu)
    # ============================================================

    {"q": "Bổ pháp là phép châm nhằm mục đích gì?", "opts": {"A": "Giảm diệt tà khí", "B": "Tăng cường chính khí", "C": "Giảm đau cấp", "D": "Thông kinh lạc"}, "ans": "B"},
    {"q": "Tả pháp là phép châm nhằm mục đích gì?", "opts": {"A": "Tăng cường chính khí", "B": "Giảm diệt tà khí, tiêu tức", "C": "Bồi bổ can dương", "D": "An thần"}, "ans": "B"},
    {"q": "Phép hô hấp bổ tả là gì?", "opts": {"A": "Châm khi bệnh nhân thở ra thì cắm kim, khi ngoài hơi thì rút", "B": "Châm khi bệnh nhân hít vào thì cắm kim, khi thở ra thì rút", "C": "Xoay kim theo chiều kim đồng hồ là bổ", "D": "Cả A và C"}, "ans": "B"},
    {"q": "Phép hô hấp tả là gì?", "opts": {"A": "Cắm kim khi bệnh nhân thở ra, rút khi hít vào", "B": "Cắm kim khi bệnh nhân hít vào, rút khi thở ra", "C": "Xoay kim ngược chiều là bổ", "D": "Cả A và C"}, "ans": "A"},
    {"q": "Niệm chuyển bổ: xoay kim theo chiều nào?", "opts": {"A": "Ngược chiều kim đồng hồ", "B": "Theo chiều kim đồng hồ (kỳ tay phải)", "C": "Cả hai chiều bằng nhau", "D": "Không có quy định"}, "ans": "B"},
    {"q": "Niệm chuyển tả: xoay kim theo chiều nào?", "opts": {"A": "Theo chiều kim đồng hồ", "B": "Ngược chiều kim đồng hồ (kỳ tay phải)", "C": "Cả hai chiều bằng nhau", "D": "Tùy theo kinh âm dương"}, "ans": "B"},
    {"q": "Phép khai hạp bổ tả: khi rút kim, dùng ngón tay bịt lỗ huyệt là phép gì?", "opts": {"A": "Tả pháp", "B": "Bổ pháp", "C": "Bình bổ bình tả", "D": "Không có ý nghĩa"}, "ans": "B"},
    {"q": "Phép khai hạp bổ tả: khi rút kim, mở lỗ huyệt (không bịt) là phép gì?", "opts": {"A": "Bổ pháp", "B": "Bình bổ bình tả", "C": "Tả pháp", "D": "Hòa pháp"}, "ans": "C"},
    {"q": "Phép thiên tiết (sao tiết) bổ tả: nhũng (đẩy mạnh) là phép gì?", "opts": {"A": "Bổ pháp", "B": "Tả pháp", "C": "Bình bổ bình tả", "D": "Hòa pháp"}, "ans": "B"},
    {"q": "Phép thiên tiết bổ tả: từ (nhẹ nhàng, chậm) là phép gì?", "opts": {"A": "Tả pháp", "B": "Bình bổ bình tả", "C": "Bổ pháp", "D": "Không có ý nghĩa"}, "ans": "C"},
    {"q": "Phép phong hỏa (tiếp nhiệt): nhóm bổ hay tả pháp?", "opts": {"A": "Bổ pháp", "B": "Tả pháp", "C": "Cả hai", "D": "Không phân loại"}, "ans": "A"},
    {"q": "Khi sử dụng phép 'cắm kim' (nhanh) rồi lưu kim lâu, đây là phép gì?", "opts": {"A": "Bổ pháp", "B": "Tả pháp", "C": "Bình bổ bình tả", "D": "Phép tuyệt bí"}, "ans": "B"},
    {"q": "Khi châm theo phép bổ, kim nên được cắm theo chiều nào so với dòng kinh khí?", "opts": {"A": "Ngược chiều", "B": "Cùng chiều", "C": "Vuông góc", "D": "Không liên quan"}, "ans": "B"},
    {"q": "Khi châm theo phép tả, kim nên được cắm theo chiều nào so với dòng kinh khí?", "opts": {"A": "Cùng chiều", "B": "Ngược chiều", "C": "Vuông góc", "D": "Không liên quan"}, "ans": "B"},
    {"q": "Phép 'Biểu Bổ Lý Tả' có nghĩa là gì?", "opts": {"A": "Bổ khí ở mặt, tả khí ở trong", "B": "Tả khí ở mặt, bổ khí ở trong", "C": "Tăng bổ kinh âm, giảm tả kinh dương", "D": "Điều hòa âm dương bằng nhau"}, "ans": "A"},
    {"q": "Khi đắc khí (de qi) đã có, xu hướng tăng thiết cảm và giữ kim lâu hơn là phép gì?", "opts": {"A": "Bổ pháp", "B": "Tả pháp", "C": "Hòa pháp (Bình bổ bình tả)", "D": "Khích pháp"}, "ans": "B"},
    {"q": "Phép bổ thì thiết cảm (Deqi) nên như thế nào?", "opts": {"A": "Mạnh, rành rõi, lan rộng", "B": "Nhẹ, ấm, bệnh nhân cảm thấy thoải mái", "C": "Gây đau để giải phóng tà khí", "D": "Không cần đắc khí"}, "ans": "B"},
    {"q": "Trứu pháp (Jiu - cứu pháp âm) được phân loại vào phép gì?", "opts": {"A": "Tả pháp", "B": "Bổ pháp vì có tính ấm", "C": "Bình bổ bình tả", "D": "Phép tự nhiên"}, "ans": "B"},
    {"q": "Châm kim nhiều, lấy nhiều máu, khi rút nhanh thuộc phép gì?", "opts": {"A": "Bổ pháp", "B": "Tả pháp", "C": "Bình bổ bình tả", "D": "Hòa pháp"}, "ans": "B"},
    {"q": "Theo YHCT, khi nặng chính khí bất túc nên áp dụng phép gì?", "opts": {"A": "Tả pháp", "B": "Bổ pháp", "C": "Không châm", "D": "Hòa pháp trước rồi bổ sau"}, "ans": "B"},

    # ============================================================
    # SECTION 5: PHỐI HUYỆT NGUYÊN TẮC (20 câu)
    # ============================================================

    {"q": "Phối huyệt theo phép 'Nguyên Lạc' có nghĩa là?", "opts": {"A": "Lấy nguyên huyệt kết hợp lạc huyệt của kinh biểu lý", "B": "Lấy mộ huyệt kết hợp du lưng", "C": "Lấy huyệt đầu kinh kết hợp huyệt cuối kinh", "D": "Lấy huyệt âm kết hợp dương"}, "ans": "A"},
    {"q": "Khi Phế bệnh, phép phối huyệt Nguyên-Lạc là?", "opts": {"A": "Thái Uyên (nguyên Phế) + Phong Long (lạc Vị)", "B": "Thái Uyên + Liệt Khuyết", "C": "Thái Uyên + Hợp Cốc", "D": "Liệt Khuyết + Phong Long"}, "ans": "A"},
    {"q": "Phối huyệt 'Mộ-Du' (Mộ-Du lưng) là kết hợp nào?", "opts": {"A": "Nguyên huyệt + Lạc huyệt", "B": "Mộ huyệt phía trước + Du lưng phía sau cùng tạng phủ", "C": "Hợp huyệt + Khích huyệt", "D": "Tỉnh huyệt + Huỳnh huyệt"}, "ans": "B"},
    {"q": "Phép phối huyệt theo 'Trên-Dưới' có ý nghĩa là?", "opts": {"A": "Kết hợp huyệt trên cận (tay) và huyệt trên chi dưới (chân) trị bệnh", "B": "Kết hợp huyệt âm và dương", "C": "Kết hợp nguyên và lạc", "D": "Kết hợp mộ và shu"}, "ans": "A"},
    {"q": "Phép phối huyệt 'Trái-Phải' áp dụng khi nào?", "opts": {"A": "Bệnh ở một bên, lấy huyệt bên đối diện (điều trị chéo)", "B": "Luôn luôn lấy cả hai bên", "C": "Bệnh ở dưới lấy huyệt ở trên", "D": "Bệnh cần lấy huyệt giao hội"}, "ans": "A"},
    {"q": "Phối huyệt 'Trên-Dưới' ví dụ: đau đầu + đau dạ dày dùng?", "opts": {"A": "Bách Hội + Túc Tam Lý", "B": "Nhân Trung + Hợp Cốc", "C": "Phong Thị + Dương Lăng Tuyền", "D": "Nội Quan + Tam Âm Giao"}, "ans": "A"},
    {"q": "Phối huyệt 'Phụ Nguyên' (Tuyệt đối) dùng trong trường hợp nào?", "opts": {"A": "Bệnh ở đường kinh đơn giản", "B": "Bệnh phức tạp, nhiều tạng phủ liên quan", "C": "Cấp cứu", "D": "Bệnh ngoại cảm"}, "ans": "B"},
    {"q": "Nguyên tắc 'Cự Thích' (châm bên đau) hay 'Mậu Thích' (châm chéo)?", "opts": {"A": "Cự Thích: châm cùng bên đau; Mậu Thích: châm bên đối diện", "B": "Ngược lại", "C": "Như nhau", "D": "Tùy theo tay thầy thuốc"}, "ans": "A"},
    {"q": "Khi điều trị mất ngủ, phối huyệt nào thường dùng?", "opts": {"A": "An Miên, Tam Âm Giao, Thần Môn", "B": "Túc Tam Lý, Hợp Cốc, Phong Long", "C": "Bách Hội, Nhân Trung, Phong Thị", "D": "Thái Khê, Tai Xi, Kun Lun"}, "ans": "A"},
    {"q": "Khi điều trị liệt mặt (Bell's palsy), nguyên tắc phối huyệt là?", "opts": {"A": "Châm xa ở chân, bỏ qua mặt", "B": "Châm tại chỗ mặt + xa châm tay chân (Hợp Cốc)", "C": "Chỉ châm Bách Hội", "D": "Châm huyệt lạc dương"}, "ans": "B"},
    {"q": "Phối huyệt trị đau đầu vùng đỉnh: chọn kinh nào là chính?", "opts": {"A": "Kinh Bàng Quang", "B": "Kinh Can", "C": "Kinh Đởm", "D": "Kinh Vị"}, "ans": "B"},
    {"q": "Phối huyệt trị đau đầu vùng trán: chọn kinh nào là chính?", "opts": {"A": "Kinh Vị", "B": "Kinh Đởm", "C": "Kinh Bàng Quang", "D": "Kinh Can"}, "ans": "A"},
    {"q": "Phối huyệt trị đau đầu vùng Dương Minh (trán): Hợp Cốc và huyệt nào?", "opts": {"A": "Nội Đình", "B": "Liệt Khuyết", "C": "Phong Long", "D": "Túc Tam Lý"}, "ans": "A"},
    {"q": "Phối huyệt trị đau đầu vùng Thiếu Dương (bên): chọn kinh gì?", "opts": {"A": "Vị", "B": "Can", "C": "Đởm", "D": "Bàng Quang"}, "ans": "C"},
    {"q": "Nguyên tắc chọn huyệt: 'Kinh mạch nào đi qua vùng bệnh, lấy huyệt kinh đó' là nguyên tắc gì?", "opts": {"A": "Phối huyệt nguyên lạc", "B": "Phối huyệt tại đầu", "C": "Phối huyệt theo đường kinh", "D": "Phối huyệt mộ-shu"}, "ans": "C"},
    {"q": "Khi điều trị bệnh ở tạng, có thể phối thêm huyệt gì để tăng hiệu quả?", "opts": {"A": "Mộ huyệt của tạng đó", "B": "Du lưng của tạng đó", "C": "Cả mộ và du lưng của tạng đó", "D": "Chỉ dùng nguyên huyệt"}, "ans": "C"},
    {"q": "Phép 'Khai-Hạp' (opening-closing) phối huyệt dùng những cặp huyệt nào?", "opts": {"A": "Nguyên-Lạc", "B": "Bát mạch giao hội (8 confluent points)", "C": "Tỉnh-Hợp", "D": "Mộ-Du lưng"}, "ans": "B"},
    {"q": "Số lượng huyệt trong một lần châm thông thường nên là bao nhiêu?", "opts": {"A": "1-2 huyệt", "B": "4-8 huyệt", "C": "10-15 huyệt", "D": "20 huyệt trở lên"}, "ans": "B"},
    {"q": "Khi phối huyệt, ưu tiên chọn huyệt gì trước?", "opts": {"A": "Huyệt cự bộ (local points)", "B": "Huyệt xa bộ (distal points) trên kinh", "C": "Huyệt đặc hiệu của chứng bệnh", "D": "Tất cả đều ngang nhau"}, "ans": "C"},
    {"q": "Phối huyệt trị chứng bệnh ở vùng lưng: lưng + chân, đây là phép gì?", "opts": {"A": "Mộ-Du", "B": "Trên-Dưới", "C": "Nguyên-Lạc", "D": "Cự Thích"}, "ans": "B"},

    # ============================================================
    # SECTION 6: CỨU PHÁP VÀ CHỐNG CHỈ ĐỊNH (15 câu)
    # ============================================================

    {"q": "Cứu pháp (moxibustion) sử dụng nguyên liệu chính là gì?", "opts": {"A": "Than tre", "B": "Ngô ải (ngà ải) - Ải Diệp (Artemisia)", "C": "Quế chi", "D": "Gừng tươi"}, "ans": "B"},
    {"q": "Cứu trực tiếp (direct moxibustion) trên da gồm mấy loại?", "opts": {"A": "1 loại", "B": "2 loại: có sẹo và không sẹo", "C": "3 loại", "D": "4 loại"}, "ans": "B"},
    {"q": "Cứu gián tiếp (indirect moxibustion) phổ biến nhất dùng gì chen giữa?", "opts": {"A": "Muối, gừng, tỏi", "B": "Vải, bông, giấy", "C": "Nhựa thông, nhựa thiên nhiên", "D": "Đá quý, hoàng kỳ"}, "ans": "A"},
    {"q": "Cứu gừng cách (cứu qua gừng): tác dụng chính là?", "opts": {"A": "Nhiệt độc, giải độc", "B": "Ấm trung, tán hàn, giải biểu", "C": "Tư âm, giảm nhiệt", "D": "Hành khí, hoạt huyết"}, "ans": "B"},
    {"q": "Cứu tỏi cách (qua tỏi): tác dụng chính là?", "opts": {"A": "Giải độc, tiêu viêm", "B": "Ấm trung, tán hàn", "C": "Hành khí hoạt huyết", "D": "Nâng dương khí"}, "ans": "A"},
    {"q": "Cứu muối cách (qua muối): thường dùng trị bệnh gì?", "opts": {"A": "Ung nhọt, vùng kinh rối", "B": "Cứu huyệt Thần Khuyết (CV8) trị chứng thổ tả hàn, tiêu chảy cấp", "C": "Đau đầu, mất ngủ", "D": "Ho hen suyễn"}, "ans": "B"},
    {"q": "Chống chỉ định cứu pháp: trường hợp nào KHÔNG nên cứu?", "opts": {"A": "Hàn chứng, dương khí hưu", "B": "Nhiệt chứng, âm hư, có thai", "C": "Bệnh khí huyết mất", "D": "Dương hào hư"}, "ans": "B"},
    {"q": "Vùng nào trên cơ thể KHÔNG được cứu?", "opts": {"A": "Vùng bụng, lưng", "B": "Vùng mặt, đầu, gần lớn mạch máu lớn, tạng sinh dục phụ nữ có thai", "C": "Vùng cổ chân tay", "D": "Vùng ngực"}, "ans": "B"},
    {"q": "Khi cứu, khoảng cách giữa điếu ngải và da khoảng bao nhiêu cm?", "opts": {"A": "0.5-1 cm", "B": "2-3 cm", "C": "5-7 cm", "D": "10 cm"}, "ans": "B"},
    {"q": "Thời gian cứu trên một điểm thường là bao nhiêu phút?", "opts": {"A": "1-2 phút", "B": "5-15 phút", "C": "20-30 phút", "D": "30-60 phút"}, "ans": "B"},
    {"q": "Cứu pháp có tác dụng chính nào sau đây?", "opts": {"A": "Ấm trung tán hàn, thông kinh lạc, dưỡng khí", "B": "Tất cả các tác dụng trên", "C": "Giảm đau, giảm viêm", "D": "Cả A và C"}, "ans": "D"},
    {"q": "Khi bị bỏng do cứu, xử trí như thế nào?", "opts": {"A": "Để tự nhiên khỏi", "B": "Bỡ phỏng nước, giữ vệ sinh, có thể băng bó", "C": "Chọc phỏng nước ngay lập tức rồi bỏ thuốc lá", "D": "Không cần xử trí"}, "ans": "B"},
    {"q": "Cứu pháp chống chỉ định ở bệnh nhân nào?", "opts": {"A": "Người cao tuổi bệnh mạn tính", "B": "Bệnh nhân sốt cao, mất nước, âm hư nội nhiệt", "C": "Người bị hàn thấp tý", "D": "Người bị dương hào hư"}, "ans": "B"},
    {"q": "Loại cứu nào tạo sẹo trên da?", "opts": {"A": "Cứu gừng cách", "B": "Cứu muối cách", "C": "Cứu trực tiếp có sẹo (Hua fa jiu)", "D": "Cứu điếu ngải"}, "ans": "C"},
    {"q": "Cứu trị chứng liệt, bí linh không nên áp dụng vào giai đoạn nào?", "opts": {"A": "Giai đoạn mạn tính", "B": "Giai đoạn cấp tính đầu", "C": "Giai đoạn phục hồi", "D": "Tất cả các giai đoạn đều được"}, "ans": "B"},

    # ============================================================
    # SECTION 7: ĐẮC KHÍ VÀ TAI BIẾN CHÂM CỨU (15 câu)
    # ============================================================

    {"q": "Đắc Khí (De Qi) là gì?", "opts": {"A": "Cảm giác tức bụng, tê, nặng, tức khi châm đúng sức khí", "B": "Cảm giác đau nhói khi kim chích vào", "C": "Cảm giác nóng ấm tại huyệt", "D": "Co thắt cơ khi rút kim"}, "ans": "A"},
    {"q": "Khi đắc khí, bác sĩ cảm thấy gì qua kim?", "opts": {"A": "Kim vào trơn, không cảm gì", "B": "Kim bị bít chặt như cá cắn câu (nhu yu shi jian)", "C": "Kim rung mạnh", "D": "Kim bị đẩy ra"}, "ans": "B"},
    {"q": "Nếu không đắc khí, nên làm gì?", "opts": {"A": "Rút kim ngay", "B": "Giữ nguyên và chờ", "C": "Điều chỉnh góc độ, độ sâu, niệm chuyển kích thích thêm", "D": "Châm thêm huyệt khác"}, "ans": "C"},
    {"q": "Vựng châm (fainting - Yun Zhen) trong châm là tai biến gì?", "opts": {"A": "Kim bị gập", "B": "Kim bị kẹt (kẹt kim)", "C": "Phản ứng sốc: bệnh nhân mặt tái, hoa mắt, chóng mặt, ngất xỉu", "D": "Nhiễm trùng tại huyệt"}, "ans": "C"},
    {"q": "Nguyên nhân hay gặp nhất của vựng châm khi châm là?", "opts": {"A": "Kim quá dài", "B": "Bệnh nhân quá đói, quá mệt, lối châm quá mạnh", "C": "Châm sai huyệt", "D": "Dùng kim bị rỉ sét"}, "ans": "B"},
    {"q": "Khi bệnh nhân vựng châm khi châm, xử trí đầu tiên là?", "opts": {"A": "Gọi cấp cứu 115", "B": "Rút hết kim, đặt bệnh nhân nằm, châm Nhân Trung, Hợp Cốc", "C": "Cho bệnh nhân uống nước", "D": "Tăng nhiệt độ phòng"}, "ans": "B"},
    {"q": "Kẹt kim (stuck needle) là hiện tượng gì?", "opts": {"A": "Kim bị gập khúc", "B": "Kim không rút ra được hoặc khó xoay do co thắt cơ cuốn kim", "C": "Kim vào quá sâu", "D": "Nhiễm trùng tại huyệt"}, "ans": "B"},
    {"q": "Kim bị gập (bent needle) thường do nguyên nhân gì?", "opts": {"A": "Kim chất lượng kém, bệnh nhân chuyển mình đột ngột, góc châm sai", "B": "Châm quá nhanh", "C": "Kim quá dài", "D": "Đắc khí quá mạnh"}, "ans": "A"},
    {"q": "Khi bị kẹt kim (co thắt cuốn kim), xử trí nào là đúng?", "opts": {"A": "Kéo mạnh rút ra ngay", "B": "Niệm chuyển phản chiều, đẩy nhẹ rồi rút; có thể đẩy bổ kim thêm sâu rồi rút", "C": "Để nguyên cho tự khỏi", "D": "Cắt da để lấy kim"}, "ans": "B"},
    {"q": "Khi kim bị gãy (broken needle) đang còn trong da, bước đầu tiên là?", "opts": {"A": "Cắt ngay làn da xung quanh", "B": "Dặn bệnh nhân không động, giữ yên vị trí, dùng nguồn lực phẫu thuật nếu cần", "C": "Rút bất kỳ phần còn lộ ra bằng tay", "D": "Bỏ qua nếu không gây khó chịu"}, "ans": "B"},
    {"q": "Trường hợp nào có NGUY CƠ cao nhất bị vựng châm khi châm?", "opts": {"A": "Bệnh nhân cao tuổi, mạn tính ổn định", "B": "Người quá đói, quá mệt, đang có thai, lần đầu châm, quá sợ hãi", "C": "Trẻ em", "D": "Bệnh nhân bệnh mạn tính"}, "ans": "B"},
    {"q": "Để phòng kẹt kim, nên làm gì?", "opts": {"A": "Giải thích bệnh nhân không động đột ngột, dặn tư thế thoải mái", "B": "Châm thật nhanh", "C": "Chỉ dùng kim ngắn", "D": "Tránh đắc khí mạnh"}, "ans": "A"},
    {"q": "Máu tụ (hematoma) sau châm xử trí như thế nào?", "opts": {"A": "Bỏ qua tự nhiên tan", "B": "Chườm lạnh ngay sau rút kim; nếu to có thể chườm ấm sau 24 giờ", "C": "Xoa mạnh ngay", "D": "Châm lại để tăng tuần hoàn"}, "ans": "B"},
    {"q": "Nhiễm trùng sau châm có thể gây ra do nguyên nhân gì?", "opts": {"A": "Không sát trùng da và kim; dùng kim nhiều lần không tiệt trùng", "B": "Châm quá sâu", "C": "Bệnh nhân dị ứng kim", "D": "Đắc khí quá mạnh"}, "ans": "A"},
    {"q": "Chống chỉ định tuyệt đối của châm là?", "opts": {"A": "Người cao tuổi", "B": "Hư chứng nặng, khu vực nhiễm trùng, bệnh nhân không hợp tác/rối loạn tâm thần nặng, có thai (các huyệt cấm)", "C": "Trẻ em dưới 5 tuổi", "D": "Bệnh nhân đang dùng thuốc"}, "ans": "B"},
    {"q": "Cảm giác đắc khí (De Qi) mà bệnh nhân mô tả là?", "opts": {"A": "Chỉ có đau nhói tại chỗ châm", "B": "Tức bụng, tê nhẹ, nặng, tức, có thể lan rộng theo đường kinh", "C": "Nóng bỏng rát tại huyệt", "D": "Không cảm thấy gì là tốt nhất"}, "ans": "B"},
    {"q": "Khi châm phải mạch máu gây chảy máu, xử trí đầu tiên?", "opts": {"A": "Tiếp tục châm bởi vì sẽ tự cầm", "B": "Rút kim, ấn băng bông vô trùng, băng ép nếu cần", "C": "Châm thêm huyệt khác để tăng tuần hoàn", "D": "Để tự nhiên cầm máu"}, "ans": "B"},
    {"q": "Biến chứng tràn khí hung (pneumothorax) có thể xảy ra khi châm sai ở vùng nào?", "opts": {"A": "Vùng bụng dưới", "B": "Vùng lưng dưới và hông", "C": "Vùng ngực và lưng trên gần phổi", "D": "Vùng chi trên"}, "ans": "C"},
    {"q": "Khi châm các huyệt vùng bụng dưới ở phụ nữ trong độ tuổi sinh sản, cần hỏi gì trước?", "opts": {"A": "Huyết áp và mạch", "B": "Có thai hay không", "C": "Tiền sử dị ứng", "D": "Lịch sử châm cứu trước đây"}, "ans": "B"},
]

# Verify
assert len(Q2) == 160, f"Expected 160 questions, got {len(Q2)}"
print(f"quiz_phase2.py loaded: {len(Q2)} questions OK")
