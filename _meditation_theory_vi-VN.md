# Meditation Theory — Taxonomy & danh mục bài viết (vi-VN)

**Phiên bản:** 3.6 · **Cập nhật:** 2026-09-22 · **Trạng thái:** khung nội dung cho phần "Thiền" trong app

> **Mục đích:** Mỗi mã `Mxxx` tương ứng với **một bài viết độc lập**. Cùng một mã có thể xuất hiện ở nhiều nhánh taxonomy; khi đó app chỉ lưu bài một lần và gắn nhiều category/tag.
>
> **Nguyên tắc 1 — Lộ trình, không xếp hạng.** "Cơ bản → chuyên sâu" là **lộ trình học kỹ năng**, không phải bảng xếp hạng giữa các truyền thống. Theravāda, Mahāyāna và Vajrayāna có nhiều điểm giao nhau; cùng một phương pháp có thể tồn tại trong nhiều truyền thống nhưng được giải thích và thực hành khác nhau.
>
> **Nguyên tắc 2 — Mã là vĩnh viễn.** Mã `Mxxx` là **ID ổn định**, không đánh số lại khi thêm/bớt bài. Vì vậy thứ tự mã trong cây **không** trùng thứ tự học; thứ tự học nằm ở phần *Lộ trình*. Mã đã gỡ bỏ thì **nghỉ hưu**, không tái sử dụng cho bài khác.
>
> **Nguyên tắc 3 — Cùng bài thì cùng mã.** Nếu hai mục thực sự là cùng một bài, dùng cùng mã và cùng tiêu đề. Nếu chỉ cùng tên nhưng nội dung/truyền thống cần giải thích khác nhau, tạo mã riêng và ghi rõ truyền thống trong tiêu đề.
>
> **Nguyên tắc 4 — Thuật ngữ.** Ưu tiên **Pāli** cho nội dung Theravāda/kinh tạng Nikāya, **Sanskrit** cho nội dung Mahāyāna/Vajrayāna, và luôn kèm **Hán–Việt** khi người Việt quen dùng dạng đó (ví dụ: *satipaṭṭhāna* = tứ niệm xứ). Xem bảng đối chiếu ở cuối file.

## Quy ước cấp độ (level)

| Mã | Tên | Ý nghĩa |
|----|-----|---------|
| **L1** | Nhập môn | Người chưa từng Thiền đọc/làm được ngay |
| **L2** | Nền tảng | Kỹ năng cốt lõi, cần thực hành lặp lại |
| **L3** | Trung cấp | Cần đã ổn định được một đề mục và hiểu khung lý thuyết |
| **L4** | Chuyên sâu | Nội dung kinh–luận, tiến trình tuệ, hệ thống truyền thống |
| **L5** | Cần điều kiện | Thực hành đòi hỏi thầy hướng dẫn / truyền thừa / quán đảnh; app chỉ trình bày ở mức **giáo dục, tổng quan** |
| **R** | Tra cứu | Bài tham khảo, bảng thuật ngữ, FAQ — không nằm trong lộ trình tuyến tính |

---

# QUY ƯỚC BẢN CHẤT TAXONOMY

Taxonomy v3.5 dùng các loại cấp cao khác nhau, thay vì coi tất cả nhánh là "phái Thiền" ngang hàng:

| Nhóm | Bản chất | Chức năng trong app |
|---|---|---|
| **A** | `foundation` — kiến thức nền | Giải thích khái niệm, bối cảnh, cách bắt đầu và an toàn |
| **B** | `skill` — kỹ năng | Kỹ năng thực hành dùng xuyên nhiều phương pháp |
| **C** | `method` — phương thức / hướng tu tập | C1 Thiền chỉ (Samatha) và C2 Thiền tuệ / minh sát (Vipassanā) — cùng là hai phương thức, được chia tiếp thành các nhóm học tập theo trình tự |
| **D** | nhiều subtype: `framework` / `practice_group` / `object_taxonomy` | D1 là khung thực hành; D2 là nhóm pháp hành; D3 là hệ thống phân loại đề mục. Các nhánh này có cấu trúc cha–con và có thể liên kết chéo |
| **E** | `tradition` — truyền thống / dòng Thiền | Theravāda, Mahāyāna, Vajrayāna và các hệ thống bên trong |
| **F** | `regional_tradition_context` — bối cảnh văn hóa / địa vực | Các cách thực hành trong Phật giáo Việt Nam |
| **G** | `application_context` / `secular_context` — ứng dụng / bối cảnh / mục tiêu | Đời sống, sức khỏe và Thiền thế tục |

**Lưu ý:** Cùng một bài có thể có nhiều thuộc tính. `methods`, `traditions`, `objects`, `goals`, `duration`, `requires`, `safety` và `sources` là các chiều dữ liệu riêng, không phải các cấp con của một taxonomy duy nhất.

# TAXONOMY TREE

> **Cấu trúc taxonomy v3.5:** Các nhánh cấp cao không được coi là những "loại Thiền" ngang hàng. Chúng được phân theo **bản chất thông tin**: kiến thức nền, kỹ năng, phương thức tu tập, khung/nhóm/hệ thống pháp hành, truyền thống, bối cảnh văn hóa và ứng dụng. Trong mỗi nhánh, các mục được phân cấp theo quan hệ **tổng quan → nhóm → thực hành/chủ đề chi tiết** khi cấu trúc nội dung yêu cầu. Một bài có thể xuất hiện ở nhiều nhánh; các trường `traditions`, `methods`, `objects`, `goals` và các trường metadata khác mô tả những chiều phân loại riêng.

```text
Thiền
│
├── M.A. KIẾN THỨC NỀN & ĐỊNH HƯỚNG
│   ├── M.A1. Hiểu về Thiền
│   │   ├── [M001] Thiền là gì? · L1
│   │   ├── [M002] Thiền Phật giáo và Thiền thế tục · L1
│   │   └── [M095] Thiền trong Tam học — Giới, Định, Tuệ · L1
│   ├── M.A2. Hiểu cách hành Thiền
│   │   ├── [M096] Chánh niệm và tỉnh giác (Sati và sampajañña) · L1
│   │   ├── [M097] Đọc thuật ngữ Thiền: Pāli, Sanskrit và Hán–Việt · L1
│   │   └── [M098] Những hiểu lầm phổ biến về Thiền · L1
│   ├── M.A3. An toàn khi hành Thiền
│   │   └── [M099] An toàn khi hành Thiền — khi nào cần điều chỉnh hoặc dừng · L1
│   ├── M.A4. Chuẩn bị một buổi Thiền
│   │   ├── [M003] Chuẩn bị trước khi Thiền · L1
│   │   ├── [M004] Tư thế Thiền · L1
│   │   └── [M005] Thời lượng và tần suất thực hành · L1
│   ├── M.A5. Trong và sau một buổi Thiền
│   │   ├── [M006] Xử lý xao lãng, buồn ngủ và bồn chồn · L1
│   │   └── [M007] Cách kết thúc một buổi Thiền · L1
│   ├── M.A6. Xây dựng thói quen
│   │   └── [M008] Xây dựng thói quen Thiền · L1
│   └── M.A7. Hỗ trợ và thực hành chuyên sâu hơn
│       ├── [M100] Thiện hữu và thầy hướng dẫn (Kalyāṇamitta) · L2
│       └── [M101] Khóa tu và thực hành tập trung dài ngày · L3
│
├── M.B. KỸ NĂNG THỰC HÀNH CHUNG
│   ├── M.B1. Nền tảng thân và hơi thở
│   │   ├── [M009] Thả lỏng cơ thể · L1
│   │   ├── [M010] Nhận biết hơi thở tự nhiên · L1
│   │   └── [M011] Đếm hơi thở · L1
│   ├── M.B2. Ổn định và duy trì chú ý
│   │   ├── [M012] Theo dõi cảm giác của hơi thở · L2
│   │   └── [M013] Neo tâm vào một đối tượng · L2
│   ├── M.B3. Làm việc với xao lãng và thái độ thực hành
│   │   ├── [M014] Nhận biết suy nghĩ và xao lãng · L2
│   │   └── [M105] Thái độ hành Thiền: tinh tấn đúng mức, không ép, không buông · L2
│   ├── M.B4. Quan sát và định hướng kinh nghiệm
│   │   ├── [M102] Ghi nhận / niệm thầm · L2
│   │   └── [M103] Như lý tác ý · L2
│   ├── M.B5. Cân bằng các yếu tố thực hành
│   │   └── [M104] Cân bằng năm căn · L3
│   ├── M.B6. Tích hợp vào chuyển động và đời sống
│   │   ├── [M015] Thiền đi (Caṅkama) · L1
│   │   └── [M016] Chánh niệm trong sinh hoạt hằng ngày · L1
│   ├── M.B7. Theo dõi và phản tư thực hành
│   │   └── [M106] Nhật ký Thiền và cách nhận biết tiến bộ · L2
│   └── M.B8. Câu hỏi thường gặp về Thiền
│       └── [M162] Câu hỏi thường gặp về Thiền · R
│
├── M.C. PHƯƠNG THỨC / HƯỚNG TU TẬP
│   ├── M.C1. Thiền chỉ (Samatha / Śamatha)
│   │   ├── M.C1.1. Nền tảng Thiền chỉ và định tâm
│   │   │   ├── [M017] Thiền chỉ (Samatha / Śamatha) · L2
│   │   │   └── [M022] Định tâm và tính liên tục của chú ý · L2
│   │   ├── M.C1.2. Các đề mục thực hành phổ biến
│   │   │   ├── [M018] Thiền chỉ với hơi thở · L2
│   │   │   ├── [M019] Thiền chỉ với cảm giác cơ thể · L2
│   │   │   ├── [M020] Thiền chỉ với âm thanh · L2
│   │   │   └── [M021] Thiền chỉ với hình ảnh / vật thể · L2
│   │   ├── M.C1.3. Trở ngại và tướng Thiền
│   │   │   ├── [M109] Năm triền cái · L2
│   │   │   └── [M108] Tướng Thiền và các giai đoạn của tướng (Nimitta) · L3
│   │   ├── M.C1.4. Các mức định và hấp thụ
│   │   │   ├── [M107] Ba mức định · L3
│   │   │   ├── [M023] Định sâu và Thiền-na (Jhāna / Dhyāna) — Tổng quan · L3
│   │   │   ├── [M110] Bốn Thiền sắc giới và năm Thiền chi · L4
│   │   │   └── [M111] Bốn xứ vô sắc · L4
│   │   └── M.C1.5. Phối hợp định và tuệ
│   │       └── [M112] Phối hợp định và tuệ · L4
│   │
│   └── M.C2. Thiền tuệ / minh sát (Vipassanā / Vipaśyanā)
│       ├── M.C2.1. Nền tảng Thiền tuệ
│       │   └── [M024] Thiền tuệ / minh sát (Vipassanā / Vipaśyanā) · L2
│       ├── M.C2.2. Quan sát trực tiếp kinh nghiệm
│       │   ├── [M029] Quan sát phản ứng của tâm · L2
│       │   ├── [M030] Trải nghiệm trực tiếp và câu chuyện của tâm · L2
│       │   ├── [M031] Chánh niệm với suy nghĩ · L2
│       │   └── [M032] Chánh niệm với cảm xúc mạnh · L3
│       ├── M.C2.3. Quan sát sinh–diệt và ba đặc tính
│       │   ├── [M025] Quan sát sinh–diệt · L3
│       │   ├── [M053] Ba đặc tính (Tilakkhaṇa) — tổng quan · L2
│       │   ├── [M026] Quán vô thường (Anicca) · L2
│       │   ├── [M027] Quán khổ / bất toại nguyện (Dukkha) · L3
│       │   └── [M028] Quán vô ngã (Anattā / Anātman) · L3
│       ├── M.C2.4. Các khung phân tích sâu hơn
│       │   ├── [M120] Phân biệt danh và sắc (Nāma-rūpa) · L3
│       │   └── [M121] Duyên khởi trong quan sát thực tế · L4
│       ├── M.C2.5. Tiến trình tuệ
│       │   ├── [M122] Tiến trình tuệ: bảy thanh tịnh và mười sáu tuệ — tổng quan · L4
│       │   └── [M123] Mười tùy phiền não của minh sát (Vipassanupakkilesa) · L4
│       └── M.C2.6. Khó khăn và an toàn
│           └── [M124] Giai đoạn khó khăn trong Thiền tuệ và cách ứng phó an toàn · L4
│
├── M.D. KHUNG / NHÓM / HỆ THỐNG PHÁP HÀNH
│   ├── M.D1. Khung Bốn niệm xứ (Satipaṭṭhāna / Smṛtyupasthāna)
│   │   ├── M.D1.0. Bốn niệm xứ (Kāyānupassanā)
│   │   │   ├── [M033] Bốn niệm xứ (Satipaṭṭhāna / Smṛtyupasthāna) — Tổng quan · L2
│   │   ├── M.D1.1. Quán thân (Kāyānupassanā)
│   │   │   ├── [M034] Quán thân (Kāyānupassanā) · L2
│   │   │   ├── [M035] Quán hơi thở trong Bốn niệm xứ (Satipaṭṭhāna) · L2
│   │   │   ├── [M113] Niệm hơi thở — 16 bước và bốn nhóm bốn (Ānāpānassati) · L4
│   │   │   ├── [M036] Quán tư thế và chuyển động (Iriyāpatha) · L2
│   │   │   └── [M114] Thân hành niệm (Kāyagatāsati) · L3
│   │   ├── M.D1.2. Quán thọ (Vedanānupassanā)
│   │   │   └── [M037] Quán cảm thọ (Vedanānupassanā) · L2
│   │   ├── M.D1.3. Quán tâm (Cittānupassanā)
│   │   │   └── [M038] Quán tâm (Cittānupassanā) · L3
│   │   ├── M.D1.4. Quán pháp (Dhammānupassanā)
│   │   │   ├── [M039] Quán pháp (Dhammānupassanā) · L3
│   │   │   ├── [M109] Năm triền cái · L2
│   │   │   ├── [M116] Quán pháp: Năm uẩn · L3
│   │   │   ├── [M117] Quán pháp: Sáu nội–ngoại xứ · L3
│   │   │   ├── [M118] Quán pháp: Bảy giác chi · L3
│   │   │   └── [M119] Quán pháp: Bốn thánh đế · L3
│   │   └── [M040] Bốn niệm xứ từ cơ bản đến chuyên sâu (Satipaṭṭhāna) · L3
│   │
│   ├── M.D2. Nhóm Tứ vô lượng tâm (Brahmavihāra)
│   │   ├── [M041] Tứ vô lượng tâm (Brahmavihāra) — Tổng quan · L2
│   │   ├── M.D2.1. Từ ái (Mettā / Maitrī)
│   │   │   ├── [M042] Từ ái (Mettā / Maitrī) · L1
│   │   │   └── [M125] Tu tập tâm từ — trình tự đối tượng (Mettā bhāvanā) · L2
│   │   ├── M.D2.2. Bi (Karuṇā)
│   │   │   └── [M043] Bi (Karuṇā) · L2
│   │   ├── M.D2.3. Tùy hỷ (Muditā)
│   │   │   └── [M044] Tùy hỷ (Muditā) · L2
│   │   ├── M.D2.4. Xả (Upekkhā / Upekṣā)
│   │   │   └── [M045] Xả (Upekkhā / Upekṣā) · L3
│   │   └── M.D2.5. Tổng hợp và phân tích chung
│   │       ├── [M046] Bốn vô lượng tâm như một hệ thống · L3
│   │       └── [M126] Kẻ thù gần và kẻ thù xa của bốn phẩm chất · L3
│   │
│   │   > **Quan hệ với D3:** Trong hệ thống 40 đề mục theo Visuddhimagga, bốn vô lượng tâm (Brahmavihāra) là một nhóm nằm trong Kammaṭṭhāna. D2 tồn tại như một nhánh chuyên đề độc lập để người dùng học riêng về Từ–Bi–Hỷ–Xả; không có nghĩa D2 và D3 là hai hệ thống hoàn toàn tách biệt.
│   │
│   └── M.D3. Hệ thống đề mục Thiền (Kammaṭṭhāna)
│       ├── M.D3.1. Tổng quan, phân loại và lựa chọn
│       │   ├── [M127] Bốn mươi đề mục Thiền (Kammaṭṭhāna) — tổng quan theo Visuddhimagga · L3
│       │   ├── [M128] Tính khí — sáu loại và cách chọn đề mục (Carita) · L3
│       │   └── [M054] Chọn đề mục phù hợp với mình · L2
│       ├── M.D3.2. Biến xứ (Kasiṇa)
│       │   └── [M060] Biến xứ — mười biến xứ (Kasiṇa) · L4
│       ├── M.D3.3. Quán bất tịnh (Asubha)
│       │   └── [M047] Quán bất tịnh (Asubha) · L4
│       ├── M.D3.4. Đề mục quán thân liên quan
│       │   └── [M048] 32 thể trược (Dvattiṃsākāra) · L4
│       ├── M.D3.5. Quán bốn đại (Catudhātuvavatthāna)
│       │   └── [M129] Quán bốn đại (Catudhātuvavatthāna) · L4
│       ├── M.D3.6. Quán vật thực (Āhāre paṭikūlasaññā)
│       │   └── [M130] Quán vật thực (Āhāre paṭikūlasaññā) · L4
│       ├── M.D3.7. Tùy niệm (Anussati)
│       │   ├── [M131] Mười tùy niệm (Dasa anussati) — tổng quan · L3
│       │   ├── M.D3.7.1. Niệm Phật (Buddhānussati / Buddhānusmṛti)
│       │   │   └── [M050] Niệm Phật (Buddhānussati / Buddhānusmṛti) · L2
│       │   ├── M.D3.7.2. Niệm Pháp (Dhammānussati / Dharmānusmṛti)
│       │   │   └── [M051] Niệm Pháp (Dhammānussati / Dharmānusmṛti) · L2
│       │   ├── M.D3.7.3. Niệm Tăng (Saṅghānussati / Saṃghānusmṛti)
│       │   │   └── [M052] Niệm Tăng (Saṅghānussati / Saṃghānusmṛti) · L2
│       │   ├── M.D3.7.4. Niệm giới, niệm thí, niệm thiên
│       │   │   └── [M132] Niệm giới, niệm thí, niệm thiên · L3
│       │   ├── M.D3.7.5. Niệm sự chết (Maraṇassati / Maraṇasmṛti)
│       │   │   └── [M049] Niệm sự chết (Maraṇassati / Maraṇasmṛti) · L3
│       │   └── M.D3.7.6. Niệm tịch tịnh (Upasamānussati)
│       │       └── [M133] Niệm tịch tịnh (Upasamānussati) · L4
│       └── M.D3.8. Liên kết chéo
│           ├── Tứ vô lượng tâm (Brahmavihāra) → xem D2
│           └── Bốn xứ vô sắc → xem [M111] trong C1. Thiền chỉ (Samatha / Śamatha)
│
├── M.E. TRUYỀN THỐNG / DÒNG Thiền
│   ├── M.E1. Truyền thống Theravāda
│   │   ├── M.E1.1. Tổng quan truyền thống
│   │   │   └── [M055] Thượng tọa bộ (Theravāda) — Bản đồ các hệ thống Thiền · L3
│   │   ├── M.E1.2. Các khung và phương thức thực hành cốt lõi
│   │   │   ├── [M056] Niệm hơi thở (Ānāpānassati) trong Thượng tọa bộ (Theravāda) · L3
│   │   │   ├── [M057] Bốn niệm xứ (Satipaṭṭhāna) — Cách tiếp cận Thượng tọa bộ (Theravāda) · L3
│   │   │   └── [M058] Thiền chỉ và Thiền tuệ (Samatha–Vipassanā) trong Thượng tọa bộ (Theravāda) · L3
│   │   ├── M.E1.3. Các hệ thống Thiền hiện đại và dòng truyền thừa
│   │   │   ├── [M059] Thiền tuệ / minh sát hiện đại (Vipassanā) — Các cách tiếp cận khác nhau · L3
│   │   │   ├── [M135] Các hệ thống Thiền Miến Điện · L4
│   │   │   └── [M136] Truyền thống Rừng Thái Lan và các cách trình bày hiện đại · L4
│   │   └── M.E1.4. Kinh điển và hệ chú giải
│   │       └── [M134] Visuddhimagga và hệ chú giải — bản đồ văn bản · L4
│   ├── M.E2. Truyền thống Đại thừa (Mahāyāna)
│   │   ├── M.E2.1. Tổng quan Đại thừa và khung Chỉ–Quán
│   │   │   ├── [M061] Đại thừa (Mahāyāna) — Bản đồ các hệ thống Thiền · L3
│   │   │   ├── [M062] Thiền chỉ và Thiền quán (Śamatha–Vipaśyanā) trong Đại thừa (Mahāyāna) · L3
│   │   │   └── M.E2.1.1. Chỉ–Quán (Zhǐguān)
│   │   │       ├── [M063] Chỉ–Quán (Zhǐguān) — Tổng quan · L3
│   │   │       └── [M137] Ma-ha Chỉ Quán và Thiền Thiên Thai tông · L4
│   │   ├── M.E2.2. Thiền tông (Zen / Chan): nhập môn và thực hành
│   │   │   ├── [M064] Thiền tông (Zen / Chan) — Tổng quan thực hành · L3
│   │   │   └── [M065] Ngồi Thiền trong Thiền tông (Zazen) · L3
│   │   ├── M.E2.3. Niệm Phật và Tịnh độ
│   │   │   ├── [M068] Niệm Phật (Niànfó / Nembutsu) — Tổng quan · L2
│   │   │   └── [M069] Quán tưởng Phật và Tịnh độ · L3
│   │   ├── M.E2.4. Kết hợp Thiền–Tịnh
│   │   │   └── [M141] Thiền – Tịnh song tu · L3
│   │   ├── M.E2.5. Thiền tông (Zen / Chan): thực hành chuyên sâu
│   │   │   ├── [M066] Chỉ quản đả tọa (Shikantaza) · L4
│   │   │   ├── [M139] Mặc chiếu (Mòzhào / Silent Illumination) · L4
│   │   │   ├── [M067] Công án (Kōan) · L5
│   │   │   └── [M140] Thoại đầu (Huàtóu) · L5
│   │   └── M.E2.6. Các hướng quán chiếu và tu tâm Đại thừa
│   │       ├── [M138] Thiền trong Duy thức (Yogācāra) — Tổng quan · L4
│   │       ├── [M070] Thiền và tánh Không (Madhyamaka / Prajñāpāramitā) · L4
│   │       └── [M142] Tu tâm và cho–nhận (Lojong / Tonglen) · L3
│   └── M.E3. Truyền thống Kim Cương thừa (Vajrayāna)
│       ├── M.E3.1. Tổng quan truyền thống
│       │   └── [M071] Kim Cương thừa (Vajrayāna) — Bản đồ các hệ thống Thiền · L3
│       ├── M.E3.2. Nền tảng đường tu và thực hành tiền hành
│       │   ├── [M077] Thiền phát triển tâm Bồ-đề (Bodhicitta) · L3
│       │   ├── [M144] Thiền phân tích theo thứ lớp đường tu (Lamrim) · L4
│       │   └── [M143] Các thực hành tiền hành (Ngöndro) · L5
│       ├── M.E3.3. Thiền chỉ và Thiền tuệ
│       │   ├── [M072] Thiền chỉ (Śamatha) trong Kim Cương thừa (Vajrayāna) · L3
│       │   └── [M073] Thiền tuệ / minh sát (Vipaśyanā) trong Kim Cương thừa (Vajrayāna) · L4
│       ├── M.E3.4. Các phương tiện thực hành đặc thù
│       │   ├── [M075] Thiền với chân ngôn (Mantra) · L4
│       │   ├── [M074] Thiền quán tưởng bản tôn (Deity Yoga) · L5
│       │   └── [M076] Thiền quán niệm vị thầy (Guru Yoga) · L5
│       └── M.E3.5. Thực hành cao cấp và yêu cầu truyền thừa
│           ├── [M078] Đại Thủ Ấn (Mahāmudrā) · L5
│           ├── [M079] Đại Viên Mãn (Dzogchen) · L5
│           └── [M080] Thực hành nâng cao: vai trò truyền thừa và hướng dẫn trực tiếp · L4

├── M.F. BỐI CẢNH VĂN HÓA / ĐỊA VỰC
│   └── M.F1. Thực hành Thiền trong Phật giáo Việt Nam
│       ├── [M145] Bản đồ thực hành Thiền tại Việt Nam · L2
│       ├── [M146] Các dòng Thiền lịch sử · L4
│       ├── [M147] Trúc Lâm Yên Tử và tinh thần "Cư trần lạc đạo" · L3
│       ├── [M148] Thiền Trúc Lâm hiện đại — đường lối "biết vọng không theo" · L3
│       ├── [M149] Truyền thống Làng Mai — chánh niệm ứng dụng · L2
│       ├── [M150] Tịnh độ và niệm Phật trong đời sống người Việt · L2
│       ├── [M151] Thượng tọa bộ / Nam tông (Theravāda) tại Việt Nam · L3
│       └── [M152] Thuật ngữ Hán–Việt thường gặp khi đọc tài liệu Thiền · R
│
└── M.G. ỨNG DỤNG / BỐI CẢNH / MỤC TIÊU
    ├── M.G1. Thiền ứng dụng & đời sống
    │   ├── M.G1.1. Ăn trong chánh niệm
    │   │   └── [M082] Ăn trong chánh niệm · L1
    │   ├── M.G1.2. Thiền khi làm việc
    │   │   └── [M083] Thiền khi làm việc · L1
    │   ├── M.G1.3. Quan sát cảm xúc trong đời sống
    │   │   └── [M084] Quan sát cảm xúc trong đời sống · L2
    │   ├── M.G1.4. Thực hành ngắn 1–5 phút
    │   │   └── [M085] Thực hành ngắn 1–5 phút · L1
    │   ├── M.G1.5. Thực hành cho người rất bận
    │   │   └── [M153] Thực hành cho người rất bận · L1
    │   ├── M.G1.6. Thực hành cùng gia đình và trẻ em
    │   │   └── [M154] Thực hành cùng gia đình và trẻ em · L1
    │   ├── M.G1.7. Thực hành nhóm và cộng đồng
    │   │   └── [M155] Thực hành nhóm và cộng đồng · L2
    │   └── M.G1.8. Âm thanh hướng dẫn, chuông và app — lợi ích và giới hạn
    │       └── [M156] Âm thanh hướng dẫn, chuông và app — lợi ích và giới hạn · L1
    └── M.G2. Thiền sức khỏe / thế tục (Secular Meditation)
        ├── M.G2.1. Thiền thế tục vì sức khỏe — Phạm vi và giới hạn
        │   └── [M086] Thiền thế tục vì sức khỏe — Phạm vi và giới hạn · L1
        ├── M.G2.2. Thiền thư giãn bằng hơi thở
        │   └── [M087] Thiền thư giãn bằng hơi thở · L1
        ├── M.G2.3. Quét cơ thể (Body Scan)
        │   └── [M088] Quét cơ thể (Body Scan) · L1
        ├── M.G2.4. Chánh niệm thế tục (Mindfulness)
        │   └── [M089] Chánh niệm thế tục (Mindfulness) · L1
        ├── M.G2.5. MBSR và MBCT — hai chương trình thế tục tiêu biểu
        │   └── [M157] MBSR và MBCT — hai chương trình thế tục tiêu biểu · L2
        ├── M.G2.6. Thiền hỗ trợ quản lý căng thẳng
        │   └── [M090] Thiền hỗ trợ quản lý căng thẳng · L1
        ├── M.G2.7. Thiền hỗ trợ giấc ngủ
        │   └── [M091] Thiền hỗ trợ giấc ngủ · L1
        ├── M.G2.8. Thiền hỗ trợ ứng phó đau và khó chịu
        │   └── [M092] Thiền hỗ trợ ứng phó đau và khó chịu · L2
        ├── M.G2.9. Thiền từ bi trong bối cảnh sức khỏe
        │   └── [M093] Thiền từ bi trong bối cảnh sức khỏe · L1
        ├── M.G2.10. Thiền nhạy cảm với sang chấn
        │   └── [M158] Thiền nhạy cảm với sang chấn · L2
        ├── M.G2.11. Đọc hiểu bằng chứng khoa học về Thiền
        │   └── [M159] Đọc hiểu bằng chứng khoa học về Thiền · R
        └── M.G2.12. Khi nào Thiền không nên thay thế chăm sóc y tế / tâm lý
            └── [M094] Khi nào Thiền không nên thay thế chăm sóc y tế / tâm lý · L1
```

---
# DANH MỤC BÀI VIẾT

> Mỗi bài gồm: **mô tả nội dung** (viết gì) và, khi cần, dòng **Thuật ngữ** (Pāli / Sanskrit / Hán–Việt) để người viết bài dùng đúng và thống nhất.

## M.A. KIẾN THỨC NỀN & ĐỊNH HƯỚNG

> **Trình tự gợi ý cho người mới:** A1 → A2 → A3 → A4 → A5 → A6. A7 là nhánh mở rộng, không phải bước bắt buộc. Các nhóm trong A được gom theo **chức năng học tập** và sắp theo hành trình từ hiểu khái niệm → chuẩn bị → thực hành → duy trì.

### M.A1. Hiểu về Thiền

#### [M001] Thiền là gì? · L1
Giải thích Thiền như một nhóm phương pháp rèn luyện chú ý, nhận biết và/hoặc trạng thái tâm; phân biệt Thiền với chỉ thư giãn hay "không suy nghĩ".
**Thuật ngữ:** *bhāvanā* (P/S) = tu tập, phát triển tâm — nghĩa rộng hơn từ "meditation"; Hán–Việt: **tu tập, Thiền định**.

#### [M002] Thiền Phật giáo và Thiền thế tục · L1
Phân biệt thực hành nằm trong bối cảnh Phật giáo với các dạng Thiền được trình bày độc lập với tôn giáo; tránh đánh đồng hai mục tiêu này.

#### [M095] Thiền trong Tam học — Giới, Định, Tuệ · L1
Đặt Thiền vào khung ba phần học của đạo Phật: nền tảng đạo đức → ổn định tâm → thấy biết. Giải thích vì sao truyền thống không tách Thiền ra khỏi lối sống, và điều này có ý nghĩa gì với người thực hành tại gia.
**Thuật ngữ:** *tisso sikkhā* (P) = tam học; *sīla* = giới, *samādhi* = định, *paññā* (S: *prajñā*) = tuệ. Liên hệ Bát chánh đạo: *sammā-vāyāma* (chánh tinh tấn), *sammā-sati* (chánh niệm), *sammā-samādhi* (chánh định).

### M.A2. Hiểu cách hành Thiền

#### [M096] Chánh niệm và tỉnh giác (Sati và sampajañña) · L1
Phân biệt hai yếu tố thường bị gộp làm một: *sati* là khả năng ghi nhớ/ bám sát đối tượng hiện tại; *sampajañña* là sự hiểu rõ bối cảnh, mục đích và tính thích hợp của hành động. Bài này là chìa khóa để người đọc không hiểu "chánh niệm" chỉ là "chú ý".
**Thuật ngữ:** *sati* (P) / *smṛti* (S) — Hán–Việt **niệm**; *sampajañña* (P) / *saṃprajanya* (S) — Hán–Việt **chánh tri, tỉnh giác**.

#### [M097] Đọc thuật ngữ Thiền: Pāli, Sanskrit và Hán–Việt · L1
Giải thích vì sao cùng một khái niệm lại có nhiều dạng chữ (*satipaṭṭhāna* / *smṛtyupasthāna* / tứ niệm xứ), cách app hiển thị thuật ngữ, và cách tra bảng đối chiếu thuật ngữ ở cuối tài liệu này. Kèm hướng dẫn đọc các dấu phụ (ā, ī, ū, ṃ, ṅ, ñ, ṭ, ḍ, ṇ, ḷ, ś, ṣ).

#### [M098] Những hiểu lầm phổ biến về Thiền · L1
Làm rõ các hiểu lầm: Thiền là làm cho tâm trống rỗng; Thiền phải thấy ánh sáng/hình ảnh mới đúng; suy nghĩ khởi lên là thất bại; Thiền là trốn tránh vấn đề; càng ngồi lâu càng giỏi; Thiền chắc chắn làm hết stress.

### M.A3. An toàn khi hành Thiền

#### [M099] An toàn khi hành Thiền — khi nào cần điều chỉnh hoặc dừng · L1
Các phản ứng có thể gặp (lo âu tăng, mất ngủ, cảm giác xa lạ với cơ thể hoặc thực tại, cảm xúc cũ trồi lên mạnh), cách giảm cường độ, cách "tiếp đất" và các dấu hiệu nên tạm dừng để tìm thầy hướng dẫn hoặc chuyên gia sức khỏe tâm thần. Liên kết [M158], [M094].

### M.A4. Chuẩn bị một buổi Thiền

#### [M003] Chuẩn bị trước khi Thiền · L1
Không gian, thời gian, quần áo, thiết bị, tiếng ồn và cách chọn thời lượng phù hợp với người mới.

#### [M004] Tư thế Thiền · L1
Hướng dẫn ngồi ghế, ngồi sàn (kiết già/bán già), quỳ, nằm và đi; nhấn mạnh sự ổn định, tỉnh táo và không gây đau. Nêu rõ: không có tư thế nào bắt buộc để Thiền "có kết quả".

#### [M005] Thời lượng và tần suất thực hành · L1
Cách bắt đầu bằng phiên ngắn, duy trì đều và tăng thời lượng từ từ thay vì cố gắng quá sức.

### M.A5. Trong và sau một buổi Thiền

#### [M006] Xử lý xao lãng, buồn ngủ và bồn chồn · L1
Các tình huống phổ biến khi mới tập và cách quay lại đối tượng mà không tự phán xét. Bài thực dụng; phần lý thuyết tương ứng nằm ở [M109] Năm triền cái.

#### [M007] Cách kết thúc một buổi Thiền · L1
Chuyển từ trạng thái tĩnh sang sinh hoạt bình thường một cách từ tốn, nhận biết cơ thể và tâm trước khi đứng dậy; có thể kèm hồi hướng nếu người dùng theo truyền thống có thực hành đó.

### M.A6. Xây dựng thói quen

#### [M008] Xây dựng thói quen Thiền · L1
Cách đặt lịch, tạo tín hiệu nhắc nhớ, theo dõi tiến bộ và giữ sự ổn định lâu dài.

### M.A7. Hỗ trợ và thực hành chuyên sâu hơn

#### [M100] Thiện hữu và thầy hướng dẫn (Kalyāṇamitta) · L2
Vai trò của người hướng dẫn trong truyền thống; cách đặt câu hỏi, cách nhận biết hướng dẫn đáng tin và các dấu hiệu cảnh báo (ép buộc, cô lập học viên, tuyên bố chứng đắc để thu hút, ràng buộc tài chính).
**Thuật ngữ:** *kalyāṇamitta* (P) / *kalyāṇamitra* (S) — Hán–Việt **thiện hữu, thiện tri thức**.

#### [M101] Khóa tu và thực hành tập trung dài ngày · L3
Khóa tu là gì, các hình thức phổ biến, cách chuẩn bị thân–tâm–công việc, điều gì thường xảy ra ở ngày 2–4, và cách quay về đời sống sau khóa tu.

## M.B. KỸ NĂNG THỰC HÀNH CHUNG

> **Trình tự gợi ý cho người mới:** B1 → B2 → B3 → B4 → B5 → B6 → B7. Đây là các kỹ năng dùng xuyên nhiều phương pháp; nhóm sau thường dựa trên khả năng đã hình thành ở nhóm trước, nhưng không phải thứ tự bắt buộc cho mọi truyền thống. B8 là mục tra cứu (R), không nằm trong lộ trình tuyến tính.

### M.B1. Nền tảng thân và hơi thở

#### [M009] Thả lỏng cơ thể · L1
Nhận biết và giảm căng ở mặt, hàm, vai, cổ, ngực, bụng và toàn thân.

#### [M010] Nhận biết hơi thở tự nhiên · L1
Quan sát hơi thở như đang diễn ra mà không ép nó dài, ngắn, sâu hay chậm.

#### [M011] Đếm hơi thở · L1
Kỹ thuật hỗ trợ người mới ổn định chú ý bằng cách đếm nhịp thở; xuất hiện trong nhiều hệ thống (Theravāda, Chan/Zen: *sūsokukan* — sổ tức quán).

### M.B2. Ổn định và duy trì chú ý

#### [M012] Theo dõi cảm giác của hơi thở · L2
Chuyển từ "đếm" sang nhận biết trực tiếp các cảm giác khi hít vào và thở ra; giới thiệu khái niệm điểm xúc chạm.

#### [M013] Neo tâm vào một đối tượng · L2
Nguyên tắc chọn một đối tượng ổn định và nhẹ nhàng đưa chú ý trở lại mỗi khi bị kéo đi.

### M.B3. Làm việc với xao lãng và thái độ thực hành

#### [M014] Nhận biết suy nghĩ và xao lãng · L2
Học cách nhận ra "đang suy nghĩ", "đang nghe", "đang nhớ" mà không cần chiến đấu với nội dung đó.

#### [M105] Thái độ hành Thiền: tinh tấn đúng mức, không ép, không buông · L2
Hình ảnh "dây đàn không quá căng, không quá chùng"; cách nhận ra mình đang gồng hoặc đang trôi; vai trò của sự thân thiện với chính mình trong lúc hành Thiền.

### M.B4. Quan sát và định hướng kinh nghiệm

#### [M102] Ghi nhận / niệm thầm (noting – labeling) · L2
Kỹ thuật đặt một nhãn ngắn cho kinh nghiệm đang xảy ra ("phồng – xẹp", "nghe", "nghĩ", "đau"). Nêu nguồn gốc trong hệ thống Mahāsi, lợi ích, và các giới hạn (ghi nhận quá dày có thể biến thành suy nghĩ về kinh nghiệm).

#### [M103] Như lý tác ý — yoniso manasikāra · L2
Cách hướng sự chú ý vào đúng khía cạnh của kinh nghiệm: từ "chuyện gì đang xảy ra với tôi" sang "hiện tượng này đang sinh và diệt như thế nào". Đây là bản lề giữa kỹ năng chú ý và Thiền tuệ.
**Thuật ngữ:** *yoniso manasikāra* (P) — Hán–Việt **như lý tác ý**; đối lập *ayoniso manasikāra* (phi như lý tác ý).

### M.B5. Cân bằng các yếu tố thực hành

#### [M104] Cân bằng năm căn — pañcindriya · L3
Giải thích năm yếu tố cần cân bằng khi thực hành: tín ↔ tuệ, tinh tấn ↔ định, với niệm là yếu tố điều phối không bao giờ thừa. Kèm dấu hiệu nhận biết mất cân bằng và cách chỉnh.
**Thuật ngữ:** *saddhā* (tín), *viriya* (tấn), *sati* (niệm), *samādhi* (định), *paññā* (tuệ); khi đã vững gọi là *pañca bala* — **ngũ lực**.

### M.B6. Tích hợp vào chuyển động và đời sống

#### [M015] Thiền đi (Caṅkama) · L1
Dùng chuyển động của bàn chân và toàn thân làm đối tượng chú ý: cách chọn đoạn đường, tốc độ, số bước, cách phối hợp với Thiền ngồi, và cách rút gọn thành thực hành ngắn khi di chuyển trong ngày.
**Thuật ngữ:** *caṅkama* (P) = kinh hành. *(Bài này đã gộp nội dung của M081 cũ.)*

#### [M016] Chánh niệm trong sinh hoạt hằng ngày · L1
Đưa kỹ năng nhận biết vào đi lại, ăn uống, tắm, làm việc, chờ đợi và những hoạt động quen thuộc.

### M.B7. Theo dõi và phản tư thực hành

#### [M106] Nhật ký Thiền và cách nhận biết tiến bộ · L2
Ghi gì sau mỗi buổi Thiền; những dấu hiệu tiến bộ đáng tin (bớt phản ứng, phục hồi nhanh hơn, nhận ra xao lãng sớm hơn) so với những dấu hiệu dễ gây ngộ nhận (trạng thái dễ chịu, hình ảnh lạ).

### M.B8. Câu hỏi thường gặp về Thiền

#### [M162] Câu hỏi thường gặp về Thiền · R
Tập hợp câu hỏi ngắn: ngồi bao lâu là đủ, nhắm hay mở mắt, đau chân thì làm sao, ngủ gật, nghe nhạc được không, Thiền có phạm tín ngưỡng của tôi không, không thấy gì thì có sai không.

## M.C. PHƯƠNG THỨC / HƯỚNG TU TẬP

### M.C1. Thiền chỉ (Samatha / Śamatha)

> **Trình tự gợi ý:** C1.1 → C1.2 → C1.3 → C1.4 → C1.5. C1 là một `method` (phương thức tu tập); các nhóm con được sắp theo mức độ thực hành từ nền tảng định tâm → đề mục → trở ngại/tướng → các mức định sâu → phối hợp định và tuệ.

### M.C1.1. Nền tảng Thiền chỉ và định tâm

#### [M017] Thiền chỉ (Samatha / Śamatha) · L2
Giải thích "calm abiding": làm lắng dịu tâm và phát triển năng lực tập trung liên tục; nêu rõ cách hiểu thay đổi theo truyền thống.
**Thuật ngữ:** *samatha* (P) / *śamatha* (S) — Hán–Việt **chỉ**, thường dịch "Thiền chỉ", "tịch chỉ".

#### [M022] Định tâm và tính liên tục của chú ý · L2
Phân biệt "cố tập trung thật mạnh" với khả năng duy trì chú ý ổn định, mềm và ít gián đoạn.

### M.C1.2. Các đề mục thực hành phổ biến

#### [M018] Thiền chỉ với hơi thở (Samatha) · L2
Dùng hơi thở làm đề mục để phát triển sự ổn định và liên tục của chú ý.

#### [M019] Thiền chỉ với cảm giác cơ thể (Samatha) · L2
Dùng một vùng cảm giác tương đối ổn định của cơ thể làm đề mục định tâm.

#### [M020] Thiền chỉ với âm thanh (Samatha) · L2
Giữ chú ý trên một âm thanh hoặc trường âm thanh trong cách thực hành phù hợp; phân biệt với việc nghe nhạc thư giãn.

#### [M021] Thiền chỉ với hình ảnh / vật thể (Samatha) · L2
Tập trung vào hình ảnh, điểm nhìn hoặc vật thể; đây là cửa ngõ dẫn sang các đề mục *kasiṇa* [M060] trong những truyền thống sử dụng chúng.

### M.C1.3. Trở ngại và tướng Thiền

#### [M109] Năm triền cái (Pañca nīvaraṇa) · L2
Năm trạng thái cản trở định và tuệ, dấu hiệu nhận biết từng cái và cách đối trị theo truyền thống. Bài này được gắn đồng thời vào nhánh Samatha và nhánh Quán pháp [M039].
**Thuật ngữ:** *kāmacchanda* (tham dục), *byāpāda* (sân hận), *thīna-middha* (hôn trầm – thụy miên), *uddhacca-kukkucca* (trạo cử – hối quá), *vicikicchā* (hoài nghi). Hán–Việt: **ngũ cái / năm triền cái**.

#### [M108] Tướng Thiền và các giai đoạn của tướng (Nimitta) · L3
Giải thích khái niệm "tướng" của đề mục và ba giai đoạn theo chú giải Theravāda; nhấn mạnh rằng tướng không phải mục tiêu và không phải ai cũng gặp.
**Thuật ngữ:** *parikamma-nimitta* (chuẩn bị tướng), *uggaha-nimitta* (học tướng/thủ tướng), *paṭibhāga-nimitta* (tợ tướng/quang tướng).

### M.C1.4. Các mức định và hấp thụ

#### [M107] Ba mức định (Khaṇika, Upacāra, Appanā) · L3
Phân biệt định sát-na (đủ dùng cho Thiền tuệ), cận định (gần ngưỡng nhập Thiền) và an chỉ định (nhập Thiền). Giúp người đọc hiểu vì sao "chưa đắc jhāna" không có nghĩa là "chưa có định".
**Thuật ngữ:** *khaṇika-samādhi* (sát-na định), *upacāra-samādhi* (cận hành định), *appanā-samādhi* (an chỉ định).

#### [M023] Định sâu và Thiền-na (Jhāna / Dhyāna) — Tổng quan · L3
Giới thiệu khái quát các trạng thái hấp thụ Thiền, cách thuật ngữ được dùng khác nhau giữa các truyền thống, và lưu ý rằng đây không phải mục tiêu bắt buộc của mọi người.
**Thuật ngữ:** *jhāna* (P) / *dhyāna* (S) — Hán–Việt **Thiền-na, tĩnh lự**; chữ "Thiền" trong Thiền tông và chữ "Zen" đều bắt nguồn từ đây.

#### [M110] Bốn Thiền sắc giới và năm Thiền chi · L4
Trình bày bốn tầng Thiền sắc giới và các Thiền chi có mặt/vắng mặt ở mỗi tầng; nêu rõ sự khác nhau giữa cách mô tả trong Kinh tạng và trong chú giải, cũng như giữa các Thiền sư hiện đại.
**Thuật ngữ:** *rūpajjhāna*; năm Thiền chi *jhānaṅga*: *vitakka* (tầm), *vicāra* (tứ), *pīti* (hỷ), *sukha* (lạc), *ekaggatā* (nhất tâm / nhất cảnh tính).

#### [M111] Bốn xứ vô sắc — arūpa-samāpatti · L4
Giới thiệu bốn tầng định vô sắc ở mức bản đồ khái niệm; nhấn mạnh yêu cầu về nền tảng định và hướng dẫn.
**Thuật ngữ:** *ākāsānañcāyatana* (không vô biên xứ), *viññāṇañcāyatana* (thức vô biên xứ), *ākiñcaññāyatana* (vô sở hữu xứ), *nevasaññānāsaññāyatana* (phi tưởng phi phi tưởng xứ).

### M.C1.5. Phối hợp định và tuệ

#### [M112] Phối hợp định và tuệ · L4
Ba mô hình thường được nói tới: lấy định làm cỗ xe, lấy tuệ làm cỗ xe (khô quán), và định–tuệ song hành. Giải thích vì sao các trường phái hiện đại nhấn mạnh khác nhau mà không mâu thuẫn với kinh điển.
**Thuật ngữ:** *samatha-yānika*, *vipassanā-yānika* (*sukkha-vipassaka* — khô quán giả), *yuganaddha* (định–tuệ song tu).

### M.C2. Thiền tuệ / minh sát (Vipassanā / Vipaśyanā)

> **Trình tự gợi ý:** C2.1 → C2.2 → C2.3 → C2.4 → C2.5 → C2.6. C2 là một `method` (phương thức tu tập); các nhóm con đi từ hiểu Thiền tuệ → quan sát trực tiếp → thấy sinh–diệt và ba đặc tính → các khung phân tích sâu hơn → bản đồ tiến trình → xử lý giai đoạn khó khăn. Đây là lộ trình sư phạm gợi ý, không phải một trình tự duy nhất của mọi truyền thống.

### M.C2.1. Nền tảng Thiền tuệ

#### [M024] Thiền tuệ / minh sát (Vipassanā / Vipaśyanā) · L2
Giải thích "insight": quan sát kinh nghiệm để thấy rõ tính chất và sự biến đổi của các hiện tượng; nhấn mạnh rằng cách triển khai khác nhau giữa các truyền thống, và rằng vipassanā trong kinh điển không đồng nghĩa với một khóa học cụ thể nào.
**Thuật ngữ:** *vipassanā* (P) / *vipaśyanā* (S) — Hán–Việt **quán, minh sát**.

### M.C2.2. Quan sát trực tiếp kinh nghiệm

#### [M029] Quan sát phản ứng của tâm · L2
Nhận biết chuỗi: đối tượng → cảm giác → thích/ghét → phản ứng → hậu quả; dùng để phát triển khả năng quan sát thay vì phản ứng tự động. Bản thực dụng của [M121].

#### [M030] Trải nghiệm trực tiếp và câu chuyện của tâm · L2
Phân biệt dữ liệu đang xảy ra (cảm giác, âm thanh, hình ảnh, suy nghĩ) với phần diễn giải, phán đoán và dự đoán được tâm thêm vào.
**Thuật ngữ:** liên hệ *papañca* (hý luận, sự lan man khái niệm).

#### [M031] Chánh niệm với suy nghĩ · L2
Quan sát suy nghĩ như một hiện tượng tâm; không cần ép tâm trống rỗng và cũng không cần tin theo mọi suy nghĩ.

#### [M032] Chánh niệm với cảm xúc mạnh · L3
Nhận biết cảm xúc qua cả cảm giác thân và trạng thái tâm; đi từng bước, có lối thoát an toàn, để "quan sát" không trở thành đè nén. Liên kết [M099], [M158].

### M.C2.3. Quan sát sinh–diệt và ba đặc tính

#### [M025] Quan sát sinh–diệt · L3
Nhận ra sự xuất hiện, biến đổi và biến mất của cảm giác, cảm xúc, ý nghĩ và trạng thái tâm.
**Thuật ngữ:** *udayabbaya* (sinh diệt); tuệ tương ứng: *udayabbayañāṇa*.

#### [M053] Ba đặc tính (Tilakkhaṇa) — tổng quan · L2
Bài tổng quan giới thiệu ba đặc tính như ba góc nhìn bổ sung nhau về cùng một kinh nghiệm, dẫn vào ba bài chi tiết M026–M028; nêu rõ nguồn và cách giải thích của từng trường phái thay vì trình bày như một công thức duy nhất.
**Thuật ngữ:** *tilakkhaṇa* (P) / *trilakṣaṇa* (S) — Hán–Việt **tam pháp ấn / ba đặc tính**.

#### [M026] Quán vô thường (Anicca) · L2
Dùng biến đổi trực tiếp của thân–tâm làm đối tượng khảo sát, thay vì chỉ hiểu vô thường như một ý niệm.
**Thuật ngữ:** *anicca* (P) / *anitya* (S) — **vô thường**.

#### [M027] Quán khổ / bất toại nguyện (Dukkha) · L3
Quan sát cách bám víu, chống đối và kỳ vọng liên hệ với kinh nghiệm bất toại nguyện; phân biệt ba tầng nghĩa của *dukkha* để người đọc không hiểu đạo Phật là bi quan.
**Thuật ngữ:** *dukkha-dukkha* (khổ khổ), *vipariṇāma-dukkha* (hoại khổ), *saṅkhāra-dukkha* (hành khổ).

#### [M028] Quán vô ngã (Anattā / Anātman) · L3
Khảo sát kinh nghiệm mà không mặc định một "cái tôi" cố định, độc lập, thường hằng; nói rõ vô ngã **không** có nghĩa "không có gì cả" hay "không có trách nhiệm cá nhân".
**Thuật ngữ:** *anattā* (P) / *anātman* (S) — **vô ngã**. Nguồn: *Anattalakkhaṇa Sutta* (SN 22.59).

### M.C2.4. Các khung phân tích sâu hơn

#### [M120] Phân biệt danh và sắc (Nāma-rūpa) · L3
Bước quan sát đầu tiên trong nhiều hệ thống minh sát: tách kinh nghiệm thành hiện tượng vật chất và hiện tượng tâm, thay vì một khối "tôi đang…".
**Thuật ngữ:** *nāma-rūpa* — Hán–Việt **danh sắc**; tuệ tương ứng: *nāmarūpaparicchedañāṇa*.

#### [M121] Duyên khởi trong quan sát thực tế · L4
Đưa mười hai chi duyên khởi xuống mức quan sát được trong một buổi Thiền: xúc → thọ → ái → thủ, và điểm có thể "chen vào" bằng chánh niệm.
**Thuật ngữ:** *paṭiccasamuppāda* (P) / *pratītyasamutpāda* (S) — Hán–Việt **duyên khởi, duyên sinh**; *phassa – vedanā – taṇhā – upādāna*.

### M.C2.5. Tiến trình tuệ

#### [M122] Tiến trình tuệ: bảy thanh tịnh và mười sáu tuệ — tổng quan · L4
Giới thiệu bản đồ tiến trình theo *Visuddhimagga* và cách nó được các hệ thống hiện đại sử dụng. Ghi chú biên tập: trình bày như **bản đồ tham khảo**, không như thang điểm để người dùng tự chấm mình.
**Thuật ngữ:** *satta visuddhi* (bảy thanh tịnh), *soḷasa ñāṇa* (mười sáu tuệ), *ñāṇa* = trí/tuệ.

#### [M123] Mười tùy phiền não của minh sát (Vipassanupakkilesa) · L4
Mười trạng thái dễ chịu hoặc ấn tượng (ánh sáng, hỷ, khinh an, lạc, quyết tín, tinh tấn, niệm mạnh, xả, và sự ưa thích chính những thứ đó) có thể bị nhầm là chứng đắc; cách nhận diện và cách tiếp tục.

### M.C2.6. Khó khăn và an toàn

#### [M124] Giai đoạn khó khăn trong Thiền tuệ và cách ứng phó an toàn · L4
Mô tả trung tính các giai đoạn khó (sợ hãi, chán nản, muốn thoát ra, thân đau, bất an kéo dài) thường được nhắc tới trong các hệ thống minh sát; cách giảm cường độ, tăng nền định và từ tâm, khi nào cần thầy hướng dẫn hoặc chuyên gia. **Bắt buộc** có liên kết tới [M099] và [M094].

## M.D. KHUNG / HỆ THỐNG PHÁP HÀNH

> **Lưu ý về D1:** Bốn niệm xứ (Satipaṭṭhāna) có đúng **bốn niệm xứ**: quán thân, quán thọ, quán tâm và quán pháp. Các bài con bên dưới là nội dung hoặc thực hành cụ thể thuộc từng niệm xứ; chúng không tạo thành các niệm xứ bổ sung.

### M.D1. Bốn niệm xứ (Satipaṭṭhāna / Smṛtyupasthāna)

> **Cấu trúc D1:** Bốn niệm xứ là một hệ thống gồm đúng **bốn lĩnh vực**: quán thân, quán thọ, quán tâm và quán pháp. Các bài về hơi thở, tư thế, thân hành niệm, năm triền cái, năm uẩn… là các nội dung/phương pháp/chủ đề nằm trong một trong bốn lĩnh vực này; chúng không phải các niệm xứ riêng.

#### [M033] Bốn niệm xứ (Satipaṭṭhāna / Smṛtyupasthāna) — Tổng quan · L2
Giới thiệu bốn lĩnh vực quán niệm: thân, thọ, tâm, pháp; giải thích các cách dịch phổ biến và cấu trúc lặp lại trong kinh (quán trong – ngoài, quán sinh – diệt, "chỉ ghi nhận để hay biết", không nương tựa và không chấp thủ).
**Thuật ngữ:** *satipaṭṭhāna* (P) / *smṛtyupasthāna* (S) — Hán–Việt **tứ niệm xứ**. Nguồn: *Satipaṭṭhāna Sutta* (MN 10), *Mahāsatipaṭṭhāna Sutta* (DN 22).

#### M.D1.1. Quán thân (Kāyānupassanā)

##### [M034] Quán thân (Kāyānupassanā) · L2
Khảo sát thân: hơi thở, tư thế, động tác, các yếu tố và các cách quán thân được truyền thống sử dụng.

##### [M035] Quán hơi thở trong Bốn niệm xứ (Satipaṭṭhāna) · L2
Đặt niệm hơi thở vào khung bốn niệm xứ, thay vì xem hơi thở chỉ là bài tập tập trung.

##### [M113] Niệm hơi thở — 16 bước và bốn nhóm bốn (Ānāpānassati) · L4
Trình bày mười sáu bước niệm hơi thở chia thành bốn nhóm bốn, tương ứng lần lượt với thân, thọ, tâm và pháp — tức cách kinh văn nối niệm hơi thở với trọn bộ bốn niệm xứ.
**Thuật ngữ:** *ānāpānassati* (P) / *ānāpānasmṛti*, *ānāpānānusmṛti* (S); bốn nhóm gọi là *catukka*. Nguồn: *Ānāpānassati Sutta* (MN 118).

##### [M036] Quán tư thế và chuyển động (Iriyāpatha) · L2
Nhận biết rõ đang đi, đứng, ngồi, nằm và các động tác trong sinh hoạt.
**Thuật ngữ:** *iriyāpatha* (bốn oai nghi); *sampajañña* trong các hoạt động thường gọi là *sampajānakārī*.

##### [M114] Thân hành niệm (Kāyagatāsati) · L3
Giới thiệu bài kinh và nhóm thực hành lấy thân làm nền tảng liên tục; phân biệt với body scan thế tục [M088] về mục tiêu và khung giải thích.
**Thuật ngữ:** *kāyagatāsati* (P) — Hán–Việt **thân hành niệm**. Nguồn: *Kāyagatāsati Sutta* (MN 119).

#### M.D1.2. Quán thọ (Vedanānupassanā)

##### [M037] Quán cảm thọ (Vedanānupassanā) · L2
Phân biệt cảm thọ dễ chịu, khó chịu và trung tính; quan sát phản ứng của tâm với từng loại; giới thiệu cách kinh phân biệt thọ "thuộc vật chất" và thọ "không thuộc vật chất".
**Thuật ngữ:** *vedanā* — Hán–Việt **thọ**; *sukha*, *dukkha*, *adukkhamasukha* (bất khổ bất lạc).

#### M.D1.3. Quán tâm (Cittānupassanā)

##### [M038] Quán tâm (Cittānupassanā) · L3
Nhận biết trạng thái tâm đang hiện hữu theo các cặp đối lập mà kinh liệt kê: có tham/không tham, có sân/không sân, có si/không si, co rút/tán loạn, quảng đại/hạn hẹp, có định/không định, giải thoát/chưa giải thoát.

#### M.D1.4. Quán pháp (Dhammānupassanā)

##### [M039] Quán pháp (Dhammānupassanā) · L3
Quan sát kinh nghiệm theo các nhóm phân loại của giáo pháp; bài này là bài mẹ, dẫn tới năm bài con bên dưới.
**Thuật ngữ:** *dhammā* ở đây là "các nhóm hiện tượng/pháp môn phân loại", không phải "giáo lý" theo nghĩa thông thường — cần nói rõ để tránh hiểu sai.

##### [M116] Quán pháp: Năm uẩn (Pañcakkhandha) · L3
Quan sát kinh nghiệm qua năm nhóm thay vì qua ý niệm "tôi".
**Thuật ngữ:** *rūpa* (sắc), *vedanā* (thọ), *saññā* (tưởng), *saṅkhāra* (hành), *viññāṇa* (thức).

##### [M117] Quán pháp: Sáu nội–ngoại xứ (Saḷāyatana) · L3
Quan sát tiến trình giác quan: căn – trần – thức, và cách trói buộc phát sinh ngay tại tiếp xúc.
**Thuật ngữ:** *saḷāyatana* (P) / *ṣaḍāyatana* (S) — Hán–Việt **lục nhập, sáu xứ**; *phassa* (xúc), *saṃyojana* (kiết sử).

##### [M118] Quán pháp: Bảy giác chi (Satta bojjhaṅga) · L3
Bảy yếu tố của sự giác ngộ, cách nhận biết yếu tố nào đang thiếu và cách nuôi dưỡng; kèm nguyên tắc: khi tâm trì trệ thì nuôi trạch pháp – tinh tấn – hỷ, khi tâm dao động thì nuôi khinh an – định – xả.
**Thuật ngữ:** *sati* (niệm), *dhammavicaya* (trạch pháp), *viriya* (tinh tấn), *pīti* (hỷ), *passaddhi* (khinh an), *samādhi* (định), *upekkhā* (xả).

##### [M119] Quán pháp: Bốn thánh đế (Cattāri ariyasaccāni) · L3
Đưa bốn sự thật từ mức giáo lý xuống mức quan sát trực tiếp trong một buổi Thiền: có khó chịu, có nguyên nhân bám víu, có lúc nó lắng xuống, có cách làm nó lắng xuống.
**Thuật ngữ:** *dukkha*, *samudaya*, *nirodha*, *magga* — Hán–Việt **khổ, tập, diệt, đạo**.

##### [M040] Bốn niệm xứ từ cơ bản đến chuyên sâu (Satipaṭṭhāna) · L3
Lộ trình gợi ý từ thân → thọ → tâm → pháp, đồng thời nói rõ rằng kinh không bắt buộc một trình tự duy nhất và nhiều hệ thống hiện đại triển khai khác nhau.

### M.D2. Tứ vô lượng tâm (Brahmavihāra)

> **Cấu trúc:** D2 là một nhóm pháp hành gồm bốn phẩm chất: Từ (Mettā), Bi (Karuṇā), Tùy hỷ (Muditā), Xả (Upekkhā). M125 là chi tiết thực hành của M042; M126 và M046 là nội dung tổng hợp.

#### [M041] Tứ vô lượng tâm (Brahmavihāra) — Tổng quan · L2
Giới thiệu bốn phẩm chất: từ, bi, hỷ, xả; nêu cả hai nhãn *Brahmavihāra* (phạm trú) và *appamaññā* (vô lượng tâm) và cách các truyền thống dùng khác nhau.
**Thuật ngữ:** *brahmavihāra* — Hán–Việt **tứ phạm trú**; *catasso appamaññāyo* — **tứ vô lượng tâm**.

#### M.D2.1. Từ ái (Mettā / Maitrī)

##### [M042] Từ ái (Mettā / Maitrī) · L1
Nuôi dưỡng thiện ý và mong muốn điều tốt lành cho mình và người khác; phân biệt từ ái với tình cảm luyến ái và với việc ép mình phải thấy dễ chịu.

##### [M125] Tu tập tâm từ — trình tự đối tượng (Mettā bhāvanā) · L2
Trình tự thường dùng: bản thân → người mình quý → người trung tính → người khó chịu → tất cả chúng sinh; cách xử lý khi tắc ở bước "bản thân" hoặc bước "người khó chịu"; các câu nguyện mẫu bằng tiếng Việt.
**Thuật ngữ:** *mettā bhāvanā*; nguồn: *Karaṇīyamettā Sutta* (Sn 1.8), *Mettā Sutta* (AN 11.15).

#### M.D2.2. Bi (Karuṇā)

##### [M043] Bi (Karuṇā) · L2
Nhận biết khổ đau và phát triển mong muốn làm giảm khổ đau, phân biệt với thương hại và với sự kiệt sức do đồng cảm.

#### M.D2.3. Tùy hỷ (Muditā)

##### [M044] Tùy hỷ (Muditā) · L2
Rèn khả năng vui trước hạnh phúc và thành công của người khác, giảm so sánh và ganh tị.

#### M.D2.4. Xả (Upekkhā / Upekṣā)

##### [M045] Xả (Upekkhā / Upekṣā) · L3
Phát triển sự cân bằng trước được–mất, khen–chê; phân biệt xả với vô cảm hay buông xuôi. Lưu ý *upekkhā* có hai nghĩa: xả trong tứ vô lượng tâm và xả như một Thiền chi/giác chi.

#### M.D2.5. Tổng hợp và phân tích chung

##### [M126] Kẻ thù gần và kẻ thù xa của bốn phẩm chất · L3
Theo chú giải: từ ↔ luyến ái / sân; bi ↔ sầu bi / tàn nhẫn; hỷ ↔ vui theo kiểu vụ lợi / ganh tị; xả ↔ dửng dưng vô minh / dao động. Bài này giúp người thực hành tự kiểm tra chất lượng tâm.
**Thuật ngữ:** *āsanna-paccatthika* (kẻ thù gần), *dūra-paccatthika* (kẻ thù xa).

##### [M046] Bốn vô lượng tâm như một hệ thống · L3
Quan hệ giữa bốn phẩm chất, cách chúng bù trừ cho nhau, và vị trí của chúng trong cả ba truyền thống — một trong những điểm giao nhau rõ nhất của Phật giáo.

### M.D3. Hệ thống đề mục Thiền (Kammaṭṭhāna)

> **Cấu trúc:** D3 là một hệ thống phân loại đề mục. M127 là bài tổng quan về 40 đề mục; các nhóm bên dưới phân rã thành các nhánh chi tiết. Riêng các nội dung đã có nhánh ở D2 hoặc C1 được thể hiện bằng liên kết chéo thay vì sao chép như một hệ thống độc lập.

#### M.D3.1. Tổng quan, phân loại và lựa chọn

##### [M127] Bốn mươi đề mục Thiền (Kammaṭṭhāna) — tổng quan theo Visuddhimagga · L3
Bản đồ 40 đề mục: 10 biến xứ, 10 bất tịnh, 10 tùy niệm, 4 phạm trú, 4 vô sắc, 1 quán vật thực, 1 phân tích bốn đại. Giải thích đề mục nào dẫn tới mức định nào và đề mục nào chỉ dừng ở cận định.
**Thuật ngữ:** *kammaṭṭhāna* (P) — Hán–Việt **nghiệp xứ**, thường dịch "đề mục Thiền".

##### [M128] Tính khí — sáu loại và cách chọn đề mục (Carita) · L3
Sáu khuynh hướng tính khí trong chú giải và đề mục được gợi ý cho từng loại; trình bày như công cụ tham khảo, không như bài trắc nghiệm tính cách.
**Thuật ngữ:** *rāgacarita*, *dosacarita*, *mohacarita*, *saddhācarita*, *buddhicarita*, *vitakkacarita*.

##### [M054] Chọn đề mục phù hợp với mình · L2
Nguyên tắc chọn đề mục theo mục tiêu, tính khí [M128], hoàn cảnh sống và hướng dẫn của thầy; cách thử một đề mục đủ lâu trước khi đổi.

#### M.D3.2. Biến xứ (Kasiṇa)

##### [M060] Biến xứ — mười biến xứ (Kasiṇa) · L4
Giới thiệu mười đề mục biến xứ (đất, nước, lửa, gió, xanh, vàng, đỏ, trắng, ánh sáng, hư không), cách chúng được dùng để phát triển định và lý do phần hướng dẫn chi tiết cần nguồn truyền thống rõ ràng.
**Thuật ngữ:** *kasiṇa* — Hán–Việt **biến xứ, biến xứ định**.

#### M.D3.3. Quán bất tịnh (Asubha)

##### [M047] Quán bất tịnh (Asubha) · L4
Nhóm quán nhằm giảm tham đắm thân xác, gồm mười đề mục tử thi trong chú giải. **Ghi chú biên tập:** trình bày trong bối cảnh lịch sử–tu viện, kèm cảnh báo không phù hợp với người đang có vấn đề về hình ảnh cơ thể, lo âu về cái chết hoặc trầm cảm.

#### M.D3.4. Đề mục quán thân liên quan

##### [M048] 32 thể trược (Dvattiṃsākāra) · L4
Quán thân theo 32 bộ phận; phân biệt danh mục và cách thực hành giữa các nguồn. Đây là một phần của *kāyagatāsati* [M114].
**Thuật ngữ:** *dvattiṃsākāra* (32 thể trược); pháp hành gọi là *paṭikūlamanasikāra* (quán yếm ố tác ý).

#### M.D3.5. Quán bốn đại (Catudhātuvavatthāna)

##### [M129] Quán bốn đại (Catudhātuvavatthāna) · L4
Quan sát thân qua bốn đặc tính: cứng/mềm, kết dính, nóng/lạnh, chuyển động — một cách tháo gỡ ý niệm "thân là tôi" mà không cần hình ảnh ghê sợ.
**Thuật ngữ:** *pathavī*, *āpo*, *tejo*, *vāyo* — **địa, thủy, hỏa, phong**.

#### M.D3.6. Quán vật thực (Āhāre paṭikūlasaññā)

##### [M130] Quán vật thực (Āhāre paṭikūlasaññā) · L4
Quán chiếu về thức ăn nhằm giảm tham vị; nêu rõ đây không phải phương pháp kiểm soát cân nặng và không nên trình bày cho người có rối loạn ăn uống.

#### M.D3.7. Tùy niệm (Anussati)

###### [M131] Mười tùy niệm (Dasa anussati) — tổng quan · L3
Bản đồ mười đề mục tùy niệm và vai trò của chúng: nuôi dưỡng niềm tin, sự an ổn và cảm hứng thực hành, đồng thời là nền cho định.
**Thuật ngữ:** *anussati* (P) / *anusmṛti* (S) — Hán–Việt **tùy niệm**. Mười đề mục: niệm Phật, Pháp, Tăng, giới, thí, thiên, sự chết, thân, hơi thở, tịch tịnh.

##### M.D3.7.1. Niệm Phật (Buddhānussati / Buddhānusmṛti)

###### [M050] Niệm Phật (Buddhānussati / Buddhānusmṛti) · L2
Quán niệm phẩm chất, hình ảnh hoặc danh hiệu của Phật; nêu rõ khác biệt giữa niệm ân đức Phật theo Theravāda và niệm danh hiệu theo Tịnh độ Đông Á [M068].
**Thuật ngữ:** *buddhānussati* (P) / *buddhānusmṛti* (S) — Hán–Việt **niệm Phật**.

##### M.D3.7.2. Niệm Pháp (Dhammānussati / Dharmānusmṛti)

###### [M051] Niệm Pháp (Dhammānussati / Dharmānusmṛti) · L2
Quán niệm các phẩm chất của Pháp như một cách củng cố định hướng thực hành.
**Thuật ngữ:** *dhammānussati* (P) / *dharmānusmṛti* (S).

##### M.D3.7.3. Niệm Tăng (Saṅghānussati / Saṃghānusmṛti)

###### [M052] Niệm Tăng (Saṅghānussati / Saṃghānusmṛti) · L2
Quán niệm cộng đồng thực hành và các phẩm chất của những người đi trước.
**Thuật ngữ:** *saṅghānussati* (P) / *saṃghānusmṛti* (S).

##### M.D3.7.4. Niệm giới, niệm thí, niệm thiên

###### [M132] Niệm giới, niệm thí, niệm thiên · L3
Ba tùy niệm ít được nhắc tới ở phương Tây nhưng rất gần với đời sống người Phật tử Việt Nam: nhớ lại giới hạnh của mình, nhớ lại hành vi bố thí/chia sẻ, và quán niệm về các phẩm chất dẫn tới cảnh giới an lành.
**Thuật ngữ:** *sīlānussati*, *cāgānussati*, *devatānussati*.

##### M.D3.7.5. Niệm sự chết (Maraṇassati / Maraṇasmṛti)

###### [M049] Niệm sự chết (Maraṇassati / Maraṇasmṛti) · L3
Quán chiếu tính hữu hạn của đời sống để tăng tỉnh thức và ưu tiên điều quan trọng, không nhằm nuôi dưỡng sợ hãi. Kèm hướng dẫn dừng lại nếu gây lo âu kéo dài.
**Thuật ngữ:** *maraṇassati* (P) / *maraṇasmṛti* (S).

##### M.D3.7.6. Niệm tịch tịnh (Upasamānussati)

###### [M133] Niệm tịch tịnh (Upasamānussati) · L4
Quán niệm về sự lắng dịu, về Niết-bàn như mục tiêu của con đường; đề mục thiên về tư duy – quán chiếu hơn là kỹ thuật chú ý.
**Thuật ngữ:** *upasamānussati*; *nibbāna* (P) / *nirvāṇa* (S) — **niết-bàn**.

#### M.D3.8. Liên kết chéo

- **Tứ vô lượng tâm (Brahmavihāra)**: xem D2. Theo hệ thống 40 đề mục của M127, đây là một nhóm nằm trong Kammaṭṭhāna; D3 không sao chép toàn bộ M041–M046.
- **Bốn xứ vô sắc**: xem [M111] trong C1. Thiền chỉ (Samatha / Śamatha); bài có thể được gắn thêm category `kammaṭṭhāna` nếu dữ liệu app cần biểu diễn quan hệ với hệ 40 đề mục.

## M.E. Truyền thống / dòng Thiền

> **Nguyên tắc phân nhóm:** E1–E3 là ba **truyền thống lớn**. Các mục E1.x, E2.x và E3.x bên dưới là **cụm học tập trong từng truyền thống**, không phải các truyền thống/phái độc lập mới. Trình tự được sắp từ tổng quan → nền tảng/phương thức → các hệ thống hoặc thực hành chuyên sâu; bài L5 chỉ trình bày ở mức giáo dục khi cần người hướng dẫn, truyền thừa hoặc quán đảnh.

### M.E1. Truyền thống Theravāda

#### M.E1.1. Tổng quan truyền thống

##### [M055] Thượng tọa bộ (Theravāda) — Bản đồ các hệ thống Thiền · L3
Giới thiệu hệ thống Thiền trong Theravāda và chỉ rõ rằng "Theravāda" không đồng nghĩa với một kỹ thuật duy nhất.

#### M.E1.2. Các khung và phương thức thực hành cốt lõi

##### [M056] Niệm hơi thở (Ānāpānassati) trong Thượng tọa bộ (Theravāda) · L3
Cách các nguồn Theravāda triển khai niệm hơi thở, từ ổn định chú ý tới nền tảng cho tuệ; liên kết [M113] cho cấu trúc 16 bước.

##### [M057] Bốn niệm xứ (Satipaṭṭhāna) — Cách tiếp cận Thượng tọa bộ (Theravāda) · L3
Bốn niệm xứ trong bối cảnh kinh điển Pāli và những cách triển khai hiện đại khác nhau.

##### [M058] Thiền chỉ và Thiền tuệ (Samatha–Vipassanā) trong Thượng tọa bộ (Theravāda) · L3
Các cách kết hợp chỉ và quán trong Theravāda, không giả định chỉ có một lộ trình chính thống duy nhất. Liên kết [M112].

#### M.E1.3. Các hệ thống Thiền hiện đại và dòng truyền thừa

##### [M059] Thiền tuệ / minh sát hiện đại (Vipassanā) — Các cách tiếp cận khác nhau · L3
Vì sao nhiều hệ thống rất khác nhau cùng mang tên "vipassanā"; cách so sánh chúng một cách công bằng theo: đề mục chính, cách dùng định, cách ghi nhận, và cấu trúc khóa tu.

##### [M135] Các hệ thống Thiền Miến Điện · L4
Giới thiệu và so sánh ở mức bản đồ: dòng Ledi Sayādaw, phương pháp ghi nhận của Mahāsi Sayādaw, dòng U Ba Khin – S. N. Goenka (quét cảm giác), cách tiếp cận dựa trên jhāna của Pa-Auk Sayādaw, và hướng quan sát tâm của U Tejaniya. Trình bày trung lập, không xếp hạng.

##### [M136] Truyền thống Rừng Thái Lan và các cách trình bày hiện đại · L4
Đặc điểm của Thiền trong truyền thống Rừng (Ajahn Mun, Ajahn Chah và các vị kế thừa): nhấn mạnh giới, lối sống, *buddho* như đề mục niệm, và cách dạy qua đời sống hằng ngày. Có thể nhắc cách trình bày ānāpānasati của Buddhadāsa.

#### M.E1.4. Kinh điển và hệ chú giải

##### [M134] Visuddhimagga và hệ chú giải — bản đồ văn bản · L4
Vai trò của *Visuddhimagga* (Thanh Tịnh Đạo, Buddhaghosa, thế kỷ V) và *Vimuttimagga* (Giải Thoát Đạo Luận) trong việc hệ thống hóa Thiền; phân biệt nội dung Kinh tạng với nội dung chú giải để người đọc biết mình đang đọc tầng nào.

### M.E2. Truyền thống Đại thừa (Mahāyāna)

#### M.E2.1. Tổng quan Đại thừa và khung Chỉ–Quán

##### [M061] Đại thừa (Mahāyāna) — Bản đồ các hệ thống Thiền · L3
Tính đa dạng của Đại thừa, đặc biệt các truyền thống Đông Á; tránh dùng "Đại thừa" như một hệ thống Thiền đơn nhất.

##### [M062] Thiền chỉ và Thiền quán (Śamatha–Vipaśyanā) trong Đại thừa (Mahāyāna) · L3
Hai chiều chỉ và quán trong bối cảnh Đại thừa, và liên hệ của chúng với bồ-đề tâm, ba-la-mật và tánh Không.

###### M.E2.1.1. Chỉ–Quán (Zhǐguān)

####### [M063] Chỉ–Quán (Zhǐguān) — Tổng quan · L3
"Chỉ" và "quán" trong hệ thống Đông Á, đặc biệt khi cần trình bày sự kết hợp hai phương diện thay vì tách thành hai "pháp môn" độc lập.
**Thuật ngữ:** 止觀 *zhǐguān* — Hán–Việt **chỉ quán**, tương ứng *śamatha–vipaśyanā*.

####### [M137] Ma-ha Chỉ Quán và Thiền Thiên Thai tông · L4
Giới thiệu *Mohe Zhiguan* (Ma-ha Chỉ Quán) của Trí Khải (Zhiyi) như một trong những hệ thống Thiền có cấu trúc nhất của Phật giáo Đông Á, và ảnh hưởng của nó tới các tông phái sau này.

#### M.E2.2. Thiền tông (Zen / Chan): nhập môn và thực hành

##### [M064] Thiền tông (Zen / Chan) — Tổng quan thực hành · L3
Bản đồ các hình thức thực hành trong Chan/Zen và sự khác nhau giữa các dòng truyền thừa (Lâm Tế / Rinzai, Tào Động / Sōtō).

##### [M065] Ngồi Thiền trong Thiền tông (Zazen) · L3
Zazen như một nhóm thực hành có nhiều cách triển khai: tư thế, cách thở, cách để mắt, và không khí của Thiền đường.

#### M.E2.3. Niệm Phật và Tịnh độ

##### [M068] Niệm Phật (Niànfó / Nembutsu) — Tổng quan · L2
Niệm danh hiệu Phật trong các truyền thống Đại thừa Đông Á; phân biệt cách thực hành và cách giải thích giữa các tông phái (trì danh, quán tưởng, thật tướng niệm Phật).

##### [M069] Quán tưởng Phật và Tịnh độ · L3
Các hình thức quán tưởng có cấu trúc liên quan đến Phật, Bồ-tát hoặc cõi Tịnh độ (nguồn tiêu biểu: *Quán Vô Lượng Thọ Kinh*); tránh đồng nhất với "hình dung tích cực" hiện đại.

#### M.E2.4. Kết hợp Thiền–Tịnh

##### [M141] Thiền – Tịnh song tu · L3
Truyền thống kết hợp tham Thiền và niệm Phật ở Trung Hoa và Việt Nam; các cách lý giải sự kết hợp này và ý nghĩa thực tiễn với người tại gia.

#### M.E2.5. Thiền tông (Zen / Chan): thực hành chuyên sâu

##### [M066] Chỉ quản đả tọa (Shikantaza) · L4
Thực hành "chỉ ngồi" trong Sōtō Zen; nhấn mạnh rằng đây không phải "ngồi không làm gì" và thường được dạy sau khi người học đã có nền.
**Thuật ngữ:** 只管打坐 *shikantaza* — Hán–Việt **chỉ quản đả tọa**.

##### [M139] Mặc chiếu (Mòzhào / Silent Illumination) · L4
Nguồn gốc Trung Hoa của dòng thực hành "im lặng mà sáng tỏ" (Hoằng Trí Chính Giác) và quan hệ của nó với shikantaza.
**Thuật ngữ:** 默照 *mòzhào* — Hán–Việt **mặc chiếu**.

##### [M067] Công án (Kōan) · L5
Công án là gì, vai trò trong một số dòng Zen, và vì sao thực hành công án gắn liền với quan hệ thầy–trò (tham vấn riêng). App chỉ trình bày ở mức giới thiệu.
**Thuật ngữ:** 公案 *kōan* / *gōng'àn* — Hán–Việt **công án**.

##### [M140] Thoại đầu (Huàtóu) · L5
Thực hành giữ một câu hỏi sống ("Cái gì đang niệm Phật?", "Ai đang kéo cái xác này?") trong dòng Lâm Tế Trung Hoa và Việt Nam; nhấn mạnh yêu cầu có người hướng dẫn.
**Thuật ngữ:** 話頭 *huàtóu* — Hán–Việt **thoại đầu**; tâm nghi gọi là **nghi tình** (疑情).

#### M.E2.6. Các hướng quán chiếu và tu tâm Đại thừa

##### [M142] Tu tâm và cho–nhận (Lojong / Tonglen) · L3
Hệ thống tu tâm bằng các câu châm ngôn trong truyền thống Kadampa–Tây Tạng, và thực hành tonglen (nhận khổ của người, trao đi an vui). Là thực hành Đại thừa, không đòi hỏi quán đảnh, nên có thể dạy rộng rãi — nhưng cần cảnh báo với người đang quá tải cảm xúc.
**Thuật ngữ:** *blo sbyong* (lojong) — **tu tâm**; *gtong len* (tonglen) — **cho và nhận**.

##### [M138] Thiền trong Duy thức (Yogācāra) — Tổng quan · L4
Cách hệ Duy thức mô tả tiến trình nhận thức và ý nghĩa của điều đó với thực hành quán; giới thiệu khái niệm chuyển y (*āśraya-parāvṛtti*) ở mức tổng quan.

##### [M070] Thiền và tánh Không (Madhyamaka / Prajñāpāramitā) · L4
Thiền phân tích và quán chiếu tánh Không trong bối cảnh Đại thừa; phần chuyên sâu cần dựa trên nguồn và trường phái cụ thể.
**Thuật ngữ:** *śūnyatā* — Hán–Việt **tánh Không**; *prajñāpāramitā* — **bát-nhã ba-la-mật**.

### M.E3. Truyền thống Kim Cương thừa (Vajrayāna)

#### M.E3.1. Tổng quan truyền thống

##### [M071] Kim Cương thừa (Vajrayāna) — Bản đồ các hệ thống Thiền · L3
Vajrayāna như một hệ thống đa dạng, có nền tảng Đại thừa nhưng thêm các phương tiện đặc thù; tránh coi nó là "Thiền phiên bản nâng cấp".

#### M.E3.2. Nền tảng đường tu và thực hành tiền hành

##### [M077] Thiền phát triển tâm Bồ-đề (Bodhicitta) · L3
Thiền phát nguyện và quán chiếu bồ-đề tâm; giao với thực hành từ bi và Tứ vô lượng tâm [M041]–[M046] và với lojong [M142].
**Thuật ngữ:** *bodhicitta* — Hán–Việt **bồ-đề tâm**; phân biệt *bodhicitta* nguyện và *bodhicitta* hành.

##### [M144] Thiền phân tích theo thứ lớp đường tu (Lamrim) · L4
Thiền quán chiếu theo thứ lớp đường tu (*lam rim*): thân người quý hiếm, vô thường, nghiệp, khổ luân hồi, bồ-đề tâm; phân biệt "Thiền phân tích" với "Thiền an trú".

##### [M143] Các thực hành tiền hành (Ngöndro) · L5
Cấu trúc các thực hành chuẩn bị (quy y – lễ lạy, bồ-đề tâm, Kim Cương Tát Đỏa, cúng dường mạn-đà-la, guru yoga); giải thích vì sao chúng đứng trước các thực hành sâu hơn. Trình bày ở mức giáo dục.

#### M.E3.3. Thiền chỉ và Thiền tuệ

##### [M072] Thiền chỉ (Śamatha) trong Kim Cương thừa (Vajrayāna) · L3
Calm abiding như nền tảng có thể đi trước hoặc song hành với các thực hành sâu hơn, tùy dòng truyền.

##### [M073] Thiền tuệ / minh sát (Vipaśyanā) trong Kim Cương thừa (Vajrayāna) · L4
Insight và Thiền phân tích trong các hệ thống Vajrayāna, cùng mối liên hệ với việc nhận ra bản chất của tâm.

#### M.E3.4. Các phương tiện thực hành đặc thù

##### [M075] Thiền với chân ngôn (Mantra) · L4
Mantra như một thành phần thực hành: chức năng, cách trì, và lý do không nên coi mọi câu chú đều thuộc cùng một hệ thống. Ghi chú về các mantra cần truyền khẩu.
**Thuật ngữ:** *mantra* — Hán–Việt **chân ngôn, thần chú**; *dhāraṇī* — **đà-la-ni, tổng trì**.

##### [M074] Thiền quán tưởng bản tôn (Deity Yoga) · L5
Giới thiệu quán tưởng bản tôn và hai giai đoạn sinh khởi/viên mãn ở mức khái niệm; ghi rõ rằng hướng dẫn chi tiết phụ thuộc truyền thừa và quán đảnh.
**Thuật ngữ:** *bskyed rim* (giai đoạn phát sinh), *rdzogs rim* (giai đoạn viên mãn).

##### [M076] Thiền quán niệm vị thầy (Guru Yoga) · L5
Cấu trúc guru yoga và vai trò của lòng tin, truyền thừa và quán tưởng; kèm phần nói thẳng về ranh giới lành mạnh trong quan hệ thầy–trò.

#### M.E3.5. Thực hành cao cấp và yêu cầu truyền thừa

##### [M078] Đại Thủ Ấn (Mahāmudrā) · L5
Giới thiệu ở mức bản đồ khái niệm và vị trí trong các dòng truyền thừa; nội dung thực hành chi tiết theo giáo thọ phù hợp.

##### [M079] Đại Viên Mãn (Dzogchen) · L5
Giới thiệu tổng quan, phân biệt ngôn ngữ học thuật với ngôn ngữ truyền khẩu của các dòng Nyingma/Dzogchen.

##### [M080] Thực hành nâng cao: vai trò truyền thừa và hướng dẫn trực tiếp · L4
Vì sao một số thực hành không nên được trình bày như bài tự học trên app; phần nào có thể cung cấp ở mức giáo dục/tổng quan; cách app thể hiện nhãn L5 cho người dùng.

## M.F. Bối cảnh văn hóa / địa vực

### M.F1. Thực hành Thiền trong Phật giáo Việt Nam

> **Vì sao có nhóm này:** người dùng Việt Nam tiếp xúc với Thiền chủ yếu qua các dòng thực hành tại Việt Nam, với hệ thuật ngữ Hán–Việt riêng. Thiếu nhóm này, danh mục sẽ giống một bản dịch tài liệu nước ngoài. Viết trung lập, không cổ vũ một dòng nào là đúng nhất.

#### [M145] Bản đồ thực hành Thiền tại Việt Nam · L2
Tổng quan các dòng thực hành đang hiện diện: Thiền tông (Trúc Lâm và các dòng khác), Tịnh độ và niệm Phật, chánh niệm ứng dụng kiểu Làng Mai, Theravāda/Nam tông, và các lớp Thiền thế tục.

#### [M146] Các dòng Thiền lịch sử · L4
Giới thiệu ba dòng thường được nhắc trong sử liệu — Tỳ-ni-đa-lưu-chi, Vô Ngôn Thông, Thảo Đường — và lưu ý rằng nhiều chi tiết dựa trên *Thiền uyển tập anh*, một nguồn cần đọc với ý thức về niên đại và thể loại.

#### [M147] Trúc Lâm Yên Tử và tinh thần "Cư trần lạc đạo" · L3
Bối cảnh đời Trần, vai trò của Trần Nhân Tông, và tinh thần tu giữa đời sống; có thể nhắc *Khóa hư lục* (Trần Thái Tông) và *Tuệ Trung Thượng Sĩ ngữ lục*.

#### [M148] Thiền Trúc Lâm hiện đại — đường lối "biết vọng không theo" · L3
Cách trình bày thực hành trong dòng Trúc Lâm được phục hưng thời hiện đại: nhận biết vọng tưởng mà không chạy theo; so sánh với [M031] và [M066] để người đọc thấy điểm giống và khác.

#### [M149] Truyền thống Làng Mai — chánh niệm ứng dụng · L2
Đặc điểm: thi kệ, chuông chánh niệm, Thiền đi, Thiền ăn, thực hành trong sinh hoạt và trong quan hệ; vị trí của cách trình bày này giữa Phật giáo và mindfulness thế tục.

#### [M150] Tịnh độ và niệm Phật trong đời sống người Việt · L2
Thực hành niệm Phật tại gia và tại chùa, khóa tu Phật thất, hộ niệm; giải thích quan hệ giữa niệm Phật như pháp môn tín nguyện và niệm Phật như đề mục định [M050], [M068].

#### [M151] Thượng tọa bộ / Nam tông (Theravāda) tại Việt Nam · L3
Sự hình thành của Nam tông Kinh và Nam tông Khmer, các trung tâm thực hành, và những thuật ngữ Pāli mà người học sẽ gặp.

#### [M152] Thuật ngữ Hán–Việt thường gặp khi đọc tài liệu Thiền · R
Bảng giải nghĩa các từ người đọc Việt hay gặp: chỉ – quán, định – tuệ, tam học, tứ niệm xứ, ngũ cái, thất giác chi, tứ vô lượng tâm, kinh hành, tọa Thiền, tham thoại đầu, nghi tình, vọng tưởng, tâm viên ý mã… Bổ sung cho bảng đối chiếu thuật ngữ ở cuối tài liệu.

## M.G. Ứng dụng / bối cảnh / mục tiêu

### M.G1. Thiền ứng dụng & đời sống

#### M.G1.1. Ăn trong chánh niệm

##### [M082] Ăn trong chánh niệm · L1
Quan sát cảm giác, tốc độ ăn, mùi vị, việc nhai và tín hiệu của thân, mà không biến bài tập thành quy tắc ăn uống cứng nhắc. **Ghi chú biên tập:** không trình bày như phương pháp giảm cân; xem [M158].

#### M.G1.2. Thiền khi làm việc

##### [M083] Thiền khi làm việc · L1
Các bài thực hành ngắn để đưa chú ý trở lại công việc, giảm chuyển đổi tác vụ không cần thiết và nhận biết căng thẳng.

#### M.G1.3. Quan sát cảm xúc trong đời sống

##### [M084] Quan sát cảm xúc trong đời sống · L2
Đưa kỹ năng nhận biết thân – thọ – tâm vào tranh luận, chờ đợi, thất vọng, lo lắng; nhấn mạnh việc dừng lại trước khi phản ứng.

#### M.G1.4. Thực hành ngắn 1–5 phút

##### [M085] Thực hành ngắn 1–5 phút · L1
Nhóm bài cực ngắn theo mục tiêu: ổn định chú ý, nhận biết hơi thở, thả lỏng, chuyển trạng thái, lấy lại khoảng dừng.

#### M.G1.5. Thực hành cho người rất bận

##### [M153] Thực hành cho người rất bận · L1
Thiết kế thực hành tối thiểu khả thi: ba hơi thở trước khi mở máy tính, một phút trước khi vào cuộc họp, một "điểm neo" cố định trong ngày; cách duy trì khi lịch vỡ.

#### M.G1.6. Thực hành cùng gia đình và trẻ em

##### [M154] Thực hành cùng gia đình và trẻ em · L1
Cách giới thiệu thực hành ngắn cho trẻ theo độ tuổi, thực hành trước bữa ăn hoặc trước giờ ngủ, và nguyên tắc không ép buộc.

#### M.G1.7. Thực hành nhóm và cộng đồng

##### [M155] Thực hành nhóm và cộng đồng · L2
Lợi ích của việc ngồi chung, cách tổ chức nhóm nhỏ, nghi thức tối giản, và cách tham gia nhóm trực tuyến mà vẫn giữ chất lượng thực hành.

#### M.G1.8. Âm thanh hướng dẫn, chuông và app — lợi ích và giới hạn

##### [M156] Âm thanh hướng dẫn, chuông và app — lợi ích và giới hạn · L1
Khi nào nên dùng bài hướng dẫn có tiếng, khi nào nên ngồi im lặng; cách dùng chuông và hẹn giờ; rủi ro phụ thuộc vào âm thanh dẫn dắt.

### M.G2. Thiền sức khỏe / thế tục (Secular Meditation)

> **Nhãn biên tập:** Nhóm này viết theo hướng **sức khỏe/thế tục**, không yêu cầu người dùng theo Phật giáo. Dùng "hỗ trợ", "có thể giúp", "thực hành thư giãn/điều hòa chú ý" thay vì tuyên bố Thiền "chữa khỏi" bệnh. Khi đề cập một tình trạng y khoa cụ thể, nêu giới hạn bằng chứng và khuyến nghị người dùng tiếp tục chăm sóc y tế phù hợp.

#### M.G2.1. Thiền thế tục vì sức khỏe — Phạm vi và giới hạn

##### [M086] Thiền thế tục vì sức khỏe — Phạm vi và giới hạn · L1
Secular meditation là gì, những mục tiêu sức khỏe có thể nhắm tới, và ranh giới giữa nội dung tự chăm sóc với điều trị y khoa/tâm lý.

#### M.G2.2. Thiền thư giãn bằng hơi thở

##### [M087] Thiền thư giãn bằng hơi thở · L1
Bài thực hành nhẹ tập trung vào cảm giác hơi thở và thả lỏng; không yêu cầu niềm tin tôn giáo.

#### M.G2.3. Quét cơ thể (Body Scan)

##### [M088] Body Scan — Quét cơ thể · L1
Di chuyển chú ý có hệ thống qua các vùng cơ thể để tăng nhận biết và hỗ trợ thư giãn; nêu rõ khác biệt về mục tiêu so với *kāyagatāsati* [M114].

#### M.G2.4. Chánh niệm thế tục (Mindfulness)

##### [M089] Mindfulness thế tục · L1
Chánh niệm như kỹ năng chú ý và nhận biết hiện tại trong bối cảnh phi tôn giáo, đồng thời **không** đồng nhất hoàn toàn với satipaṭṭhāna.

#### M.G2.5. MBSR và MBCT — hai chương trình thế tục tiêu biểu

##### [M157] MBSR và MBCT — hai chương trình thế tục tiêu biểu · L2
Cấu trúc 8 tuần, nguồn gốc, các bài tập chính và phạm vi ứng dụng của hai chương trình được nghiên cứu nhiều nhất; nêu rõ đây là chương trình có giảng viên, app không thay thế được.

#### M.G2.6. Thiền hỗ trợ quản lý căng thẳng

##### [M090] Thiền hỗ trợ quản lý căng thẳng · L1
Bài tập hướng tới nhận biết căng thẳng, tạo khoảng dừng và điều hòa chú ý; dùng ngôn ngữ "hỗ trợ" thay vì cam kết hiệu quả điều trị.

#### M.G2.7. Thiền hỗ trợ giấc ngủ

##### [M091] Thiền hỗ trợ giấc ngủ · L1
Thực hành thư giãn và giảm kích hoạt trước khi ngủ; nêu rõ đây không thay thế việc tìm nguyên nhân mất ngủ khi cần.

#### M.G2.8. Thiền hỗ trợ ứng phó đau và khó chịu

##### [M092] Thiền hỗ trợ ứng phó đau và khó chịu · L2
Hướng chú ý tới cảm giác đau, phản ứng và căng thẳng đi kèm một cách an toàn; tránh hứa hẹn giảm đau cho mọi người.

#### M.G2.9. Thiền từ bi trong bối cảnh sức khỏe

##### [M093] Thiền từ bi trong bối cảnh sức khỏe · L1
Ứng dụng các bài compassion/loving-kindness bằng ngôn ngữ thế tục để hỗ trợ thái độ ít tự phán xét và biết chăm sóc bản thân.

#### M.G2.10. Thiền nhạy cảm với sang chấn

##### [M158] Thiền nhạy cảm với sang chấn · L2
Nguyên tắc thực hành an toàn cho người có tiền sử sang chấn: cho phép mở mắt, chọn điểm neo trung tính hoặc bên ngoài, phiên ngắn, luôn có "lối ra", không ép ở lại với cảm giác mạnh. Nêu rõ giới hạn của app và vai trò của chuyên gia.

#### M.G2.11. Đọc hiểu bằng chứng khoa học về Thiền

##### [M159] Đọc hiểu bằng chứng khoa học về Thiền · R
Cách đọc một nghiên cứu về Thiền: cỡ mẫu, nhóm đối chứng, hiệu ứng kỳ vọng, khác biệt giữa "có ý nghĩa thống kê" và "có ý nghĩa với đời sống"; vì sao app dùng ngôn ngữ thận trọng.

#### M.G2.12. Khi nào Thiền không nên thay thế chăm sóc y tế / tâm lý

##### [M094] Khi nào Thiền không nên thay thế chăm sóc y tế / tâm lý · L1
Giới hạn của app, các tình huống cần tìm bác sĩ hoặc chuyên gia sức khỏe tâm thần, và cách trình bày cảnh báo mà không làm người dùng hoảng sợ.

---

# LỘ TRÌNH HỌC

## Lộ trình chính (người mới, không phân biệt truyền thống)

> **Nguyên tắc:** Đây là trình tự học gợi ý dựa trên độ khó và sự phụ thuộc kỹ năng, không phải một thứ tự bắt buộc cho mọi truyền thống. Ở các bước rẽ hướng, người dùng chọn một nhánh phù hợp thay vì học hết mọi nhánh.

```text
Bước 0 — Hiểu mình đang học gì                         L1
M001 → M002 → M095 → M096 → M098
M097 = bài tra cứu thuật ngữ, có thể đọc khi cần

Bước 1 — Chuẩn bị an toàn và sẵn sàng                  L1
M099 → M003 → M004 → M005

Bước 2 — Thực hành một buổi Thiền cơ bản              L1
M009 → M010 → M011 → M012 → M006 → M007

Bước 3 — Ổn định kỹ năng và hình thành thói quen       L1–L2
M008 → M013 → M014 → M105 → M102 → M103 → M015 → M016 → M106

Bước 4 — Chọn một phương thức / hướng thực hành        L2
├── Thiền chỉ:              M017 → M022 → M018 → M019 → M020 → M021
│                           → M109 → M108 → M107 → M023
├── Bốn niệm xứ:            M033 → M034 → M035 → M036 → M037 → M038 → M039
├── Thiền tuệ / minh sát:    M024 → M029 → M030 → M031 → M025 → M053
│                           → M026 → M027 → M028
└── Tứ vô lượng tâm:         M041 → M042 → M125 → M043 → M044 → M045 → M046

Bước 5 — Đào sâu một hướng                                 L3–L4
├── Thiền chỉ:              M110 → M111 → M112
├── Bốn niệm xứ:            M113 → M114 → M116 → M117 → M118 → M119 → M040
├── Thiền tuệ / minh sát:   M120 → M121 → M032 → M122 → M123 → M124
└── Đề mục:                 M127 → M128 → M054 → M131 → M050 → M049

Bước 6 — Tìm hiểu truyền thống                               L3–L4
Việt Nam:   M145 → M147 → M148 → M149 → M150 → M151
Theravāda:  M055 → M056 → M057 → M058 → M059 → M135 → M136 → M134
Mahāyāna:   M061 → M062 → M063 → M137 → M064 → M065 → M068 → M069 → M141 → M138 → M070 → M142
Vajrayāna:  M071 → M077 → M144 → M072 → M073 → M075

Bước 7 — Nội dung cần điều kiện                                 L5
Chỉ trình bày ở mức giáo dục/tổng quan; luôn kèm nhãn "cần thầy hướng dẫn":
M067, M140, M074, M076, M078, M079, M143
```

## Lộ trình phụ — Sức khỏe / thế tục (không cần nền Phật học)

```text
M086 → M087 → M088 → M089 → M090 / M091 / M092 / M093
        → M157 (nếu muốn chương trình có cấu trúc)
        → M158 (nếu có tiền sử sang chấn)
        → M094 (bắt buộc hiển thị ở cuối nhánh này)
```

## Lộ trình phụ — Người bận, mỗi ngày dưới 10 phút

```text
M085 → M153 → M015 → M082 → M083 → M016 → M084
```

## Nguyên tắc lộ trình

1. **Các nhóm A, B và các nhóm con trong C/D là cấu trúc nội dung; trình tự học chỉ là gợi ý.**
2. **Bài L5 không bao giờ nằm trong lộ trình tự động.** Chỉ hiện khi người dùng chủ động tìm hiểu.
3. **Không khóa nội dung theo thứ tự cứng.** Người dùng phải luôn tìm được bài bất kỳ qua tra cứu trong app.
4. **Bài an toàn đi kèm, không đi sau.** [M099] xuất hiện trước khi bắt đầu thực hành; [M124] và [M158] phải hiện cùng lúc với nội dung tương ứng.

# QUY TẮC DÙNG MÃ VÀ METADATA TRONG APP

## 1. Một bài, nhiều nhánh
Nếu bài có cùng nội dung cốt lõi, chỉ tạo **một record**:

```yaml
id: M010
title: "Nhận biết hơi thở tự nhiên"
level: L1
categories: [nhap-mon, ky-nang-chung, samatha]
```

> Chỉ gắn nhãn truyền thống khi bài **thực sự** trình bày phương pháp trong bối cảnh truyền thống đó; không gắn cả ba nhánh chỉ vì "hơi thở có mặt ở khắp nơi".

## 2. Bài tổng quát và bài theo truyền thống là hai bài khác nhau

```text
[M017] Samatha / Śamatha — Thiền an tĩnh        ← khái niệm chung
[M058] Samatha–Vipassanā trong Theravāda        ← cách một truyền thống dùng
[M062] Thiền chỉ và Thiền quán (Śamatha–Vipaśyanā) trong Đại thừa (Mahāyāna)
[M072] Thiền chỉ (Śamatha) trong Kim Cương thừa (Vajrayāna)
```

## 3. Cùng tiêu đề = cùng khái niệm; cùng mã = cùng bài
Nếu muốn viết riêng cách thực hành theo từng truyền thống, tạo bài mới thay vì nhồi vào một bài. Mã mới lấy số kế tiếp chưa dùng (hiện tại: **M164** trở đi).

## 4. "Truyền thống" là metadata, không phải taxonomy duy nhất

```yaml
id: M018
title: "Samatha với hơi thở"
level: L2
traditions: [chung]            # chung | theravada | mahayana | vajrayana | viet-nam | the-tuc
methods:    [samatha]
objects:    [hoi-tho]
goals:      [dinh-tam, an-tinh]
duration:   [10-20p]
requires:   [M010, M013]       # gợi ý nên đọc trước
related:    [M056, M113]
safety:     none               # none | caution | needs-teacher
sources:    ["MN 118", "Visuddhimagga VIII"]
terms:
  pali:     "samatha"
  sanskrit: "śamatha"
  hanviet:  "chỉ"
```

Nhờ vậy app có thể cho người dùng duyệt theo **lộ trình**, theo **phương pháp**, theo **truyền thống**, theo **mục tiêu**, theo **thời lượng** hoặc theo **cấp độ** mà không phải nhân bản bài viết.

## 5. Ba trường bắt buộc mà bản v1 chưa có
- `level` — để dựng lộ trình và để người dùng biết bài có hợp với mình không.
- `safety` — để app tự động gắn cảnh báo và chặn gợi ý sai đối tượng (ví dụ không gợi ý [M047] hay [M130] cho người dùng đang ở nhánh rối loạn ăn uống).
- `terms` — để bật tính năng tra thuật ngữ ngay trong bài.

---

# NGUYÊN TẮC BIÊN TẬP

1. **Không dùng taxonomy để xếp hạng truyền thống.** "Chuyên sâu" nghĩa là khó hơn hoặc cần nhiều điều kiện hơn, không phải "truyền thống A cao hơn truyền thống B".
2. **Phân biệt Pāli và Sanskrit, và ghi cả Hán–Việt.** Ví dụ: samatha/śamatha, vipassanā/vipaśyanā, mettā/maitrī, upekkhā/upekṣā, satipaṭṭhāna/smṛtyupasthāna, buddhānussati/buddhānusmṛti. Viết đúng dấu phụ; nếu hệ thống hiển thị không hỗ trợ, phải có phương án dự phòng thống nhất (không tùy tiện bỏ dấu ở chỗ này mà giữ ở chỗ khác).
3. **Phân tầng nguồn.** Nói rõ nội dung đến từ Kinh tạng, chú giải, hay cách trình bày của một vị thầy hiện đại. Đây là điều người đọc Việt Nam rất hay bị nhầm.
4. **Ghi rõ phạm vi truyền thống trong bài.** Cùng một từ có thể được định nghĩa hoặc thực hành khác nhau.
5. **Không đồng nhất mindfulness hiện đại với satipaṭṭhāna.** Có quan hệ lịch sử, nhưng "mindfulness" thế tục là phạm trù hiện đại rộng hơn và có mục tiêu khác.
6. **Thực hành cần điều kiện phải có nhãn.** Bài L5 luôn kèm thông báo rằng app chỉ trình bày ở mức giáo dục khi truyền thống yêu cầu thầy hướng dẫn, truyền thừa hoặc quán đảnh.
7. **Nhóm sức khỏe dùng ngôn ngữ bằng chứng.** Ưu tiên "hỗ trợ", "có thể giúp"; không quảng bá Thiền như phương pháp chữa bệnh.
8. **An toàn là một phần nội dung, không phải phụ lục.** Mọi bài có `safety: caution` phải dẫn tới [M099]; nội dung liên quan sức khỏe tâm thần phải dẫn tới [M094].
9. **Không hứa hẹn chứng đắc và không mô tả trạng thái như thành tích.** Đặc biệt ở [M110], [M122], [M123].
10. **Giọng văn trung lập và tôn trọng.** Không chê một pháp môn để nâng pháp môn khác; khi các nguồn bất đồng thì trình bày sự bất đồng đó.

---

# BẢNG THUẬT NGỮ ĐỐI CHIẾU

| Pāli | Sanskrit | Hán–Việt | Tiếng Việt thường dùng | English |
|------|----------|----------|------------------------|---------|
| bhāvanā | bhāvanā | tu tập | tu tập, phát triển tâm | mental cultivation |
| samatha | śamatha | chỉ | Thiền chỉ, an tĩnh | calm abiding |
| vipassanā | vipaśyanā | quán | Thiền quán, minh sát | insight |
| sati | smṛti | niệm | chánh niệm | mindfulness |
| sampajañña | saṃprajanya | chánh tri | tỉnh giác | clear comprehension |
| samādhi | samādhi | định | định, tập trung | concentration |
| paññā | prajñā | tuệ | trí tuệ | wisdom |
| sīla | śīla | giới | giới, đạo đức | ethical conduct |
| jhāna | dhyāna | Thiền-na, tĩnh lự | Thiền định sâu | absorption |
| kammaṭṭhāna | karmasthāna | nghiệp xứ | đề mục Thiền | meditation subject |
| nimitta | nimitta | tướng | tướng Thiền | sign, mental image |
| satipaṭṭhāna | smṛtyupasthāna | tứ niệm xứ | bốn niệm xứ | foundations of mindfulness |
| kāyānupassanā | — | quán thân | quán thân | contemplation of body |
| vedanānupassanā | — | quán thọ | quán cảm thọ | contemplation of feeling |
| cittānupassanā | — | quán tâm | quán tâm | contemplation of mind |
| dhammānupassanā | dharmānupassanā | quán pháp | quán pháp | contemplation of dhammas |
| ānāpānassati | ānāpānasmṛti | nhập xuất tức niệm, an-ban niệm | niệm hơi thở | mindfulness of breathing |
| kāyagatāsati | — | thân hành niệm | niệm thân | mindfulness immersed in body |
| caṅkama | caṅkrama | kinh hành | Thiền đi | walking meditation |
| nīvaraṇa | nivaraṇa | cái, triền cái | năm chướng ngại | hindrance |
| bojjhaṅga | bodhyaṅga | giác chi | bảy yếu tố giác ngộ | factor of awakening |
| indriya | indriya | căn | năm căn | faculty |
| bala | bala | lực | năm lực | power |
| khandha | skandha | uẩn | năm uẩn | aggregate |
| āyatana | āyatana | xứ, nhập | sáu xứ | sense base |
| dhātu | dhātu | giới, đại | bốn đại | element |
| anicca | anitya | vô thường | vô thường | impermanence |
| dukkha | duḥkha | khổ | khổ, bất toại nguyện | unsatisfactoriness |
| anattā | anātman | vô ngã | vô ngã | non-self |
| tilakkhaṇa | trilakṣaṇa | tam pháp ấn | ba đặc tính | three characteristics |
| paṭiccasamuppāda | pratītyasamutpāda | duyên khởi | duyên sinh | dependent origination |
| nāma-rūpa | nāma-rūpa | danh sắc | thân và tâm | mind and matter |
| taṇhā | tṛṣṇā | ái | tham ái | craving |
| upādāna | upādāna | thủ | chấp thủ | clinging |
| papañca | prapañca | hý luận | tâm lan man, thêu dệt | conceptual proliferation |
| yoniso manasikāra | yoniśo manaskāra | như lý tác ý | hướng tâm đúng cách | wise attention |
| vitakka / vicāra | vitarka / vicāra | tầm / tứ | hướng tâm / duy trì tâm | initial / sustained application |
| pīti / sukha | prīti / sukha | hỷ / lạc | hỷ / lạc | rapture / bliss |
| ekaggatā | ekāgratā | nhất cảnh tính | nhất tâm | one-pointedness |
| upacāra-samādhi | — | cận hành định | cận định | access concentration |
| appanā-samādhi | — | an chỉ định | định nhập Thiền | absorption concentration |
| brahmavihāra | brahmavihāra | tứ phạm trú | tứ vô lượng tâm | divine abodes |
| mettā | maitrī | từ | từ ái, lòng thương | loving-kindness |
| karuṇā | karuṇā | bi | lòng bi | compassion |
| muditā | muditā | hỷ | tùy hỷ | appreciative joy |
| upekkhā | upekṣā | xả | tâm xả | equanimity |
| anussati | anusmṛti | tùy niệm | niệm tưởng | recollection |
| buddhānussati | buddhānusmṛti | niệm Phật | niệm Phật | recollection of the Buddha |
| maraṇassati | maraṇasmṛti | tử tùy niệm | niệm sự chết | mindfulness of death |
| asubha | aśubha | bất tịnh | quán bất tịnh | foulness |
| kasiṇa | kṛtsna | biến xứ | đề mục biến xứ | kasiṇa device |
| ñāṇa | jñāna | trí | tuệ, trí | knowledge |
| visuddhi | viśuddhi | thanh tịnh | thanh tịnh | purification |
| vimutti | vimukti | giải thoát | giải thoát | liberation |
| nibbāna | nirvāṇa | niết-bàn | niết-bàn | nibbāna |
| kalyāṇamitta | kalyāṇamitra | thiện tri thức | thầy, bạn đạo tốt | spiritual friend |
| — | bodhicitta | bồ-đề tâm | tâm bồ-đề | awakening mind |
| suññatā | śūnyatā | không tánh | tánh Không | emptiness |
| — | zhǐguān 止觀 | chỉ quán | chỉ và quán | calming and contemplation |
| — | dhyāna → chán → zen 禪 | Thiền | Thiền tông | Zen / Chan |
| — | niànfó 念佛 | niệm Phật | niệm Phật | recitation of Buddha's name |

---

# NGUỒN THAM KHẢO GỢI Ý CHO NGƯỜI VIẾT BÀI

## Kinh tạng Pāli (nền cho nhóm A–E)
- *Satipaṭṭhāna Sutta* (MN 10) và *Mahāsatipaṭṭhāna Sutta* (DN 22) — nền cho nhóm D.
- *Ānāpānassati Sutta* (MN 118) — nền cho [M113], [M056].
- *Kāyagatāsati Sutta* (MN 119) — nền cho [M114], [M048].
- *Anattalakkhaṇa Sutta* (SN 22.59) — nền cho [M028].
- *Karaṇīyamettā Sutta* (Sn 1.8) — nền cho [M042], [M125].
- Bản dịch tiếng Việt tham khảo: Đại tạng kinh Việt Nam (HT. Thích Minh Châu) cho Nikāya; đối chiếu với bản Anh ngữ khi cần.

## Chú giải và luận
- *Visuddhimagga* (Thanh Tịnh Đạo) — nền cho [M127], [M128], [M108], [M122], [M126].
- *Vimuttimagga* (Giải Thoát Đạo Luận) — đối chiếu với Visuddhimagga.
- *Mohe Zhiguan* (Ma-ha Chỉ Quán, Trí Khải) — nền cho [M137].

## Nguồn Đại thừa / Kim Cương thừa
- 84000 — *The King of Samādhis Sūtra*: cặp śamatha–vipaśyanā trong văn cảnh Đại thừa. https://84000.co/translation/toh127
- 84000 — *The Perfection of Wisdom in Eighteen Thousand Lines*: bốn niệm xứ, tứ vô lượng tâm, niệm hơi thở và các đề mục quán. https://84000.co/translation/toh10/UT22084-029-001-glossary/toh3808
- 84000 — Glossary: *ānāpānānusmṛti* = mindfulness of breathing in and out. https://scholar.84000.co/authority/entity-37381
- 84000 — *smṛtyupasthāna* và *brahmavihāra* trong tư liệu Đại thừa. https://84000.co/pdf-redirect/toh176_84000-the-teaching-of-vimalakirti.pdf
- *Quán Vô Lượng Thọ Kinh* — nền cho [M069].

## Đông Á và Việt Nam
- Encyclopedia.com — tổng quan Thiền Phật giáo Đông Á và việc kết hợp śamatha/vipaśyanā. https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/buddhist-meditation-east-asian-buddhist-meditation
- *Thiền uyển tập anh* — nguồn chính cho [M146]; đọc kèm nghiên cứu hiện đại về niên đại.
- *Khóa hư lục* (Trần Thái Tông), *Tuệ Trung Thượng Sĩ ngữ lục*, *Cư trần lạc đạo phú* (Trần Nhân Tông) — nền cho [M147].
- Tài liệu của các dòng thực hành đương đại tại Việt Nam cho [M148]–[M151]; khi trích dẫn, ghi rõ đây là cách trình bày của một dòng, không phải định nghĩa chung.

## Sức khỏe / thế tục
- NCCIH — tổng quan về meditation/mindfulness, hiệu quả và an toàn. https://www.nccih.nih.gov/health/meditation-and-mindfulness-effectiveness-and-safety
- Tài liệu chương trình MBSR/MBCT cho [M157]; các nghiên cứu về tác dụng không mong muốn cho [M099], [M158].

> **Lưu ý về đường dẫn:** các URL trên lấy từ bản v1 của tài liệu. Cần kiểm tra lại trước khi xuất bản, và ưu tiên trích nguồn gốc (kinh, luận, trang của tổ chức) thay vì trang tổng hợp.

---

# THAY ĐỔI SO VỚI BẢN v1–v2

## Thêm mới (M095–M163, 68 bài — mã M115 để trống, chưa dùng; về sau M160, M161 và M163 nghỉ hưu ở v3.6)
- **Nền tảng còn thiếu:** tam học [M095], sati–sampajañña [M096], cách đọc thuật ngữ [M097], hiểu lầm phổ biến [M098], an toàn [M099], thầy hướng dẫn [M100], khóa tu [M101].
- **Kỹ năng:** ghi nhận [M102], như lý tác ý [M103], cân bằng ngũ căn [M104], thái độ hành Thiền [M105], nhật ký [M106].
- **Samatha:** ba mức định [M107], nimitta [M108], năm triền cái [M109], bốn Thiền và Thiền chi [M110], bốn xứ vô sắc [M111], phối hợp định–tuệ [M112].
- **Niệm xứ:** 16 bước ānāpānassati [M113], kāyagatāsati [M114], và bốn bài con của quán pháp [M116]–[M119] — trước đây [M039] đứng một mình mà không có nội dung cụ thể.
- **Thiền tuệ:** danh sắc [M120], duyên khởi [M121], tiến trình tuệ [M122], tùy phiền não của minh sát [M123], giai đoạn khó khăn [M124].
- **Từ bi:** trình tự rải tâm từ [M125], kẻ thù gần/xa [M126].
- **Đề mục truyền thống:** 40 kammaṭṭhāna [M127], carita [M128], bốn đại [M129], vật thực [M130], mười tùy niệm [M131], niệm giới/thí/thiên [M132], niệm tịch tịnh [M133]. Đây là khung mà bản v1 thiếu, khiến các bài [M047]–[M052] trông rời rạc.
- **Truyền thống:** hệ văn bản Theravāda [M134], hệ thống Miến Điện [M135], truyền thống Rừng Thái [M136], Thiên Thai [M137], Duy thức [M138], mặc chiếu [M139], thoại đầu [M140], Thiền–tịnh song tu [M141], lojong/tonglen [M142], ngöndro [M143], lamrim [M144].
- **Nhóm K mới — Phật giáo Việt Nam [M145]–[M152].** Đây là bổ sung quan trọng nhất: người dùng Việt gặp Thiền qua các dòng này và qua thuật ngữ Hán–Việt.
- **Đời sống:** người bận [M153], gia đình và trẻ em [M154], nhóm [M155], âm thanh hướng dẫn [M156].
- **Sức khỏe:** MBSR/MBCT [M157], trauma-sensitive [M158], đọc hiểu bằng chứng [M159].
- **Nhóm N mới — tra cứu M160–M163**, phục vụ trực tiếp yêu cầu "dễ tra cứu"; về sau M162 chuyển sang **B8**, còn M160, M161 và M163 nghỉ hưu (v3.6).

## Gộp và chỉnh
- **v3.3 — Phân cấp tiếp A, B, C1, C2:** A được chia theo hành trình người mới; B theo nhóm kỹ năng từ nền tảng thân–hơi thở → ổn định chú ý → xử lý xao lãng → quan sát → cân bằng → tích hợp đời sống → phản tư; C1/C2 được chia thành các nhóm học tập có cùng chức năng và trình tự gợi ý.
- **v3.3 — Sửa vị trí D1 trong danh mục bài viết:** Bốn niệm xứ được đặt đúng dưới nhóm D, không còn nằm xen giữa C1 và C2.
- **[M081] gộp vào [M015]** — "Thiền đi" và "Thiền đi trong đời sống" là cùng một kỹ năng. Mã M081 **nghỉ hưu**, không dùng lại.
- **[M053] đổi tên** thành "Ba đặc tính — tilakkhaṇa: tổng quan" và **chuyển từ nhóm F sang nhóm E**, đứng trước M026–M028 thay vì lặp lại chúng ở cuối một nhóm khác.
- **[M060] Kasiṇa chuyển từ nhóm Theravāda sang nhóm G** (đề mục Thiền), vì nó là một trong 40 kammaṭṭhāna chứ không phải đặc trưng riêng của Theravāda hiện đại.
- **Tái cấu trúc cây cũ** ("Hai trục Thiền cốt lõi") thành **C. Samatha** và **E. Vipassanā**, với **D. Satipaṭṭhāna** ở giữa làm khung nối. Nhóm cũ gộp hai trục vào một nhánh nên cây bị lệch và lộ trình khó dựng.
- **Đổi tên nhóm F cũ** ("Các pháp quán & niệm truyền thống") thành **G. Đề mục Thiền truyền thống — Kammaṭṭhāna**, đúng tên gọi của hệ thống này.
- **Thêm cấp độ L1–L5/R cho toàn bộ bài** và thêm ba trường metadata bắt buộc: `level`, `safety`, `terms`.
- **Chuẩn hóa thuật ngữ:** *Buddha-anusmṛti* → *buddhānusmṛti*; thêm dạng Sanskrit cho các anussati; thêm Hán–Việt cho toàn bộ thuật ngữ chính; thêm dòng **Thuật ngữ** vào từng bài khi cần.
- **Bổ sung bảng đối chiếu thuật ngữ** 5 cột ở cuối tài liệu.
- **Nâng cấp phần nguồn:** chia theo tầng (Kinh tạng / chú giải / Đại thừa / Việt Nam / thế tục) và gắn nguồn với mã bài cụ thể.

## TÁI CẤU TRÚC TAXONOMY Ở v3.6

- **Gỡ nhóm H (Tra cứu & công cụ):** [M162] chuyển vào **B8. Câu hỏi thường gặp về Thiền** (nhánh B, cấp độ R); M160, M161 và M163 **nghỉ hưu**, không tái sử dụng.
- **G1 và G2 phân cấp thành mục con:** G1.1–G1.8 và G2.1–G2.12 — mỗi nhánh con là một mục riêng trong cả TAXONOMY TREE lẫn DANH MỤC BÀI VIẾT.
- Đồng bộ các tham chiếu M160/M163 còn sót trong tài liệu; cập nhật thống kê mã và phân bố cấp độ.

## TÁI CẤU TRÚC TAXONOMY Ở v3.5

- Phân cấp **E1. Truyền thống Theravāda** thành E1.1–E1.4: tổng quan → các khung/phương thức cốt lõi → hệ thống Thiền hiện đại và dòng truyền thừa → kinh điển và hệ chú giải.
- Phân cấp **E2. Truyền thống Đại thừa (Mahāyāna)** thành E2.1–E2.6: tổng quan/chỉ–quán → Thiền tông nhập môn → Niệm Phật/Tịnh độ → Thiền–Tịnh → Thiền tông chuyên sâu → các hướng quán chiếu và tu tâm Đại thừa; trong E2.1, [M137] nằm dưới cụm Chỉ–Quán (Zhǐguān) như một hệ thống cụ thể.
- Phân cấp **E3. Truyền thống Kim Cương thừa (Vajrayāna)** thành E3.1–E3.5: tổng quan → nền tảng đường tu và thực hành tiền hành → Thiền chỉ/Thiền tuệ → phương tiện đặc thù → thực hành cao cấp và yêu cầu truyền thừa.
- Đồng bộ **TAXONOMY TREE** và **DANH MỤC BÀI VIẾT** cho toàn bộ E1–E3; các cụm E1.x/E2.x/E3.x là nhóm học tập bên trong truyền thống, không phải truyền thống độc lập.
- Cập nhật **Lộ trình học – Bước 6** để trình tự tìm hiểu Theravāda/Mahāyāna/Vajrayāna khớp với cấu trúc mới; các bài L5 vẫn để ở Bước 7.

## TÁI CẤU TRÚC TAXONOMY Ở v3.4

- Đồng bộ **TAXONOMY TREE** với phần **DANH MỤC BÀI VIẾT**; không còn tình trạng cây cấp cao vẫn phẳng trong khi danh mục bên dưới đã phân nhóm.
- A được chia thành **A1–A7** theo hành trình người mới: hiểu về Thiền → hiểu cách hành Thiền → an toàn → chuẩn bị → trong/sau buổi Thiền → xây dựng thói quen → hỗ trợ/chuyên sâu.
- B được chia thành **B1–B7** theo tiến trình kỹ năng: nền tảng thân/hơi thở → ổn định chú ý → xử lý xao lãng → quan sát → cân bằng → tích hợp đời sống → phản tư.
- C1 và C2 được phản ánh đầy đủ trong cây với các nhóm **C1.1–C1.5** và **C2.1–C2.6**, thay vì chỉ hiển thị hai nhánh phẳng.
- D1, D2 và D3 được duy trì theo quan hệ **tổng quan → nhóm thành phần → bài chi tiết**; D2 được ghi rõ quan hệ với D3, vì Brahmavihāra là một nhóm trong hệ thống 40 đề mục theo cách trình bày của Visuddhimagga.
- Chuyển **[M054] Chọn đề mục phù hợp với mình** về đúng nhóm **D3.1. Tổng quan, phân loại và lựa chọn**, đồng thời cập nhật trình tự lộ trình tương ứng.
- Sửa các heading Markdown trùng/lặp và căn chỉnh cấp heading của phần danh mục bài viết theo cây taxonomy.


- **Không coi A–G là bảy "loại Thiền" ngang hàng.** Mỗi nhóm được gắn với một bản chất thông tin riêng: nền tảng, kỹ năng, phương thức, khung/pháp hành, truyền thống, địa vực và ứng dụng/bối cảnh.
- **Gộp Samatha và Vipassanā vào nhóm C — phương thức / hướng tu tập**, vì đây là hai `method` cốt lõi.
- **Đưa Satipaṭṭhāna, Brahmavihāra và Kammaṭṭhāna vào nhóm D — khung / hệ thống pháp hành**, nhưng vẫn phân biệt nội bộ: Satipaṭṭhāna là `framework`, Brahmavihāra là `practice_group`, Kammaṭṭhāna là `object_taxonomy`.
- **Gộp Theravāda, Mahāyāna và Vajrayāna vào nhóm E — truyền thống / dòng Thiền**, là nơi phù hợp để mô tả truyền thống thay vì dùng truyền thống như thuộc tính duy nhất của mọi bài.
- **Đưa Phật giáo Việt Nam vào nhóm F — bối cảnh văn hóa / địa vực**, vì nhánh này bao quát nhiều dòng khác nhau cùng hiện diện tại Việt Nam.
- **Gộp Thiền ứng dụng & đời sống và Thiền sức khỏe / thế tục vào nhóm G**, vì cả hai đều mô tả bối cảnh sử dụng và mục tiêu ứng dụng, không phải một "phái".
- **Chuẩn hóa tiêu đề:** ưu tiên tiếng Việt trước, thuật ngữ Pāli/Sanskrit đặt phía sau trong ngoặc đơn, ví dụ `Thiền chỉ (Samatha)`, `Bốn niệm xứ (Satipaṭṭhāna)`, `Tứ vô lượng tâm (Brahmavihāra)`.

## Đề xuất cho vòng sau
1. Viết trước 25 bài L1 để có một lộ trình hoàn chỉnh cho người mới, rồi mới mở rộng.
2. Mỗi bài L1–L2 nên có kèm **một bài thực hành có hướng dẫn** (audio/script) — hiện danh mục mới chỉ có phần lý thuyết.
3. Nhờ ít nhất một vị tăng/ni hoặc giáo thọ của mỗi truyền thống đọc soát các nhóm A–G trước khi xuất bản.

## Thống kê bản v3.6
- Tổng số bài: **158** (v2: 161; taxonomy được tái cấu trúc và phân cấp tiếp ở v3.3–v3.6).
- Mã đang dùng: M001–M163, trừ **M081** (đã nghỉ hưu, gộp vào M015), **M115** (để trống, chưa dùng) và **M160**, **M161**, **M163** (nghỉ hưu khi gỡ nhóm H ở v3.6).
- Mã kế tiếp khi thêm bài mới: **M164**.
- Phân bố cấp độ: L1 ≈ 40 bài · L2 ≈ 45 · L3 ≈ 40 · L4 ≈ 23 · L5 ≈ 7 · R ≈ 3.
- Taxonomy cấp cao: **7 nhóm** (A–G); A/B/C/D đều có phân nhóm nội bộ, trong đó C phân biệt hai `method`, D phân biệt `framework` / `practice_group` / `object_taxonomy`.
