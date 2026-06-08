# -*- coding: utf-8 -*-
# Phase 1: Mạch Học - Pulse Diagnosis
# 160 câu trắc nghiệm

Q1 = [
    # =====================================================================
    # SECTION 1: Vị trí và nguyên lý bắt mạch (20 câu)
    # =====================================================================
    {
        "q": "Vị trí Thốn tay trái tương ứng tạng nào?",
        "opts": {"A": "Tâm", "B": "Phế", "C": "Can", "D": "Tỳ"},
        "ans": "A"
    },
    {
        "q": "Vị trí Quan tay trái tương ứng tạng nào?",
        "opts": {"A": "Vị", "B": "Can/Đởm", "C": "Thận", "D": "Tâm bào"},
        "ans": "B"
    },
    {
        "q": "Vị trí Xích tay trái tương ứng tạng nào?",
        "opts": {"A": "Can", "B": "Tỳ", "C": "Thận/Bàng quang", "D": "Phế đại trường"},
        "ans": "C"
    },
    {
        "q": "Vị trí Thốn tay phải tương ứng tạng nào?",
        "opts": {"A": "Tâm", "B": "Phế/Đại trường", "C": "Can", "D": "Thận"},
        "ans": "B"
    },
    {
        "q": "Vị trí Quan tay phải tương ứng tạng nào?",
        "opts": {"A": "Can/Đởm", "B": "Tâm", "C": "Tỳ/Vị", "D": "Thận/Bàng quang"},
        "ans": "C"
    },
    {
        "q": "Vị trí Xích tay phải tương ứng tạng nào?",
        "opts": {"A": "Phế", "B": "Thận/Tử cung (hoặc Tâm bào)", "C": "Can", "D": "Tỳ"},
        "ans": "B"
    },
    {
        "q": "Khi bắt mạch, người bệnh nên ở tư thế nào là chuẩn nhất?",
        "opts": {"A": "Nằm ngửa, tay để xuôi thân", "B": "Ngồi thẳng, tay để thoải mái ngang tim", "C": "Đứng thẳng", "D": "Nằm nghiêng"},
        "ans": "B"
    },
    {
        "q": "Ngón tay nào của thầy thuốc đặt lên vị trí Quan khi bắt mạch?",
        "opts": {"A": "Ngón trỏ", "B": "Ngón giữa", "C": "Ngón áp út", "D": "Ngón cái"},
        "ans": "B"
    },
    {
        "q": "Bắt mạch Thốn là vị trí tương ứng với xương nào trên cổ tay?",
        "opts": {"A": "Xương quay", "B": "Xương trụ", "C": "Xương thuyền", "D": "Đầu mỏm xương quay"},
        "ans": "D"
    },
    {
        "q": "Theo Y học cổ truyền, tần số mạch bình thường là bao nhiêu lần/phút?",
        "opts": {"A": "40-50", "B": "50-60", "C": "60-90", "D": "90-110"},
        "ans": "C"
    },
    {
        "q": "Theo chuẩn Y học cổ truyền, một nhịp thở tương ứng với bao nhiêu nhịp mạch?",
        "opts": {"A": "2 nhịp", "B": "4 nhịp", "C": "6 nhịp", "D": "8 nhịp"},
        "ans": "B"
    },
    {
        "q": "Phương pháp bắt mạch dùng ba mức áp lực (cử, án, ấn mạnh) gọi là gì?",
        "opts": {"A": "Tam tiếp pháp", "B": "Cửu hậu pháp", "C": "Phù trung án pháp", "D": "Thuốc ấn pháp"},
        "ans": "C"
    },
    {
        "q": "Mạch bình thường của người trưởng thành thường có đặc điểm nào sau đây?",
        "opts": {"A": "Có thần, có lực, đều đặn, không quá nhanh không quá chậm", "B": "Nhanh, dài, mạnh", "C": "Trầm, chậm, yếu", "D": "Hoạt, hư, không đều"},
        "ans": "A"
    },
    {
        "q": "Khi bắt mạch, áp lực nhẹ chỉ chạm tay đã cảm nhận được mạch gọi là mức áp lực nào?",
        "opts": {"A": "Án (trung)", "B": "Ấn mạnh (án)", "C": "Cử (phù)", "D": "Thuốc ấn (mạch trầm)"},
        "ans": "C"
    },
    {
        "q": "Quan Thốn Xích được xác định theo mốc gì trên cổ tay?",
        "opts": {"A": "Xương khuỷu tay", "B": "Đầu mỏm xương quay (styloid process)", "C": "Khớp cổ tay", "D": "Cấp thủ trước"},
        "ans": "B"
    },
    {
        "q": "Mạch ở vị trí Xích tay trái phản ánh tình trạng của tạng phủ nào?",
        "opts": {"A": "Tâm và Tiểu trường", "B": "Can và Đởm", "C": "Thận và Bàng quang", "D": "Phế và Đại trường"},
        "ans": "C"
    },
    {
        "q": "Khi bệnh nhân sống tính, hốt hoảng, mạch Thốn tay trái biến đổi bất thường, thầy thuốc nghĩ đến tạng nào?",
        "opts": {"A": "Phế", "B": "Tỳ", "C": "Tâm", "D": "Can"},
        "ans": "C"
    },
    {
        "q": "Vị trí Quan tay phải phản ánh tạng phủ nào theo YHCT?",
        "opts": {"A": "Can và Đởm", "B": "Tâm và Tiểu trường", "C": "Tỳ và Vị", "D": "Phế và Đại trường"},
        "ans": "C"
    },
    {
        "q": "Trước khi bắt mạch, cần cho người bệnh nghỉ ít nhất bao lâu để mạch ổn định?",
        "opts": {"A": "1 phút", "B": "5-10 phút", "C": "30 phút", "D": "Không cần nghỉ"},
        "ans": "B"
    },
    {
        "q": "Mạch có thể bị ảnh hưởng bởi yếu tố nào sau đây làm sai lệch kết quả bắt mạch?",
        "opts": {"A": "Chỉ uống nước ấm", "B": "Vừa ăn no, vận động mạnh, xúc cảm mạnh", "C": "Ngủ đủ giấc", "D": "Ngồi yên lặng yếu"},
        "ans": "B"
    },

    # =====================================================================
    # SECTION 2: 28 Mạch tượng - nhận biết (60 câu)
    # =====================================================================
    {
        "q": "Mạch Phù có đặc điểm nào?",
        "opts": {"A": "Ấn mạnh mới cảm nhận được", "B": "Cử nhẹ đã cảm nhận, ấn mạnh thì không rõ", "C": "Đi chậm và yếu", "D": "Nhịp không đều"},
        "ans": "B"
    },
    {
        "q": "Mạch Trầm có đặc điểm nào?",
        "opts": {"A": "Cử nhẹ đã cảm nhận được", "B": "Phải ấn mạnh sát xương mới cảm nhận rõ", "C": "Đi nhanh như nước chảy", "D": "Như dây đàn rung"},
        "ans": "B"
    },
    {
        "q": "Mạch Trì (chậm) có bao nhiêu nhịp/lần thở?",
        "opts": {"A": "Trên 5 nhịp/lần thở", "B": "Dưới 4 nhịp/lần thở", "C": "Đúng 4 nhịp/lần thở", "D": "Không đều, có lúc ngừng"},
        "ans": "B"
    },
    {
        "q": "Mạch Sác (nhanh) có bao nhiêu nhịp/lần thở?",
        "opts": {"A": "Dưới 3 nhịp/lần thở", "B": "4 nhịp/lần thở", "C": "Trên 5 nhịp/lần thở", "D": "Không xác định được"},
        "ans": "C"
    },
    {
        "q": "Mạch Hư có đặc điểm nào?",
        "opts": {"A": "To, nhanh, mạnh", "B": "Bất cứ mức áp lực nào cũng cảm thấy trống rỗng, không có lực", "C": "Nhỏ, chậm, mạnh", "D": "Cường và dài"},
        "ans": "B"
    },
    {
        "q": "Mạch Thực có đặc điểm nào?",
        "opts": {"A": "Nhỏ yếu, không có lực", "B": "To, mạnh, có lực ở cả 3 mức cử-án-ấn mạnh", "C": "Nhanh, trống rỗng", "D": "Rung như dây đàn"},
        "ans": "B"
    },
    {
        "q": "Mạch Hoạt có đặc điểm nào?",
        "opts": {"A": "Đi chậm, nén vào mới cảm thấy", "B": "Đi nhanh liên tiếp trơn tru như hạt châu lăn trên khay", "C": "Mạnh và dài như dây đàn", "D": "Nhỏ mà yếu"},
        "ans": "B"
    },
    {
        "q": "Mạch Sáp có đặc điểm nào?",
        "opts": {"A": "Trơn tru, nhanh", "B": "Khó khăn, không trơn tru, như dao cạo tre", "C": "Nhỏ, yếu, không lực", "D": "Dài, cường"},
        "ans": "B"
    },
    {
        "q": "Mạch Hồng có đặc điểm nào?",
        "opts": {"A": "Nhỏ, yếu, chậm", "B": "To, mạnh như sóng, đến cuối thì yếu đi", "C": "Ngừng lại rồi đi tiếp", "D": "Đi phát thì có nhịp ngừng"},
        "ans": "B"
    },
    {
        "q": "Mạch Tế có đặc điểm nào?",
        "opts": {"A": "To, mạnh, to", "B": "Nhỏ như chỉ, sắp mất nhưng vẫn có lực", "C": "Dài, cường như dây đàn", "D": "Nhanh, trống rỗng"},
        "ans": "B"
    },
    {
        "q": "Mạch Huyền có đặc điểm nào?",
        "opts": {"A": "Trơn tru như hạt châu", "B": "Dài, cường, căng như dây đàn huyền", "C": "Nhỏ, yếu, không lực", "D": "Ngừng rồi lại đi"},
        "ans": "B"
    },
    {
        "q": "Mạch Khẩn (Cấp) có đặc điểm nào?",
        "opts": {"A": "Như dây đàn huyền, dài cường", "B": "Như dây đàn cắt, to cường, căng hơn Mạch Huyền", "C": "Trơn tru như hạt châu", "D": "Nhỏ như chỉ"},
        "ans": "B"
    },
    {
        "q": "Mạch Hoãn có đặc điểm nào?",
        "opts": {"A": "Nhanh như nước chảy", "B": "Đi chậm, hòa nhã, như nước chảy chậm trong sông", "C": "Mạnh mạnh như Hồng mạch", "D": "Có nhịp ngừng không đều"},
        "ans": "B"
    },
    {
        "q": "Mạch Kết có đặc điểm nào?",
        "opts": {"A": "Nhanh và có nhịp ngừng đều đặn", "B": "Chậm và có nhịp ngừng không đều", "C": "Nhanh và đều đặn", "D": "Dài cường như dây đàn"},
        "ans": "B"
    },
    {
        "q": "Mạch Đại (khác Mạch Đại nghĩa là to) có đặc điểm nào?",
        "opts": {"A": "Chậm và có nhịp ngừng không đều", "B": "Có nhịp ngừng đều đặn sau một số nhịp nhất định", "C": "Nhanh và có nhịp ngừng đều", "D": "Mạnh, cường, không ngừng"},
        "ans": "B"
    },
    {
        "q": "Mạch Nhu (Nhuyễn) có đặc điểm nào?",
        "opts": {"A": "Căng như dây đàn", "B": "Mềm, yếu, như phao nước trên mặt nước, nổi nổi thì có mất thì không", "C": "Nhanh, to, mạnh", "D": "Ngừng lại rồi đi"},
        "ans": "B"
    },
    {
        "q": "Mạch Tán có đặc điểm nào?",
        "opts": {"A": "Trơn tru như hạt châu", "B": "Phù, to, vô lực, ấn vào mất đi", "C": "Dài cường như dây đàn", "D": "Nhỏ như chỉ"},
        "ans": "B"
    },
    {
        "q": "Mạch Phục (ấn sâu) có đặc điểm nào?",
        "opts": {"A": "Ấn nhẹ đã cảm thấy", "B": "Phải ấn rất mạnh, ép sát đến xương mới cảm nhận được", "C": "Nhỏ như chỉ, có lực", "D": "Dài cường như dây đàn"},
        "ans": "B"
    },
    {
        "q": "Mạch Cách có đặc điểm nào?",
        "opts": {"A": "Phù, to, cường như mặt trong của trống, ấn vào thì rỗng không", "B": "Trầm, to, mạnh ở cả 3 mức", "C": "Nhỏ, yếu, chậm", "D": "Trơn tru như hạt châu"},
        "ans": "A"
    },
    {
        "q": "Mạch Lao có đặc điểm nào?",
        "opts": {"A": "Phù, yếu, ấn vào không còn", "B": "Trầm, to, cường, dài, ấn mạnh vẫn còn rõ, như có gì cố định trong lòng mạch", "C": "Nhanh, nhỏ, yếu", "D": "Ngừng rồi lại đi"},
        "ans": "B"
    },
    {
        "q": "Mạch Động (Sắm) có đặc điểm nào?",
        "opts": {"A": "Dài, cường như dây đàn", "B": "Như hạt đậu tương nổi lên, có phát có cường, không đi về hai đầu, như động vật", "C": "Nhỏ như chỉ, yếu", "D": "Trơn tru, nhanh"},
        "ans": "B"
    },
    {
        "q": "Mạch Tức (Kíp) có đặc điểm nào?",
        "opts": {"A": "Đi nhanh như người chạy gấp", "B": "Đi rất nhanh hơn cả Mạch Sác, trên 7 nhịp/lần thở", "C": "Đi chậm như người mệt", "D": "Dài cường như dây đàn"},
        "ans": "B"
    },
    {
        "q": "Mạch Sán có đặc điểm nào?",
        "opts": {"A": "Nhỏ yếu, không có lực", "B": "To, nhanh, cường và có lực, mạnh hơn Mạch Hồng", "C": "Chậm, yếu, trơn tru", "D": "Dài, cường như dây đàn"},
        "ans": "B"
    },
    {
        "q": "Mạch Vi có đặc điểm nào?",
        "opts": {"A": "To, mạnh, cường", "B": "Rất nhỏ yếu, không có, khó cảm nhận, sắp mất", "C": "Nhanh, trơn tru", "D": "Dài, cường như dây đàn"},
        "ans": "B"
    },
    {
        "q": "Mạch Nhược có đặc điểm nào?",
        "opts": {"A": "Trơn tru, nhanh như hạt châu", "B": "Trầm, nhỏ, mềm, vô lực", "C": "Cường, dài như dây đàn", "D": "To, mạnh, nhanh"},
        "ans": "B"
    },
    {
        "q": "Mạch Tuyệt có đặc điểm nào?",
        "opts": {"A": "Đi rất nhanh không ngừng", "B": "Mất hẳn mạch, không cảm nhận được, là dấu hiệu bệnh nguy cấp", "C": "Nhỏ, yếu nhưng vẫn cảm nhận được", "D": "Dài cường như dây đàn"},
        "ans": "B"
    },
    {
        "q": "Phân biệt Mạch Hoạt và Mạch Sáp: Mạch Hoạt thì sao?",
        "opts": {"A": "Đi khó khăn, như dao cạo tre", "B": "Đi trơn tru, nhanh, như hạt châu lăn", "C": "Dài, cường, căng", "D": "Nhỏ, yếu, sắp mất"},
        "ans": "B"
    },
    {
        "q": "Phân biệt Mạch Huyền và Mạch Khẩn: Mạch Khẩn cường hơn Mạch Huyền như thế nào?",
        "opts": {"A": "Mạch Khẩn mềm hơn", "B": "Mạch Khẩn cường như dây đàn cắt, căn hơn; Mạch Huyền như dây đàn huyền mềm hơn", "C": "Mạch Khẩn nhanh hơn", "D": "Mạch Khẩn nhỏ hơn"},
        "ans": "B"
    },
    {
        "q": "Phân biệt Mạch Kết, Mạch Đại (có nhịp ngừng), Mạch Thực Gian: Mạch Kết có đặc điểm gì?",
        "opts": {"A": "Nhanh, có nhịp ngừng đều", "B": "Chậm, có nhịp ngừng bất thường (không đều)", "C": "Có nhịp ngừng đều sau số nhịp nhất định", "D": "Không có nhịp ngừng"},
        "ans": "B"
    },
    {
        "q": "Mạch Hồng phân biệt với Mạch Thực như thế nào?",
        "opts": {"A": "Mạch Hồng mềm hơn, cuối nhịp yếu đi; Mạch Thực mạnh đều cả nhịp", "B": "Mạch Hồng nhỏ hơn Mạch Thực", "C": "Mạch Hồng chậm hơn Mạch Thực", "D": "Mạch Hồng có nhịp ngừng, Mạch Thực không có"},
        "ans": "A"
    },
    {
        "q": "Mạch Tế và Mạch Nhược đều nhỏ yếu, điều gì phân biệt chúng?",
        "opts": {"A": "Mạch Tế ấn nhẹ đã thấy, Mạch Nhược phải ấn mạnh mới thấy", "B": "Mạch Tế trầm, nhỏ, còn lực; Mạch Nhược trầm, nhỏ, mềm, không lực", "C": "Mạch Tế nhanh hơn Mạch Nhược", "D": "Mạch Tế dài hơn Mạch Nhược"},
        "ans": "B"
    },
    {
        "q": "Mạch Phù và Mạch Tán đều là phù nổi, phân biệt như thế nào?",
        "opts": {"A": "Mạch Phù còn có lực, ấn vào vẫn cảm nhận; Mạch Tán cử nhẹ đã thấy, ấn vào thì mất", "B": "Mạch Phù không có lực, Mạch Tán có lực", "C": "Mạch Phù nhỏ hơn Mạch Tán", "D": "Mạch Phù chậm hơn Mạch Tán"},
        "ans": "A"
    },
    {
        "q": "Mạch Cách và Mạch Lao đều có dạng Phù-to-cường, phân biệt như thế nào?",
        "opts": {"A": "Mạch Cách phù, to, rỗng như mặt trong của trống; Mạch Lao trầm, cường, to, cố định trong lòng mạch", "B": "Mạch Cách trầm, Mạch Lao phù", "C": "Mạch Cách có nhịp ngừng, Mạch Lao không có", "D": "Mạch Cách nhỏ hơn, Mạch Lao to hơn"},
        "ans": "A"
    },
    {
        "q": "Mạch Trì có bao nhiêu nhịp trên một phút?",
        "opts": {"A": "Dưới 60 nhịp/phút", "B": "60-90 nhịp/phút", "C": "90-110 nhịp/phút", "D": "Trên 120 nhịp/phút"},
        "ans": "A"
    },
    {
        "q": "Mạch Sác có bao nhiêu nhịp trên một phút?",
        "opts": {"A": "Dưới 60", "B": "60-90", "C": "Trên 90", "D": "Không xác định"},
        "ans": "C"
    },
    {
        "q": "Mạch Hoãn khác Mạch Trì ở điểm nào?",
        "opts": {"A": "Mạch Hoãn nhanh hơn Mạch Trì", "B": "Mạch Hoãn hòa nhã, mềm mại hơn; Mạch Trì đơn thuần là chậm", "C": "Mạch Hoãn có nhịp ngừng, Mạch Trì không có", "D": "Mạch Hoãn nhỏ hơn, Mạch Trì to hơn"},
        "ans": "B"
    },
    {
        "q": "Mạch Đại (có nhịp ngừng đều) khác Mạch Kết ở điểm nào?",
        "opts": {"A": "Mạch Đại nhanh còn Mạch Kết chậm", "B": "Mạch Đại nhịp ngừng đều đặn và sau số nhịp cố định; Mạch Kết chậm và nhịp ngừng bất thường", "C": "Mạch Đại không có nhịp ngừng", "D": "Mạch Đại to hơn Mạch Kết"},
        "ans": "B"
    },
    {
        "q": "Mạch Nhu (Nhuyễn) thường gặp ở đối tượng nào nhất?",
        "opts": {"A": "Người có phong hàn", "B": "Người âm hóa thịnh, khí âm dồi dào, hoặc phụ nữ có thai bình thường", "C": "Người khí hư huyết kiệt", "D": "Người có bệnh nội tạng cấp"},
        "ans": "B"
    },
    {
        "q": "Mạch Vi là dạng mạch như thế nào?",
        "opts": {"A": "To và mạnh", "B": "Rất nhỏ, khó cảm nhận, gọi là 'khí của thở phào cuối cùng'", "C": "Nhanh và cường", "D": "Chậm và mềm"},
        "ans": "B"
    },
    {
        "q": "Mạch Động (Sắm) thường xuất hiện ở vị trí nào?",
        "opts": {"A": "Thốn", "B": "Quan", "C": "Xích", "D": "Cả 3 vị trí nhưng thường thấy rõ ở Quan"},
        "ans": "D"
    },
    {
        "q": "Mạch Phục (ấn sâu) khác Mạch Trầm ở điểm nào?",
        "opts": {"A": "Mạch Phục nông hơn Mạch Trầm", "B": "Mạch Phục phải ấn sát đến xương mới cảm thấy, sâu hơn Mạch Trầm", "C": "Mạch Phục nhanh hơn Mạch Trầm", "D": "Mạch Phục to hơn Mạch Trầm"},
        "ans": "B"
    },
    {
        "q": "Mạch Tức (Kíp) là mạch đi nhanh như thế nào so với Mạch Sác?",
        "opts": {"A": "Cùng tốc độ như Mạch Sác", "B": "Chậm hơn Mạch Sác", "C": "Nhanh hơn Mạch Sác, trên 7 nhịp/lần thở", "D": "Đi không đều"},
        "ans": "C"
    },
    {
        "q": "Mạch Sán thường gặp trong bệnh cảnh nào?",
        "opts": {"A": "Khí hư bệnh", "B": "Bệnh nhiệt cường thực, cao huyết áp", "C": "Bệnh hàn lạnh, khí hư", "D": "Âm hóa thiếu"},
        "ans": "B"
    },
    {
        "q": "Mạch Tuyệt báo hiệu điều gì?",
        "opts": {"A": "Bệnh nhẹ, sắp khỏi", "B": "Bệnh nguy, khí tuyệt, tiên lượng xấu", "C": "Khí hư bình thường", "D": "Phụ nữ có thai"},
        "ans": "B"
    },
    {
        "q": "Mạch Nhược và Mạch Hư đều biểu hiện khí hư, điều gì phân biệt?",
        "opts": {"A": "Mạch Nhược phù, Mạch Hư trầm", "B": "Mạch Hư to và vô lực ở cả ba mức; Mạch Nhược trầm, nhỏ, mềm, vô lực", "C": "Mạch Nhược nhanh hơn Mạch Hư", "D": "Mạch Nhược có nhịp ngừng, Mạch Hư không có"},
        "ans": "B"
    },
    {
        "q": "Mạch Lao thường xuất hiện ở trường hợp bệnh lý nào?",
        "opts": {"A": "Bệnh mới cấp tính", "B": "Khí cố hợp tạng nội tạng, khối u, khí tích lâu ngày", "C": "Khí hư cấp tính", "D": "Phong nhiệt ngoại cảm"},
        "ans": "B"
    },
    {
        "q": "Mạch Cách thường xuất hiện khi nào?",
        "opts": {"A": "Khi âm hóa thiên thủy", "B": "Mất huyết nhiều, tinh khí hai thiếu, phụ nữ băng huyết", "C": "Bệnh nhiệt cường", "D": "Đàm âm ứng tắc"},
        "ans": "B"
    },
    {
        "q": "Mạch Khẩn (Cấp) thường gặp trong bệnh cảnh nào?",
        "opts": {"A": "Khí âm thiếu, khí hư", "B": "Nhiệt bệnh cấp, can khí cường, Can dương vượng", "C": "Phong hàn biểu chứng", "D": "Tỳ vị khí hư"},
        "ans": "B"
    },
    {
        "q": "Mạch Tán (Dispersed) là dấu hiệu của tình trạng nào?",
        "opts": {"A": "Bệnh còn nhẹ, khí huyết bình thường", "B": "Nguyên khí suy bại, khí huyết tán, tinh lực cạn kiệt", "C": "Nhiệt bệnh cấp tính", "D": "Đàm âm ứng kết"},
        "ans": "B"
    },
    {
        "q": "Mạch Hoãn thường gặp ở dạng bệnh nào?",
        "opts": {"A": "Nhiệt bệnh, khí hư", "B": "Thấp chứng, Tỳ vị khí hư, phong nhiệt biểu", "C": "Can khí cường", "D": "Huyết tắc, Âm hóa thiếu"},
        "ans": "B"
    },
    {
        "q": "Mạch Sáp đặc trưng cho trạng thái bệnh lý nào?",
        "opts": {"A": "Khí trở lại, huyết ứ nhiều", "B": "Tinh khí không đủ, huyết ứ, khí trệ tắc, không trơn tru", "C": "Âm hóa thiếu nhiệt", "D": "Phong nhiệt ngoại cảm"},
        "ans": "B"
    },
    {
        "q": "Mạch Hồng thường gặp trong trường hợp nào?",
        "opts": {"A": "Hàn lạnh biểu chứng", "B": "Nhiệt cực mạnh, khí phần nóng bốc, mất tán thoát", "C": "Khí hư huyết kiệt", "D": "Đàm âm ứng tắc"},
        "ans": "B"
    },
    {
        "q": "Mạch Tế thường gặp trong trường hợp nào?",
        "opts": {"A": "Nhiệt bệnh cường thực", "B": "Khí hư, huyết hư, kinh sợ, đau đớn cực độ", "C": "Phong ngoại cảm", "D": "Can khí cường"},
        "ans": "B"
    },
    {
        "q": "Trường hợp nào sau đây là biểu hiện của Mạch Huyền?",
        "opts": {"A": "Mạch như dây đàn huyền, dài và cường", "B": "Mạch như hạt châu lăn", "C": "Mạch vô lực, ấn vào mất", "D": "Mạch nhỏ như chỉ"},
        "ans": "A"
    },
    {
        "q": "Mạch Thực biểu hiện hình thái như thế nào?",
        "opts": {"A": "Ấn nhẹ mất đi, có lực nhỏ", "B": "To, mạnh, có lực cả 3 mức cử-án-ấn mạnh", "C": "Nhanh, trống rỗng", "D": "Cường như dây đàn, dài"},
        "ans": "B"
    },
    {
        "q": "Mạch Hư biểu hiện hình thái như thế nào?",
        "opts": {"A": "Nhanh, cường, to", "B": "To, trống rỗng, bất cứ mức áp lực nào cũng thấy trống không, vô lực", "C": "Nhỏ như chỉ, trầm", "D": "Dài, cường như dây đàn"},
        "ans": "B"
    },
    {
        "q": "Mạch Phù và Mạch Trầm khác nhau ở điều gì cơ bản nhất?",
        "opts": {"A": "Mạch Phù nhanh, Mạch Trầm chậm", "B": "Mạch Phù nổi nổi, cử nhẹ đã thấy; Mạch Trầm sâu, phải ấn mạnh mới thấy", "C": "Mạch Phù to, Mạch Trầm nhỏ", "D": "Mạch Phù có lực, Mạch Trầm không có lực"},
        "ans": "B"
    },
    {
        "q": "Mạch Trì và Mạch Sác khác nhau ở điều gì?",
        "opts": {"A": "Mạch Trì to hơn Mạch Sác", "B": "Mạch Trì chậm (dưới 4 nhịp/thở), Mạch Sác nhanh (trên 5 nhịp/thở)", "C": "Mạch Trì có nhịp ngừng, Mạch Sác không", "D": "Mạch Trì cường hơn Mạch Sác"},
        "ans": "B"
    },
    {
        "q": "Mạch Phục rất sâu, khác Mạch Trầm ở điểm nào?",
        "opts": {"A": "Mạch Phục nông hơn Mạch Trầm", "B": "Mạch Phục phải ép tay sát xương mới cảm nhận; Mạch Trầm ấn vừa mạnh đã thấy", "C": "Mạch Phục to hơn Mạch Trầm", "D": "Mạch Phục nhanh hơn Mạch Trầm"},
        "ans": "B"
    },

    # =====================================================================
    # SECTION 3: Mạch chủ bệnh (40 câu)
    # =====================================================================
    {
        "q": "Mạch Phù chủ bệnh gì?",
        "opts": {"A": "Lý chứng", "B": "Biểu chứng", "C": "Hàn chứng", "D": "Nhiệt chứng"},
        "ans": "B"
    },
    {
        "q": "Mạch Trầm chủ bệnh gì?",
        "opts": {"A": "Biểu chứng", "B": "Lý chứng", "C": "Nhiệt chứng", "D": "Phong chứng"},
        "ans": "B"
    },
    {
        "q": "Mạch Trì chủ bệnh gì?",
        "opts": {"A": "Nhiệt chứng", "B": "Hàn chứng", "C": "Biểu chứng", "D": "Âm hóa thiếu"},
        "ans": "B"
    },
    {
        "q": "Mạch Sác chủ bệnh gì?",
        "opts": {"A": "Hàn chứng", "B": "Nhiệt chứng", "C": "Khí hư", "D": "Biểu chứng"},
        "ans": "B"
    },
    {
        "q": "Mạch Hư chủ bệnh gì?",
        "opts": {"A": "Thực chứng", "B": "Hư chứng (khí hư, huyết hư)", "C": "Biểu chứng cấp tính", "D": "Lý nhiệt cường"},
        "ans": "B"
    },
    {
        "q": "Mạch Thực chủ bệnh gì?",
        "opts": {"A": "Hư chứng", "B": "Thực chứng (tắc trệ, thực nhiệt)", "C": "Hàn biểu", "D": "Khí hư"},
        "ans": "B"
    },
    {
        "q": "Mạch Hoạt chủ bệnh gì?",
        "opts": {"A": "Khí hư, hàn chứng", "B": "Đàm ẩm, thực nhiệt, thực tích, phụ nữ có thai", "C": "Biểu chứng", "D": "Huyết hư, âm hóa thiếu"},
        "ans": "B"
    },
    {
        "q": "Mạch Sáp chủ bệnh gì?",
        "opts": {"A": "Nhiệt cường, đàm ẩm", "B": "Tinh khí hư, huyết ứ, khí trệ tắc", "C": "Biểu chứng phong hàn", "D": "Can khí cường"},
        "ans": "B"
    },
    {
        "q": "Mạch Hồng chủ bệnh gì?",
        "opts": {"A": "Hàn lạnh, khí hư", "B": "Nhiệt cường, mất tán thoát (khí phần cực nhiệt)", "C": "Biểu phong hàn", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Tế chủ bệnh gì?",
        "opts": {"A": "Thực nhiệt", "B": "Khí hư, huyết hư, kinh sợ", "C": "Biểu chứng", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Huyền chủ bệnh gì?",
        "opts": {"A": "Tỳ vị khí hư", "B": "Can bệnh, đau đớn, thủy ẩm (đàm ẩm)", "C": "Biểu chứng cấp", "D": "Huyết hư"},
        "ans": "B"
    },
    {
        "q": "Mạch Hoãn chủ bệnh gì?",
        "opts": {"A": "Nhiệt cường, Can bệnh", "B": "Thấp chứng, Tỳ vị khí hư, khí trệ thành thấp", "C": "Biểu chứng hàn", "D": "Huyết hư"},
        "ans": "B"
    },
    {
        "q": "Mạch Kết chủ bệnh gì?",
        "opts": {"A": "Nhiệt bệnh cấp", "B": "Âm hàn nội động, khí trệ, huyết tắc, đàm kết, khí cự", "C": "Khí hư", "D": "Biểu chứng"},
        "ans": "B"
    },
    {
        "q": "Mạch Đại (nhịp ngừng đều) chủ bệnh gì?",
        "opts": {"A": "Can khí cường", "B": "Tạng bệnh nguy kịch, khí hư, cũng gặp thoái hóa tạng khí", "C": "Biểu nhiệt", "D": "Đàm ẩm nhiệt kết"},
        "ans": "B"
    },
    {
        "q": "Mạch Khẩn chủ bệnh gì?",
        "opts": {"A": "Tỳ vị khí hư", "B": "Can khí cường, nhiệt cường cực, đau đớn, tắc chứng", "C": "Biểu chứng ngoại cảm", "D": "Huyết hư"},
        "ans": "B"
    },
    {
        "q": "Mạch Phù Trì (phù và chậm) chủ bệnh gì?",
        "opts": {"A": "Biểu nhiệt", "B": "Biểu hàn (phong hàn), ngoại cảm phong hàn", "C": "Lý nhiệt", "D": "Khí hư"},
        "ans": "B"
    },
    {
        "q": "Mạch Phù Sác (phù và nhanh) chủ bệnh gì?",
        "opts": {"A": "Biểu hàn", "B": "Biểu nhiệt (phong nhiệt cảm mạo)", "C": "Lý hàn", "D": "Khí hư"},
        "ans": "B"
    },
    {
        "q": "Mạch Trầm Trì (trầm và chậm) chủ bệnh gì?",
        "opts": {"A": "Biểu chứng", "B": "Lý hàn (hàn lạnh bên trong)", "C": "Nhiệt bệnh", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Trầm Sác (trầm và nhanh) chủ bệnh gì?",
        "opts": {"A": "Biểu hàn", "B": "Lý nhiệt (nhiệt tích bên trong)", "C": "Khí hư", "D": "Phong nhiệt ngoại cảm"},
        "ans": "B"
    },
    {
        "q": "Mạch Hoạt Sác (hoạt và nhanh) thường gặp trong trường hợp nào?",
        "opts": {"A": "Hàn bệnh ngoại cảm", "B": "Đàm nhiệt kết hợp, nhiệt cường đàm nhiều", "C": "Khí hư, huyết kiệt", "D": "Can khí cường"},
        "ans": "B"
    },
    {
        "q": "Mạch Huyền Tế (huyền và nhỏ) chủ bệnh gì?",
        "opts": {"A": "Nhiệt cường", "B": "Can khí hư, huyết hư, can thận âm hư", "C": "Biểu chứng", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Trầm Huyền (trầm và huyền) chủ bệnh gì?",
        "opts": {"A": "Biểu nhiệt", "B": "Can khí ứng trệ, can khí cường lý, đàm ẩm", "C": "Khí hư", "D": "Huyết hư"},
        "ans": "B"
    },
    {
        "q": "Mạch Phù Hoạt (phù và hoạt) thường gặp trong trường hợp nào?",
        "opts": {"A": "Lý hàn", "B": "Phong đàm (phong cường kết hợp đàm ẩm)", "C": "Khí hư", "D": "Can thận âm hư"},
        "ans": "B"
    },
    {
        "q": "Mạch Trầm Tế (trầm và nhỏ) chủ bệnh gì?",
        "opts": {"A": "Nhiệt bệnh ngoại cảm", "B": "Đau đớn lý, khí hư lý, phong thấp nhiệt khí hư", "C": "Biểu chứng", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Sác Hư (nhanh và rỗng trong) thường gặp trong trường hợp nào?",
        "opts": {"A": "Lý hàn", "B": "Nhiệt cường, âm hư, mất tán thoát khí mất nhiều", "C": "Khí hư", "D": "Biểu hàn"},
        "ans": "B"
    },
    {
        "q": "Mạch Hoạt Huyền (hoạt và huyền) thường gặp trong trường hợp nào?",
        "opts": {"A": "Khí hư, huyết hư", "B": "Can bệnh kết hợp đàm ẩm, Can khí cường + đàm ẩm", "C": "Biểu hàn", "D": "Nhiệt cường thuần túy"},
        "ans": "B"
    },
    {
        "q": "Mạch Nhu Hoạt (nhu và hoạt) thường gặp trong trường hợp nào?",
        "opts": {"A": "Nhiệt cường", "B": "Tỳ hư sinh thấp, đàm ẩm uẩn dựng", "C": "Can khí cường", "D": "Biểu hàn"},
        "ans": "B"
    },
    {
        "q": "Mạch Phù Hồng (phù và hồng) thường gặp trong trường hợp nào?",
        "opts": {"A": "Hàn biểu", "B": "Dương minh kinh bệnh, nhiệt cường khí phần", "C": "Khí hư", "D": "Can khí cường"},
        "ans": "B"
    },
    {
        "q": "Mạch Trầm Huyền Sác (trầm, huyền, nhanh) thường gặp trong trường hợp nào?",
        "opts": {"A": "Hàn biểu", "B": "Can đởm nhiệt cường, nhiệt bệnh bên trong với Can khí ứng", "C": "Khí hư", "D": "Biểu nhiệt"},
        "ans": "B"
    },
    {
        "q": "Mạch Hư Sác (hư và nhanh) thường gặp khi nào?",
        "opts": {"A": "Thực nhiệt cường", "B": "Âm hư sinh nhiệt nội, khí âm lưỡng thịnh", "C": "Biểu hàn", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Trì Tế (chậm và nhỏ) thường gặp trong trường hợp nào?",
        "opts": {"A": "Nhiệt cường", "B": "Dương khí hư, hàn đông khí hư, hàn đàm ngưng tắc mạch", "C": "Biểu nhiệt", "D": "Đàm nhiệt"},
        "ans": "B"
    },
    {
        "q": "Mạch Trầm Thực (trầm và mạnh) chủ bệnh gì?",
        "opts": {"A": "Biểu chứng", "B": "Lý thực nhiệt hoặc lý hàn thực (tích tụ bên trong)", "C": "Khí hư", "D": "Phong nhiệt"},
        "ans": "B"
    },
    {
        "q": "Mạch Phù Nhược (phù và nhược) thường gặp khi nào?",
        "opts": {"A": "Nhiệt cường", "B": "Khí hư biểu, Phế khí hư (khí hư ở phù phần)", "C": "Biểu hàn", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Hoạt Thực (hoạt và mạnh) thường gặp khi nào?",
        "opts": {"A": "Khí hư", "B": "Thực nhiệt tích tụ (lý nhiệt cường thực, táo bón, bụng đau)", "C": "Hàn biểu", "D": "Âm hóa thiếu"},
        "ans": "B"
    },
    {
        "q": "Mạch Khẩn Sác (khẩn và nhanh) thường gặp khi nào?",
        "opts": {"A": "Khí hư", "B": "Nhiệt cường cực, can âm cực kỳ hư, can dương cường vượng", "C": "Biểu hàn", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Tế Sác (nhỏ và nhanh) thường gặp khi nào?",
        "opts": {"A": "Nhiệt cường thực", "B": "Âm hóa thiếu, hư lao nhiệt, âm hư sinh nhiệt", "C": "Biểu hàn", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Phù Sác Vô Lực thường gặp khi nào?",
        "opts": {"A": "Nhiệt cường", "B": "Khí âm lưỡng thịnh (âm hư sinh nhiệt nội)", "C": "Biểu hàn", "D": "Đàm nhiệt"},
        "ans": "B"
    },
    {
        "q": "Mạch Huyền Sác (huyền và nhanh) thường gặp khi nào?",
        "opts": {"A": "Khí hư hàn lạnh", "B": "Can khí cường hóa (hóa nhiệt từ can khí ứng), can âm hư", "C": "Biểu hàn", "D": "Tỳ hư đàm"},
        "ans": "B"
    },
    {
        "q": "Mạch Tức (Kíp) thường gặp khi nào?",
        "opts": {"A": "Hàn lạnh bên trong", "B": "Nhiệt cực độc cường, tinh thiên khí nội, tâm hỏa bốc mạnh", "C": "Khí hư cấp", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Sán thường gặp khi nào?",
        "opts": {"A": "Hàn biểu", "B": "Cao huyết áp, nhiệt cường, can khí cường vượng, tâm hỏa mạnh", "C": "Khí hư", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Nhu (Nhuyễn) Trì (nhu và chậm) thường gặp khi nào?",
        "opts": {"A": "Nhiệt cường thực", "B": "Khí hư kinh lạc, dương hư hàn trệ, có thể gặp ở người già yếu", "C": "Biểu nhiệt", "D": "Đàm ẩm nhiệt"},
        "ans": "B"
    },

    # =====================================================================
    # SECTION 4: Tứ chẩn kết hợp mạch (20 câu)
    # =====================================================================
    {
        "q": "Tứ chẩn YHCT gồm những phương pháp nào?",
        "opts": {"A": "Vọng, Văn, Vấn, Thiết (Nhìn-Nghe-Hỏi-Cảm)", "B": "Nội soi, X-quang, siêu âm, xét nghiệm", "C": "Chỉ vọng, hỏi hàn, bắt mạch, bấm huyệt", "D": "Khám bệnh, kê đơn, bắt mạch, thủ thuật"},
        "ans": "A"
    },
    {
        "q": "Khi vọng (nhìn) thấy sắc mặt xanh nhạt kết hợp mạch Huyền Tế, nghi đến bệnh gì?",
        "opts": {"A": "Tâm hỏa cường", "B": "Can khí hư, huyết hư, can thận âm hư", "C": "Tỳ vị nhiệt", "D": "Phế khí hư"},
        "ans": "B"
    },
    {
        "q": "Khi vọng (nhìn) thấy sắc mặt đỏ, mắt đỏ, kết hợp mạch Sác Hồng, nghi đến bệnh gì?",
        "opts": {"A": "Hàn lạnh bệnh", "B": "Nhiệt cường, Tâm hỏa thượng bốc, khí phần nhiệt cường", "C": "Khí hư", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Khi văn (nghe-ngửi) giọng nói yếu, thở ngắn kết hợp mạch Hư Nhược, nghi đến bệnh gì?",
        "opts": {"A": "Nhiệt cường thực", "B": "Phế khí hư, Tâm khí hư, tông khí bao hư", "C": "Đàm ẩm ứng tắc", "D": "Can khí cường"},
        "ans": "B"
    },
    {
        "q": "Khi văn (nghe-ngửi) ngửi thấy hơi thở hôi thối kết hợp mạch Sác Hoạt Thực, nghi đến bệnh gì?",
        "opts": {"A": "Tỳ hư", "B": "Vị nhiệt tích, thực nhiệt táo kiết ở Dương minh", "C": "Biểu hàn", "D": "Khí hư"},
        "ans": "B"
    },
    {
        "q": "Khi vấn (hỏi bệnh) bệnh nhân cho biết đau sườn kết hợp mạch Huyền, nghi đến bệnh gì?",
        "opts": {"A": "Tỳ vị nhiệt", "B": "Can đởm khí ứng, can khí cường", "C": "Phế khí hư", "D": "Thận âm hư"},
        "ans": "B"
    },
    {
        "q": "Khi vấn (hỏi) bệnh nhân cho biết đau đầu đỉnh đầu kết hợp mạch Khẩn Huyền, nghi đến bệnh gì?",
        "opts": {"A": "Khí hư", "B": "Can dương thiếu thịnh, phong đăng lên đỉnh đầu", "C": "Tâm hỏa", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Khi thiết (bắt mạch) thấy mạch Hoạt, bệnh nhân nữ không có kinh nguyệt, nghi đến gì đầu tiên?",
        "opts": {"A": "Can khí ứng trệ", "B": "Có thai", "C": "Khí hư kinh bội", "D": "Đàm ẩm kết"},
        "ans": "B"
    },
    {
        "q": "Khi thiết (bắt mạch, toàn thân) sắc mặt vàng, bên trong lòng bàn tay vàng, kết hợp mạch Hoãn Nhược, nghi đến bệnh gì?",
        "opts": {"A": "Nhiệt cường", "B": "Thấp nhiệt hoàng đản, Tỳ hư thấp nhiệt", "C": "Can khí cường", "D": "Tâm hỏa"},
        "ans": "B"
    },
    {
        "q": "Kết hợp vọng thấy mặt phù, nghe thở khó, hỏi thấy có đàm, bắt mạch Hoạt Nhược, nghi đến gì?",
        "opts": {"A": "Can khí cường", "B": "Phế khí hư + đàm ẩm, đàm ẩm ứng Phế", "C": "Nhiệt cường Tâm", "D": "Thận khí hư"},
        "ans": "B"
    },
    {
        "q": "Khi kết hợp tứ chẩn, mạch thường qua mô tả tính chất gì?",
        "opts": {"A": "Chỉ là tăng tốc/giảm tốc mạch đập", "B": "Vị trí, tốc độ, cường độ, hình thái, tính chất của mạch, phản ánh trạng thái khí huyết và tạng phủ", "C": "Chỉ là đo học áp mạch", "D": "Chỉ phản ánh nhiệt độ cơ thể"},
        "ans": "B"
    },
    {
        "q": "Khi bệnh nhân khai đau đông vào mùa lạnh, thèm ấm, sợ lạnh, kết hợp mạch Trì Huyền, nghi bệnh gì?",
        "opts": {"A": "Nhiệt bệnh Can", "B": "Hàn tắc (phong hàn thấp tý), can khí ứng hàn", "C": "Âm hóa thiếu", "D": "Khí hư"},
        "ans": "B"
    },
    {
        "q": "Phương pháp 'toàn thư hội chẩn' trong YHCT là gì?",
        "opts": {"A": "Chỉ bắt mạch đơn thuần", "B": "Kết hợp cả bốn phương pháp vọng-văn-vấn-thiết để cho ra chẩn đoán toàn diện", "C": "Chỉ hỏi bệnh nhân", "D": "Chỉ nhìn sắc mặt"},
        "ans": "B"
    },
    {
        "q": "Trong trường hợp mạch Kết xuất hiện, kết hợp vọng thấy môi tím, miệng tím, nghi đến bệnh gì?",
        "opts": {"A": "Nhiệt cường", "B": "Huyết tắc, khí trệ, tắc chứng (Tâm khí ứng huyết, tắc chứng khí hư)", "C": "Khí hư", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Kết hợp tứ chẩn với mạch Tam xuất hiện (trầm, nhỏ, vô lực), sắc mặt trắng nhạt, sợ lạnh thì nghi gì?",
        "opts": {"A": "Nhiệt cường", "B": "Dương khí đại hư, hàn đông bên trong, tinh thoát dương hư", "C": "Biểu nhiệt", "D": "Can khí cường"},
        "ans": "B"
    },
    {
        "q": "Khi khám bệnh nhi (trẻ em), có nên đưa ra kết luận chỉ trên bắt mạch không?",
        "opts": {"A": "Có, bắt mạch là đủ", "B": "Không, cần kết hợp vọng-văn-vấn-thiết vì trẻ em khó hợp tác hỏi bệnh chính xác", "C": "Chỉ cần hỏi mẹ", "D": "Chỉ cần nhìn màu da"},
        "ans": "B"
    },
    {
        "q": "Vọng (nhìn) lưỡi đỏ, gai lưỡi, kết hợp mạch Sác Hồng, biểu hiện gì?",
        "opts": {"A": "Hàn lạnh", "B": "Nhiệt cường, tâm nhiệt, khí phần nhiệt cường", "C": "Khí hư", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Khi bắt mạch thấy mạch Phù Trì, hỏi bệnh nhân thấy sợ lạnh, sống lưng cốt cứng, nghi đến bệnh gì?",
        "opts": {"A": "Biểu nhiệt", "B": "Biểu hàn (ngoại cảm phong hàn), Thái dương kinh chứng", "C": "Khí hư", "D": "Lý nhiệt"},
        "ans": "B"
    },
    {
        "q": "Khi thiết (bắt mạch) thấy mạch Hoạt Sác, hỏi bệnh nhân thấy bứt ngực, đàm nhiều màu vàng, nghi đến gì?",
        "opts": {"A": "Khí hư Phế", "B": "Đàm nhiệt ứng Phế, Phế nhiệt khắc đàm", "C": "Hàn lạnh biểu", "D": "Can khí cường"},
        "ans": "B"
    },
    {
        "q": "Vọng thấy mặt phù nhân, chân phù, hỏi có tiểu ít, bắt mạch Trầm Huyền Nhược, nghi đến gì?",
        "opts": {"A": "Nhiệt cường", "B": "Thận dương hư không khơi cơ, nước âm tràn lan (thủy ẩm/phù thũng)", "C": "Biểu hàn", "D": "Đàm ẩm"},
        "ans": "B"
    },

    # =====================================================================
    # SECTION 5: Mạch phụ nữ có thai, trẻ em (20 câu)
    # =====================================================================
    {
        "q": "Mạch Hoạt Sác xuất hiện ở phụ nữ trong độ tuổi sinh sản, không thấy kinh nguyệt, nghi đến gì đầu tiên?",
        "opts": {"A": "Đàm ẩm kết", "B": "Có thai", "C": "Kinh bội do khí hư", "D": "Nhiệt bệnh"},
        "ans": "B"
    },
    {
        "q": "Mạch Thiếu Thận (mạch xích tay phải, biến động bất thường) ở phụ nữ, theo YHCT có thể báo hiệu điều gì?",
        "opts": {"A": "Nhiệt bệnh", "B": "Có thai (có một số trường phái dùng vị trí Xích phải để báo hiệu thai)", "C": "Khí hư", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Hoa (Nhuyễn, mềm, trơn) ở phụ nữ có thai là biểu hiệu gì?",
        "opts": {"A": "Bệnh lý nghiêm trọng", "B": "Bình thường, khí huyết âm no, nuôi dưỡng thai tốt", "C": "Mất huyết", "D": "Nhiệt cường"},
        "ans": "B"
    },
    {
        "q": "Phụ nữ có thai gặp mạch Sáp, nghi đến điều gì?",
        "opts": {"A": "Thai khỏe mạnh", "B": "Khí hư huyết ứ, có thể gây dọa xảy thai", "C": "Nhiệt cường", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Mạch Ly Kiên (mạch Xích tay trái cường rõ) theo một số sách YHCT báo hiệu gì?",
        "opts": {"A": "Bệnh nặng", "B": "Có thai hoặc thai nghén, tăng cường sinh lực sinh sản", "C": "Khí hư", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Trẻ em dưới 3 tuổi thường không đặt mạch Thốn-Quan-Xích mà dùng phương pháp nào?",
        "opts": {"A": "Bắt mạch 3 vị trí như người lớn", "B": "Dùng 'Nhất chỉ định mạch' (một ngón tay cảm nhận toàn bộ)", "C": "Không bắt mạch cho trẻ em", "D": "Chỉ bắt mạch Quan"},
        "ans": "B"
    },
    {
        "q": "Mạch bình thường của trẻ sơ sinh nhanh hơn người lớn, thường ở mức nào?",
        "opts": {"A": "60-70 nhịp/phút", "B": "120-140 nhịp/phút", "C": "90-100 nhịp/phút", "D": "50-60 nhịp/phút"},
        "ans": "B"
    },
    {
        "q": "Trẻ em mạch Sác thường biểu hiện gì?",
        "opts": {"A": "Bệnh lý hàn lạnh", "B": "Nhiệt chứng (sốt, viêm nhiễm), hoặc bình thường nếu tần số trong giới hạn tuổi", "C": "Khí hư", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Trẻ em mạch Phù Sác, có sốt, sợ gió, hỏi thấy sợ lạnh, nghi đến gì?",
        "opts": {"A": "Lý nhiệt", "B": "Biểu nhiệt (ngoại cảm phong nhiệt, cảm mạo sốt)", "C": "Khí hư", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Trẻ em mạch Hoạt Sác, có đàm nhiều, nghi đến gì?",
        "opts": {"A": "Khí hư", "B": "Đàm nhiệt ứng Phế hoặc vị nhiệt đàm nhiều", "C": "Hàn lạnh", "D": "Can khí cường"},
        "ans": "B"
    },
    {
        "q": "Trẻ em mạch Tế Nhược, sờ tay lạnh chân, mặt trắng nhạt, nghi đến gì?",
        "opts": {"A": "Nhiệt cường", "B": "Dương khí hư, hàn lạnh bên trong, khí hư nghiêm trọng", "C": "Biểu nhiệt", "D": "Đàm nhiệt"},
        "ans": "B"
    },
    {
        "q": "Phụ nữ có thai gần sinh (tháng cuối), mạch Hoạt Sác Mạnh, báo hiệu điều gì?",
        "opts": {"A": "Thai bệnh lý", "B": "Thai khỏe, chuẩn bị phát động (chuẩn bị vượt cạn)", "C": "Khí hư", "D": "Mất huyết nhiều"},
        "ans": "B"
    },
    {
        "q": "Phụ nữ sau sinh (hậu sản) mạch Sáp, nghi đến gì?",
        "opts": {"A": "Nhiệt cường", "B": "Khí hư huyết ứ sau sinh, huyết kiệt khí hư", "C": "Biểu nhiệt", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Phụ nữ có thai mạch Trì Nhược, nghi đến gì?",
        "opts": {"A": "Nhiệt cường thai khí", "B": "Thai khí hư, nguyên khí suy, có thể gây dọa xảy thai hoặc sinh thiếu tháng", "C": "Biểu hàn", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Trẻ em mạch Huyền Sác, hay giật mình, mặt đỏ, nghi đến gì?",
        "opts": {"A": "Khí hư", "B": "Nhiệt động phong, can phong nội động (Cam Phong, Kinh Giác)", "C": "Hàn lạnh", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Phụ nữ trước kỳ nguyệt (kinh nguyệt sắp đến) mạch Hoạt, là bình thường hay bệnh lý?",
        "opts": {"A": "Bệnh lý, cần điều trị", "B": "Bình thường, khí huyết sung mãn chuẩn bị hành kinh", "C": "Dấu hiệu viêm nhiễm", "D": "Dấu hiệu có thai"},
        "ans": "B"
    },
    {
        "q": "Trẻ sơ sinh (tuần đầu) mạch quá chậm (Trì), nghi đến gì?",
        "opts": {"A": "Bình thường", "B": "Hàn lạnh hoặc suy yếu tiên thiên, tim mạch bất thường", "C": "Nhiệt cường", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Phụ nữ có thai mạch Huyền Sác, nghi đến gì?",
        "opts": {"A": "Thai bình thường", "B": "Can khí cường + nhiệt, có thể gây nguyên khí hư hoặc dọa xảy thai niệu bản", "C": "Khí hư", "D": "Đàm ẩm"},
        "ans": "B"
    },
    {
        "q": "Trẻ em mạch Trầm Hoạt, bụng chướng, nghi đến gì?",
        "opts": {"A": "Biểu nhiệt", "B": "Thực tích (tiêu hóa kém, thức ăn tích tụ), Tỳ vị thấp trệ", "C": "Khí hư", "D": "Can khí cường"},
        "ans": "B"
    },
    {
        "q": "Phụ nữ mang thai mạch Vi (khó cảm nhận, rất nhỏ yếu), tiên lượng như thế nào?",
        "opts": {"A": "Bình thường", "B": "Nguyên khí suy bại, có thể gây sối thai, thai chết lưu, tình trạng nguy hiểm", "C": "Thai khỏe mạnh", "D": "Chuẩn bị sinh"},
        "ans": "B"
    },
]

# Verify question count
assert len(Q1) == 160, f"Expected 160 questions, got {len(Q1)}"

if __name__ == "__main__":
    print(f"Total questions in Q1: {len(Q1)}")
    print("All 160 questions loaded successfully.")
