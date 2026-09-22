# QUY CHUẨN VIẾT BÀI HỎI & ĐÁP PHẬT GIÁO (vi-VN)

> **Bộ nhớ công việc:** Mọi bài viết thuộc danh sách `_qa_vi-VN.md` phải tuân theo file này. Đọc lại file này TRƯỚC KHI viết mỗi bài, kể cả các phiên sau.

---

## 1. Các file trong dự án

| File | Vai trò |
|---|---|
| `_qa_vi-VN.md` | Danh sách các bài cần viết (mã Q.xN). Viết tất cả **trừ** Q.A1, Q.A2, Q.A3. |
| `_general_buddhism_vi-VN.md` | Phân loại Phật giáo phổ thông (mã G.x / GBxxx) — dùng để tham chiếu chéo. |
| `_meditation_theory_vi-VN.md` | Phân loại kiến thức Thiền (mã M.x) — dùng để tham chiếu chéo. |
| `Q_A1_an_thit_co_tao_nghiep_sat_sinh_khong.md` / `.html` | Bài mẫu đã hoàn thiện — tham khảo cấu trúc và giọng văn. |
| `Q_*.md` | Nội dung soạn sẵn **gợi ý câu trả lời** cho từng bài (tham khảo để viết bài .html tương ứng). |

---

## 2. Quy tắc đặt tên và tiêu đề

- Tên file HTML: `Q_<mã>_<tên-bài-viết-không-dấu>.html` — giống chính xác tên file `.md` tương ứng, chỉ đổi đuôi thành `.html`.
  - Ví dụ: `Q.D5.2` → file `Q_D5_2_...html`; bài Q.A1 → `Q_A1_an_thit_co_tao_nghiep_sat_sinh_khong.html`.
- `<title>` và `<h1>`: `Q.xN. Tên bài viết` (viết hoa đúng quy tắc tiếng Việt).
- Gộp các mục con thành **1 bài viết**; các mục con là **danh sách mục lục**. Nếu chỉ có 1 mục con thì xem nội dung, nếu đủ dài vẫn nên thêm mục lục.

---

## 3. Cấu trúc file HTML (chuẩn chung)

1. HTML hoàn chỉnh, `lang="vi"`, UTF-8, CSS nhúng trực tiếp (không phụ thuộc CDN, dùng được độc lập trên mọi nền tảng).
2. Đầu bài: kicker "Hỏi & Đáp Phật giáo" + `<h1>` (mã + tên bài) + phụ đề/trích dẫn mở đầu.
3. Hộp **"Trả lời ngắn gọn"** ngay sau tiêu đề.
4. **Mục lục** (nav.toc) liệt kê các mục con của bài, có link neo.
5. Thân bài chia các `<section>` có `id` khớp mục lục. Có thể gộp/bổ sung mục con của file `.md` cho hợp lý.
6. Cuối bài: **"Chú giải"** (giải thích từ lạ, từ Pali/Sanskrit/Hán-Việt hay dùng, cho người mới) + **"Nguồn kinh điển"** (danh sách nguồn đã dùng, kèm mã kinh và truyền thống) + ghi chú cần thiết.

---

## 4. Nguyên tắc nội dung

- Ngôn từ dễ hiểu, an toàn. **KHÔNG tự bịa** giáo lý, kinh văn, trích dẫn.
- Các marker kiểu `citeturn627474search1` trong file `.md` là rác từ công cụ tìm kiếm — **luôn xóa sạch**, không đưa vào HTML.
- Không diễn đạt kiểu "2 bài còn lại trong nhóm", "bài này khép lại…", "chỉ có… bài" — danh sách bài sẽ còn được bổ sung dần.
- **Không dùng** "trong app", "của app", "app Buddha" — nội dung phải dùng được trên nhiều nền tảng. Phần "Gợi ý thông điệp kết cho app" trong file `.md` phải chuyển thành lời kết neutral.
- Mỗi bài phải tự trọn vẹn (standalone), người mới đọc không cần bài trước vẫn hiểu.

---

## 5. Quy tắc thuật ngữ (chỉ giải thích LẦN ĐẦU trong mỗi bài)

- Từ Pali/Sanskrit: từ tiếng Việt đứng trước, kèm Pali/Sanskrit + Anh trong ngoặc:
  - `chánh niệm (Pali: sati - Anh: mindfulness)`
  - `Thiền chỉ (Pali: Samatha - Anh: Tranquillity meditation)`
  - `Thiền quán (Pali: Vipassanā - Anh: Insight meditation)`
- Từ Hán Việt khó/phức tạp: dịch nghĩa ngắn trong ngoặc + Anh:
  - `sơn hà (núi sông - mountains and rivers)`
- Cụm từ phức tạp: dịch nghĩa trong ngoặc + Anh.
- Từ hay dùng bằng Pali/Sanskrit: `<từ Việt> (Pali: <từ Pali>)` hoặc `<từ Việt> (Pali: <từ Pali>, Anh: <từ Anh>)`.
- Ba truyền thống (format bắt buộc ở LẦN ĐẦU xuất hiện trong bài):
  - `Phật giáo Nam truyền (Thượng tọa bộ - Pali: Theravāda - Anh: Way of the Elders)` → lần sau chỉ: `Phật giáo Nam truyền`
  - `Phật giáo Đại thừa (Sanskrit: Mahāyāna - Anh: Great Vehicle)` → lần sau chỉ: `Phật giáo Đại thừa`
  - `Phật giáo Kim Cương thừa (Sanskrit: Vajrayāna - Anh: Diamond Vehicle)` → lần sau chỉ: `Phật giáo Kim Cương thừa`
- Giải thích chỉ xuất hiện ở lần xuất hiện **đầu tiên** trong bài; lần 2, 3… dùng tên ngắn.

---

## 6. Dẫn nguồn

- Khi một đoạn/ý trích hoặc dựa vào kinh nào, chèn dòng nguồn theo format:
  - Lần đầu: `[Nguồn: Kinh Tăng Chi Bộ, AN 2.31 (Aṅguttara Nikāya, AN 2.31) - Phật giáo Nam truyền (Thượng tọa bộ - Pali: Theravāda - Anh: Way of the Elders)]`
  - Các lần sau: `[Nguồn: Kinh Tăng Chi Bộ, AN 2.31 - Phật giáo Nam truyền]`
- Chỉ dẫn số hiệu kinh (SN, MN, AN, DN, Dhp…) khi **thực sự chắc chắn**. Nếu không chắc số hiệu, dùng cách nói mơ hồ chính đáng ("theo kinh điển Phật giáo sơ kỳ…") và **không bịa số kinh**.
- Cuối mỗi bài có mục "Nguồn kinh điển" liệt kê các nguồn đã dùng (tên kinh, mã, truyền thống).

---

## 7. Tham chiếu chéo phân loại

- Khi bài liên quan chủ đề trong phân loại khác, chèn ghi chú dạng: `(tham khảo: G.C5 – Vô ngã)` hoặc `(tham khảo: M.A1 – ...)`.
- Dùng tiết chế (1–3 lần/bài), chỉ khi thực sự phù hợp. KHÔNG nhân bản nội dung bài khác.

---

## 8. Giọng văn và an toàn nội dung

- Ấm áp, điềm tĩnh, không hù dọa, không lên án; phân biệt rõ **giáo lý** với **quan niệm dân gian / truyền thống cụ thể**.
- Nghiệp và khổ không dùng để đe dọa; luôn hướng về thực hành và chuyển hóa.
- Chủ đề nhạy cảm (tự sát, tang gia, tâm linh dân gian, "vong hồn", nhập hồn…): cẩn trọng, không tuyệt đối hóa, không khẳng định điều không chắc chắn, khuyến khích hỗ trợ chuyên môn (y tế/tâm lý) khi cần.
- Kết bài bằng thông điệp thực hành ngắn gọn, neutral (không nhắc "app").

---

## 9. Tiến độ viết bài

- [x] Q.A1–Q.A3 (đã có từ trước)
- [ ] Q.B1–Q.B8
- [ ] Q.C1–Q.C4
- [ ] Q.D1–Q.D5
- [ ] Q.E1–Q.E4
- [ ] Q.F1–Q.F6
- [ ] Q.G1–Q.G4
- [ ] Q.H1–Q.H5
- [ ] Q.I1–Q.I6
- [ ] Q.J1–Q.J4
