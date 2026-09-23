# Phật giáo phổ thông — Taxonomy & danh mục bài viết (vi-VN)

**Phiên bản:** 1.0 · **Cập nhật:** 2026-09-19 · **Trạng thái:** khung nội dung cho phần "Phật giáo phổ thông" trong app

> **Mục đích:** Mỗi mã `GBxxx` tương ứng với **một bài viết độc lập**. Cùng một mã có thể xuất hiện ở nhiều nhánh taxonomy; khi đó app chỉ lưu bài một lần và gắn nhiều category/tag.
>
> **Nguyên tắc 1 — Lộ trình, không xếp hạng.** "Cơ bản → nâng cao" là **lộ trình học kiến thức**, không phải bảng xếp hạng giữa các truyền thống. Theravāda, Mahāyāna và Vajrayāna cùng xuất phát từ Đức Phật Thích-ca; "Theravāda là gốc, Mahāyāna là nhánh" hay "Kim cương thừa là cao hơn" đều là cách nói không dùng trong app.
>
> **Nguyên tắc 2 — Mã là vĩnh viễn.** Mã `GBxxx` là **ID ổn định**, không đánh số lại khi thêm/bớt bài. Thứ tự mã trong cây **không** quyết định thứ tự học; thứ tự học nằm ở phần *Lộ trình*. Mã đã gỡ bỏ thì **nghỉ hưu**, không tái sử dụng.
>
> **Nguyên tắc 3 — Cùng bài thì cùng mã.** Nếu hai mục thực sự là cùng một bài, dùng cùng mã và cùng tiêu đề. Nếu chỉ cùng tên nhưng phạm vi truyền thống khác nhau, tạo mã riêng và ghi rõ trong tiêu đề hoặc metadata.
>
> **Nguyên tắc 4 — Thuật ngữ.** Ưu tiên **Pāli** cho nội dung Theravāda/kinh tạng Pāli, **Sanskrit** cho nội dung Mahāyāna/Vajrayāna, luôn kèm **Hán–Việt** khi người Việt quen dùng dạng đó; với tên riêng Đông Á và Tây Tạng ghi kèm nguyên văn (ví dụ: niệm Phật — *niànfó*; năm mới Tây Tạng — *Losar*). Xem bảng đối chiếu ở cuối file.
>
> **Nguyên tắc 5 — Quan hệ với phân mục Thiền.** Phân mục này trình bày **kiến thức phổ thông** (lịch sử, giáo lý, văn hóa, lễ hội). Nội dung **thực hành Thiền chi tiết** thuộc phân mục Thiền với mã `Mxxx`; các bài ở đây luôn dẫn link sang mã M tương ứng thay vì nhân bản nội dung.

## Quy ước cấp độ (level)

| Mã | Tên | Ý nghĩa |
|----|-----|---------|
| **L1** | Nhập môn | Người chưa biết gì về Phật giáo đọc hiểu ngay |
| **L2** | Nền tảng | Khái niệm cốt lõi cần nắm để đọc tiếp các bài khác |
| **L3** | Trung cấp | Cần đã quen khái niệm nền; lịch sử chi tiết, tư tưởng tông phái |
| **L4** | Chuyên sâu | Văn bản học, tư tưởng triết học phức tạp — cho người muốn đào sâu |
| **L5** | Cần điều kiện | Kiến thức gắn thực hành đòi truyền thừa/quán đảnh — *phân mục này hiện không dùng; xem phân mục Thiền* |
| **R** | Tra cứu | Bảng, danh mục, FAQ, lịch — không nằm trong lộ trình tuyến tính |

---

# QUY ƯỚC BẢN CHẤT TAXONOMY

Các nhánh cấp cao được phân theo **bản chất thông tin**, thay vì coi tất cả là các "loại Phật giáo" ngang hàng:

| Nhóm | Bản chất | Chức năng trong app |
|---|---|---|
| **A** | `foundation` — nhập môn & định hướng | Trả lời "Phật giáo là gì", giúp người mới bắt đầu đúng cách |
| **B** | `history` — lịch sử | Cuộc đời Đức Phật, kết tập kinh điển, phân nhánh bộ phái, hình thành ba truyền thống, lan truyền ra thế giới và vào Việt Nam |
| **C** | `core_doctrine` — lý thuyết nền tảng chung | Giáo lý cả ba truyền thống **cùng thừa nhận** (tứ diệu đế, bát chánh đạo, duyên khởi, nghiệp, ngũ uẩn, Niết-bàn…) |
| **D / E / F** | `tradition` — ba truyền thống lớn | Mỗi truyền thống là một nhánh hoàn chỉnh: tổng quan → kinh điển → đường tu → các nước → **lễ hội riêng của truyền thống đó** |
| **G** | `comparison` — so sánh & định hướng | Đối chiếu ba truyền thống và thái độ học đa truyền thống lành mạnh |
| **H** | `reference_tool` — tra cứu & công cụ | Thuật ngữ, kinh điển, tông phái, lịch lễ hội, FAQ |

**Lưu ý:** Cùng một bài có thể có nhiều thuộc tính. `traditions`, `categories`, `calendar` (hệ lịch của lễ hội) và `sources` là các chiều dữ liệu riêng, không phải cấp con của taxonomy. Bài về Việt Nam viết một lần ở B7 và gắn thêm category khi cần xuất hiện ở E5.

# TAXONOMY TREE

> **Cấu trúc v1.0:** Trục chính là hành trình học của người mới: **định hướng → lịch sử → giáo lý nền chung → từng truyền thống (kèm lễ hội) → so sánh → tra cứu**. Nhóm C chỉ chứa giáo lý chung cho cả ba truyền thống; điểm khác biệt của từng truyền thống nằm trong D/E/F và được tổng hợp ở G.

```text
Phật giáo phổ thông
│
├── G.A. NHẬP MÔN & ĐỊNH HƯỚNG
│   ├── G.A1. Hiểu về Phật giáo
│   │   ├── [GB001] Phật giáo là gì? · L1
│   │   ├── [GB002] Tam bảo — Phật, Pháp, Tăng · L1
│   │   ├── [GB003] Đạo Phật và các tôn giáo thờ đấng sáng thế · L1
│   │   ├── [GB004] Những hiểu lầm phổ biến về đạo Phật · L1
│   │   └── [GB005] Đọc thuật ngữ Phật giáo: Pāli, Sanskrit và Hán–Việt · L1
│   ├── G.A2. Bắt đầu học như thế nào
│   │   ├── [GB006] Người mới học Phật bắt đầu từ đâu · L1
│   │   ├── [GB007] Cách đọc kinh và tài liệu Phật giáo · L1
│   │   └── [GB008] Quy y, tại gia và xuất gia — các mức cam kết · L1
│   ├── G.A3. Người Phật tử tại gia
│   │   ├── [GB009] Tam quy — quy y Phật, Pháp, Tăng · L1
│   │   ├── [GB010] Ngũ giới — năm điều rèn luyện cho người tại gia · L1
│   │   ├── [GB011] Đời sống Phật tử tại gia · L1
│   │   └── [GB012] Tín và tuệ trong đạo Phật · L2
│   └── G.A4. Định hướng đa truyền thống
│       └── [GB013] Học Phật nên bắt đầu từ truyền thống nào? · L1
│
├── G.B. LỊCH SỬ PHẬT GIÁO
│   ├── G.B1. Bối cảnh
│   │   └── [GB014] Ấn Độ thời Đức Phật — bối cảnh xã hội và tôn giáo · L2
│   ├── G.B2. Cuộc đời Đức Phật
│   │   ├── [GB015] Cuộc đời Đức Phật — tổng quan và dòng thời gian · L1
│   │   ├── [GB016] Thái tử Tất-đạt-đa và bốn cảnh tượng · L1
│   │   ├── [GB017] Xuất gia và sáu năm tầm đạo · L2
│   │   ├── [GB018] Thành đạo dưới cội Bồ-đề · L2
│   │   ├── [GB019] Chuyển pháp luân — bài thuyết pháp đầu tiên · L2
│   │   ├── [GB020] 45 năm hoằng hóa và Tăng đoàn đầu tiên · L2
│   │   ├── [GB021] Nhập diệt tại Câu-thi-na · L2
│   │   └── [GB022] Sử liệu và truyền thuyết về Đức Phật · L3
│   ├── G.B3. Giữ gìn giáo pháp
│   │   └── [GB023] Kết tập kinh điển — giữ gìn giáo pháp sau Đức Phật · L3
│   ├── G.B4. Phân nhánh — các bộ phái sơ kỳ
│   │   ├── [GB024] Sự phân liệt đầu tiên — Thượng tọa bộ và Đại chúng bộ · L3
│   │   ├── [GB025] Bản đồ các bộ phái sơ kỳ · L3
│   │   └── [GB026] A-dục vương — Phật giáo vượt ra khỏi Ấn Độ · L2
│   ├── G.B5. Ba truyền thống lớn hình thành
│   │   ├── [GB027] Ba truyền thống lớn — bản đồ toàn cảnh · L2
│   │   ├── [GB028] Sự trỗi dậy của Đại thừa · L3
│   │   ├── [GB029] Sự hình thành Mật giáo và Kim cương thừa · L3
│   │   └── [GB030] Phật giáo Ấn Độ — một nghìn năm thịnh suy · L3
│   ├── G.B6. Phật giáo lan truyền
│   │   ├── [GB031] Phật giáo Nam truyền — Sri Lanka và Đông Nam Á · L2
│   │   ├── [GB032] Phật giáo Đại Thừa — Con đường tơ lụa và Đông Á · L2
│   │   ├── [GB033] Phật giáo Kim Cương Thừa — Himalaya và Mông Cổ · L2
│   │   └── [GB034] Phật giáo hiện đại — hành trình ra thế giới · L3
│   └── G.B7. Phật giáo Việt Nam
│       ├── [GB035] Phật giáo vào Việt Nam — từ những thế kỷ đầu Công nguyên · L2
│       ├── [GB036] Phật giáo Việt Nam thời Lý–Trần · L3
│       ├── [GB037] Phật giáo Việt Nam cận — hiện đại · L2
│       └── [GB038] Bản đồ Phật giáo Việt Nam hôm nay · L2
│
├── G.C. LÝ THUYẾT NỀN TẢNG CHUNG (đúng cho mọi truyền thống)
│   ├── G.C1. Tứ diệu đế
│   │   ├── [GB039] Tứ diệu đế — tổng quan · L1
│   │   ├── [GB040] Khổ đế · L2
│   │   ├── [GB041] Tập đế · L2
│   │   ├── [GB042] Diệt đế · L2
│   │   └── [GB043] Đạo đế · L2
│   ├── G.C2. Bát chánh đạo
│   │   ├── [GB044] Bát chánh đạo — tổng quan và ba nhóm · L1
│   │   ├── [GB045] Nhóm Giới: chánh ngữ, chánh nghiệp, chánh mạng · L2
│   │   ├── [GB046] Nhóm Định: chánh tinh tấn, chánh niệm, chánh định · L2
│   │   └── [GB047] Nhóm Tuệ: chánh kiến, chánh tư duy · L2
│   ├── G.C3. Duyên khởi
│   │   ├── [GB048] Duyên khởi — tổng quan · L2
│   │   └── [GB049] Mười hai chi duyên khởi · L3
│   ├── G.C4. Nghiệp, luân hồi và các cõi
│   │   ├── [GB050] Nghiệp — hiểu đúng và hiểu sai · L1
│   │   ├── [GB051] Luân hồi và tái sinh · L2
│   │   ├── [GB052] Sáu cõi và vũ trụ quan Phật giáo · L2
│   │   └── [GB053] Công đức, phước điền và hồi hướng · L2
│   ├── G.C5. Ngũ uẩn và vô ngã
│   │   ├── [GB054] Ngũ uẩn — "tôi" được cấu thành từ những gì · L2
│   │   ├── [GB055] Vô ngã — hiểu đúng một khái niệm dễ hiểu sai · L2
│   │   └── [GB056] Ba đặc tính và các pháp ấn · L2
│   ├── G.C6. Tam học và hạnh sống
│   │   ├── [GB057] Tam học — Giới, Định, Tuệ · L2
│   │   └── [GB058] Từ, bi, hỷ, xả trong đời sống · L1
│   └── G.C7. Mục tiêu giải thoát
│       ├── [GB059] Niết-bàn là gì · L2
│       ├── [GB060] Bốn bậc thánh và tiến trình giải thoát · L3
│       └── [GB061] Các Đức Phật — quá khứ, hiện tại và vị lai · L2
│
├── G.D. TRUYỀN THỐNG THERAVĀDA
│   ├── G.D1. Tổng quan
│   │   ├── [GB062] Thượng tọa bộ (Theravāda) — tổng quan · L1
│   │   └── [GB063] Lịch sử Theravāda · L3
│   ├── G.D2. Kinh điển
│   │   ├── [GB064] Tam tạng Pāli — bản đồ kinh điển · L2
│   │   ├── [GB065] A-tỳ-đàm (Abhidhamma) là gì · L3
│   │   └── [GB066] Hệ chú giải và Thanh tịnh đạo · L3
│   ├── G.D3. Đường tu và đời sống
│   │   ├── [GB067] Con đường tu trong Theravāda · L2
│   │   ├── [GB068] Thiền trong Theravāda — nhập môn · L2
│   │   ├── [GB069] Đời sống tăng đoàn Theravāda · L2
│   │   └── [GB070] Đời sống Phật tử tại gia Theravāda · L2
│   ├── G.D4. Theravāda ở các nước
│   │   ├── [GB071] Theravāda Sri Lanka · L2
│   │   ├── [GB072] Theravāda Thái Lan · L2
│   │   ├── [GB073] Theravāda Miến Điện · L2
│   │   ├── [GB074] Theravāda Lào và Campuchia · L2
│   │   └── [GB075] Theravāda tại Việt Nam · L2
│   └── G.D5. Lễ hội Phật giáo Nam truyền - Theravāda
│       └── [GB076] Lễ hội Phật giáo Nam truyền - Theravāda · L1
│
├── G.E. TRUYỀN THỐNG MAHĀYĀNA
│   ├── G.E1. Tổng quan
│   │   ├── [GB083] Đại thừa (Mahāyāna) — tổng quan · L1
│   │   └── [GB084] Lịch sử hình thành và phát triển Đại thừa · L3
│   ├── G.E2. Tư tưởng nền tảng
│   │   ├── [GB085] Bồ-tát và bồ-đề tâm · L1
│   │   ├── [GB086] Sáu ba-la-mật · L2
│   │   ├── [GB087] Tánh Không — nhập môn · L3
│   │   ├── [GB088] Phật tánh (Như lai tạng) · L3
│   │   ├── [GB089] Ba thân Phật (Tam thân) · L3
│   │   ├── [GB090] Duy thức — nhập môn · L3
│   │   └── [GB091] Các Đức Phật và Bồ-tát chính trong Đại thừa · L2
│   ├── G.E3. Kinh điển
│   │   ├── [GB092] Bản đồ kinh điển Đại thừa · L2
│   │   ├── [GB093] Bát-nhã Tâm kinh và Kim cang bát-nhã · L2
│   │   ├── [GB094] Kinh Diệu pháp Liên hoa (Pháp Hoa) · L3
│   │   ├── [GB095] Kinh Hoa Nghiêm (Avataṃsaka) · L4
│   │   └── [GB096] Kinh Duy-ma-cật · L3
│   ├── G.E4. Các tông phái
│   │   ├── [GB097] Bản đồ các tông phái Đại thừa · L2
│   │   ├── [GB098] Thiền tông (Chan / Zen) · L2
│   │   ├── [GB099] Tịnh độ tông · L2
│   │   ├── [GB100] Thiên Thai tông · L3
│   │   ├── [GB101] Hoa Nghiêm tông · L4
│   │   ├── [GB102] Pháp tướng tông (Duy thức tông) · L3
│   │   ├── [GB103] Tam luận tông · L4
│   │   └── [GB104] Chân ngôn tông (Shingon) và Mật tông Đông Á · L3
│   ├── G.E5. Phật giáo Đông Á — các nước
│   │   ├── [GB105] Phật giáo Trung Quốc · L2
│   │   ├── [GB106] Phật giáo Nhật Bản · L3
│   │   ├── [GB107] Phật giáo Triều Tiên · L3
│   │   └── Phật giáo Việt Nam → tham khảo B7
│   ├── G.E6. Đời sống và thực hành
│   │   ├── [GB108] Khóa công phu và nghi lễ Đại thừa · L2
│   │   ├── [GB109] Ăn chay trong Phật giáo · L2
│   │   └── [GB110] Niệm Phật trong đời sống người tại gia · L2
│   └── G.E7. Lễ hội Phật giáo Đại thừa - Mahāyāna
│       └── [GB111] Lễ hội Phật giáo Đại Thừa - Mahāyāna · L1
│
├── G.F. TRUYỀN THỐNG VAJRAYĀNA
│   ├── G.F1. Tổng quan
│   │   ├── [GB117] Kim cương thừa (Vajrayāna) — tổng quan · L2
│   │   └── [GB118] Từ Mật giáo Ấn Độ đến các nước Himalaya · L3
│   ├── G.F2. Khái niệm nền tảng
│   │   ├── [GB119] Bốn trường phái chính của Phật giáo Tây Tạng · L2
│   │   ├── [GB120] Thầy tâm linh — Lama, Guru và truyền thừa · L2
│   │   ├── [GB121] Quán đảnh (Abhiṣeka) là gì · L2
│   │   ├── [GB122] Chân ngôn, mạn-đà-la và bản tôn — nhìn cho hiểu · L2
│   │   ├── [GB123] Con đường tu trong Kim cương thừa · L3
│   │   ├── [GB124] Tulku — hệ thống tái sinh, Dalai Lama và Karmapa · L2
│   │   └── [GB125] Cờ cầu nguyện, bánh xe kinh và đèn bơ · L1
│   ├── G.F3. Kinh điển
│   │   └── [GB126] Kinh điển Tây Tạng — Kangyur và Tengyur · L3
│   ├── G.F4. Các nước và hiện tại
│   │   ├── [GB127] Tây Tạng và cộng đồng lưu vong · L3
│   │   └── [GB128] Vajrayāna ở Bhutan, Mông Cổ, Nepal và nơi khác · L3
│   └── G.F5. Lễ hội Phật giáo Kim Cương Thừa - Vajrayāna
│       └── [GB129] Lễ hội Phật giáo Kim Cương Thừa - Vajrayāna · L2
│
├── G.G. SO SÁNH & ĐỊNH HƯỚNG
│   ├── G.G1. So sánh ba truyền thống lớn
│   │   └──  [GB134] So sánh ba truyền thống lớn — bảng đối chiếu · L2
│   └── G.G2. Một đạo Phật, nhiều con đường
│       └── [GB135] Một đạo Phật, nhiều con đường — thái độ không tông phái · L2
│
└── G.H. TRA CỨU
    ├── G.H1. Danh mục Kinh điển thường gặp
    │   └── [GB137] Danh mục kinh điển thường gặp — từ Nikāya đến Tantra · R
    ├── G.H2. Danh mục tông phái, truyền thừa
    │   └── [GB138] Danh mục tông phái, trường phái và truyền thừa · R
    └── G.H3. Câu hỏi thường gặp
        └── [GB140] Câu hỏi thường gặp về Phật giáo · R
```

---

# DANH MỤC BÀI VIẾT

> Mỗi bài gồm **mô tả nội dung** (viết gì) và, khi cần, dòng **Thuật ngữ** để người viết bài dùng đúng và thống nhất. Với bài lễ hội, bắt buộc ghi **hệ lịch** và **biến thể theo nước**.

## G.A. NHẬP MÔN & ĐỊNH HƯỚNG

> **Trình tự gợi ý cho người mới:** A1 → A2 → A3; A4 đọc trước khi bước sang nhóm D/E/F.

### G.A1. Hiểu về Phật giáo

#### [GB001] Phật giáo là gì? · L1
Định nghĩa Phật giáo như một con đường giáo dục và thực hành để diệt khổ, do Đức Phật Thích-ca hướng dẫn; giải thích "Phật" nghĩa là "người tỉnh thức", không phải tên riêng hay đấng thần linh. Kèm bảng: Phật giáo có gì (giáo lý, thực hành, cộng đồng, nghệ thuật) và không có gì (sách giáo điều bất biến, đấng sáng thế, hình phạt trần thế).
**Thuật ngữ:** *buddha* (P/S) = người tỉnh thức, bậc giác ngộ; *Buddha* viết hoa chỉ Đức Phật Thích-ca Mâu-ni.

#### [GB002] Tam bảo — Phật, Pháp, Tăng · L1
Ba chỗ nương tựa của mọi truyền thống Phật giáo: bậc giác ngộ (Phật), giáo pháp (Pháp) và cộng đồng tu học (Tăng). Nêu rõ "Tăng" theo nghĩa gốc là cộng đồng tứ chúng (cả xuất gia lẫn tại gia), không chỉ chỉ riêng nhà sư.
**Thuật ngữ:** *ratanattaya* (P) / *triratna* (S) — Hán–Việt **tam bảo**.

#### [GB003] Đạo Phật và các tôn giáo thờ đấng sáng thế · L1
So sánh một cách tôn trọng: Phật giáo không có đấng sáng tạo toàn năng; nghiệp là quy luật nhân quả chứ không phải phần thưởng/trừng phạt; chư Thiên tồn tại trong vũ trụ quan Phật giáo nhưng không phải đối tượng cầu xin tối thượng. Trả lời câu hỏi "Phật giáo là tôn giáo hay triết lý?" bằng cách trình bày cả hai cách nhìn.

#### [GB004] Những hiểu lầm phổ biến về đạo Phật · L1
Làm rõ: đạo Phật bi quan (khổ đế không phải lời than mà là chẩn đoán); thờ tượng là thờ ngẫu tượng; cầu Phật là xin lộc; "tất cả là nghiệp" nên buông xuôi; tu là trốn đời; ăn chay mới là Phật tử; niệm Phật để được bảo hộ như bùa hộ mệnh. Mỗi hiểu lầm kèm câu trả lời ngắn và dẫn link bài tương ứng.

#### [GB005] Đọc thuật ngữ Phật giáo: Pāli, Sanskrit và Hán–Việt · L1
Vì sao cùng một khái niệm có nhiều dạng chữ (*kamma/karma*, *nibbāna/nirvāṇa*, *thiện nghiệp*), cách app hiển thị thuật ngữ và cách tra bảng đối chiếu [GB136]. Phân biệt cộng đồng: Pāli = kinh tạng Theravāda, Sanskrit = Đại thừa, Hán–Việt = văn bản dịch sang Hán. Kèm hướng dẫn đọc dấu phụ (ā, ī, ū, ṃ, ṅ, ñ, ṭ, ḍ, ṇ, ḷ, ś, ṣ). Liên kết [M097], [M160].

### G.A2. Bắt đầu học như thế nào

#### [GB006] Người mới học Phật bắt đầu từ đâu · L1
Bản đồ học: hiểu khái niệm → nghe chuyện Đức Phật → học giáo lý nền → tìm hiểu truyền thống mình gần gũi → kết hợp thực hành (dẫn sang phân mục Thiền). Trình bày lộ trình trong app và cách dùng nhóm A–H của phân mục này.

#### [GB007] Cách đọc kinh và tài liệu Phật giáo · L1
Phân tầng nguồn: kinh điển → chú giải → luận → sách giảng hiện đại → bài viết mạng; vì sao một câu có thể được giải thích khác nhau ở các tầng khác nhau. Hướng dẫn chọn bản dịch tiếng Việt đáng tin và cách đặt câu hỏi khi gặp hai tài liệu mâu thuẫn. Đây là kỹ năng "phòng giả" cho người mới.

#### [GB008] Quy y, tại gia và xuất gia — các mức cam kết · L1
Giải thích các mức độ: người quan tâm → Phật tử quy y tại gia → hành giả giữ bát quan trai → xuất gia sa-di/sư. Xóa hiểu lầm "học Phật là phải ăn chay, xuất gia"; mỗi mức cam kết kèm điều kiện thực tế.

### G.A3. Người Phật tử tại gia

#### [GB009] Tam quy — quy y Phật, Pháp, Tăng · L1
Nghi thức quy y là gì, lời quy y (*buddhaṃ saraṇaṃ gacchāmi*…) nghĩa là gì, quy y khác xin phù hộ ở chỗ nào. Nêu rõ tam quy là nền chung của cả ba truyền thống (nghi thức bên ngoài có thể khác).
**Thuật ngữ:** *tisaraṇa* (P) / *triśaraṇa* (S) — Hán–Việt **tam quy, quy y tam bảo**.

#### [GB010] Ngũ giới — năm điều rèn luyện cho người tại gia · L1
Năm giới (không sát sinh, không trộm cắp, không tà dâm, không nói dối, không dùng chất say) trình bày như **luyện tập** chứ không phải "răn đe"; mỗi giới kèm lý do, phạm vi và cách áp dụng trong việc đời. Nêu cách giữ giới khác nhau giữa các truyền thống và văn hóa.
**Thuật ngữ:** *pañcasīla* (P/S) — Hán–Việt **ngũ giới**.

#### [GB011] Đời sống Phật tử tại gia · L1
Tổng quan đời sống tại gia: lễ Phật buổi sáng, đọc kinh, đi chùa ngày rằm và mùng một, cúng dường, bố thí, tham lễ. Nhấn mạnh các tập quán khác nhau theo truyền thống và vùng miền; tránh quy định "phải như thế mới đúng".

#### [GB012] Tín và tuệ trong đạo Phật · L2
Tín (*saddhā*) nghĩa là lòng tin đã kiểm chứng — như tin cây cầu chắc để bước qua — khác với tín ngưỡng mù quáng; quan hệ bổ trợ giữa tin và hiểu biết trong tiến trình học. Giúp người mới thoát khỏi hai cực đoan: tin tất cả và hoài nghi tất cả.
**Thuật ngữ:** *saddhā* (P) / *śraddhā* (S) — Hán–Việt **tín**.

### G.A4. Định hướng đa truyền thống

#### [GB013] Học Phật nên bắt đầu từ truyền thống nào? · L1
Hướng dẫn lựa chọn dựa trên: môi trường sống (ở Việt Nam thường gần Bắc tông/Tịnh độ), ngôn ngữ kinh sách mình đọc được, hình thực hành hợp tính cách (niệm, ngồi Thiền, nghiên cứu). Kết luận: giáo lý nền (nhóm C) là chung, không cần chọn ngay; dẫn tới [GB027], [GB134].

## G.B. LỊCH SỬ PHẬT GIÁO

> **Trình tự gợi ý:** B1 → B2 → B3 → B4 → B5 → B6; B7 có thể đọc độc lập cho người dùng Việt Nam. Bài nhóm B dùng nguồn sử liệu và ghi rõ độ chắc chắn (xem [GB022]).

### G.B1. Bối cảnh

#### [GB014] Ấn Độ thời Đức Phật — bối cảnh xã hội và tôn giáo · L2
Đông Bắc Ấn thế kỷ 6–5 TCN: Bà-la-môn giáo với hệ đẳng cấp, triết học Upanishad, và phong trào sa-môn (*śramaṇa*) tìm đạo ngoài truyền thống Veda. Giúp người đọc hiểu các khái niệm Đức Phật kế thừa (nghiệp, luân hồi, thiền định) và các khái niệm Ngài cách tân (vô ngã, trung đạo).

### G.B2. Cuộc đời Đức Phật

#### [GB015] Cuộc đời Đức Phật — tổng quan và dòng thời gian · L1
Toàn bộ cuộc đời trong một bài kèm dòng thời gian: sinh tại Lumbini → lớn lên ở Kapilavastu → xuất gia → thành đạo tại Bodh Gaya → thuyết pháp 45 năm → nhập diệt tại Kushinagar ở tuổi 80. Ghi chú niên đại: truyền thống ghi 623–543 TCN, nghiên cứu hiện đại đặt khoảng 480–400 TCN — trình bày cả hai.
**Thuật ngữ:** *Śākyamuni* = Thích-ca Mâu-ni, "hiền giả của dòng Thích-ca"; *siddhattha/siddhārtha* = Tất-đạt-đa.

#### [GB016] Thái tử Tất-đạt-đa và bốn cảnh tượng · L1
Cuộc sống cung đình, bốn cảnh tượng (già, bệnh, chết, sa-môn) và quyết định xuất gia; người vợ Yaśodharā và con trai Rāhula theo sử liệu. Viết vừa tôn trọng truyền thống vừa cho thấy đây là cách kinh điển kể lại ý nghĩa của sự kiện.

#### [GB017] Xuất gia và sáu năm tầm đạo · L2
Học thiền với hai đạo sư Āḷāra Kālāma và Uddaka Rāmaputta; sáu năm khổ hạnh với nhóm năm đồng bạn; nhận bát cháo sữa của Sujātā và quay về con đường trung đạo. Bài học về "không ép, không buông" từ chính cuộc đời Đức Phật (liên kết thái độ hành Thiền [M105]).

#### [GB018] Thành đạo dưới cội Bồ-đề · L2
Đêm thiền định tại Uruvelā (Bodh Gaya): các giai đoạn chứng tri theo kinh điển, cám dỗ của Ma vương (*Māra*) và ý nghĩa biểu tượng của chúng. Nêu rõ các truyền thống kể chi tiết khác nhau.
**Thuật ngữ:** *bodhi* = bồ-đề, giác ngộ; *Bodhirukkha* = cội bồ-đề.

#### [GB019] Chuyển pháp luân — bài thuyết pháp đầu tiên · L2
Bài kinh *Dhammacakkappavattana* (Chuyển pháp luân) tại vườn Lộc (Sarnath) cho năm vị đồng bạn cũ: trung đạo và tứ diệu đế lần đầu được thuyết. Phân tích ngắn cấu trúc bài kinh và vì sao nó được coi là "bản khai sinh" của Phật giáo.
**Thuật ngữ:** *dhammacakkappavattana* — Hán–Việt **chuyển pháp luân**.

#### [GB020] 45 năm hoằng hóa và Tăng đoàn đầu tiên · L2
Tổ chức Tăng đoàn, các đệ tử lớn (Sāriputta, Moggallāna, Ānanda), việc cho phụ nữ xuất gia (Mahāpajāpatī), cách Ngài du hóa và giảng dạy cho đủ mọi tầng lớp. Ghi chú: truyền thống Pāli ghi 45 năm hoằng hóa, một số truyền thống Đông Á ghi 49.
**Thuật ngữ:** *saṅgha/saṃgha* = Tăng-già, Tăng đoàn.

#### [GB021] Nhập diệt tại Câu-thi-na · L2
Những ngày cuối, di giáo ("các pháp hữu vi đều vô thường, hãy tinh tấn"), nhập diệt tuổi 80 và phân chia xá-lợi thành tám phần. Ý nghĩa của lễ đốt trà-tích và thờ xá-lợi trong các truyền thống sau này.
**Thuật ngữ:** *parinibbāna/parinirvāṇa* — Hán–Việt **bát-niết-bàn, nhập diệt**.

#### [GB022] Sử liệu và truyền thuyết về Đức Phật · L3
Tách hai tầng thông tin: tầng truyền thuyết (trường ca *Buddhacarita*, truyện tích các thời) và tầng sử liệu (bia Lumbini của A-dục vương, niên đại tranh luận, khảo cổ các thánh tích). Trang bị cho người đọc thói quen hỏi "thông tin này thuộc tầng nào?" — nguyên tắc dùng xuyên suốt phân mục.

### G.B3. Giữ gìn giáo pháp

#### [GB023] Kết tập kinh điển — giữ gìn giáo pháp sau Đức Phật · L3
Cơ chế truyền khẩu và các lần kết tập: thứ nhất tại Rajagaha (trưởng lão Mahākassapa), thứ hai tại Vesāli vì tranh cãi giới luật, thứ ba dưới thời A-dục vương, và lần ghi chép kinh điển Pāli thành văn tự tại Sri Lanka (thế kỷ 1 TCN). Giải thích vì sao có nhiều bản kinh tương đồng nhưng không giống hệt nhau.

### G.B4. Phân nhánh — các bộ phái sơ kỳ

#### [GB024] Sự phân liệt đầu tiên — Thượng tọa bộ và Đại chúng bộ · L3
Bối cảnh và nguyên nhân phân liệt (tranh cãi mười điều giới luật tại Vesāli), sự hình thành hai khối Thượng tọa bộ (Sthavira) và Đại chúng bộ (Mahāsāṃghika); ghi chú của nghiên cứu hiện đại: phân liệt là tiến trình dần dần, không phải một sự kiện cắt đôi.

#### [GB025] Bản đồ các bộ phái sơ kỳ · L3
Bản đồ khoảng 18–20 bộ phái trong 2–3 thế kỷ sau: Thuyết nhất thiết hữu bộ (Sarvāstivāda), Phân biệt bộ (Vibhajyavāda — tổ tiên dòng Theravāda), Pháp tạng bộ (Dharmaguptaka — luật tạng đang dùng ở Đông Á!), Chánh lượng bộ… Chỉ bộ phái nào còn lưu dòng hôm nay và vì sao bài này hữu ích khi đọc lịch sử các truyền thống.

#### [GB026] A-dục vương — Phật giáo vượt ra khỏi Ấn Độ · L2
Từ vua chinh chiến đến Phật tử hộ pháp; các trụ đá và sắc lệnh; mạng lưới truyền giáo (trong đó có phái đoàn sang Sri Lanka). Vai trò của A-dục vương trong việc biến Phật giáo từ phong trào địa phương thành tôn giáo xuyên lục địa.

### G.B5. Ba truyền thống lớn hình thành

#### [GB027] Ba truyền thống lớn — bản đồ toàn cảnh · L2
Bài "bản đồ mẹ" dẫn vào nhóm D/E/F: dòng thời gian từ Phật giáo sơ kỳ → các bộ phái → Đại thừa (khoảng TCN–CN) → Kim cương thừa (thế kỷ 6–7); bảng so sánh nhanh tên gọi (Thượng tọa bộ/Nam tông; Đại thừa/Bắc tông; Kim cương thừa/Mật tông); nhấn mạnh ba truyền thống không phải ba "giáo hội" tách biệt mà giao thoa liên tục. Liên kết [GB134].

#### [GB028] Sự trỗi dậy của Đại thừa · L3
Nguồn gốc Đại thừa: kinh Bát-nhã xuất hiện, lý tưởng bồ-tát, vai trò tháp và cư sĩ; trình bày các giả thuyết học thuật về nguồn gốc và ghi rõ Đại thừa không "tách ra từ Đại chúng bộ" như sách cũ thường nói. Thời kỳ Đại thừa và các bộ phái chung sống hàng thế kỷ trong cùng tăng viện.

#### [GB029] Sự hình thành Mật giáo và Kim cương thừa · L3
Mật giáo Ấn Độ từ thế kỷ 6–7: tantra, mandala, mantra, quán tưởng bản tôn — phát triển trên nền triết học Đại thừa; các tên gọi "Chân ngôn thừa" (Mantrayāna), "Kim cương thừa" (Vajrayāna). Liên kết [GB117].

#### [GB030] Phật giáo Ấn Độ — một nghìn năm thịnh suy · L3
Từ đỉnh cao (Nalanda, hoàng gia bảo trợ) đến suy tàn (mất bảo trợ, chiến loạn, các cuộc tấn công của quân Thổ vào thế kỷ 12–13 khiến Phật giáo gần như biến mất khỏi Ấn Độ); sự hồi sinh nhỏ vào thế kỷ 19–20 (kể cả phong trào của Ambedkar, 1956). Giải thích vì sao Ấn Độ — quê hương đạo Phật — hôm nay chỉ có thiểu số Phật tử.

### G.B6. Phật giáo lan truyền

#### [GB031] Phật giáo Nam truyền — Sri Lanka và Đông Nam Á · L2
Con đường Nam truyền: Sri Lanka (Mahinda, Saṅghamittā, ghi chép Tam tạng), Miến Điện, Thái Lan, Lào, Campuchia; đặc trưng chung: kinh Pāli, luật Dharmaguptaka không dùng, tăng đoàn giữ vai trò trung tâm văn hóa — giáo dục. Chi tiết từng nước nằm ở nhóm D4.

#### [GB032] Phật giáo Đại Thừa — Con đường tơ lụa và Đông Á · L2
Con đường Đại Thừa: Trung Á, Kucha (Cưu-ma-la-thập), Trung Quốc (đầu CN), các đợt dịch kinh vĩ đại, rồi Triều Tiên, Nhật Bản, Việt Nam; đặc trưng chung: kinh dịch từ Sanskrit sang Hán, Đại thừa làm chủ đạo. Chi tiết từng nước ở nhóm E5.

#### [GB033] Phật giáo Kim Cương Thừa — Himalaya và Mông Cổ · L2
Con đường Kim Cương Thừa: vào Tây Tạng thế kỷ 7–8 (Śāntarakṣita, Padmasambhava, tu viện Samye), phổ biến thứ hai thế kỷ 10–11 (Atiśa, Marpa), sang Bhutan, Mông Cổ, Nepal và các cộng đồng Nga (Buryatia, Kalmykia). Chi tiết ở nhóm F.

#### [GB034] Phật giáo hiện đại — hành trình ra thế giới · L3
Từ thế kỷ 19: học giả phương Tây dịch kinh, phong trào Thiền định và chánh niệm, dòng người Việt và Tây Tạng di tản mang Phật giáo ra thế giới, "Phật giáo dấn thân" (Thích Nhất Hạnh), Phật giáo châu Âu — Mỹ hôm nay. Bối cảnh giúp người đọc hiểu vì sao app có cả ba truyền thống.

### G.B7. Phật giáo Việt Nam

> **Vì sao có nhóm riêng:** người dùng Việt Nam cần biết gốc tích các hình thức Phật giáo mình gặp hằng ngày. Viết một lần ở đây; các nhánh E5/D4 chỉ liên kết chéo. Phối hợp với nhóm F1 phân mục Thiền ([M145]–[M152]) phần thực hành.

#### [GB035] Phật giáo vào Việt Nam — từ những thế kỷ đầu Công nguyên · L2
Hai con đường truyền vào: bộ phái Ấn Độ theo biển và Đại thừa Trung Hoa xuống phía nam; trung tâm Luy Lâu sớm; các thiền sư India và Trung Hoa đến Giao Chỉ. Ghi chú về độ chắc chắn của tư liệu giai đoạn này.

#### [GB036] Phật giáo Việt Nam thời Lý–Trần · L3
Phật giáo trở thành quốc giáo thời Lý; thiền phái Trúc Lâm do Trần Nhân Tông sáng lập; vai trò tăng sĩ trong triều chính; văn học Phật giáo Trần ("Cư trần lạc đạo"). Liên kết [M146], [M147].

#### [GB037] Phật giáo Việt Nam cận — hiện đại · L2
Từ suy yếu thời Lê–Nguyễn đến phong trào chấn hưng đầu thế kỷ 20 (Khối Từ thiện, cải cách tăng giáo), các tổ chức giáo hội qua các giai đoạn lịch sử, đến Giáo hội Phật giáo Việt Nam thống nhất hiện nay. Viết trung lập theo nguyên tắc biên tập số 10.

#### [GB038] Bản đồ Phật giáo Việt Nam hôm nay · L2
Các dòng hiện hữu: Bắc tông (Thiền, Tịnh độ, Thiền–Tịnh song tu) — dòng chủ đạo; Nam tông Kinh và Nam tông Khmer; dòng Trúc Lâm phục hưng; truyền thống Làng Mai; các trung tâm Thiền hiện đại. Kèm "mẹo nhận diện": vào một ngôi chùa Việt, nhận biết chùa thuộc dòng nào qua tượng, nghi thức, màu cà sa. Liên kết [M145].

## G.C. LÝ THUYẾT NỀN TẢNG CHUNG

> **Quy tắc của nhóm C:** chỉ chứa giáo lý **cả ba truyền thống cùng thừa nhận**. Điểm khác nhau trong cách diễn giải (ví dụ: Niết-bàn được hiểu khác nhau) không viết ở đây mà nằm ở D/E/F và [GB134]. Người đọc xong nhóm C sẽ đọc được hầu hết bài của mọi truyền thống.

### G.C1. Tứ diệu đế

#### [GB039] Tứ diệu đế — tổng quan · L1
Khung giáo lý trung tâm của toàn bộ Phật giáo: khổ, tập, diệt, đạo — trình bày qua ẩn dụ bác sĩ chẩn bệnh (bệnh — nguyên nhân — tiên lượng — đơn thuốc). Giải thích vì sao gọi là "thánh đế" và vì sao đây là "bộ xương sống" chung của mọi tông phái.
**Thuật ngữ:** *cattāri ariyasaccāni* (P) / *catvāri āryasatāni* (S) — Hán–Việt **tứ thánh đế**.

#### [GB040] Khổ đế · L2
Ba dạng khổ: khổ khổ (khổ giác quan), hoại khổ (khổ vì đổi thay), hành khổ (khổ tiềm ẩn trong mọi pháp hữu vi). Xóa hiểu lầm "Phật giáo dạy đời toàn là khổ": khổ đế là một nhận định chẩn đoán, không phải lời than.

#### [GB041] Tập đế · L2
Gốc của khổ là ái (*taṇhā*) — tham dục giác quan, muốn tồn tại, muốn hủy diệt — và chuỗi duyên nối ái với tái sinh. Phân biệt ham muốn đơn thuần với ái tạo khổ.

#### [GB042] Diệt đế · L2
Khổ có thể chấm dứt hoàn toàn — đây là tuyên bố "có lối thoát" của đạo Phật; diệt không phải hủy diệt mà như ngọn lửa tắt vì hết nhiên liệu. Dẫn sang [GB059] Niết-bàn.

#### [GB043] Đạo đế · L2
Con đường đưa đến diệt khổ là thánh đạo tám nhánh; giới thiệu nhanh ba nhóm Giới–Định–Tuệ và dẫn sang nhóm C2. Đạo đế là cầu nối giữa giáo lý và thực hành.

### G.C2. Bát chánh đạo

#### [GB044] Bát chánh đạo — tổng quan và ba nhóm · L1
Tám nhánh: chánh kiến, chánh tư duy, chánh ngữ, chánh nghiệp, chánh mạng, chánh tinh tấn, chánh niệm, chánh định; gom thành ba nhóm Tuệ – Giới – Định. Nêu rõ "chánh" (*sammā*) nghĩa là "trọn vẹn, đúng hướng", không đối lập với "tà" theo nghĩa đạo đức phê phán. Kèm sơ đồ八角 hình bánh xe pháp.
**Thuật ngữ:** *aṭṭhaṅgika magga* (P) / *aṣṭāṅga mārga* (S) — Hán–Việt **bát chánh đạo**.

#### [GB045] Nhóm Giới: chánh ngữ, chánh nghiệp, chánh mạng · L2
Ba nhánh đạo đức: nói chuyện thế nào là "chánh ngữ", nghề nghiệp nào bất thiện, áp dụng trong việc đời hiện đại (nói trên mạng, kinh doanh). Cơ sở cho năm giới và luật xuất gia ở mọi truyền thống.

#### [GB046] Nhóm Định: chánh tinh tấn, chánh niệm, chánh định · L2
Ba nhánh rèn tâm: nỗ lực đúng mức, chánh niệm và định. Viết ở mức khái niệm普及; hướng dẫn thực hành chi tiết thuộc phân mục Thiền — dẫn [M095], [M096] và nhóm B/C của phân mục đó.

#### [GB047] Nhóm Tuệ: chánh kiến, chánh tư duy · L2
Hai nhánh trí tuệ: thấy đúng thực tại (tứ diệu đế, ba đặc tính) và suy nghĩ đúng hướng (xả tham, vô hại). Chánh kiến đứng đầu con đường — vì sao "tin đúng" là bước đầu, không phải bước cuối.

### G.C3. Duyên khởi

#### [GB048] Duyên khởi — tổng quan · L2
Định luật cốt lõi: "cái này có thì cái kia có; cái này sinh thì cái kia sinh" — mọi hiện tượng đều tùy thuộc điều kiện mà phát sinh. Duyên khởi là lý giải chung của nghiệp, luân hồi và con đường giải thoát; công thức ngắn gọn kèm ví dụ đời thường (hạt giống – điều kiện – cây).
**Thuật ngữ:** *paṭiccasamuppāda* (P) / *pratītyasamutpāda* (S) — Hán–Việt **duyên khởi, duyên sinh**.

#### [GB049] Mười hai chi duyên khởi · L3
Trình bày 12 chi từ vô minh đến lão tử; các cách giải thích trong truyền thống: mô hình ba đời (chú giải Theravāda), quán sát sát-na (Trung quán), và cách ứng dụng thực hành. Bài khái niệm; phần quan sát thực tế thuộc Thiền tuệ [M121].

### G.C4. Nghiệp, luân hồi và các cõi

#### [GB050] Nghiệp — hiểu đúng và hiểu sai · L1
Nghiệp = hành động có chủ đích (thân, khẩu, ý) và kết quả của nó; không phải số phận, không phải sự trừng phạt của ai. Ba điểm cần nắm: nghiệp quá khứ không mặc định tương lai; ý chí hiện tại là "khoản tự do" của mỗi người; nghiệp vừa là kết quả vừa là hành động đang tạo. Trả lời các câu hỏi thực tế: sao người làm lành gặp dữ, nghiệp có tính không?
**Thuật ngữ:** *kamma* (P) / *karma* (S) — Hán–Việt **nghiệp**; *cetanā* = tư, chủ đích — "ý nghiệp là lớn nhất".

#### [GB051] Luân hồi và tái sinh · L2
Tái sinh không cần "linh hồn bất biến" — hình ảnh ngọn nến mồi sang ngọn nến khác; dòng tương tục thức – nghiệp nối các đời. Nêu sự khác nhau giữa các trường phái về giai đoạn trung hữu (*antarābhava*) — ví dụ cho việc cùng một vấn đề được trả lời khác nhau theo tông phái.

#### [GB052] Sáu cõi và vũ trụ quan Phật giáo · L2
Sáu cõi (địa ngục, ngạ quỷ, súc sinh, a-tu-la, người, trời) và ba cõi (dục, sắc, vô sắc); mô hình 31 cõi trong chú giải Theravāda; vũ trụ quan này là cách mô tả kinh nghiệm tâm – hoàn cảnh sống, không phải bản đồ thiên văn. Cõi Tịnh độ của Đại thừa được giới thiệu ngắn và dẫn [GB099].

#### [GB053] Công đức, phước điền và hồi hướng · L2
Ba nền móng phước: bố thí, trì giới, tu tập; thực hành hồi hướng công đức — chia phước cho người khuất mặt, người thân — có mặt ở **cả ba truyền thống**. Phân biệt làm phước với "buôn bán công đức"; phước và tuệ như hai cánh.

### G.C5. Ngũ uẩn và vô ngã

#### [GB054] Ngũ uẩn — "tôi" được cấu thành từ những gì · L2
Năm nhóm cấu thành kinh nghiệm: sắc, thọ, tưởng, hành, thức; phân tích một trải nghiệm đời thường (ví dụ: nghe một câu khen) thành năm uẩn để thấy "cái tôi" là sự hợp thành, không phải thực thể.
**Thuật ngữ:** *pañcakkhandha* (P) / *pañca-skandha* (S) — Hán–Việt **năm uẩn**.

#### [GB055] Vô ngã — hiểu đúng một khái niệm dễ hiểu sai · L2
Vô ngã (*anattā/anātman*) nghĩa là không có một "cái tôi" cố định, độc lập, thường hằng — **không** có nghĩa "không tồn tại", không phủ định trách nhiệm cá nhân hay ký ức. Trình bày vô ngã như phân tích kinh nghiệm, phân biệt với hư vô chủ nghĩa. Liên kết [M028].

#### [GB056] Ba đặc tính và các pháp ấn · L2
Vô thường, khổ, vô ngã như ba con dấu kiểm chứng giáo pháp; ghi chú một số truyền thống Đông Á dùng bốn pháp ấn (thêm "niết-bàn tịch tĩnh"). Khái niệm; phần quán chiếu thực hành thuộc [M053], [M025]–[M028].

### G.C6. Tam học và hạnh sống

#### [GB057] Tam học — Giới, Định, Tuệ · L2
Tam học như chương trình học ba bước có trình tự của toàn bộ con đường Phật giáo; giới là nền của định, định là nền của tuệ — cách hiểu chung cho mọi truyền thống dù mỗi truyền thống nhấn mạnh khác nhau. Liên kết [M095].
**Thuật ngữ:** *tisso sikkhā* (P) / *trīṇi śikṣāṇi* (S) — Hán–Việt **tam học**.

#### [GB058] Từ, bi, hỷ, xả trong đời sống · L1
Giới thiệu ngắn bốn phẩm chất tâm phổ quát — lòng thương, sự cảm thông trước khổ của người khác, niềm vui với hạnh phúc của người khác, tâm bình thản — với ví dụ áp dụng trong gia đình, công sở. Bản phổ thông; bản thực hành chi tiết ở [M041]–[M046].

### G.C7. Mục tiêu giải thoát

#### [GB059] Niết-bàn là gì · L2
Niết-bàn = dập tắt lửa tham, sân, si; còn dư y (tự tại) và vô dư y (các truyền thống giải thích khác nhau); vì sao Niết-bàn không thể mô tả bằng ngôn từ khái niệm mà chỉ biết qua đường tu. Các cách tiếp cận khác nhau giữa ba truyền thống được tóm ở [GB134].
**Thuật ngữ:** *nibbāna* (P) / *nirvāṇa* (S) — Hán–Việt **niết-bàn**.

#### [GB060] Bốn bậc thánh và tiến trình giải thoát · L3
Bốn bậc theo kinh tạng Pāli: nhập lưu, nhất lai, bất lai, a-la-hán — cùng khung mười kiết sử được lần lượt đoạn trừ. Ghi chú: Đại thừa diễn đạt tiến trình qua thập địa bồ-tát — hai bản đồ này không mâu thuẫn về mặt chức năng. Liên kết [GB085].
**Thuật ngữ:** *sotāpanna/srotāpanna* = tu-đà-hoàn (nhập lưu); *arahant/arhat* = a-la-hán.

#### [GB061] Các Đức Phật — quá khứ, hiện tại và vị lai · L2
Đức Phật Thích-ca không phải Phật duy nhất: các Phật quá khứ (trong đó Nhiên Đăng/Dīpaṅkara nổi tiếng), và Đức Phật Di-lặc (Maitreya) trong tương lai — niềm tin chung cho cả ba truyền thống. Phân biệt "Phật" như tước hiệu và tên riêng; mở đường sang [GB089] ba thân Phật.

## G.D. TRUYỀN THỐNG THERAVĀDA

> **Trình tự gợi ý:** D1 → D2 → D3 → D4 → D5; với người chỉ quan tâm lễ hội, có thể vào thẳng D5 sau [GB062]. Nhóm D nói về truyền thống như một nền văn hóa — tôn giáo; nội dung Thiền thuộc [M055]–[M059], [M134]–[M136].

### G.D1. Tổng quan

#### [GB062] Thượng tọa bộ (Theravāda) — tổng quan · L1
Theravāda nghĩa là "giáo pháp của các trưởng lão"; khu vực (Sri Lanka, Thái Lan, Miến Điện, Lào, Campuchia); đặc trưng nhận diện: kinh điển Pāli, lý tưởng a-la-hán, con đường tuần tự, tăng đoàn giữ vai trò xã hội lớn. "Nam tông" ở Việt Nam gọi ai — xóa nhầm lẫn Nam tông/Nam tông Kinh/Nam tông Khmer.

#### [GB063] Lịch sử Theravāda · L3
Từ bộ phái Vibhajyavāda đến dòng chính tại Sri Lanka: Mahinda và vua Devānaṃpiya Tissa, Đại tự (Mahāvihāra), ghi chép Tam tạng (thế kỷ 1 TCN), chú giải của Buddhaghosa (thế kỷ 5), các đợt suy thoái — phục hưng, reform movement Dhammayuttika thế kỷ 19, và Theravāda toàn cầu hóa hôm nay.

### G.D2. Kinh điển

#### [GB064] Tam tạng Pāli — bản đồ kinh điển · L2
Cấu trúc Luật – Kinh – Luận: Luật tạng (quy định tăng ni), Kinh tạng gồm năm bộ Nikāya (Trường, Trung, Tương ưng, Tăng chi, Tiểu bộ), A-tỳ-đàm; mỗi tạng chứa gì, độ khó đọc thế nào, nên bắt đầu đọc từ đâu (gợi ý: kinh Trung bộ và Tăng chi). Liên kết [GB137].
**Thuật ngữ:** *tipiṭaka* (P) / *tripiṭaka* (S) — Hán–Việt **tam tạng** (ba giỏ kinh).

#### [GB065] A-tỳ-đàm (Abhidhamma) là gì · L3
Tạng thứ ba: hệ thống phân tích tất cả kinh nghiệm thành các "pháp" cuối cùng; bảy bộ theo truyền thống Pāli; vì sao Abhidhamma được coi là khó và thường được học sau — bài chỉ ở mức bản đồ, không đi vào chi tiết pháp số.

#### [GB066] Hệ chú giải và Thanh tịnh đạo · L3
Vai trò của các bộ chú giải (*aṭṭhakathā*) và tác phẩm *Visuddhimagga* (Thanh tịnh đạo) của Buddhaghosa: nơi hệ thống hóa đường tu Giới–Định–Tuệ; phân biệt nội dung kinh gốc với nội dung chú giải khi đọc tài liệu Theravāda. Liên kết [M134].

### G.D3. Đường tu và đời sống

#### [GB067] Con đường tu trong Theravāda · L2
Bức tranh đường tu: quy y → giữ giới → bố thí, tạo phước → nghe pháp → thiền chỉ và thiền tuệ → chứng quả. Khái niệm "tuần tự tu học" (*anupubbasikkhā*) và vai trò của tăng đoàn trụ trì giáo pháp. Bài khung; các pháp môn chi tiết ở các bài sau của D3 và phân mục Thiền.

#### [GB068] Thiền trong Theravāda — nhập môn · L2
Tổng quan đề mục thiền Theravāda ở mức phổ thông: niệm hơi thở, tứ vô lượng tâm, tứ niệm xứ, đề mục 40; hướng người muốn thực hành sang lộ trình Thiền của app. Liên kết [M055]–[M058], [M127].

#### [GB069] Đời sống tăng đoàn Theravāda · L2
Một ngày của nhà sư: khất thực, nghe giáo giới, nghiên cứu kinh điển, thiền tọa; bản quy y diệt trừ (*pātimokkha*) hai lần tháng; mùa An cư; các dòng rừng (forest tradition) và dòng chùa làng; quan hệ sư phó – đệ tử.

#### [GB070] Đời sống Phật tử tại gia Theravāda · L2
Thực hành tại gia: giữ ngũ giới, bố thí cho tăng đoàn (dāna), thọ bát quan trai ngày Uposatha, cúng dường công đức cho người quá cố, đến chùa nghe pháp; tập quán vùng miền (Thái, Lào, Miến, Khmer) khác nhau ra sao.

### G.D4. Theravāda ở các nước

> Mỗi bài viết theo một khung chung: lịch sử vào nước đó → tổ chức tăng đoàn hôm nay → đặc trưng thực hành →貢献 nổi bật (ví dụ: Thiền Miến Điện hiện đại với [M135]).

#### [GB071] Theravāda Sri Lanka · L2
Cái nôi của Theravāda: từ Mahinda đến Kandy, Phật giáo và quốc gia, tổ chức Asgiriya–Malwatte, phong trào phục hưng thế kỷ 19, ngày trai giới Poson.

#### [GB072] Theravāda Thái Lan · L2
Từ Sukhothai đến hôm nay: hai hệ phái Mahānikai và Dhammayuttika, vai trò nhà vua, hệ thống tăng đoàn quốc gia, truyền thống rừng (Ajahn Mun, Ajahn Chah), Phật giáo trong đời sống Thái hiện đại. Liên kết [M136].

#### [GB073] Theravāda Miến Điện · L2
Bagan và vua Anawrahta, truyền thống thiền định dân chúng hóa (Ledi Sayādaw trở đi), các hệ thống Thiền Miến Điện có ảnh hưởng toàn cầu. Liên kết [M135].

#### [GB074] Theravāda Lào và Campuchia · L2
Phật giáo Lào (tăng đoàn, tập quán Boun) và Campuchia (Angkor, Phật giáo Khmer, sự gián đoạn lịch sử thế kỷ 20 và sự hồi phục).

#### [GB075] Theravāda tại Việt Nam · L2
Hai bộ phận: Nam tông Kinh (hình thành đầu thế kỷ 20 quanh chùa Bửu Quang, Sài Gòn và các tự viện kế thừa — đối chiếu lại tư liệu lịch sử trong nước khi viết bài) và Nam tông Khmer ở Tây Nam Bộ; tự viện, mùa An cư, lễ hội Chôl Chnăm Thmây và Ok Om Bok của cộng đồng Khmer. Liên kết [M151].

### G.D5. Lễ hội Theravāda

> **Nguyên tắc chung:** lễ Theravāda gắn với lịch mặt trăng và mùa (mưa, gặt). Mỗi bài phải ghi: ý nghĩa giáo lý gốc → tập quán từng nước → ngày tính theo hệ lịch nào (không cố định dương lịch).

## G.E. TRUYỀN THỐNG MAHĀYĀNA

> **Trình tự gợi ý:** E1 → E2 → E3 → E4 → E5/E6 → E7. Nhóm E rộng nhất; người dùng Việt Nam sẽ thấy nhiều nội dung quen thuộc (Tịnh độ, Vu Lan, niệm Phật).

### G.E1. Tổng quan

#### [GB083] Đại thừa (Mahāyāna) — tổng quan · L1
"Đại thừa" = cỗ xe lớn: lý tưởng đưa tất cả chúng sinh đến giác ngộ, không chỉ giải thoát cá nhân; đặc trưng: kinh điển Sanskrit (dịch Hán/Tạng), bồ-tát đạo, nhiều Phật và Bồ-tát, nghi lễ phong phú; vùng: Trung Quốc, Việt Nam, Triều Tiên, Nhật. Nhấn mạnh: Đại thừa rất đa dạng, không phải một hệ thống đơn nhất.

#### [GB084] Lịch sử hình thành và phát triển Đại thừa · L3
Từ phong trào bồ-tát và kinh Bát-nhã đầu CN, qua Nagarjuna (Trung quán) và Vasubandhu (Duy thức), các trung tâm Nalanda; sự xuất hiện ở Trung Quốc qua dịch kinh (Cưu-ma-la-thập, Huyền Trang); quan hệ phức tạp với các bộ phái — Đại thừa không ra đời như một sự kiện "chia đôi" duy nhất (liên kết [GB028]).

### G.E2. Tư tưởng nền tảng

#### [GB085] Bồ-tát và bồ-đề tâm · L1
Bồ-tát là ai — từ "người hướng tới giác ngộ" đến lý tưởng "giác ngộ vì chúng sinh"; bồ-đề tâm nguyện và bồ-đề tâm hành; vì sao bồ-tát đạo là trái tim của Đại thừa; nguồn gốc từ các truyện tiền thân (Jātaka) — di sản chung với Theravāda.
**Thuật ngữ:** *bodhisatta* (P) / *bodhisattva* (S) — Hán–Việt **bồ-tát**; *bodhicitta* — **bồ-đề tâm**.

#### [GB086] Sáu ba-la-mật · L2
Sáu hoàn thiện: bố thí, trì giới, nhẫn nhục, tinh tấn, thiền định, trí tuệ; mỗi ba-la-mật kèm ví dụ đời thường của người tại gia; ghi chú bản mười ba-la-mật thêm phương tiện, nguyện, lực, trí. Đây là "chương trình học" của bồ-tát.
**Thuật ngữ:** *pāramitā* — Hán–Việt **đáo bỉ ngạn / ba-la-mật**.

#### [GB087] Tánh Không — nhập môn · L3
*Śūnyatā* không phải "không có gì" mà là "không tồn tại độc lập, tự tính"; tánh Không chính là duyên khởi nhìn từ phía khác; giải thích các câu quen thuộc: "sắc tức thị không", "pháp không có tự tính"; vì sao thấy tánh Không là thấy trung đạo. Liên kết [M070].
**Thuật ngữ:** *suññatā* (P) / *śūnyatā* (S) — Hán–Việt **không, tánh Không**.

#### [GB088] Phật tánh (Như lai tạng) · L3
Dạy rằng mọi chúng sinh đều có khả năng thành Phật — "như lai tạng"; quan hệ giữa Phật tánh và tánh Không (hai cách diễn đạt, không mâu thuẫn); ý nghĩa thực tiễn: không ai bị loại khỏi con đường. Ghi chú các tranh luận lịch sử về khái niệm này.

#### [GB089] Ba thân Phật (Tam thân) · L3
Khung tư tưởng giúp hiểu vì sao Đại thừa có nhiều Phật: thân pháp (dharmakāya — chân như), thân báo (saṃbhogakāya — thân trang nghiêm trong cõi Tịnh độ), thân ứng (nirmāṇakāya — thân lịch sử như Thích-ca). Giải thích ngắn gọn, dùng ví dụ mặt trời – ánh sáng.
**Thuật ngữ:** *trikāya* — Hán–Việt **tam thân**.

#### [GB090] Duy thức — nhập môn · L3
Hệ Duy thức (Yogācāra): mọi hiện tượng là thức biến hiện; các tầng thức (trong gồm a-lại-da thức); phân biệt Duy thức với chủ nghĩa duy tâm/phủ nhận thế giới. Bài bản đồ; liên kết [M138].

#### [GB091] Các Đức Phật và Bồ-tát chính trong Đại thừa · L2
"Who is who" trong chùa Bắc tông: Phật Thích-ca, A-di-đà (Phương Tây), Dược sư (Phương Đông), Di-lặc; Quán Thế Âm (Quán Âm — và sự chuyển giới tính hình tượng ở Trung Quốc), Văn-thù, Phổ Hiền, Địa Tạng; nhận diện qua tay cầm, tư thế, vật riding; mỗi vị đại diện điều gì trong đời sống tín ngưỡng.

### G.E3. Kinh điển

#### [GB092] Bản đồ kinh điển Đại thừa · L2
Các "họ" kinh lớn: Bát-nhã, Pháp Hoa, Hoa Nghiêm, Bảo Tích, Đại tập, Niết-bàn (Đại thừa); các đợt dịch sang Hán và tính chất văn bản Đại thừa (không có "bản gốc" duy nhất); Đại tạng Hán văn (Taishō) và cách trích dẫn kinh. Liên kết [GB137].

#### [GB093] Bát-nhã Tâm kinh và Kim cang bát-nhã · L2
Hai bản kinh được đọc tụng nhất trong Bắc tông: Tâm kinh (260 chữ) và Kim cang bát-nhã ba-la-mật kinh; giải thích câu chữ từng đoạn một ở mức phổ thông, lịch sử bản dịch (Huyền Trang), và cách đọc tụng trong khóa lễ ([GB108]).

#### [GB094] Kinh Diệu pháp Liên hoa (Pháp Hoa) · L3
Nội dung chính: phương tiện thiện xảo (upāya), "nhất Phật thừa" — mọi con đường đều dẫn đến Phật quả, chương Đề-bà-đạt-đa, thọ mạng vô lượng của Đức Phật; ảnh hưởng lớn tới các tông Đông Á và tập quán tụng "Nam Miao Pháp Liên Hoa Kinh" (Nichiren).

#### [GB095] Kinh Hoa Nghiêm (Avataṃsaka) · L4
Bộ kinh được coi là đỉnh triết học Đại thừa: cảnh giới "nhất thiết trong nhất thiết" — lưới đế châu của Thiên đế (Indra), sự tương tức tương nhập của mọi hiện tượng; vì sao kinh này khó và thường đọc phân đoạn; ảnh hưởng sang Hoa Nghiêm tông ([GB101]).

#### [GB096] Kinh Duy-ma-cật · L3
Truyện vị bồ-tát cư sĩ Duy-ma-cật bác bệnh và thuyết pháp — hình mẫu bồ-tát tại gia, đối thoại với các vị đại đệ tử; kinh văn giàu chất văn chương và hóm hỉnh; đặc biệt gần gũi với người tu tại gia.

### G.E4. Các tông phái

> Mỗi bài tông phái viết theo khung: nguồn hình thành → tư tưởng cốt lõi → thực hành chính → hiện diện hôm nay (nước nào, chùa nào ở Việt Nam).

#### [GB097] Bản đồ các tông phái Đại thừa · L2
Bản đồ: Trung Quốc có tám tông lớn (Thiền, Tịnh độ, Thiên Thai, Hoa Nghiêm, Pháp tướng/Duy thức, Tam luận, Luật, Chân ngôn/Mật); Nhật thêm Thiên Thai tông (Tendai), Nichiren; Việt Nam: Thiền và Tịnh độ là hai dòng chính, kết hợp thành Thiền – Tịnh song tu. Dẫn vào các bài chi tiết.

#### [GB098] Thiền tông (Chan / Zen) · L2
Từ Bồ-đề-đạt-ma đến Lục tổ Huệ Năng và *Kinh Lục tổ đàn kinh*; đặc trưng "trực chỉ nhân tâm", tông phong; các dòng Lâm Tế (Rinzai) và Tào Động (Sōtō); Thiền tông tại Việt Nam. Bài phổ thông về tông phái; thực hành thuộc [M064]–[M067], [M139], [M140].

#### [GB099] Tịnh độ tông · L2
Dựa trên các kinh Vô lượng thọ, Quán Vô lượng thọ, A-di-đà: Phật A-di-đà và cõi Cực lạc, 48 lời nguyện; công thức "tín – nguyện – hạnh" (tin, phát nguyện, niệm Phật); vì sao được gọi là "pháp môn dễ hành" cho mọi người. Liên kết [M068], [M069], [M150].

#### [GB100] Thiên Thai tông · L3
Tôn giáo đầu tiên do người Trung Hoa sáng lập hệ thống: Trí Khải và núi Thiên Thai; phân loại giáo pháp (phan giáo) trong *Pháp hoa huyền nghĩa*; hệ thống Chỉ – Quán có cấu trúc bậc nhất Đông Á. Liên kết [M137].

#### [GB101] Hoa Nghiêm tông · L4
Tông xây trên kinh Hoa Nghiêm ([GB095]): pháp tạng và thuyết "lý sự vô ngại"; tưởng tượng vũ trụ tương tức; vị trí trong triết học Đông Á.

#### [GB102] Pháp tướng tông (Duy thức tông) · L3
Tông do Huyền Trang mang về từ Ấn Độ sau hành trình Tây du trứ danh; giảng dạy hệ Duy thức ([GB090]) với tính học viện cao; vì sao có ảnh hưởng lớn đến khoa cử và triết học Phật giáo Đông Á.

#### [GB103] Tam luận tông · L4
Truyền thừa tư tưởng Trung quán (Madhyamaka) của Long thụ tại Trung Quốc: Tam luận (Trung quán, Bách luận, Thập nhị môn luận); phép biện chứng phủ định song tuyển "không — không không"; ảnh hưởng lan sang Thiền tông. Liên kết [M070].

#### [GB104] Chân ngôn tông (Shingon) và Mật tông Đông Á · L3
Mật giáo truyền sang Trung Quốc (Thiện Vô Qu Ngại Trí) rồi Nhật (Kūkai, núi Kōya): tam mật tương ứng (thân – khẩu – ý), mandala Thai tạng giới – Kim cương giới; phân biệt Mật tông Đông Á với Vajrayāna Tây Tạng (nhóm F) — cùng nguồn Ấn Độ, phát triển khác nhau.

### G.E5. Phật giáo Đông Á — các nước

> **Liên kết chéo:** Phật giáo Việt Nam đã có nhóm riêng B7 ([GB035]–[GB038]); các bài đó gắn thêm category `mahayana` để hiện trong nhóm này.

#### [GB105] Phật giáo Trung Quốc · L2
Từ Hán minh đế ("Lieutenant mơ vàng") qua các đợt dịch kinh, phát triển tám tông, bốn lần pháp nạn (persecutions), tương tác Nho – Đạo – Phật ("tam giáo đồng nguyên"), và Phật giáo Trung Quốc đại lục hôm nay. Bài cơ sở để hiểu mọi truyền thống Đông Á khác.

#### [GB106] Phật giáo Nhật Bản · L3
Vào Nhật thế kỷ 6 qua Triều Tiên; các thời kỳ Nara, Heian (Tendai, Shingon), Kamakura bùng nổ các tông phổ thông (Tịnh độ Chân tông, Nhật Liên, Thiền), quan hệ "Phật giáo tang lễ" hiện đại, các tôn giáo mới phát sinh từ Phật giáo. Bài giúp hiểu văn hóa đại chúng (thiền trong trà đạo, nghệ thuật, manga).

#### [GB107] Phật giáo Triều Tiên · L3
Vào bán đảo thế kỷ 4; thời thống nhất Tân La (Bulguksa, Seokguram), thiền Seon và trình độ học thuật của Jinul, kỳ hạn压制 thời Joseon, Phật giáo Hàn Quốc hiện đại (tông Jogye) và làn sóng Thiền Hàn ra thế giới.

### G.E6. Đời sống và thực hành

#### [GB108] Khóa công phu và nghi lễ Đại thừa · L2
Khóa công phu sáng – tối trong tự viện và tại gia: niệm hương, tán Phật, Tâm kinh, Đại bi chú, sám pháp, hồi hướng; ý nghĩa từng phần; cách một người mới tham dự khóa lễ tại chùa Bắc tông (đứng, lạy, xá) mà không sợ làm sai.

#### [GB109] Ăn chay trong Phật giáo · L2
Vì sao Phật giáo Đại thừa khuyến khích ăn chay (kinh Lăng-già, đại bi tâm) trong khi Theravāda không bắt buộc (thịt tam tịnh); các mức chay: trường chay, chay kỳ (mùng 1, rằm); ăn chay và sức khỏe; gỡ hiểu lầm "chưa ăn chay chưa phải Phật tử". So sánh trung lập giữa các truyền thống.

#### [GB110] Niệm Phật trong đời sống người tại gia · L2
Niệm Phật như pháp đời sống: niệm như thế nào (khẩu niệm, tâm niệm, mười niệm pháp), niệm với chuỗi hạt, khóa Phật thất, hộ niệm cho người bệnh và người sắp mất; niệm Phật cầu an – cầu siêu hiểu đúng. Bài phổ thông; thực hành định tâm thuộc [M068]; văn hóa Việt thuộc [M150].

### G.E7. Lễ hội Đại thừa / Đông Á

> **Nguyên tắc chung:** lễ Đông Á theo **âm lịch Việt – Trung**; ngày cùng tên nhưng tập quán khác nhau theo nước; phải ghi rõ "âm lịch tháng nào, ngày nào". Việt Nam có Phật đản 15/4 — khác Trung Quốc 8/4 — ghi rõ trong từng bài.

#### [GB111] Lễ hội Phật giáo Đông Á · L1

## G.F. TRUYỀN THỐNG VAJRAYĀNA

> **Trình tự gợi ý:** F1 → F2 → F3 → F4 → F5. Khuyến nghị đọc [GB083] (Đại thừa) trước [GB117] vì Vajrayāna xây trên nền Đại thừa. Nội dung thực hành thuộc [M071]–[M080]; nhóm F ở đây là kiến thức phổ thông về văn hóa — lịch sử.

### G.F1. Tổng quan

#### [GB117] Kim cương thừa (Vajrayāna) — tổng quan · L2
"Kim cương" = vật chất rắn chắc không thể phá vỡ — chỉ phương tiện mạnh mẽ; định vị: phương tiện đặc thù trong Đại thừa (không phải "tôn giáo thứ tư" cũng không phải "bản nâng cấp"); đặc trưng: truyền thừa, quán đảnh, bản tôn, chân ngôn; vùng: Tây Tạng, Bhutan, Mông Cổ, Nepal. Xóa hai hiểu lầm đối xứng: "Mật tông là phù phép" và "Mật tông là con đường thần tốc cho mọi người".

#### [GB118] Từ Mật giáo Ấn Độ đến các nước Himalaya · L3
Tuyến truyền的历史 narrative: tantra Phật giáo phát triển ở Ấn (thế kỷ 6–7 trở đi) → truyền vào Tây Tạng thế kỷ 8 (Śāntarakṣita, Padmasambhava, tu viện Samye, tranh luận Hội đồng Lhasa) → giai đoạn sarcophagus thứ hai thế kỷ 10–11 (Atiśa, Marpa, dịch lại kinh tạng) → hình thành các trường phái. Ghi chú trung lập về giai đoạn "pháp nạn Langdarma".

### G.F2. Khái niệm nền tảng

#### [GB119] Bốn trường phái chính của Phật giáo Tây Tạng · L2
Nyingma (cổ mật, Padmasambhava, Đại viên mãn), Kagyu (truyền khẩu, Marpa – Milarepa, Đại thủ ấn, Karmapa), Sakya (gia tộc Khôn, đạo thứ Lamdré), Gelug (Tông-kha-pa, Lam-rim, Dalai Lama); phong trào Rimé ("vô thiên vị") thế kỷ 19; ghi chú tôn giáo Bön là truyền thống riêng biệt. Mỗi phái: đặc trưng tu học và nhân vật tiêu biểu.

#### [GB120] Thầy tâm linh — Lama, Guru và truyền thừa · L2
Vì sao Vajrayāna đặt truyền thừa và thầy ở vị trí trung tâm; quan hệ thầy – trò trong truyền thống; **phần bắt buộc:** ranh giới lành mạnh — dấu hiệu một lama/cộng đồng đáng tin và dấu hiệu cảnh báo (tham chiếu [M080] về yêu cầu truyền thừa). Viết trung lập, không tôn vinh hay bôi nhọ cá nhân cụ thể.

#### [GB121] Quán đảnh (Abhiṣeka) là gì · L2
Quán đảnh như nghi thức "trao quyền thực hành" một pháp môn — không phải phước lành thần bí mua được; các loại quán đảnh; vì sao một số thực hành yêu cầu quán đảnh trước. Trả lời các câu hỏi thường gặp ("tôi đi lễ được quán đắp không?").

#### [GB122] Chân ngôn, mạn-đà-la và bản tôn — nhìn cho hiểu · L2
Ba "phương tiện mật": chân ngôn (mantra — OM MANI PADME HÙM nghĩa gì), mạn-đà-la (bản đồ tâm thức và thế giới thanh tịnh), bản tôn (yidam — hình tượng giác ngộ để tự nhận). Trình bày như ngôn ngữ biểu tượng chứ không phải phép màu. Liên kết [M074], [M075].

#### [GB123] Con đường tu trong Kim cương thừa · L3
Bức tranh đường tu: các tư duy nền (thân người khó được, vô thường, nghiệp, khổ luân hồi) → tiền hành (ngöndro) → tu bản tôn → các giai đoạn sinh khởi/viên mãn → các pháp tối hậu (Đại thủ ấn, Đại viên mãn). Bài bản đồ phổ thông; chi tiết thực hành ở [M143], [M144], [M077]–[M079].

#### [GB124] Tulku — hệ thống tái sinh, Dalai Lama và Karmapa · L2
Tulku: vị thầy tái sinh được nhận diện lại tiếp tục đường tu; lịch sử hệ thống (từ Karmapa thế kỷ 13), Dalai Lama thứ nhất đến thứ 14, tục "golden urn" thời Thanh; các câu hỏi hiện đại về tulkus trẻ em. Trình bày cách các truyền thống tự hiểu và cách nghiên cứu học thuật mô tả.

#### [GB125] Cờ cầu nguyện, bánh xe kinh và đèn bơ · L1
"从 nhìn thấy đến hiểu": cờ kinh năm màu (nguyên lý gió mang câu chú), bánh xe kinh (quay = tụng), đèn bơ (ánh sáng trí tuệ), phù lục? không — ghi chú đúng các vật phẩm thật sự có; những gì du khách nên và không nên làm khi đến tu viện. Bài nhẹ, hình ảnh, đáp ứng tò mò phổ thông.

### G.F3. Kinh điển

#### [GB126] Kinh điển Tây Tạng — Kangyur và Tengyur · L3
Kangyur (lời Phật dịch sang Tạng, khoảng 100 tập) và Tengyur (chú giải, hơn 200 tập); các bản mộc in lịch sử (Narthang, Derge); thêm tạng tantrza riêng của phái Nyingma; dự án dịch 84000 ra tiếng Anh. Vị trí của tantra trong tạng kinh so với kinh Ba-la-mật.

### G.F4. Các nước và hiện tại

#### [GB127] Tây Tạng và cộng đồng lưu vong · L3
Từ unification thế kỷ 7 đến chế độ Dalai Lama, năm 1959 và dòng người di tản, việc tái lập học viện tại Ấn Độ (Dharamsala...), tình trạng tôn giáo trong và ngoài Tây Tạng hôm nay. **Viết trung lập** theo nguyên tắc biên tập: trình bày các nguồn bất đồng, tránh ngôn ngữ chính trị một chiều.

#### [GB128] Vajrayāna ở Bhutan, Mông Cổ, Nepal và nơi khác · L3
Bhutan (quốc giáo Drukpa Kagyu, Gross National Happiness), Mông Cổ (Gelug, giai đoạn Xô viết, hồi phục sau 1990), Nepal (Phật giáo Newar — dòng Vajrayāna Ấn Độ duy nhất còn sống tại chỗ), cộng đồng Buryat – Kalmykia – Tuva của Nga; Vajrayāna phương Tây.

### G.F5. Lễ hội Vajrayāna

> **Nguyên tắc chung:** lễ theo **lịch Tây Tạng** (chênh lệch khoảng 1–2 tháng so với âm lịch Việt — Trung tùy năm); mỗi bài phải ghi nguyên tắc quy đổi, không tự chuyển sang ngày dương lịch cố định.

#### [GB129] Lễ hội Vajrayāna  · L2

## G.G. SO SÁNH & ĐỊNH HƯỚNG

#### [GB134] So sánh ba truyền thống lớn — bảng đối chiếu · L2
Bảng so sánh tổng thể Theravāda / Mahāyāna / Vajrayāna: kinh điển và ngôn ngữ, lý tưởng (a-la-hán / bồ-tát / bồ-tát với phương tiện mật), phạm vi địa lý, hình thức thực hành tiêu biểu, lễ lớn nhất trong năm; kèm danh mục "điểm chung lớn" (tứ diệu đế, bát chánh đạo, luật, tăng đoàn, Niết-bàn). Kết luận: khác biệt là về phương tiện và nhấn mạnh, không phải về "đạo nào thật, đạo nào giả".

#### [GB135] Một đạo Phật, nhiều con đường — thái độ không tông phái · L2
Vì sao người học nên tôn trọng mọi truyền thống; các vị thầy hiện đại học qua nhiều dòng (phong trào Rimé; các thiền sư Việt Nam kết hợp Thiền – Tịnh); làm sao đọc một bài chê tông phái khác và giữ thái độ cân bằng; câu trả lời cho "tông nào đúng nhất?" — câu hỏi cần được chuyển thành "tông nào hợp với mình?". Liên kết nguyên tắc biên tập số 1 và 10.

## G.H. TRA CỨU & CÔNG CỤ

#### [GB137] Danh mục kinh điển thường gặp — từ Nikāya đến Tantra · R
Danh mục kinh điển ba truyền thống kèm gợi ý bản dịch tiếng Việt và độ khó: Nikāya (Pāli), kinh Đại thừa Hán dịch tiêu biểu, tantra chính; hướng dẫn trích dẫn (ví dụ "MN 10" nghĩa là gì). Dẫn từ [GB064], [GB092], [GB126].

#### [GB138] Danh mục tông phái, trường phái và truyền thừa · R
Tra cứu tên các bộ phái, tông phái, dòng truyền (từ Thuyết nhất thiết hữu bộ đến Nichiren): tên Pāli/Sanskrit/Hán, khu vực, tôn chỉ một dòng. Tránh người đọc nhầm lẫn giữa các "tông" và "phái".

#### [GB140] Câu hỏi thường gặp về Phật giáo · R
Tập hợp câu hỏi ngắn người mới hay hỏi: Phật tử có được uống rượu không; đi chùa lạy thế nào; Phật và Bồ-tát khác nhau ra sao; kinh nào nên đọc trước; tu tại gia có được không; thắp hương mấy nén; con số may mắn; sao hạn, cúng sao có phải Phật giáo không…
---

# LỘ TRÌNH HỌC

## Lộ trình chính (người mới, không chọn truyền thống)

> **Nguyên tắc:** Đây là trình tự gợi ý theo độ khó và phụ thuộc khái niệm, không phải thứ tự bắt buộc. Người dùng có thể nhảy đến bất kỳ bài nào qua tra cứu [GB141].

```text
Bước 0 — Định hướng                                       L1
GB001 → GB002 → GB003 → GB004 → GB013
GB005, GB007 = bài kỹ năng đọc, có thể đọc khi cần

Bước 1 — Cuộc đời Đức Phật và nguồn gốc                  L1–L2
GB015 → GB016 → GB017 → GB018 → GB019 → GB020 → GB021
Đào sâu khi muốn: GB014, GB022, GB023

Bước 2 — Lý thuyết nền tảng chung                        L1–L3
GB039 → GB040 → GB041 → GB042 → GB043 → GB044 → GB045 → GB046 → GB047
→ GB048 → GB050 → GB051 → GB052 → GB054 → GB055 → GB056 → GB057 → GB059
Đào sâu khi muốn: GB049, GB053, GB058, GB060, GB061

Bước 3 — Bản đồ ba truyền thống                          L2
GB027 → GB134 → chọn một truyền thống ở Bước 4

Bước 4 — Tìm hiểu một truyền thống                       L1–L4
├── Theravāda:  xem lộ trình Theravāda bên dưới
├── Mahāyāna:   xem lộ trình Mahāyāna bên dưới
└── Vajrayāna:  xem lộ trình Vajrayāna bên dưới

Bước 5 — Lịch sử lan truyền và bối cảnh                  L2–L3
GB024 → GB025 → GB026 → GB028 → GB029 → GB030
→ GB031 / GB032 / GB033 (chọn tuyến quan tâm) → GB034

Bước 6 — Bắt đầu thực hành
Chuyển sang phân mục Thiền (mã M) theo lộ trình của phân mục đó;
bài chuyển tiếp: [GB057], [GB068], [GB110]
```

## Lộ trình theo truyền thống — Theravāda

```text
GB062 → GB063 → GB064 → GB067 → GB068 → GB069 → GB070
→ (GB065, GB066 khi muốn đào sâu kinh điển)
→ một bài quốc gia: GB071 / GB072 / GB073 / GB074 / GB075
→ nhóm lễ hội: GB076 → GB077 → GB079 → GB080
```

## Lộ trình theo truyền thống — Mahāyāna

```text
GB083 → GB084 → GB085 → GB086 → GB091 → GB092 → GB093
→ (GB087 → GB089 → GB090 khi muốn đào sâu tư tưởng)
→ GB097 → chọn tông phái: GB098 / GB099 / GB100…
→ một bài quốc gia: GB105 / GB106 / GB107 (Việt Nam: GB035–GB038)
→ đời sống: GB108 → GB109 → GB110
→ nhóm lễ hội: GB111 → GB112 → GB114 → GB116
```

## Lộ trình theo truyền thống — Vajrayāna

```text
(đề nghị đọc trước GB083 – GB085 về Đại thừa)
GB117 → GB118 → GB119 → GB120 → GB121 → GB122 → GB123 → GB124
→ GB126 → một bài quốc gia: GB127 / GB128
→ nhóm lễ hội: GB129 → GB130 → GB131
```

## Lộ trình phụ — Người Việt Nam muốn hiểu đạo Phật quanh mình

```text
GB038 → GB035 → GB036 → GB037 → GB108 → GB110 → GB114 → GB116 → GB112 → GB075
```

## Lộ trình phụ — "Sắp đến lễ, tôi muốn hiểu lễ này"

```text
Đọc bài lễ cụ thể trong D5 / E7 / F5 → quay về bài nguồn
(Ví dụ: trước Vu Lan đọc [GB114] → [GB021], [GB053]; trước Vesak đọc [GB077] → [GB015].)
Công cụ: [GB139] lịch lễ hội ba truyền thống.
```

## Nguyên tắc lộ trình

1. **Các nhóm A–H là cấu trúc nội dung; trình tự học chỉ là gợi ý** và hiển thị dưới dạng "Bước tiếp theo" chứ không khóa bài.
2. **Lịch sử không đợi giáo lý, giáo lý không đợi lịch sử.** Người dùng có thể bắt đầu từ nhóm nào tùy hứng thú; app gợi ý bài nền khi phát hiện khái niệm chưa có.
3. **Bài lễ hội là cửa vào hợp pháp.** Nhiều người Việt đến với đạo Phật qua Vu Lan hay Phật đản; mỗi bài lễ phải tự đứng được và dẫn ngược về bài giáo lý tương ứng.
4. **Không có nội dung khóa theo thứ tự.** Mọi bài luôn tra cứu được qua [GB141].

# QUY TẮC DÙNG MÃ VÀ METADATA TRONG APP

## 1. Một bài, nhiều nhánh
Ví dụ bài về Phật giáo Việt Nam viết một lần ở B7 nhưng hiện ra ở E5:

```yaml
id: GB038
title: "Bản đồ Phật giáo Việt Nam hôm nay"
level: L2
traditions: [viet-nam, mahayana, theravada]   # bài nói về cả ba dòng tại VN
categories: [lich-su, viet-nam]
```

## 2. Bài chung và bài theo truyền thống là hai bài khác nhau

```text
[GB044] Bát chánh đạo — tổng quan            ← giáo lý chung (nhóm C)
[GB067] Con đường tu trong Theravāda          ← cách một truyền thống triển khai
[GB123] Con đường tu trong Kim cương thừa     ← cách truyền thống khác triển khai
```

## 3. Cùng tiêu đề = cùng khái niệm; cùng mã = cùng bài
Tạo mã mới cho bài mới, lấy số kế tiếp chưa dùng (hiện tại: **GB142** trở đi). Mã gỡ bỏ phải ghi vào danh sách nghỉ hưu, không dùng lại.

## 4. Truyền thống và lễ hội là metadata, không phải taxonomy duy nhất

```yaml
id: GB077
title: "Vesak — Phật đản, Thành đạo và Nhập diệt trong một ngày"
level: L1
traditions: [theravada]
categories: [le-hoi, theravada]
calendar: theravada-lunar      # lunar | theravada-lunar | tibetan-lunar | solar
date: "rằm tháng Vesākha (khoảng tháng 5–6 dương lịch, tính theo năm)"
requires: [GB062]
related:  [GB112, GB131, GB139]
sources:  ["Truyền thống Sri Lanka / Thái Lan; Nghị quyết LHQ về Ngày Vesak"]
```

Nhờ vậy app có thể: duyệt theo **truyền thống**, theo **chủ đề** (lịch sử / giáo lý / lễ hội), theo **cấp độ**; và quan trọng nhất với nhóm lễ hội — **tính ngày dương lịch theo năm** và gửi nhắc lịch.

## 5. Các trường bắt buộc
- `level` — dựng lộ trình và giúp người dùng biết bài có hợp với mình không.
- `calendar` — với mọi bài thuộc nhóm lễ hội (D5/E7/F5); không được quy đổi sang ngày dương lịch cố định trong nội dung bài.
- `terms` — để bật tra thuật ngữ ngay trong bài (chung dữ liệu với phân mục Thiền).

---

# NGUYÊN TẮC BIÊN TẬP

1. **Không dùng taxonomy để xếp hạng truyền thống.** "Nâng cao" nghĩa là cần nhiều kiến thức nền hơn, không phải "truyền thống A cao hơn truyền thống B". Cấm các công thức "Theravāda是小乘".
2. **Phân biệt Pāli và Sanskrit, ghi kèm Hán–Việt**; với tên riêng Đông Á và Tây Tạng giữ nguyên văn kèm giải nghĩa (*niànfó*, *Losar*, *tulku*). Viết đúng dấu phụ; có phương án dự phòng thống nhất nếu hệ thống hiển thị không hỗ trợ.
3. **Phân tầng nguồn: kinh điển → chú giải → luận → nghiên cứu hiện đại → tập quán dân gian.** Nhiều nội dung "Phật giáo" mà người Việt quen thuộc (ngày vía, cúng sao, cài hoa Vu Lan) thuộc tầng tập quán — ghi rõ nguồn gốc thay vì gán "kinh dạy".
4. **Ghi phạm vi truyền thống trong bài.** Chỉ gắn nhãn truyền thống khi nội dung thực sự đặc thù; giáo lý chung thì không gắn cả ba nhãn "vì đâu cũng có".
5. **Nhóm C chỉ chứa giáo lý chung.** Nếu một điểm giáo lý được các truyền thống giải thích khác nhau (Niết-bàn, tái sinh trung hữu, tiến trình chứng ngộ), trình bày bản phổ quát ở C và các bản riêng ở D/E/F.
6. **Bài lễ hội phải đủ ba lớp: ý nghĩa giáo lý gốc — tập quán từng vùng — cách tính ngày theo hệ lịch tương ứng.** Không biến bài lễ thành hướng dẫn cúng bái cầu lợi; giải thích nghi thức theo tinh thần giáo lý.
7. **Lịch sử ghi độ chắc chắn của thông tin.** Niên đại Đức Phật, chi tiết các lần kết tập, Phật giáo Việt Nam sơ kỳ… đều có nhiều phương án; trình bày các phương án chính và ghi nguồn, thay vì chọn một rồi trình bày như sự thật duy nhất.
8. **Không khẳng định hay phủ nhận giáo điều siêu hình một cách tự ý.** Với các nội dung như cõi giới, tái sinh, phước bội phần: trình bày "các truyền thống hiểu như thế nào", kèm góc nhìn học thuật khi có.
9. **Dễ hiểu là yêu cầu cốt lõi.** Mỗi khái niệm khó phải có ít nhất một ví dụ đời thường hoặc hình ảnh minh họa; ưu tiên bảng, dòng thời gian, sơ đồ; câu văn ngắn. L1 phải đọc được bởi học sinh trung học.
10. **Giọng văn trung lập và tôn trọng** — giữa các tông phái, giữa Phật giáo với các tôn giáo khác, và với các vấn đề nhạy cảm lịch sử — chính trị (ví dụ [GB127]): trình bày các nguồn bất đồng, không dùng ngôn ngữ phe phái.

---

# BẢNG THUẬT NGỮ ĐỐI CHIẾU (khởi đầu cho [GB136])

| Pāli | Sanskrit | Hán–Việt | Tiếng Việt thường dùng | English |
|------|----------|----------|------------------------|---------|
| buddha | buddha | Phật | Đức Phật, bậc giác ngộ | Buddha / awakened one |
| dhamma | dharma | Pháp | giáo pháp | Dhamma / Dharma |
| saṅgha | saṃgha | Tăng-già | tăng đoàn, cộng đồng tu học | Sangha |
| tissaraṇa | triśaraṇa | tam quy | quy y tam bảo | three refuges |
| sīla | śīla | giới | giới đức, quy tắc rèn luyện | virtue / precepts |
| pañcasīla | pañcaśīla | ngũ giới | năm giới | five precepts |
| dukkha | duḥkha | khổ | khổ, bất toại nguyện | suffering |
| ariyasacca | āryasatya | thánh đế | tứ diệu đế | Noble Truth |
| magga | mārga | đạo | con đường, bát chánh đạo | path |
| paṭiccasamuppāda | pratītyasamutpāda | duyên khởi | nhân duyên sinh | dependent origination |
| kamma | karma | nghiệp | nghiệp, nhân quả | karma / action |
| saṃsāra | saṃsāra | luân hồi | vòng sinh tử | cyclic existence |
| puñña | puṇya | phước | công đức, phước báu | merit |
| nibbāna | nirvāṇa | niết-bàn | niết-bàn | nirvana |
| parinibbāna | parinirvāṇa | bát-niết-bàn | nhập diệt | final nirvana |
| arahant | arhat | a-la-hán | bậc la-hán | arhat |
| sotāpanna | srotāpanna | tu-đà-hoàn | nhập lưu | stream-enterer |
| bodhisatta | bodhisattva | bồ-tát | bồ-tát | bodhisattva |
| — | bodhicitta | bồ-đề tâm | tâm bồ-đề | awakening mind |
| pāramī | pāramitā | ba-la-mật | độ, hoàn thiện | perfection |
| suññatā | śūnyatā | (tánh) không | tánh Không | emptiness |
| — | tathāgatagarbha | như lai tạng | Phật tánh | buddha-nature |
| — | trikāya | tam thân | ba thân Phật | three bodies |
| paññā | prajñā | tuệ | trí tuệ | wisdom |
| khandha | skandha | uẩn | năm uẩn | aggregate |
| anicca | anitya | vô thường | vô thường | impermanence |
| anattā | anātman | vô ngã | vô ngã | non-self |
| taṇhā | tṛṣṇā | ái | tham ái | craving |
| mettā | maitrī | từ | từ ái | loving-kindness |
| karuṇā | karuṇā | bi | lòng bi | compassion |
| brahmavihāra | brahmavihāra | tứ phạm trú | tứ vô lượng tâm | divine abodes |
| tipiṭaka | tripiṭaka | tam tạng | ba tạng kinh điển | Triple Basket |
| vinaya | vinaya | luật (tạng) | luật xuất gia | monastic discipline |
| sutta | sūtra | kinh | kinh | discourse / sutra |
| abhidhamma | abhidharma | a-tỳ-đàm, luận | đối pháp | higher teaching |
| nikāya | āgama | bộ (kinh), a-hàm | bộ kinh | collection |
| uposatha | upoṣadha | bố-tát | ngày trai giới | observance day |
| vassa | varṣā | an cư | mùa an cư kiết hạ | rains retreat |
| — | kaṭhina | ca-thi-na | lễ dâng y | robe-offering ceremony |
| — | vesākha (tháng) | — | tháng Phật đản | Vesak month |
| — | pūjā | cúng dường | lễ cúng, nghi quyến | devotional ritual |
| — | gāthā | kệ | bài kệ | verse |
| — | stūpa | tháp | bảo tháp, tháp xá-lợi | stupa |
| — | mantra | chân ngôn | câu chú | mantra |
| — | maṇḍala | mạn-đà-la | đồ hình | mandala |
| — | tantra | tục (kinh Mật) | tantra, kinh Mật | tantra |
| — | vajra | kim cương | kim cương | vajra / diamond |
| — | guru (Tib. lama) | sư, lama | thầy tâm linh | teacher / lama |
| — | abhiṣeka | quán đảnh | quán đảnh | empowerment |
| — | tulku (Tib.) | hóa thân | vị tái sinh | incarnate lama |
| dhyāna → chán 禪 | dhyāna | Thiền | Thiền tông | Chan / Zen |
| — | niànfó 念佛 | niệm Phật | niệm Phật | buddha-recitation |
| — | sthaviravāda | Thượng tọa bộ | Nam tông, đạo Nam | Way of the Elders |
| — | mahāyāna | Đại thừa | Bắc tông, đạo Bắc | Great Vehicle |
| — | vajrayāna | Kim cương thừa | Mật tông, Mật giáo | Diamond / Vajra Vehicle |

> **Ghi chú:** từ "Hīnayāna (Tiểu thừa)" xuất hiện trong một số văn bản Đại thừa; ngày nay **không dùng** như tên gọi một truyền thống trong app vì hàm ý đánh giá; khi cần nói đến các bộ phái sơ kỳ dùng "Phật giáo bộ phái" hoặc "Theravāda" khi chỉ đúng dòng này.

---

# NGUỒN THAM KHẢO GỢI Ý CHO NGƯỜI VIẾT BÀI

## Kinh điển và bản dịch tiếng Việt
- Kinh tạng Pāli bản dịch HT. Thích Minh Châu (Trường bộ, Trung bộ) — nền cho nhóm C, D.
- Tâm kinh, Kim cang, Pháp Hoa — các bản dịch và giải nghĩa của HT. Thích Trí Quang — nền cho [GB093], [GB094].
- Suttacentral (suttacentral.net) — đối chiếu kinh Pāli với A-hàm Hán dịch.
- 84000 (84000.co) — kinh tạng Tây Tạng đang dịch Anh ngữ — nền cho [GB126].

## Lịch sử và nghiên cứu
- Peter Harvey, *An Introduction to Buddhism* — giáo trình cân bằng cho nhóm B, C.
- Andrew Skilton, *A Concise History of Buddhism* — dòng lịch sử các trường phái cho B4–B5.
- Nguyễn Lang, *Việt Nam Phật giáo sử luận* — nền cho B7.
- *Thiền uyển tập anh* (kèm nghiên cứu hiện đại) — B7 và [M146].
- Heinz Bechert & Richard Gombrich (chủ biên), *The World of Buddhism* — bản đồ các truyền thống.

## Lễ hội và văn hóa
- Tài liệu các tổ chức Phật giáo quốc gia (Sri Lanka, Thái Lan, Tây Tạng lưu vong) về lịch lễ theo năm — nền cho D5, F5; luôn đối chiếu ít nhất hai nguồn vì ngày lễ tính theo trăng/trăng Tây Tạng.
- Nghiên cứu văn hóa dân gian Việt Nam về Vu Lan, ngày vía, Tết Nguyên tiêu — dùng kèm nguyên tắc phân tầng nguồn (tập quán ≠ kinh điển).

## Tra cứu
- Nyanatiloka Mahāthera, *Buddhist Dictionary* — thuật ngữ Pāli.
- 佛光大辭典 (Từ điển Phật học Quang Đài / Fo Guang Dictionary) — thuật ngữ Hán – Việt.
- CBETA (cbeta.org) — đại tạng Hán văn khi cần trích dẫn kinh Đại thừa.

> **Lưu ý:** kiểm tra lại nguồn trước khi xuất bản; ưu tiên nguồn gốc (kinh, luận, trang của tổ chức truyền thống) thay vì trang tổng hợp; các chi tiết lịch sử Việt Nam ở [GB035], [GB075] cần đối chiếu tư liệu trong nước trước khi viết.

---

# GHI CHÚ PHIÊN BẢN v1.0

## Tư tưởng cấu trúc
- Trục chính theo yêu cầu: **lịch sử (B) → lý thuyết nền chung (C) → ba truyền thống từ cơ bản đến nâng cao (D/E/F), mỗi truyền thống có nhóm lễ hội riêng (D5, E7, F5)**; A làm lớp nhập môn, G so sánh, H tra cứu.
- Mã `GBxxx` tách hẳn khỏi mã `Mxxx` của phân mục Thiền để hai phân mục liên kết chéo mà không xung đột ID.
- Nhóm C được định nghĩa nghiêm ngặt là "giáo lý chung cả ba truyền thống"; mọi điểm khác biệt nằm ở D/E/F và tổng hợp tại [GB134].
- Phật giáo Việt Nam viết một lần ở B7 và gắn metadata để hiện diện ở E5/D4 — theo nguyên tắc "một bài, nhiều nhánh".

## Đề xuất cho vòng sau
1. **Ưu tiên viết trước ~30 bài L1**: A1–A3, [GB015]–[GB016], C1–C2, [GB050], [GB058], [GB062], [GB083], [GB085], nhóm lễ hội lớn ([GB077], [GB112], [GB114]) — đủ cho một lộ trình hoàn chỉnh của người mới.
2. **[GB139] lịch lễ hội cần dựng thành dữ liệu có cấu trúc theo năm** (ba hệ lịch) trước khi viết bài tĩnh; đây là tính năng "nhắc lễ" tự nhiên của app.
3. Mời ít nhất một vị tăng/ni hoặc giáo thọ của **mỗi truyền thống** đọc soát nhóm D, E, F và các bài lễ hội trước khi xuất bản.
4. Cân nhắc vòng sau thêm nhóm "Phật giáo và các vấn đề hiện đại" (Phật giáo với khoa học, môi trường, tâm lý học) — đã cố tình để ngoài phạm vi v1.0.

## Thống kê bản v1.0
- Tổng số bài: **141** (GB001–GB141; chưa có mã nghỉ hưu).
- Mã kế tiếp khi thêm bài mới: **GB142**.
- Phân bố cấp độ: L1 ≈ 27 · L2 ≈ 73 · L3 ≈ 32 · L4 = 3 · L5 = 0 (dành cho phân mục Thiền) · R = 6.
- Nhóm lễ hội: Theravāda 7 bài (D5) · Đại thừa/Đông Á 6 bài (E7) · Vajrayāna 5 bài (F5), cộng công cụ lịch [GB139].
- Taxonomy cấp cao: **7 nhóm** (A–H, không dùng nhóm riêng cho "so sánh" tách khỏi G — hiện G gộp so sánh & định hướng).
