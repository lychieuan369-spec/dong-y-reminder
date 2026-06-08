# -*- coding: utf-8 -*-
# Phase 4: Ôn Bệnh Học - Warm Disease School (160 questions)

Q4 = [
    # ============================================================
    # SECTION 1: Vệ Khí Dinh Huyết biện chứng (40 câu)
    # ============================================================

    # --- Vệ phận (10 câu) ---
    {"q": "Đặc điểm chính của Vệ phận trong Ôn Bệnh là gì?",
     "opts": {"A": "Sốt cao, khát nước, mê sảng", "B": "Sốt, sợ gió, không sợ lạnh hoặc sợ lạnh nhẹ", "C": "Ban chẩn tay, tiểu đỏ", "D": "Cổ cứng, co giật"},
     "ans": "B"},

    {"q": "Phép trị Vệ phận là gì?",
     "opts": {"A": "Thanh nhiệt giải độc", "B": "Nhuận âm trị nhiệt", "C": "Tân lương, giải biểu", "D": "Cường âm linh dương"},
     "ans": "C"},

    {"q": "Triệu chứng nào KHÔNG thuộc Vệ phận?",
     "opts": {"A": "Sợ gió", "B": "Đau đầu nhẹ", "C": "Mê sảng", "D": "Mạch phù sác"},
     "ans": "C"},

    {"q": "Lưỡi trong Vệ phận thường có đặc điểm gì?",
     "opts": {"A": "Lưỡi đỏ, không rêu", "B": "Lưỡi hồng bình thường hoặc rêu trắng mỏng", "C": "Lưỡi tím đen", "D": "Lưỡi vàng dày"},
     "ans": "B"},

    {"q": "Vệ phận tương ứng với giai đoạn nào của bệnh?",
     "opts": {"A": "Giai đoạn cuối cùng", "B": "Giai đoạn toàn thân", "C": "Giai đoạn khởi phát, bệnh còn ở ngoài", "D": "Giai đoạn hồi phục"},
     "ans": "C"},

    {"q": "Mạch của Vệ phận thường là?",
     "opts": {"A": "Trầm và sác", "B": "Phù sác hoặc phù sác", "C": "Hoãn và hoạt", "D": "Tế và nhược"},
     "ans": "B"},

    {"q": "Biến chứng của Vệ phận nếu không trị kịp là gì?",
     "opts": {"A": "Thoát dương", "B": "Truyền vào Khí phận", "C": "Cân Dương bất túc", "D": "Phế âm tổn thương"},
     "ans": "B"},

    {"q": "Nhiệt ở Vệ phận có thể giải ra bằng đường nào là chính?",
     "opts": {"A": "Qua mồ hôi (Hãn)", "B": "Qua tiểu tiện", "C": "Qua đại tiện", "D": "Qua nôn"},
     "ans": "A"},

    {"q": "Thuốc nào được dùng chủ yếu ở Vệ phận?",
     "opts": {"A": "Thạch cao, Tri mẫu", "B": "Ngân hoa, Liên kiều, Bạc hà", "C": "Hương dược, Cần địa", "D": "Hoàng liên, Hoàng bá"},
     "ans": "B"},

    {"q": "Vệ phận bệnh nhẹ thì dùng phương tễ nào?",
     "opts": {"A": "Bạch Hổ Thang", "B": "Ngân Kiều Tán", "C": "Thanh Doanh Thang", "D": "Tê Giác Địa Hoàng Thang"},
     "ans": "B"},

    # --- Khí phận (10 câu) ---
    {"q": "Đặc điểm của Khí phận trong Ôn Bệnh là gì?",
     "opts": {"A": "Sốt sợ lạnh, đau đầu", "B": "Sốt cao, khát nước, không sợ lạnh, mồ hôi nhiều", "C": "Ban chẩn, tiểu đỏ", "D": "Mê sảng, cẩm tay"},
     "ans": "B"},

    {"q": "Phép trị Khí phận là gì?",
     "opts": {"A": "Giải biểu, tân lương", "B": "Thanh Khí tiết nhiệt", "C": "Lương Huyết, tán ứ", "D": "Ích âm, sinh tân"},
     "ans": "B"},

    {"q": "Lưỡi trong Khí phận thường có đặc điểm gì?",
     "opts": {"A": "Lưỡi hồng nhạt, rêu trắng", "B": "Lưỡi đỏ, rêu vàng dày hoặc khô", "C": "Lưỡi tím nhạt", "D": "Lưỡi trắng trơn"},
     "ans": "B"},

    {"q": "Mạch của Khí phận thường là?",
     "opts": {"A": "Phù sác", "B": "Hồng sác hoặc Hoạt sác", "C": "Trầm tế", "D": "Kỳ sác"},
     "ans": "B"},

    {"q": "Thuốc nào là chủ yếu trong điều trị Khí phận?",
     "opts": {"A": "Ngân hoa, Bạc hà", "B": "Thạch cao, Tri mẫu, Ngân hoa", "C": "Tê Giác, Cần địa", "D": "Hoàng liên giải độc thang"},
     "ans": "B"},

    {"q": "Khí phận nhiệt kết Đại trường (Dương minh Vũ nhiệt) thì dùng phép gì?",
     "opts": {"A": "Thanh nhiệt sinh tân", "B": "Thông hạ tiết nhiệt (Thừa khí thang)", "C": "Giải biểu tán hàn", "D": "Nhiệt âm trợ dương"},
     "ans": "B"},

    {"q": "Biến chứng nguy hiểm của Khí phận là gì?",
     "opts": {"A": "Thương Âm", "B": "Hư nhiệt truyền Doanh phận", "C": "Dương hồi thoát", "D": "Khí trú hóa kém"},
     "ans": "B"},

    {"q": "Khí phận Phong nhiệt phạm Phế thì biểu hiện gì?",
     "opts": {"A": "Đau sườn, buồn nôn", "B": "Ho, mặt đỏ, khát nước, mạch sác xuống hàng", "C": "Tiểu đỏ, ban đỏ", "D": "Cảm cảm, ra mồ hôi"},
     "ans": "B"},

    {"q": "Bài thuốc điều trị Khí phận nhiệt mạc Phế là?",
     "opts": {"A": "Ngân Kiều Tán", "B": "Ma Hạnh Thạch Cam Thang", "C": "Bạch Hổ Thang", "D": "Tang Cúc Ẩm"},
     "ans": "B"},

    {"q": "Triệu chứng 'Tứ Đại' (bốn lớn) trong Khí phận bao gồm?",
     "opts": {"A": "Sốt cao, khát nhiều, mồ hôi nhiều, mạch hồng sác", "B": "Sốt, sợ lạnh, đau đầu, ngẹt mũi", "C": "Mê sảng, ban chẩn, cẩm tay", "D": "Đàm nhọt, ho, khó thở, sương hàng"},
     "ans": "A"},

    # --- Doanh phận (10 câu) ---
    {"q": "Đặc điểm của Doanh phận là gì?",
     "opts": {"A": "Sốt cao, khát nước nhiều", "B": "Sốt về đêm nặng, không khát hoặc khát ít, lưỡi đỏ không rêu", "C": "Sợ lạnh, đau đầu, sốt nhẹ", "D": "Ban chẩn, tiểu đỏ xuất huyết"},
     "ans": "B"},

    {"q": "Phép trị Doanh phận là gì?",
     "opts": {"A": "Thanh Khí tiết nhiệt", "B": "Thanh Doanh tiết nhiệt, thấu âm", "C": "Giải biểu, tân lương", "D": "Cường âm linh dương"},
     "ans": "B"},

    {"q": "Lưỡi trong Doanh phận có đặc điểm gì?",
     "opts": {"A": "Đỏ khô hoặc tím nhạt, ít rêu hoặc không rêu", "B": "Hồng bình thường, rêu trắng mỏng", "C": "Vàng dày, ướt", "D": "Trắng trơn nhỏ"},
     "ans": "A"},

    {"q": "Mạch của Doanh phận thường là?",
     "opts": {"A": "Phù sác", "B": "Tế sác", "C": "Hoãn hoạt", "D": "Trầm nhược"},
     "ans": "B"},

    {"q": "Bài thuốc chính điều trị Doanh phận là?",
     "opts": {"A": "Bạch Hổ Thang", "B": "Thanh Doanh Thang", "C": "Ngân Kiều Tán", "D": "Tang Cúc Ẩm"},
     "ans": "B"},

    {"q": "Biến chứng nguy hiểm của Doanh phận là?",
     "opts": {"A": "Nhiệt truyền Khí phận", "B": "Thương Âm nghiêm trọng, nhiệt truyền Huyết phận", "C": "Bệnh lui, hồi phục", "D": "Âm dương cân bằng"},
     "ans": "B"},

    {"q": "Triệu chứng tâm thần của Doanh phận biểu hiện như thế nào?",
     "opts": {"A": "Mê sảng, cắt tiếng, bứt bức", "B": "Bình thường hoặc ngủ mê nhiều", "C": "Hôn mê, co giật", "D": "Lo lắng, mất ngủ nhẹ"},
     "ans": "A"},

    {"q": "Doanh phận khác Khí phận ở điểm nào chính?",
     "opts": {"A": "Sốt cao hơn", "B": "Không khát hoặc khát rất ít, lưỡi đỏ không rêu", "C": "Mồ hôi nhiều hơn", "D": "Mạch phù sác hơn"},
     "ans": "B"},

    {"q": "Nhiệt truyền vào Tâm Bào trong Doanh phận gây ra triệu chứng gì?",
     "opts": {"A": "Đau bụng, nôn mửa", "B": "Hôn mê, nói ngàn", "C": "Co giật, cắt tiếng", "D": "Tiểu đỏ, xuất huyết"},
     "ans": "B"},

    {"q": "Điều trị Doanh phận nên thêm thuốc nào để 'thấu âm'?",
     "opts": {"A": "Hoàng kỳ, Đảng sâm", "B": "Mạch đông, Huyền sâm, Cần địa", "C": "Phục linh, Bạch truật", "D": "Ngũ vị, Toan táo"},
     "ans": "B"},

    # --- Huyết phận (10 câu) ---
    {"q": "Đặc điểm của Huyết phận là gì?",
     "opts": {"A": "Sốt, khát nước, mồ hôi nhiều", "B": "Nhiệt cực thịnh, Huyết động cuồng, Huyết ứ, Huyết khô", "C": "Mê sảng nhẹ, lưỡi đỏ ít rêu", "D": "Sợ gió, ngẹt mũi, đau đầu"},
     "ans": "B"},

    {"q": "Bốn cơ chế bệnh chính của Huyết phận là gì?",
     "opts": {"A": "Phế sát, Tỳ hoa, Khí hồi, Thận âm", "B": "Nhiệt cuồng Huyết, Huyết ứ, Huyết khô, Huyết động loạt", "C": "Khí hồi, Âm hồi, Dương hồi, Huyết hồi", "D": "Phong nhiệt, Hàn nhiệt, Thấp nhiệt, Ôn nhiệt"},
     "ans": "B"},

    {"q": "Phép trị Huyết phận là gì?",
     "opts": {"A": "Thanh Khí tiết nhiệt", "B": "Thanh nhiệt lương huyết, tán ứ giải độc", "C": "Giải biểu, tân lương", "D": "Ích âm, sinh tân"},
     "ans": "B"},

    {"q": "Lưỡi trong Huyết phận có đặc điểm gì?",
     "opts": {"A": "Hồng bình thường", "B": "Đỏ sẫm hoặc tím nhạt, khô không rêu hoặc rêu vàng cháy", "C": "Trắng mỏng", "D": "Vàng dày ướt"},
     "ans": "B"},

    {"q": "Bài thuốc chính điều trị Huyết phận là?",
     "opts": {"A": "Ngân Kiều Tán", "B": "Tê Giác Địa Hoàng Thang", "C": "Bạch Hổ Thang", "D": "Tang Cúc Ẩm"},
     "ans": "B"},

    {"q": "Xuất huyết trong Huyết phận có thể xuất hiện ở đâu?",
     "opts": {"A": "Chỉ ở da", "B": "Nhiều vị trí: da (ban), mũi, miệng, tiểu tiện, đại tiện", "C": "Chỉ ở phế", "D": "Chỉ ở vị trường"},
     "ans": "B"},

    {"q": "Huyết khô trong Huyết phận gây ra triệu chứng gì?",
     "opts": {"A": "Xuất huyết nhiều", "B": "Âm hao, có sốt âm, lưỡi đỏ khô, mạch tế sác", "C": "Sốt cao, mồ hôi nhiều", "D": "Mê sảng, nói ngàn"},
     "ans": "B"},

    {"q": "Biến chứng thoát dương trong Huyết phận biểu hiện như thế nào?",
     "opts": {"A": "Sốt cao, xuất huyết", "B": "Tay chân lạnh, mồ hôi lạnh, mạch vi sác, tinh thần mờ", "C": "Co giật mạnh", "D": "Khát nước dữ dội"},
     "ans": "B"},

    {"q": "Thuốc nào quan trọng trong trị Huyết phận?",
     "opts": {"A": "Thạch cao, Tri mẫu", "B": "Tê giác, Linh dương giác, Cần địa, Tê giác", "C": "Ngân hoa, Liên kiều", "D": "Hoàng kỳ, Đảng sâm"},
     "ans": "B"},

    {"q": "Nhiệt cuồng Huyết động (nhiệt bức huyết hành) trong Huyết phận thì phép trị là?",
     "opts": {"A": "Ích khí cố tuyệt", "B": "Thanh nhiệt lương huyết, cầm huyết chỉ huyết", "C": "Giải biểu, giải độc", "D": "Ôn Dương hộ Dương"},
     "ans": "B"},

    # ============================================================
    # SECTION 2: Tam Tiêu biện chứng (Ngô Cúc Thông) (35 câu)
    # ============================================================

    {"q": "Tam Tiêu biện chứng do ai sáng lập?",
     "opts": {"A": "Diệp Thiên Sĩ", "B": "Ngô Cúc Thông", "C": "Vương Mạnh Anh", "D": "Liêu Kinh"},
     "ans": "B"},

    {"q": "Thượng Tiêu trong Tam Tiêu biện chứng bao gồm tạng phủ nào?",
     "opts": {"A": "Tỳ và Vị", "B": "Can và Thận", "C": "Tâm và Phế", "D": "Tiểu trường và Đại trường"},
     "ans": "C"},

    {"q": "Trung Tiêu trong Tam Tiêu biện chứng bao gồm tạng phủ nào?",
     "opts": {"A": "Tâm và Phế", "B": "Tỳ và Vị", "C": "Thận và Bàng quang", "D": "Can và Đảm"},
     "ans": "B"},

    {"q": "Hạ Tiêu trong Tam Tiêu biện chứng bao gồm tạng phủ nào?",
     "opts": {"A": "Tâm và Phế", "B": "Tỳ và Vị", "C": "Can, Thận, Bàng quang", "D": "Phế và Đại trường"},
     "ans": "C"},

    {"q": "Ngô Cúc Thông viết tác phẩm nào về Ôn Bệnh?",
     "opts": {"A": "Ôn Nhiệt Luận", "B": "Ôn Bệnh Điều Biện", "C": "Ôn Bệnh Tiêu Tiết", "D": "Wen Re Jing Wei"},
     "ans": "B"},

    {"q": "Thượng Tiêu bệnh nhiệt mạc Phế biểu hiện gì?",
     "opts": {"A": "Đau bụng, đàm nhọt vàng", "B": "Ho, khó thở, sốt, mạch sác xuống hàng", "C": "Tiểu đỏ vàng sẫm, ban chẩn", "D": "Hôn mê, co giật"},
     "ans": "B"},

    {"q": "Phép trị Thượng Tiêu bệnh Phế là?",
     "opts": {"A": "Thông hạ", "B": "Tư Phế, tiết nhiệt, hóa đàm", "C": "Hành khí, hoạt huyết", "D": "Lâm ích tán"},
     "ans": "B"},

    {"q": "Thượng Tiêu bệnh nhiệt truyền Tâm Bào biểu hiện gì?",
     "opts": {"A": "Ho, sương hàng, đàm nhọt", "B": "Hôn mê, nói ngàn, cắt tiếng", "C": "Đau bụng, nôn mửa", "D": "Tiểu nhiều lần, khát nước"},
     "ans": "B"},

    {"q": "Phép trị Thượng Tiêu bệnh Tâm Bào là?",
     "opts": {"A": "Ích âm sinh tân", "B": "Thanh tâm, khai khiếu, tỉnh thần", "C": "Tiết Phế khai khiếu", "D": "Cường âm linh dương"},
     "ans": "B"},

    {"q": "Trung Tiêu bệnh nhiệt kết Vị trường biểu hiện gì?",
     "opts": {"A": "Sốt, sợ lạnh, đau đầu", "B": "Bụng căng cứng, táo bón, sốt cao buổi chiều, nói ngàn", "C": "Ban chẩn, tiểu đỏ", "D": "Co giật, cổ cứng"},
     "ans": "B"},

    {"q": "Phép trị Trung Tiêu Vị trường nhiệt kết là?",
     "opts": {"A": "Thanh nhiệt giải độc đơn thuần", "B": "Thừa Khí thông hạ, tiết nhiệt thông bên", "C": "Giải biểu tân lương", "D": "Cường âm linh dương"},
     "ans": "B"},

    {"q": "Trung Tiêu bệnh Thấp nhiệt trở trung là?",
     "opts": {"A": "Sốt cao, khát nước nhiều, mồ hôi nhiều", "B": "Sốt về buổi chiều, thân nặng, buồn nôn, lưỡi rêu vàng nhớt", "C": "Xuất huyết nhiều nơi", "D": "Co giật, cổ cứng"},
     "ans": "B"},

    {"q": "Phép trị Trung Tiêu Thấp nhiệt trở trung là?",
     "opts": {"A": "Bạch Hổ Thang", "B": "Thanh hóa, khai uất, thông trung", "C": "Ngân Kiều Tán", "D": "Tê Giác Địa Hoàng Thang"},
     "ans": "B"},

    {"q": "Hạ Tiêu bệnh nhiệt thương Can âm biểu hiện gì?",
     "opts": {"A": "Sốt cao, khát nước", "B": "Sốt âm, đau lưng, tay chân thường động run, lưỡi đỏ ít rêu", "C": "Táo bón, bụng căng", "D": "Ho, khó thở"},
     "ans": "B"},

    {"q": "Hạ Tiêu bệnh nhiệt thương Thận âm biểu hiện gì?",
     "opts": {"A": "Ho, mạch đỏ", "B": "Sốt âm, di tinh, lưng gối yếu mềm, lưỡi đỏ, mạch tế sác", "C": "Bụng căng, buồn nôn", "D": "Ban chẩn, tiểu đỏ"},
     "ans": "B"},

    {"q": "Phép trị Hạ Tiêu bệnh thương âm là?",
     "opts": {"A": "Thanh Khí tiết nhiệt", "B": "Phục Mạch Thang, trợ âm khu nhiệt, kích dương linh âm", "C": "Giải biểu tân lương", "D": "Thông hạ tiết nhiệt"},
     "ans": "B"},

    {"q": "Hạ Tiêu bệnh Hỏa nhiệt động Can phong biểu hiện gì?",
     "opts": {"A": "Ho, khó thở, sốt", "B": "Co giật, cổ cứng, mắt trắng đen, lưỡi cứng đỏ", "C": "Bụng căng, táo bón", "D": "Khát nước, tiểu nhiều"},
     "ans": "B"},

    {"q": "Ngô Cúc Thông nhấn mạnh rằng truyền biến trong Tam Tiêu theo thứ tự nào?",
     "opts": {"A": "Hạ -> Trung -> Thượng", "B": "Thượng -> Trung -> Hạ", "C": "Có thể thứ tự bất kỳ", "D": "Trung -> Thượng -> Hạ"},
     "ans": "B"},

    {"q": "Đặc điểm của Thượng Tiêu bệnh so với Hạ Tiêu bệnh là?",
     "opts": {"A": "Thượng tiêu khó trị hơn", "B": "Thượng tiêu bệnh nhẹ hơn, dư dành âm tế hơn Hạ tiêu", "C": "Thượng tiêu luôn dẫn đến thoát dương", "D": "Thượng tiêu không liên quan đến Tâm và Phế"},
     "ans": "B"},

    {"q": "Thấp nhiệt ở Trung Tiêu thì nên tránh dùng thuốc nào?",
     "opts": {"A": "Thấp nhiệt, Khuyên thích", "B": "Thuốc béo nhuận, khô tanh, trực tiếp bổ Khí", "C": "Thuốc thanh nhiệt", "D": "Thuốc hóa uất"},
     "ans": "B"},

    {"q": "Tam Tiêu biện chứng có mấy loại biến thể chính?",
     "opts": {"A": "2 loại", "B": "3 loại (Thượng, Trung, Hạ)", "C": "4 loại", "D": "5 loại"},
     "ans": "B"},

    {"q": "Chứng Trung Tiêu Thấp nhiệt tắc lung khác Khí phận đơn thuần ở điểm nào?",
     "opts": {"A": "Sốt cao hơn", "B": "Có thêm thân nặng, ngực đầy, buồn nôn, lưỡi rêu nhớt", "C": "Xuất huyết nhiều hơn", "D": "Co giật nhiều hơn"},
     "ans": "B"},

    {"q": "Hạ Tiêu nhiệt mà âm kiệt (cuối giai đoạn) thì biểu hiện gì?",
     "opts": {"A": "Sốt cao, xuất huyết", "B": "Tay chân thường động run, lưỡi đỏ khô, mạch tế sác", "C": "Táo bón, bụng căng cứng", "D": "Ho, mạch đỏ"},
     "ans": "B"},

    {"q": "Theo Ngô Cúc Thông, khi bệnh ở Thượng Tiêu không thể trị dùng phép 'Tư Phế giải biểu' mà truyền xuống, cần dùng phép gì?",
     "opts": {"A": "Thanh Doanh khu nhiệt", "B": "Thừa Khí Thang thông hạ", "C": "Trả về 'bào' chứa Tâm, khai khiếu tỉnh thần", "D": "Phục Mạch Thang dự âm"},
     "ans": "C"},

    {"q": "Tác phẩm 'Ôn Bệnh Điều Biện' được Ngô Cúc Thông viết vào thời nào?",
     "opts": {"A": "Nhà Minh", "B": "Nhà Thanh", "C": "Nhà Tống", "D": "Nhà Hán"},
     "ans": "B"},

    {"q": "Trung Tiêu Vị nhiệt bốc lên (Wi re shang chong) biểu hiện gì?",
     "opts": {"A": "Ho, khó thở", "B": "Nuốt khô, miệng đắng, sốt, lưỡi rêu vàng khô", "C": "Tiểu đỏ, ban chẩn", "D": "Co giật, cổ cứng"},
     "ans": "B"},

    {"q": "Điều trị Trung Tiêu Vị nhiệt khô biểu hiện 'Táo Hàn' dùng bài thuốc nào?",
     "opts": {"A": "Bạch Hổ Thang", "B": "Tăng Khí Thang (Thừa khí thang biến)", "C": "Ngân Kiều Tán", "D": "Tang Cúc Ẩm"},
     "ans": "B"},

    {"q": "Hạ Tiêu nhiệt tắc Bào cung (bó cung huyết) thì dùng phép gì?",
     "opts": {"A": "Thông hạ tiết nhiệt", "B": "Lương huyết giải độc, chúc huyết tống kinh", "C": "Thanh Khí sinh tân", "D": "Tư Phế hóa đàm"},
     "ans": "B"},

    {"q": "Theo Ngô Cúc Thông, Vị là gì trong Trung Tiêu?",
     "opts": {"A": "Nội quan", "B": "Tên thứ (cái chum) nước cốc tinh vi", "C": "Dương cơ căn bản", "D": "Gốc rễ của Hậu Thiên"},
     "ans": "B"},

    {"q": "Thượng Tiêu Phế nhiệt truyền xuống Đại trường biểu hiện như thế nào?",
     "opts": {"A": "Sốt cao, khát nhiều", "B": "Ho, khó thở kèm với đại tiện lỏng, chảy máu", "C": "Hôn mê, nói ngàn", "D": "Co giật, lưỡi cứng"},
     "ans": "B"},

    {"q": "Thượng Tiêu Tâm nhiệt (Tâm hỏa) biểu hiện như thế nào?",
     "opts": {"A": "Sốt cao, khát nước", "B": "Miệng nhiệt, lửa, tiểu tiện vàng đỏ và ít, tâm phiền", "C": "Táo bón, bụng căng", "D": "Ban chẩn, xuất huyết"},
     "ans": "B"},

    {"q": "Trung Tiêu Thấp nhiệt hỗn hợp biểu hiện gì?",
     "opts": {"A": "Sốt cao, khát nước, mồ hôi nhiều", "B": "Sốt thấp không được làm lui, miệng đắng nhạt, ngực đầy, buồn nôn",
              "C": "Ban chẩn, xuất huyết", "D": "Co giật, mắt trắng"},
     "ans": "B"},

    {"q": "Hạ Tiêu bệnh hồi phục thường có biểu hiện gì?",
     "opts": {"A": "Sốt lại cao hơn", "B": "Sốt lui dần, âm phục hồi, tay chân ấm, tinh thần tỉnh táo hơn", "C": "Xuất huyết nhiều hơn", "D": "Co giật lại"},
     "ans": "B"},

    {"q": "Ngô Cúc Thông phân biệt Ôn Bệnh với Thương Hàn ở điểm nào chính?",
     "opts": {"A": "Ôn Bệnh do khí lạnh, Thương Hàn do phong nhiệt", "B": "Ôn Bệnh khởi phát từ miệng-mũi, thường hàm âm, Thương Hàn do hàn tắc biểu Dương", "C": "Ôn Bệnh chỉ gây sốt, Thương Hàn chỉ gây lạnh", "D": "Ôn Bệnh chỉ trị được bằng Tam Tiêu"},
     "ans": "B"},

    {"q": "Triệu chứng 'Xuân Ôn' (Ôn Âm) trong Hạ Tiêu giai đoạn cuối là gì?",
     "opts": {"A": "Sốt cao buổi sáng", "B": "Sốt âm buổi chiều và tối, âm kiệt, tay chân thường động run", "C": "Sốt buổi sáng, lạnh buổi tối", "D": "Sốt liên tục không lui"},
     "ans": "B"},

    # ============================================================
    # SECTION 3: Phân biệt Thương Hàn vs Ôn Bệnh (25 câu)
    # ============================================================

    {"q": "Thương Hàn do ai hệ thống hóa thành 'Thương Hàn Luận'?",
     "opts": {"A": "Diệp Thiên Sĩ", "B": "Trương Trọng Cảnh", "C": "Ngô Cúc Thông", "D": "Vương Mạnh Anh"},
     "ans": "B"},

    {"q": "Thương Hàn khởi phát theo biện chứng nào?",
     "opts": {"A": "Vệ Khí Dinh Huyết", "B": "Lục kinh (Thái dương, Dương minh, Thiếu dương, Thái âm, Thiếu âm, Quyết âm)", "C": "Tam Tiêu", "D": "Ngũ Tạng"},
     "ans": "B"},

    {"q": "Ôn Bệnh khởi phát theo biện chứng nào chủ yếu?",
     "opts": {"A": "Lục kinh", "B": "Vệ Khí Dinh Huyết hoặc Tam Tiêu", "C": "Ngũ hành", "D": "Kinh lạc"},
     "ans": "B"},

    {"q": "Thương Hàn Thái Dương bệnh biểu hiện gì khác Ôn Bệnh Vệ phận?",
     "opts": {"A": "Sốt cao hơn", "B": "Sợ lạnh nhiều hơn sợ gió, đau gáy cổ cứng, mạch phù căng", "C": "Khát nước nhiều hơn", "D": "Mê sảng sớm hơn"},
     "ans": "B"},

    {"q": "Ôn Bệnh Vệ phận khác Thương Hàn Thái Dương bệnh ở điểm nào?",
     "opts": {"A": "Sợ lạnh nhiều hơn", "B": "Sợ gió nhiều hơn sợ lạnh, khát nước, họng đau, mạch phù sác", "C": "Đau đầu ít hơn", "D": "Lưỡi rêu trắng dày hơn"},
     "ans": "B"},

    {"q": "Phép trị khi mới mắc bệnh: Ôn Bệnh dùng gì, Thương Hàn dùng gì?",
     "opts": {"A": "Ôn Bệnh: Ma Hoàng Thang; Thương Hàn: Ngân Kiều Tán", "B": "Ôn Bệnh: Ngân Kiều Tán/Tang Cúc Ẩm; Thương Hàn: Ma Hoàng Thang/Quế Chi Thang", "C": "Cả hai dùng Bạch Hổ Thang", "D": "Cả hai dùng Tiểu Sài Hồ Thang"},
     "ans": "B"},

    {"q": "Khi nói 'Thương Hàn uất nhiệt hóa hỏa' có nghĩa là gì?",
     "opts": {"A": "Thương Hàn biến thành Ôn Bệnh", "B": "Hàn khí uất lại hóa thành nhiệt sau vài ngày", "C": "Ôn Bệnh biến thành Thương Hàn", "D": "Bệnh trở thành mãn tính"},
     "ans": "B"},

    {"q": "Ôn Bệnh có thể gây thương âm sớm hơn Thương Hàn vì sao?",
     "opts": {"A": "Ôn bệnh kém khí hơn", "B": "Ôn nhiệt là dương tặc, dễ hun đốt âm dịch, hàm thương âm từ đầu", "C": "Ôn bệnh dùng thuốc nhiều hơn", "D": "Ôn bệnh ít giải biểu hơn"},
     "ans": "B"},

    {"q": "Thương Hàn Lục Kinh và Ôn Bệnh Vệ-Khí-Dinh-Huyết khác nhau ở đâu?",
     "opts": {"A": "Thương Hàn tập trung vào tạng phủ, Ôn Bệnh tập trung vào kinh lạc", "B": "Thương Hàn theo kinh mạc tuyến, Ôn Bệnh theo hàm thương âm dịch là chính", "C": "Thương Hàn không có giai đoạn cuối", "D": "Ôn Bệnh không có giai đoạn khởi phát"},
     "ans": "B"},

    {"q": "Dương Minh Kinh chứng của Thương Hàn tương ứng với giai đoạn nào của Ôn Bệnh?",
     "opts": {"A": "Vệ phận", "B": "Khí phận", "C": "Doanh phận", "D": "Huyết phận"},
     "ans": "B"},

    {"q": "Theo Diệp Thiên Sĩ, Ôn Bệnh không như Thương Hàn vì 'Ôn Bệnh khí đầu tiên vào đâu'?",
     "opts": {"A": "Vào Thái Dương kinh", "B": "Vào Phế và Vệ (Vệ phận)", "C": "Vào Tâm Bào", "D": "Vào Thâm Tinh"},
     "ans": "B"},

    {"q": "Thương Hàn táo bón (Dương minh Phủ chứng) dùng Ma Tử Nhân Hoàn/Thừa Khí Thang. Ôn Bệnh Khí phận táo bón dùng gì?",
     "opts": {"A": "Bạch Hổ Thang đơn thuần", "B": "Thừa Khí Thang biến chế, có thể thêm thuốc dưỡng âm", "C": "Ngân Kiều Tán", "D": "Cường âm linh dương"},
     "ans": "B"},

    {"q": "Ôn Bệnh có thể có 'nghịch truyền' là gì?",
     "opts": {"A": "Bệnh đi từ Hạ lên Thượng", "B": "Từ Vệ phận (hoặc Thượng Tiêu) đột ngột truyền thẳng vào Tâm Bào, bỏ qua Khí và Doanh phận", "C": "Bệnh từ Thương Hàn biến thành Ôn Bệnh", "D": "Bệnh từ tạng phủ vào kinh lạc"},
     "ans": "B"},

    {"q": "Thương Hàn ít gây 'nghịch truyền' hơn Ôn Bệnh vì sao?",
     "opts": {"A": "Hàn là âm tặc, ít bị hóa nhiệt cấp", "B": "Thương Hàn dùng thuốc mạnh hơn", "C": "Thương Hàn tồn tại ngắn hơn", "D": "Thương Hàn không ảnh hưởng Tâm Bào"},
     "ans": "A"},

    {"q": "Sai biệt về lưỡi: Ôn Bệnh lưỡi đỏ, Thương Hàn buổi đầu lưỡi thế nào?",
     "opts": {"A": "Lưỡi đỏ, ít rêu", "B": "Lưỡi hồng bình thường hoặc rêu trắng mỏng", "C": "Lưỡi tím nhạt", "D": "Lưỡi vàng dày khô"},
     "ans": "B"},

    {"q": "Khí phận Ôn Bệnh và Dương Minh Kinh chứng Thương Hàn có gì giống nhau?",
     "opts": {"A": "Đều sợ lạnh nhiều", "B": "Đều có sốt cao, khát nước, lưỡi rêu vàng", "C": "Đều hôn mê, nói ngàn", "D": "Đều có ban chẩn"},
     "ans": "B"},

    {"q": "Phân biệt: Doanh phận Ôn Bệnh và Thiếu Âm Kinh Thương Hàn ở điểm nào?",
     "opts": {"A": "Đều có sốt cao", "B": "Doanh phận sốt âm, lưỡi đỏ không rêu; Thiếu Âm có lạnh cực, mạch tế nhược", "C": "Đều có hôn mê", "D": "Đều có ban chẩn"},
     "ans": "B"},

    {"q": "Ôn Bệnh Thấp Nhiệt (Thấp Ôn) khác Thương Hàn ở điểm nào?",
     "opts": {"A": "Ôn Bệnh không có thân nặng", "B": "Ôn Bệnh có thêm uất nhớt, thân nặng, lưỡi rêu nhớt; Thương Hàn chỉ có hàn và nhiệt đơn thuần", "C": "Ôn Bệnh khát nước nhiều hơn", "D": "Ôn Bệnh không có đau đầu"},
     "ans": "B"},

    {"q": "Biến chứng nào của Ôn Bệnh KHÔNG có trong Thương Hàn?",
     "opts": {"A": "Sốt cao, khát nước", "B": "Nghịch truyền Tâm Bào, xuất huyết nhiều nơi, âm kiệt nhanh", "C": "Táo bón", "D": "Co giật"},
     "ans": "B"},

    {"q": "Thương Hàn chính thống trị bằng gì, Ôn Bệnh chính thống trị bằng gì?",
     "opts": {"A": "Cả hai dùng Thừa Khí Thang", "B": "Thương Hàn: phát hãn, hòa giải, thông hạ; Ôn Bệnh: thanh nhiệt, lương huyết, dự âm", "C": "Thương Hàn dùng thuốc lạnh, Ôn Bệnh dùng thuốc ấm", "D": "Cả hai dùng thuốc giải biểu"},
     "ans": "B"},

    {"q": "Tại sao Ôn Bệnh cấm dùng phát hãn bằng Ma Hoàng?",
     "opts": {"A": "Ma Hoàng quá đắt", "B": "Ma Hoàng tán hàn phát biểu mạnh, dễ khuếch tán Ôn nhiệt thêm, gây ra âm thoát", "C": "Ma Hoàng gây hôn mê", "D": "Ma Hoàng không có tác dụng với Ôn Bệnh"},
     "ans": "B"},

    {"q": "Giai đoạn cuối Thương Hàn là gì, giai đoạn cuối Ôn Bệnh là gì?",
     "opts": {"A": "Đều là Thoát Dương", "B": "Thương Hàn: Thiếu Âm lạnh cực (Dương hồi) hoặc phục; Ôn Bệnh: Huyết phận âm kiệt, thoát dương", "C": "Thương Hàn: Xuất huyết; Ôn Bệnh: Co giật", "D": "Đều là hôn mê"},
     "ans": "B"},

    {"q": "Ôn Bệnh Đông Ôn (Ôn Âm mùa đông) khác Thương Hàn ở điểm nào?",
     "opts": {"A": "Đông Ôn chỉ xảy ra vào mùa hè", "B": "Đông Ôn khởi phát có sốt, sợ lạnh ít, khát nước, rêu hồng ở trong; Thương Hàn sợ lạnh nhiều, chưa có nhiệt rị", "C": "Đông Ôn chỉ ảnh hưởng Phế", "D": "Đông Ôn không có đau đầu"},
     "ans": "B"},

    {"q": "Theo Vương Mạnh Anh, Ôn Bệnh và Thương Hàn 'đồng trung dị tố' (giống và khác) ở điểm nào?",
     "opts": {"A": "Giống: đều do phong; Khác: đường đầu vào khác nhau", "B": "Giống: đều là ngoại cảm; Khác: Ôn Bệnh do Ôn nhiệt tặc, Thương Hàn do Hàn tặc, tính chất ôn khí khác hàn khí", "C": "Giống: đều trị bằng phát hãn; Khác: Ôn Bệnh nhanh hơn", "D": "Giống: đều ảnh hưởng Tâm; Khác: Thương Hàn ảnh hưởng Phế nhiều hơn"},
     "ans": "B"},

    {"q": "Trên lâm sàng, dấu hiệu nào để phân biệt Vệ phận Ôn Bệnh với Thái Dương Trúng Phong Thương Hàn?",
     "opts": {"A": "Mức độ sốt", "B": "Ôn Bệnh họng đau, khát nước từ đầu; Thái Dương Trúng Phong chỉ sợ gió, ra mồ hôi, không khát", "C": "Mức độ đau đầu", "D": "Mức độ sợ lạnh"},
     "ans": "B"},

    # ============================================================
    # SECTION 4: Ôn bệnh phương tễ đặc trưng (30 câu)
    # ============================================================

    {"q": "Ngân Kiều Tán (Yin Qiao San) chủ trị biểu chứng gì?",
     "opts": {"A": "Khí phận nhiệt mạc Phế", "B": "Vệ phận Phong nhiệt phạm Phế (Ôn bệnh giai đoạn đầu)", "C": "Doanh phận nhiệt cuồng Tâm Bào", "D": "Huyết phận xuất huyết"},
     "ans": "B"},

    {"q": "Thành phần chính của Ngân Kiều Tán là gì?",
     "opts": {"A": "Thạch cao, Tri mẫu, Ngân hoa, Liên kiều", "B": "Ngân hoa, Liên kiều, Bạc hà, Bạt đậu, Cam thảo, Nhật canh, Lô căn, Trúc dịch", "C": "Cần địa, Tê giác, Mạch đông, Nguyên sâm", "D": "Hoàng liên, Hoàng cầm, Hoàng bá, Chi tử"},
     "ans": "B"},

    {"q": "Tang Cúc Ẩm (Sang Ju Yin) chủ trị biểu chứng gì?",
     "opts": {"A": "Khí phận nhiệt tắc Phế", "B": "Vệ phận Phong nhiệt phạm Phế thể nhẹ (ho nhiều hơn Ngân Kiều Tán)", "C": "Doanh phận khu nhiệt", "D": "Huyết phận tán ứ"},
     "ans": "B"},

    {"q": "Thành phần chính của Tang Cúc Ẩm là gì?",
     "opts": {"A": "Ngân hoa, Liên kiều, Bạc hà", "B": "Tang lá, Cúc hoa, Hạnh nhân, Liên kiều, Bạc hà, Cam thảo, Lô căn, Vỹ canh", "C": "Thạch cao, Tri mẫu, Cam thảo", "D": "Cần địa, Tê giác, Mạch đông"},
     "ans": "B"},

    {"q": "Bạch Hổ Thang gồm những vị thuốc nào?",
     "opts": {"A": "Ngân hoa, Liên kiều, Bạc hà, Cam thảo", "B": "Thạch cao (quân), Tri mẫu (thần), Cam thảo (tá), Ngân gạo (sứ)", "C": "Cần địa, Mạch đông, Huyền sâm, Tê giác", "D": "Hoàng liên, Hoàng cầm, Chi tử, Hòa thanh"},
     "ans": "B"},

    {"q": "Bạch Hổ Thang chủ trị chứng gì trong Ôn Bệnh?",
     "opts": {"A": "Vệ phận phong nhiệt", "B": "Khí phận 'Tứ Đại' (Dương minh Kinh chứng): sốt cao, khát nhiều, mồ hôi nhiều, mạch hồng sác", "C": "Doanh phận nhiệt cuồng", "D": "Huyết phận xuất huyết"},
     "ans": "B"},

    {"q": "Bạch Hổ Thang thêm Nhân Sâm (Bai Hu Jia Ren Shen Tang) dùng trong trường hợp nào?",
     "opts": {"A": "Thêm nhiệt độ lớn", "B": "Bệnh nhân khí hồi suy, nhiệt cao và mất nước nhiều, mạch hồng sác vô lực", "C": "Bệnh nhân âm hồi cao", "D": "Bệnh nhân có ban chẩn nhiều"},
     "ans": "B"},

    {"q": "Bạch Hổ Thang thêm Cần Địa, Mạch Đông, Nhân Sâm biết gì?",
     "opts": {"A": "Bạch Hổ Nhân Sâm Thang", "B": "Bạch Hổ Gia Cần Địa Mạch Đông Nhân Sâm Thang, dùng khi nhiệt cao, âm tổn, khí hồi", "C": "Thanh Doanh Thang", "D": "Zhu Ye Shi Gao Tang"},
     "ans": "B"},

    {"q": "Thanh Doanh Thang (Qing Ying Tang) chủ trị chứng gì?",
     "opts": {"A": "Vệ phận phong nhiệt", "B": "Doanh phận nhiệt, thanh Doanh khu nhiệt, thấu âm", "C": "Khí phận táo bón", "D": "Huyết phận xuất huyết"},
     "ans": "B"},

    {"q": "Thanh Doanh Thang gồm những vị thuốc nào?",
     "opts": {"A": "Thạch cao, Tri mẫu, Cam thảo, Ngân gạo", "B": "Tê giác, Cần địa, Huyền sâm, Mạch đông, Trúc Diệp, Đan sâm, Hoàng liên, Ngân hoa", "C": "Ngân hoa, Liên kiều, Bạc hà, Bạt đậu", "D": "Hổ phách, Ngưu hoàng, Xạ hương"},
     "ans": "B"},

    {"q": "Tê Giác Địa Hoàng Thang (Xi Jiao Di Huang Tang) chủ trị chứng gì?",
     "opts": {"A": "Khí phận nhiệt kết", "B": "Huyết phận nhiệt cuồng Huyết động (thanh nhiệt lương huyết, tán ứ)", "C": "Vệ phận giải biểu", "D": "Doanh phận thấu âm"},
     "ans": "B"},

    {"q": "Tê Giác Địa Hoàng Thang gồm những vị thuốc nào?",
     "opts": {"A": "Ngân hoa, Liên kiều, Bạc hà", "B": "Tê giác (hoặc Trâu y giác thay Tê giác), Cần địa, Xích thược, Đan bì", "C": "Thạch cao, Tri mẫu, Ngân gạo, Cam thảo", "D": "Hoàng liên, Hoàng cầm, Hoàng bá, Chi tử"},
     "ans": "B"},

    {"q": "Phương tễ nào được dùng để 'khai khiếu tỉnh thần' khi nhiệt truyền Tâm Bào?",
     "opts": {"A": "Bạch Hổ Thang", "B": "An Cung Ngưu Hoàng Hoàn, Zi Xue Dan, hoặc Zhi Bao Dan", "C": "Ngân Kiều Tán", "D": "Thanh Doanh Thang"},
     "ans": "B"},

    {"q": "An Cung Ngưu Hoàng Hoàn dùng trong trường hợp nào?",
     "opts": {"A": "Vệ phận phong nhiệt", "B": "Nhiệt truyền Tâm Bào: hôn mê, nói ngàn, sốt cao, lưỡi đỏ", "C": "Khí phận táo bón", "D": "Hạ Tiêu âm kiệt"},
     "ans": "B"},

    {"q": "Zhu Ye Shi Gao Tang (Trúc Diệp Thạch Cao Thang) dùng khi nào?",
     "opts": {"A": "Đầu giai đoạn Ôn Bệnh", "B": "Sau Khí phận: nhiệt còn dư, khí âm lưỡng hại, tâm phiền khát nước, tiểu tiện ít", "C": "Giai đoạn Huyết phận", "D": "Thương Hàn Thái Dương"},
     "ans": "B"},

    {"q": "Điều trị Doanh phận có thể thêm Ngân hoa, Liên kiều vào Thanh Doanh Thang để làm gì?",
     "opts": {"A": "Tăng tác dụng thanh nhiệt", "B": "Thấu âm biểu (giải biểu) để dẫn nhiệt từ Doanh ra Khí mà giải", "C": "Tăng tác dụng cầm huyết", "D": "Tăng tác dụng khai khiếu"},
     "ans": "B"},

    {"q": "Hóa Ban Thang (Hua Ban Tang) biến phương của Bạch Hổ Thang dùng khi nào?",
     "opts": {"A": "Vệ phận bệnh nhẹ", "B": "Khí phận nhiệt mạc Phế kèm ban chẩn (nhiệt + uất)", "C": "Hạ Tiêu âm kiệt", "D": "Huyết phận thoát dương"},
     "ans": "B"},

    {"q": "Ma Hạnh Thạch Cam Thang (Ma Xing Shi Gan Tang) dùng trong trường hợp nào Ôn Bệnh?",
     "opts": {"A": "Vệ phận phong nhiệt nhẹ", "B": "Khí phận nhiệt mạc Phế: sốt cao, khó thở, ho, ngực đau, không sợ lạnh", "C": "Doanh phận nhiệt cuồng", "D": "Huyết phận xuất huyết"},
     "ans": "B"},

    {"q": "Ngân Kiều Tán nên lui/thoái lui những vị thuốc nào khi khi Ôn tắc Phế (nhiệt mạc Phế)?",
     "opts": {"A": "Lui Ngân hoa, Liên kiều", "B": "Lui Bạc hà (vì phát tán quá mạnh, có thể tổn âm), thêm Hạnh nhân, Chế tỳ bà diệp, Lô căn", "C": "Lui Cam thảo", "D": "Lui Trúc dịch"},
     "ans": "B"},

    {"q": "Phục Mạch Thang (Fu Mai Tang) dùng trong trường hợp nào?",
     "opts": {"A": "Khí phận nhiệt kết", "B": "Hạ Tiêu giai đoạn cuối: âm kiệt, mạch tế sác, nhiệt âm, tay chân lạnh", "C": "Vệ phận phong nhiệt", "D": "Thượng Tiêu nhiệt mạc Phế"},
     "ans": "B"},

    {"q": "San Jia Fu Mai Tang (Tam Giáp Phục Mạch Thang) dùng khi nào?",
     "opts": {"A": "Khí phận táo bón", "B": "Hạ Tiêu âm kiệt kèm phong động nội (tay chân thường động run), thêm Quy bản, Mẫu lệ, Miết giáp vào Phục Mạch Thang", "C": "Vệ phận giải biểu", "D": "Doanh phận khu nhiệt"},
     "ans": "B"},

    {"q": "Huang Lian Jie Du Tang (Hoàng Liên Giải Độc Thang) dùng trong trường hợp nào của Ôn Bệnh?",
     "opts": {"A": "Vệ phận phong nhiệt", "B": "Khí phận hoặc Doanh phận: tam Khí (ba chứng khí nhiệt) độc nhiệt cực thực", "C": "Huyết phận âm kiệt", "D": "Hạ Tiêu âm hồi"},
     "ans": "B"},

    {"q": "Điều trị Vệ phận phong nhiệt thể nặng, có thể bổ sung thêm thuốc gì vào Ngân Kiều Tán?",
     "opts": {"A": "Hoàng kỳ, Đảng sâm", "B": "Hoàng cầm, Chi tử, Sinh Ma, Cúc hoa", "C": "Thạch cao, Tri mẫu", "D": "Cần địa, Mạch đông"},
     "ans": "B"},

    {"q": "Tang Cúc Ẩm khác Ngân Kiều Tán ở điểm nào chính?",
     "opts": {"A": "Tang Cúc Ẩm mạnh hơn", "B": "Tang Cúc Ẩm nhiều hơn Tang lá và Cúc hoa, lục hóa âm giải biểu, chủ trị Phong nhiệt phạm Phế với triệu chứng ho nhiều", "C": "Ngân Kiều Tán mạnh hơn về khu nhiệt", "D": "Tang Cúc Ẩm có thêm Tê giác"},
     "ans": "B"},

    {"q": "Thanh Doanh Thang là bài thuốc của ai?",
     "opts": {"A": "Trương Trọng Cảnh", "B": "Ngô Cúc Thông (trong Ôn Bệnh Điều Biện)", "C": "Diệp Thiên Sĩ", "D": "Liêu Kinh"},
     "ans": "B"},

    {"q": "Tê Giác Địa Hoàng Thang là bài thuốc có xuất xứ từ đâu?",
     "opts": {"A": "Thương Hàn Luận", "B": "Bào Cao Luận (Bei Ji Qian Jin Yao Fang) của Tôn Tư Mão, sau được Diệp Thiên Sĩ và Ôn Bệnh gia sử dụng", "C": "Ôn Bệnh Điều Biện của Ngô Cúc Thông", "D": "Wen Re Jing Wei"},
     "ans": "B"},

    {"q": "Bạch Hổ Thang ở Ôn Bệnh có thêm 'Nhân Sâm' thì gọi là gì và dùng khi nào?",
     "opts": {"A": "Bạch Hổ gia Quế Chi Thang; khi có lạnh cực", "B": "Bạch Hổ gia Ren Shen Tang; khi nhiệt cao, mồ hôi nhiều, khí âm lưỡng tái (cả khí và âm đều tổn)", "C": "Bạch Hổ gia Cần Địa Thang; khi âm kiệt", "D": "Bạch Hổ gia Cang Mi Thang; khi táo bón"},
     "ans": "B"},

    {"q": "Ngân Kiều Tán và Ma Hạnh Thạch Cam Thang khác nhau ở điều gì chính?",
     "opts": {"A": "Ngân Kiều Tán cho nhiệt ở Khí phận, Ma Hạnh Thạch Cam Thang cho nhiệt ở Vệ phận", "B": "Ngân Kiều Tán chủ Vệ phận phong nhiệt nhẹ; Ma Hạnh Thạch Cam Thang chủ Khí phận nhiệt mạc Phế với khó thở, ngực đau rõ ràng", "C": "Hai bài thuốc tương đương nhau", "D": "Ma Hạnh Thạch Cam Thang có chứa Tê giác"},
     "ans": "B"},

    {"q": "Trong bài Thanh Doanh Thang, vị thuốc nào có tác dụng 'thấu âm biểu' (dẫn nhiệt ra ngoài)?",
     "opts": {"A": "Tê giác, Cần địa", "B": "Ngân hoa, Liên kiều (thêm vào)", "C": "Đan sâm, Trúc Diệp", "D": "Hoàng liên"},
     "ans": "B"},

    {"q": "Khi Ôn Bệnh ở Khí phận có ban chẩn (uất nhiệt), Bạch Hổ Thang được biến chế thêm gì?",
     "opts": {"A": "Thêm Nhân Sâm", "B": "Thêm Thương bồ, Hóa nhân (Hóa Ban Thang)", "C": "Thêm Cần địa, Mạch đông", "D": "Thêm Tê giác"},
     "ans": "B"},

    # ============================================================
    # SECTION 5: Diệp Thiên Sĩ học thuyết (20 câu)
    # ============================================================

    {"q": "Diệp Thiên Sĩ là ai trong Ôn Bệnh học?",
     "opts": {"A": "Người hệ thống Tam Tiêu biện chứng", "B": "Thầy thuốc nhà Thanh, người sáng lập biện chứng Vệ-Khí-Dinh-Huyết trong Ôn Bệnh", "C": "Người viết Thương Hàn Luận", "D": "Người viết Ôn Bệnh Tiêu Tiết"},
     "ans": "B"},

    {"q": "Tác phẩm chính của Diệp Thiên Sĩ là gì?",
     "opts": {"A": "Ôn Bệnh Điều Biện", "B": "Ôn Nhiệt Luận (Ôn Re Lun) - do học trò ghi lại từ y án", "C": "Wen Re Jing Wei", "D": "Thương Hàn Luận"},
     "ans": "B"},

    {"q": "Diệp Thiên Sĩ nhận xét 'Wen bing yu Shang Han da yi' có nghĩa là gì?",
     "opts": {"A": "Ôn Bệnh và Thương Hàn là một", "B": "Ôn Bệnh khác Thương Hàn ở nhiều điểm: nhiệt tặc ở Vệ, hay thương âm, khác biện cách trị", "C": "Ôn Bệnh chính là Thương Hàn biến thể", "D": "Ôn Bệnh nhẹ hơn Thương Hàn"},
     "ans": "B"},

    {"q": "Diệp Thiên Sĩ mô tả lưỡi Chẩn (舌診) trong Ôn Bệnh thế nào?",
     "opts": {"A": "Lưỡi không có giá trị chẩn đoán Ôn Bệnh", "B": "Lưỡi là gương độc của Tâm; lưỡi đỏ: Doanh-Huyết phận; rêu vàng dày: Khí phận; rêu trắng: Vệ phận", "C": "Chỉ cần nhìn mạch là đủ", "D": "Lưỡi chỉ quan trọng trong Thương Hàn"},
     "ans": "B"},

    {"q": "Theo Diệp Thiên Sĩ, lưỡi 'Sẫm hồng' (đỏ sẫm) biểu hiện Ôn bệnh ở phận nào?",
     "opts": {"A": "Vệ phận", "B": "Khí phận", "C": "Doanh-Huyết phận (nhiệt vào Doanh Huyết)", "D": "Tam tiêu chuyển hóa"},
     "ans": "C"},

    {"q": "Đặc điểm lưỡi Khí phận theo Diệp Thiên Sĩ là gì?",
     "opts": {"A": "Lưỡi đỏ, không rêu", "B": "Lưỡi vàng (rêu vàng), hoặc khô, biểu hiện nhiệt tắc Khí phận", "C": "Lưỡi trắng mỏng", "D": "Lưỡi tím nhạt"},
     "ans": "B"},

    {"q": "Diệp Thiên Sĩ mô tả phần biểu hiện của 'Dinh phận' (Ban chẩn) thế nào?",
     "opts": {"A": "Ban chẩn chỉ là phát ban da bình thường", "B": "Ban chẩn: nhiệt truyền Huyết phận, huyết rể ra ngoài cơ thể (ban đỏ hoặc ban sẫm, có thể nổi lên)", "C": "Ban chẩn chỉ xảy ra ở trẻ em", "D": "Ban chẩn không có giá trị chẩn đoán"},
     "ans": "B"},

    {"q": "Theo Diệp Thiên Sĩ, 'Vệ Khí Doanh Huyết' tương ứng với lớp nào của cơ thể?",
     "opts": {"A": "Kinh lạc, Phủ, Tạng, Tướng", "B": "Biểu (Vệ) -> Bán biểu bán lý (Khí) -> Lý (Doanh) -> Cực lý (Huyết)", "C": "Da, Cơ, Xương, Tủy", "D": "Phế, Tỳ, Tâm, Thận"},
     "ans": "B"},

    {"q": "Diệp Thiên Sĩ nhấn mạnh 'bảo vệ Tâm âm' trong điều trị Ôn Bệnh vì sao?",
     "opts": {"A": "Tâm âm là gốc rễ của sức đề kháng", "B": "Nhiệt độc dễ hun đốt Tâm âm, gây Tâm Bào bị thương, dẫn đến hôn mê, nói ngàn", "C": "Tâm âm liên quan đến sinh sướng", "D": "Tâm âm tăng cường miễn dịch"},
     "ans": "B"},

    {"q": "Đặc điểm 'nhiệt' trong Ôn Bệnh theo Diệp Thiên Sĩ là gì?",
     "opts": {"A": "Nhiệt là âm tặc", "B": "Nhiệt là Dương tặc, dễ khô, dễ thương âm; phải dùng thuốc lương nhuận và dự âm từ sớm", "C": "Nhiệt có thể trị được bằng phát hãn", "D": "Nhiệt chỉ tồn tại ở biểu"},
     "ans": "B"},

    {"q": "Diệp Thiên Sĩ phân làm mấy loại lưỡi chính trong chẩn đoán Ôn Bệnh?",
     "opts": {"A": "2 loại (hồng và đỏ)", "B": "Nhiều dạng: lưỡi hồng (Vệ phận), lưỡi đỏ (Khí/Doanh phận), lưỡi sẫm đỏ (Huyết phận), lưỡi tím nhạt (Huyết ứ/khô)", "C": "3 loại đơn giản", "D": "Chỉ 1 loại tổng quát"},
     "ans": "B"},

    {"q": "Khi Diệp Thiên Sĩ nói 'Lưỡi hồng, rêu trắng mỏng' biểu hiện Ôn Bệnh ở giai đoạn nào?",
     "opts": {"A": "Khí phận", "B": "Vệ phận (bệnh ở ngoài, chưa vào sâu)", "C": "Doanh phận", "D": "Huyết phận"},
     "ans": "B"},

    {"q": "Đặc điểm của ban chẩn 'Dinh' (Chẩn) là gì?",
     "opts": {"A": "Nổi lên trên mặt da, đỏ, ấn vào mất màu", "B": "Phẳng với mặt da, đỏ sẫm, ấn không mất màu; biểu hiện nhiệt trong Huyết phận nghiêm trọng", "C": "Xuất hiện chủ yếu ở bàn tay", "D": "Màu vàng nhạt, ấn mất màu"},
     "ans": "B"},

    {"q": "Đặc điểm của ban chẩn 'Chẩn' (Ban) là gì?",
     "opts": {"A": "Phẳng với mặt da", "B": "Nổi cao trên mặt da, đỏ tươi, ấn vào mất màu (phù đang); biểu hiện nhiệt trong Khí-Doanh phận, chưa vào Huyết sâu", "C": "Màu tím nhạt", "D": "Chỉ ở mặt"},
     "ans": "B"},

    {"q": "Theo Diệp Thiên Sĩ, ban chẩn xuất hiện ở giai đoạn nào của Ôn Bệnh?",
     "opts": {"A": "Vệ phận", "B": "Khí-Doanh giao thoa hoặc Doanh-Huyết phận", "C": "Chỉ ở Huyết phận", "D": "Chỉ ở giai đoạn khởi phục"},
     "ans": "B"},

    {"q": "Điều trị ban chẩn theo Diệp Thiên Sĩ là gì?",
     "opts": {"A": "Giải biểu tăng cần phát hãn", "B": "Thanh Doanh lương Huyết, tán ứ giải độc, không được phát hãn hay tiêu đạo", "C": "Dùng Bạch Hổ Thang", "D": "Dùng Thừa Khí Thang"},
     "ans": "B"},

    {"q": "Lưỡi 'Jing (Khám) đỏ - Rêu vàng khô' biểu hiện Ôn Bệnh ở giai đoạn nào?",
     "opts": {"A": "Vệ phận", "B": "Khí phận nhiệt cực (Dương minh/Vị trường nhiệt kết)", "C": "Hạ Tiêu âm kiệt", "D": "Ôn Bệnh hồi phục"},
     "ans": "B"},

    {"q": "Lưỡi 'Sởi khô, không rêu hoặc rêu đen' biểu hiện Ôn Bệnh ở giai đoạn nào?",
     "opts": {"A": "Vệ phận", "B": "Huyết phận nghiêm trọng, âm kiệt cực, nhiệt độc thuốc huyết", "C": "Khí phận nhiệt tắc Phế", "D": "Doanh phận nhiệt cuồng"},
     "ans": "B"},

    {"q": "Diệp Thiên Sĩ đề xuất quan sát gì ngoài lưỡi để hỗ trợ chẩn đoán Ôn Bệnh?",
     "opts": {"A": "Chỉ cần nhìn lưỡi", "B": "Quan sát rêu lưỡi, màu sắc lưỡi, trạng thái ẩm ướt/khô, hình dạng lưỡi + kết hợp mạch, ngũ quan", "C": "Chỉ cần bắm mạch", "D": "Chỉ cần xem ban chẩn"},
     "ans": "B"},

    {"q": "Giao điểm quan trọng nhất giữa Diệp Thiên Sĩ và Ngô Cúc Thông trong Ôn Bệnh học là gì?",
     "opts": {"A": "Họ mâu thuẫn về toàn bộ lý thuyết", "B": "Cả hai đóng góp hệ thống hóa Ôn Bệnh: Diệp Thiên Sĩ qua Vệ-Khí-Doanh-Huyết, Ngô Cúc Thông qua Tam Tiêu; bổ sung cho nhau", "C": "Họ chỉ đồng ý về phép giải biểu", "D": "Họ chỉ khác nhau về thuốc"},
     "ans": "B"},

    # ============================================================
    # SECTION 6: Vệ phận bệnh và phép giải biểu (10 câu)
    # ============================================================

    {"q": "Phép giải biểu trong Ôn Bệnh khác Thương Hàn ở điều gì?",
     "opts": {"A": "Ôn Bệnh dùng phát hãn mạnh (Ma Hoàng), Thương Hàn dùng giải biểu nhẹ", "B": "Ôn Bệnh dùng tân lương-giải biểu (thuốc mát nhẹ, không dùng phát hãn mạnh), Thương Hàn dùng tán hàn phát biểu", "C": "Cả hai dùng cùng một phép", "D": "Ôn Bệnh không có phép giải biểu"},
     "ans": "B"},

    {"q": "Vì sao Ôn Bệnh CẤM dùng Ma Hoàng Thang để giải biểu?",
     "opts": {"A": "Ma Hoàng Thang khó tìm", "B": "Ma Hoàng Thang tán hàn phát biểu mạnh, dễ khuếch tán Ôn nhiệt thêm, gây ra âm thoát", "C": "Ma Hoàng Thang gây táo bón", "D": "Ma Hoàng Thang gây hôn mê"},
     "ans": "B"},

    {"q": "Vệ phận giải biểu Ôn Bệnh dùng những thuốc có tính vị nào?",
     "opts": {"A": "Tán, nhiệt (cay ấm)", "B": "Cay mát (Xin Liang), nhẹ nhàng giải biểu; Ví dụ: Ngân hoa, Liên kiều, Bạc hà, Ngân hồ", "C": "Khổ, lạnh, tiêu tiết", "D": "Mặn, âm, khổ, nhuận"},
     "ans": "B"},

    {"q": "Triệu chứng nào cho thấy Ôn Bệnh còn ở Vệ phận và cần tiếp tục giải biểu?",
     "opts": {"A": "Khát nước nhiều, lưỡi đỏ, rêu vàng", "B": "Sợ gió vẫn còn, sốt chưa lui, mồ hôi ít hoặc chưa ra mồ hôi, mạch phù sác", "C": "Hôn mê, nói ngàn", "D": "Ban chẩn, tiểu đỏ"},
     "ans": "B"},

    {"q": "Khi Vệ phận đã giải biểu thành công, biểu hiện như thế nào?",
     "opts": {"A": "Sốt tăng cao hơn", "B": "Ra mồ hôi nhẹ, sốt lui, sợ gió hết, tinh thần tỉnh táo", "C": "Xuất hiện ban chẩn", "D": "Khát nước tăng"},
     "ans": "B"},

    {"q": "Nếu giải biểu không đúng cách, Vệ phận có thể biến chứng như thế nào?",
     "opts": {"A": "Bệnh tự khỏi", "B": "Nhiệt vào sâu (truyền vào Khí phận), hoặc gây thương âm, hoặc nghịch truyền Tâm Bào", "C": "Bệnh thành mãn tính nhẹ", "D": "Biến thành Thương Hàn"},
     "ans": "B"},

    {"q": "Ngân Kiều Tán dùng bao nhiêu lượng Ngân hoa và Liên kiều trong nguyên phương?",
     "opts": {"A": "5g mỗi vị", "B": "Ngân hoa 1 lượng (30g), Liên kiều 1 lượng (30g) - theo nguyên phương Ngô Cúc Thông", "C": "10g mỗi vị", "D": "15g Ngân hoa, 20g Liên kiều"},
     "ans": "B"},

    {"q": "Vệ phận có thêm triệu chứng 'Uất nhiệt' (thấp) thì thêm thuốc gì vào Ngân Kiều Tán?",
     "opts": {"A": "Thêm Cần địa, Tê giác", "B": "Thêm Hoa hương, Hoạt thạch, Thương bồ để hóa thấp", "C": "Thêm Thạch cao, Tri mẫu", "D": "Thêm Hoàng liên, Hoàng bá"},
     "ans": "B"},

    {"q": "Vệ phận có thêm triệu chứng ho nhiều (Ôn bệnh phạm Phế thể nặng) nên dùng bài thuốc nào?",
     "opts": {"A": "Bạch Hổ Thang", "B": "Tang Cúc Ẩm hoặc thêm Hạnh nhân, Lô căn, Qua lâu bì vào Ngân Kiều Tán", "C": "Thanh Doanh Thang", "D": "Thừa Khí Thang"},
     "ans": "B"},

    {"q": "Kết quả chẩn đoán Ôn Bệnh ở Vệ phận cần phân biệt với bệnh nào trong ngoại cảm khác?",
     "opts": {"A": "Liệt nửa người", "B": "Cảm mạo Phong nhiệt (Phong nhiệt cảm mạo); phân biệt qua mức độ nặng, tốc độ truyền biến, khả năng thương âm", "C": "Đái tháo đường", "D": "Tăng huyết áp"},
     "ans": "B"},
]

# Verify count
assert len(Q4) == 160, f"Expected 160 questions, got {len(Q4)}"

if __name__ == "__main__":
    print(f"Total questions in Q4: {len(Q4)}")
    sections = {
        "Vệ Khí Dinh Huyết": 0,
        "Tam Tiêu": 0,
        "Phân biệt": 0,
        "Phương tễ": 0,
        "Diệp Thiên Sĩ": 0,
        "Giải biểu": 0,
    }
    print("quiz_phase4.py loaded successfully.")
