# Resume Evidence Audit

**A structured AI workflow for evaluating resume evidence against a target job description.**

How do you prepare a CV for screening without spending months revising its wording and layout? Resume Evidence Audit turns that process into a documented assessment: identify the role's requirements, locate supporting evidence, distinguish presentation issues from qualification gaps, and prioritize revisions.

The system evaluates how clearly a resume documents relevant qualifications. It supports students, transfer students, early-career applicants, experienced professionals, and career changers.

[English](#english) · [Tiếng Việt](#tiếng-việt)

---

## English

### System overview

Resume Evidence Audit is an instruction-based AI skill with the internal name `evaluate-resume`. It combines a structured evaluation rubric, evidence-mapping rules, report specifications, and a Python scoring utility.

The AI assistant interprets the supplied documents and performs the assessment. The scoring utility validates checklist identifiers and calculates summaries from recorded observations; it does not evaluate qualifications or verify claims independently.

The workflow maintains three separate assessment dimensions:

| Dimension | Evaluation question |
| --- | --- |
| Document integrity | Are relevant details readable, extractable, and associated with the correct section, role, and dates? |
| Requirement evidence | Which job requirements are supported by explicit resume content, and at what scope? |
| Communication quality | Do the structure, bullets, and project descriptions make that evidence clear and relevant? |

This separation prevents polished wording from concealing missing evidence and prevents a document-format issue from being treated as a qualification gap.

### Evaluation workflow

| Stage | System operation | Result |
| --- | --- | --- |
| 1. Scope definition | Establish the resume version, target role, job description, career stage, and available inspection tools. Evaluate one job description at a time. | Assessment boundary and review mode |
| 2. Document inspection | Inspect rendered appearance and extracted reading order when supported. Trace section boundaries and employer–title–date–bullet associations. | Document-integrity findings and inspection limitations |
| 3. Requirement decomposition | Extract five requirement groups. Preserve required/preferred distinctions, alternatives, equivalency clauses, experience thresholds, and timing. | Structured job specification |
| 4. Evidence mapping | Match each required/preferred requirement and major responsibility to explicit resume content with a stable locator. | Requirement-to-evidence matrix |
| 5. Rubric assessment | Apply the 100-check rubric across nine scored domains; review experience bullets and project contributions. | Item-level observations, category scores, and coverage |
| 6. Revision prioritization | Classify issues and order changes by their effect on target positioning, requirement visibility, document integrity, and evidence quality. | Prioritized action plan |
| 7. Report generation | Present findings, evidence, limitations, and supported before/after revisions. Keep unconfirmed facts separate from usable edits. | Reviewable audit report |

#### Requirement decomposition

The job description is organized into five groups:

1. Required technical skills, with preferred skills identified separately.
2. Tools and platforms.
3. Core responsibilities and expected outputs.
4. Industry and domain terminology.
5. Education and certifications.

Each requirement retains its source wording, strength, acceptable aliases, expected scope, and timing. For example, **“Python or R” remains one alternative group**, rather than becoming two mandatory requirements. Application conditions such as location or availability are tracked separately when explicitly stated.

#### Evidence mapping and issue classification

The evidence matrix records:

| Field | Purpose |
| --- | --- |
| Requirement ID and strength | Identify the criterion and distinguish required, preferred, contextual, or ambiguous wording |
| Resume evidence and locator | Cite the relevant page, section, role/project, or bullet |
| Evidence rating | Record the strength of documented support on the 0–2 scale |
| Relationship | Distinguish direct, transferable, partial, not evidenced, or contradicted support |
| Issue classification | Separate wording/visibility issues, facts requiring confirmation, and qualification development |
| Recommended action | Specify the next revision or information needed |

A technology mentioned in a Skills section establishes term presence; contextual experience demonstrates application. A requirement absent from the resume is recorded as **not evidenced**, unless supplied facts establish an actual qualification gap.

### Scoring methodology

| Value | Definition |
| --- | --- |
| **0** | Evidence is absent or unclear |
| **1** | Evidence is present but weak, partial, or inconsistent |
| **2** | Evidence is clear, relevant, and supported at the required scope |
| **U** | Assessment is unavailable because necessary information or inspection is missing |
| **NA** | The check is genuinely inapplicable |

Every checklist item records a rating, evidence, location, rationale, and proposed fix. Reports show category points and possible points, counts of scored/unknown/inapplicable checks, and assessment coverage. Requirement coverage is reported separately from presentation quality. An overall score is not produced by default.

The ratings are an internal review framework. They do not represent an employer's ATS score, an independently verified measure of ability, or an interview probability. The same scoring rules structure the review, but model-generated judgments can vary and remain open to human review.

### Bullet and project analysis

Experience bullets are reviewed for **action, object, method, scope, result, and relevance**. These components guide diagnosis; every bullet does not need all six, and numerical metrics are not mandatory.

Project reviews examine the objective, individual contribution, technologies, workflow, outputs, and status. For technical projects, the review also considers implementation, evaluation, error handling, deployment, and demonstrated reliability where relevant. Class projects, local applications, volunteer work, and unfinished projects can provide evidence when their scope is stated accurately.

**Illustrative revision — appropriate only when the underlying work supports it:**

> Before: Used Python for data analysis.
>
> After: Cleaned survey data with Python and pandas and summarized response patterns for an institutional research report.

The revision clarifies the action, method, and output without inventing a performance metric.

### Operating modes and inputs

| Supplied material | Mode | Assessment scope |
| --- | --- | --- |
| Resume + job description | Targeted | Evaluate evidence against one role's documented requirements |
| Resume only | General | Review evidence and structure; mark job-dependent checks unknown |
| Screenshot or image | Visual only | Assess readable visible content; leave actual file extraction unverified |
| Job description only | Requirement analysis | Produce requirement lists and an evidence-gathering plan |
| Neither | Input request | Request the resume and job description before assessment |

PDF and DOCX inspection requires appropriate file-processing tools in the host environment. Pasted text supports content review, but does not establish that the original file was parsed correctly.

### Setup and usage

1. Obtain the complete skill package and preserve `SKILL.md`, `references/`, and `scripts/` together.
2. Install the package using your AI assistant's documented skill-loading process. The internal skill name is `evaluate-resume`.
3. Provide the current resume and the complete job description for one target role.
4. Invoke the skill with the prompt below.

The README is documentation, not the executable skill package. If the assistant does not support installation, it must still be able to read the skill instructions and referenced resources. File-inspection and Python features depend on the tools available to that assistant.

#### Package responsibilities

| Resource | Responsibility |
| --- | --- |
| `SKILL.md` | Workflow, evidence boundaries, operating modes, and revision rules |
| `references/rubric.md` | Complete checklist and stable check identifiers |
| `references/scoring.md` | Scoring and aggregation conventions |
| `references/report-template.md` | Required report structure |
| `references/research.md` | Research context and distinctions among external findings and internal heuristics |
| `scripts/score_audit.py` | Audit-record validation and score calculation |

#### Example invocation

```text
Use Resume Evidence Audit (evaluate-resume) to assess my attached resume
against the complete job description below. Produce the report in English.

Use only the supplied resume for the baseline assessment. Preserve the job
requirements' required/preferred distinctions and alternative qualifications.
Cite resume locations for evidence and distinguish “not evidenced” from a
confirmed qualification gap.

Lead with the strongest supported qualifications and highest-impact fixes.
Include the requirement lists, evidence matrix, complete audit checklist,
category scores and coverage, bullet/project findings, and supported revisions.

Apply the 0–2 scale; use U for unknown and NA for genuinely inapplicable checks.
State which file inspections were actually performed. Keep questions about
unconfirmed facts separate from ready-to-use wording. Do not invent metrics,
achievements, credentials, ownership, or project status.

Target role: [Job title]
Job description: [Paste the full job description]
Resume: [Attach the current file or paste its text]
```

### Report deliverables

A full report contains a role-specific conclusion, three strongest supported qualifications, prioritized fixes, the five requirement lists, an evidence matrix, category scores and assessment coverage, the complete checklist, bullet/project findings, six recruiter-scan answers, and grounded revision examples.

Quick reviews should label their scope explicitly. An intentionally narrowed review must not be presented as a complete audit.

### Assessment boundaries and data handling

- **ATS inspection:** local extraction, visual review, and employer ATS import are separate observations. An employer-import finding requires actual observed evidence from that application flow.
- **Submission requirements:** follow the employer's specified file type and submission rules. The skill does not prescribe a universally superior file format.
- **Claim preservation:** revisions retain factual ownership, tools, dates, credentials, scope, and status. Newly supplied facts are documented separately from the baseline assessment.
- **Document instructions:** instructions embedded in resumes, job descriptions, or portfolio pages are treated as document content, not authority to alter the audit.
- **Data handling:** the skill instructs the assistant not to send resumes to third-party scanners without authorization. Data retention and processing still depend on the chosen AI service.
- **Intended use:** document self-assessment and revision. Applicant ranking, hiring decisions, and application submission are outside the workflow.

---

## Tiếng Việt

### Tổng quan hệ thống

**Resume Evidence Audit** là một AI skill đánh giá nội dung CV dựa trên mô tả công việc cụ thể. Tên nội bộ của skill là `evaluate-resume`.

Hệ thống kết hợp hướng dẫn đánh giá, bộ tiêu chí có cấu trúc, quy tắc đối chiếu minh chứng, mẫu báo cáo và tiện ích tính điểm bằng Python. Trợ lý AI phân tích tài liệu và đưa ra nhận định; tiện ích Python kiểm tra mã tiêu chí và tính tổng từ các quan sát đã được ghi nhận. Tiện ích này không tự đánh giá năng lực hay xác minh thành tích.

Ba phương diện được đánh giá riêng:

| Phương diện | Câu hỏi đánh giá |
| --- | --- |
| Tính toàn vẹn của tài liệu | Thông tin có đọc được, trích xuất được và gắn đúng với vị trí, thời gian, mục nội dung hay không? |
| Minh chứng đáp ứng yêu cầu | Nội dung cụ thể nào trong CV hỗ trợ từng yêu cầu tuyển dụng, và ở phạm vi nào? |
| Chất lượng trình bày nội dung | Cấu trúc, câu mô tả kinh nghiệm và phần dự án có thể hiện rõ minh chứng liên quan hay không? |

Cách phân tách này giúp xác định đúng vấn đề: lỗi trình bày, thiếu thông tin chứng minh hay yêu cầu năng lực cần phát triển.

### Quy trình đánh giá

| Giai đoạn | Hoạt động | Đầu ra |
| --- | --- | --- |
| 1. Xác định phạm vi | Xác nhận phiên bản CV, vị trí, mô tả công việc và công cụ có thể sử dụng; đánh giá từng vị trí riêng biệt | Phạm vi và chế độ đánh giá |
| 2. Kiểm tra tài liệu | Xem bố cục và thứ tự văn bản được trích xuất khi có công cụ hỗ trợ; kiểm tra liên kết giữa công ty, chức danh, thời gian và nội dung | Phát hiện về tính toàn vẹn và giới hạn kiểm tra |
| 3. Phân rã yêu cầu | Tách yêu cầu thành năm nhóm; giữ nguyên điều kiện bắt buộc, ưu tiên, lựa chọn thay thế, tương đương và thời điểm đáp ứng | Bộ yêu cầu có cấu trúc |
| 4. Đối chiếu minh chứng | Gắn từng yêu cầu và trách nhiệm chính với nội dung cụ thể trong CV | Ma trận yêu cầu–minh chứng |
| 5. Áp dụng bộ tiêu chí | Đánh giá 100 tiêu chí thuộc chín nhóm; phân tích kinh nghiệm và đóng góp trong dự án | Nhận định từng tiêu chí, điểm từng nhóm và phạm vi đánh giá |
| 6. Ưu tiên chỉnh sửa | Phân loại vấn đề theo định vị ứng tuyển, khả năng nhận diện năng lực, tính toàn vẹn và chất lượng minh chứng | Kế hoạch chỉnh sửa theo thứ tự ưu tiên |
| 7. Tổng hợp báo cáo | Trình bày kết luận, căn cứ, giới hạn và ví dụ chỉnh sửa; tách thông tin cần xác nhận | Báo cáo có thể kiểm tra lại |

### Mô hình yêu cầu và minh chứng

Mô tả công việc được chia thành năm nhóm: **kỹ năng chuyên môn; công cụ và nền tảng; trách nhiệm và đầu ra; thuật ngữ lĩnh vực; học vấn và chứng chỉ**.

Hệ thống giữ nguyên logic của yêu cầu. Ví dụ, “Python hoặc R” được xem là một nhóm lựa chọn thay thế, không chuyển thành hai yêu cầu bắt buộc. Các điều kiện ứng tuyển được nêu rõ, như địa điểm hoặc thời gian có thể làm việc, được theo dõi riêng.

Mỗi dòng trong ma trận ghi nhận mã và mức độ yêu cầu, nội dung minh chứng cùng vị trí trong CV, điểm đánh giá, mối quan hệ với yêu cầu, loại vấn đề và hành động đề xuất.

Việc ghi một công cụ trong mục Skills thể hiện sự hiện diện của thuật ngữ; mô tả cách sử dụng công cụ trong công việc cung cấp minh chứng về khả năng ứng dụng. Khi CV chưa đề cập một năng lực, kết luận mặc định là **chưa được thể hiện trong tài liệu**, không tự suy ra ứng viên không có năng lực đó.

Vấn đề được phân loại thành: cách diễn đạt/khả năng nhận diện thông tin, dữ kiện cần xác nhận và năng lực cần phát triển khi đã có căn cứ xác định.

### Phương pháp chấm điểm

| Giá trị | Định nghĩa |
| --- | --- |
| **0** | Chưa có minh chứng hoặc nội dung chưa rõ |
| **1** | Có minh chứng nhưng còn yếu, chưa đầy đủ hoặc thiếu nhất quán |
| **2** | Minh chứng rõ ràng, phù hợp và đáp ứng phạm vi yêu cầu |
| **U** | Chưa đủ thông tin hoặc chưa thực hiện được việc kiểm tra cần thiết |
| **NA** | Tiêu chí thực sự không áp dụng |

Mỗi tiêu chí có điểm, minh chứng, vị trí tham chiếu, lý do và đề xuất chỉnh sửa. Báo cáo nêu điểm đạt/tối đa của từng nhóm, số tiêu chí đã chấm/chưa xác định/không áp dụng và phạm vi đã đánh giá. Mức độ thể hiện yêu cầu tuyển dụng được trình bày riêng với chất lượng diễn đạt; mặc định không tạo một điểm tổng.

Đây là thang đánh giá nội bộ, không phải điểm ATS của nhà tuyển dụng, kết quả xác minh năng lực hay xác suất được phỏng vấn. Nhận định của mô hình có thể thay đổi và cần được người dùng xem xét.

### Phân tích kinh nghiệm và dự án

Các câu mô tả kinh nghiệm được xem xét theo **hành động, đối tượng, phương pháp, phạm vi, kết quả và mức độ liên quan**. Không bắt buộc mọi câu phải có đủ sáu thành phần hoặc số liệu định lượng.

Phần dự án được xem xét theo mục tiêu, đóng góp cá nhân, công nghệ, quy trình, đầu ra và trạng thái thực hiện. Với dự án kỹ thuật, việc triển khai, đánh giá, xử lý lỗi và độ tin cậy được xem xét khi phù hợp. Dự án môn học, ứng dụng chạy cục bộ hoặc công việc chưa hoàn thành vẫn có thể là minh chứng nếu phạm vi được mô tả chính xác.

### Chế độ hoạt động

| Tài liệu được cung cấp | Phạm vi đánh giá |
| --- | --- |
| CV và mô tả công việc | Đánh giá theo yêu cầu của một vị trí cụ thể |
| Chỉ có CV | Đánh giá minh chứng và cấu trúc; các tiêu chí phụ thuộc vị trí được đánh dấu chưa xác định |
| Chỉ có ảnh chụp | Đánh giá nội dung nhìn thấy; chưa xác minh khả năng trích xuất của file gốc |
| Chỉ có mô tả công việc | Phân tích yêu cầu và lập kế hoạch thu thập minh chứng |
| Chưa có cả hai | Yêu cầu cung cấp tài liệu trước khi đánh giá |

Kiểm tra PDF/DOCX phụ thuộc vào công cụ xử lý file trong môi trường sử dụng. Nội dung được dán dưới dạng văn bản không chứng minh rằng file gốc được đọc đúng.

### Cài đặt và sử dụng

1. Lấy trọn bộ skill; giữ `SKILL.md`, `references/` và `scripts/` cùng nhau.
2. Cài đặt theo hướng dẫn nạp skill của trợ lý AI đang sử dụng. Tên nội bộ là `evaluate-resume`.
3. Cung cấp CV hiện tại và toàn bộ mô tả công việc của một vị trí.
4. Sử dụng prompt bên dưới.

README là tài liệu hướng dẫn. Nếu nền tảng không hỗ trợ cài skill, trợ lý vẫn cần đọc được hướng dẫn và các tài liệu tham chiếu. Chức năng kiểm tra file và chạy Python phụ thuộc vào công cụ của nền tảng.

Các tài nguyên chính gồm `SKILL.md` cho quy trình; `references/rubric.md` cho bộ tiêu chí; `references/scoring.md` cho quy tắc tính điểm; `references/report-template.md` cho cấu trúc báo cáo; `references/research.md` cho bối cảnh nghiên cứu; và `scripts/score_audit.py` cho kiểm tra bản ghi và tính điểm.

#### Prompt mẫu

```text
Sử dụng Resume Evidence Audit (evaluate-resume) để đánh giá CV đính kèm
với toàn bộ mô tả công việc bên dưới. Trả lời bằng tiếng Việt.

Chỉ sử dụng CV được cung cấp để đánh giá ban đầu. Giữ nguyên sự phân biệt
bắt buộc/ưu tiên và các lựa chọn năng lực thay thế trong yêu cầu tuyển dụng.
Dẫn vị trí cụ thể trong CV cho từng minh chứng. Phân biệt thông tin chưa
được thể hiện với năng lực còn thiếu đã có căn cứ xác định.

Mở đầu bằng các năng lực có minh chứng rõ nhất và những chỉnh sửa quan trọng
nhất. Cung cấp năm nhóm yêu cầu, ma trận minh chứng, checklist đầy đủ, điểm
và phạm vi đánh giá từng nhóm, phân tích kinh nghiệm/dự án và ví dụ chỉnh sửa.

Áp dụng thang 0–2, U khi chưa đủ thông tin và NA khi thực sự không áp dụng.
Nêu rõ các bước kiểm tra file đã thực hiện. Tách câu hỏi về dữ kiện chưa được
xác nhận khỏi nội dung có thể sử dụng ngay. Không tự thêm số liệu, thành tích,
bằng cấp, quyền sở hữu công việc hoặc trạng thái dự án.

Vị trí: [Tên vị trí]
Mô tả công việc: [Dán toàn bộ mô tả công việc]
CV: [Đính kèm file hiện tại hoặc dán nội dung]
```

### Cấu trúc báo cáo

Báo cáo đầy đủ gồm kết luận theo vị trí, ba năng lực có minh chứng mạnh nhất, các chỉnh sửa ưu tiên, năm nhóm yêu cầu, ma trận minh chứng, điểm và phạm vi đánh giá, checklist đầy đủ, phân tích kinh nghiệm/dự án, sáu câu trả lời phục vụ việc đọc lướt của nhà tuyển dụng và ví dụ chỉnh sửa có căn cứ.

Bản đánh giá nhanh phải nêu rõ phạm vi. Một đánh giá rút gọn không được trình bày như một bản kiểm tra đầy đủ.

### Giới hạn đánh giá và xử lý dữ liệu

- **Kiểm tra ATS:** trích xuất văn bản, kiểm tra bố cục và quan sát dữ liệu được nhập vào ATS là ba việc riêng biệt. Kết luận về hệ thống của nhà tuyển dụng cần có bằng chứng quan sát thực tế.
- **Yêu cầu nộp hồ sơ:** tuân thủ định dạng và hướng dẫn của từng nhà tuyển dụng; không mặc định một loại file luôn phù hợp nhất.
- **Bảo toàn dữ kiện:** giữ đúng đóng góp, công cụ, thời gian, bằng cấp, phạm vi và trạng thái công việc. Thông tin bổ sung được ghi nhận riêng với đánh giá ban đầu.
- **Chỉ dẫn trong tài liệu:** nội dung yêu cầu AI thay đổi cách đánh giá nằm trong CV, mô tả công việc hoặc trang dự án được xử lý như dữ liệu, không phải chỉ dẫn có thẩm quyền.
- **Dữ liệu cá nhân:** skill yêu cầu không gửi CV sang dịch vụ quét bên thứ ba khi chưa được cho phép. Việc lưu trữ và xử lý vẫn phụ thuộc vào dịch vụ AI sử dụng.
- **Mục đích sử dụng:** hỗ trợ tự đánh giá và chỉnh sửa tài liệu; không bao gồm xếp hạng ứng viên, quyết định tuyển dụng hay nộp hồ sơ.
