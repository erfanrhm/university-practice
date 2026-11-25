# Chapter 3  — Initial API Contract

## Resources
- **User**: `id`, `name`, `email`
- **Task**: `id`, `title`, `description`, `status`, `userId`, `createdAt`

Allowed task statuses: `TODO`, `IN_PROGRESS`, `DONE`.

## Base URL
`/api/v1`

## Endpoint summary

### Users
| Method | Endpoint | Purpose | Success status |
|---|---|---|---|
| GET | `/users` | List users | 200 OK |
| POST | `/users` | Create a user | 201 Created |
| GET | `/users/{userId}` | Get one user | 200 OK |
| PUT | `/users/{userId}` | Replace/update a user | 200 OK |
| DELETE | `/users/{userId}` | Delete a user | 204 No Content |

### Tasks
| Method | Endpoint | Purpose | Success status |
|---|---|---|---|
| GET | `/tasks` | List tasks; optional `userId` and `status` filters | 200 OK |
| POST | `/tasks` | Create a task | 201 Created |
| GET | `/tasks/{taskId}` | Get one task | 200 OK |
| PUT | `/tasks/{taskId}` | Replace/update a task | 200 OK |
| PATCH | `/tasks/{taskId}/status` | Change task status | 200 OK |
| DELETE | `/tasks/{taskId}` | Delete a task | 204 No Content |

## Common status codes
- `200 OK`: request completed successfully.
- `201 Created`: a new resource was created.
- `204 No Content`: deletion succeeded; response has no body.
- `400 Bad Request`: invalid input or validation error.
- `404 Not Found`: requested user/task does not exist.
- `409 Conflict`: duplicate email or another resource conflict.
- `500 Internal Server Error`: unexpected server-side error.

## Error response example
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request data is invalid."
  }
}
```
فعالیت کلاسی ۵ 

معرفی پروژه:

در این فعالیت، یک پروژه فرضی با عنوان سیستم مدیریت اطلاعات دانشجویان (Student Management System) در نظر گرفته شده است.
---

1. طراحی پنج Test Case 

برای پروژه مدیریت اطلاعات دانشجویان، پنج Test Case زیر طراحی شده است:

شماره| عنوان Test Case| ورودی (Input)| نتیجه مورد انتظار (Expected Result)| وضعیت
TC-01| ثبت‌نام دانشجوی جدید| نام، شماره دانشجویی و معدل معتبر| ثبت موفق اطلاعات دانشجو| موفق
TC-02| ثبت شماره دانشجویی تکراری| شماره دانشجویی که قبلاً ثبت شده است| نمایش پیام خطا و جلوگیری از ثبت تکراری| ناموفق
TC-03| وارد کردن معدل نامعتبر| معدل منفی مانند 5-| نمایش پیام خطا و رد مقدار نامعتبر| ناموفق
TC-04| جستجوی دانشجو| شماره دانشجویی معتبر و موجود| نمایش اطلاعات دانشجوی موردنظر| موفق
TC-05| حذف اطلاعات دانشجو| شماره دانشجویی یک دانشجوی موجود| حذف اطلاعات و نمایش پیام موفقیت| موفق

توضیح جدول

- شماره: شناسه اختصاصی هر تست است.
- عنوان Test Case: عملیاتی است که قرار است بررسی شود.
- ورودی (Input): اطلاعاتی است که برای اجرای تست وارد می‌کنیم.
- نتیجه مورد انتظار: خروجی صحیحی است که باید از سیستم دریافت کنیم.
- وضعیت: نتیجه اجرای فرضی تست را مشخص می‌کند.

---

2. رسم یک Pipeline مفهومی

       نوشتن کد برنامه
              |
              v
      ارسال کد به GitHub
              |
              v
        ساخت پروژه (Build)
              |
              v
       اجرای تست‌ها (Test)
              |
              v
     ساخت Docker Image
              |
              v
       انتشار برنامه (Deploy)
              |
              v
           پایان

توضیح مراحل Pipeline

1. Code Development: برنامه‌نویس کدهای پروژه را می‌نویسد.
2. Code Push: کدهای نوشته‌شده به مخزن GitHub ارسال می‌شوند.
3. Build: پروژه ساخته و برای اجرا آماده می‌شود.
4. Test Execution: تست‌های طراحی‌شده روی برنامه اجرا می‌شوند.
5. Docker Build: در صورت موفقیت تست‌ها، Docker Image ساخته می‌شود.
6. Deploy: برنامه در محیط موردنظر منتشر و اجرا می‌شود.

---

3. مشخص کردن مرحله شکست Test

در Pipeline ممکن است در هر مرحله خطا یا مشکلی به وجود بیاید.

برای مثال، فرض می‌کنیم در پروژه مدیریت اطلاعات دانشجویان، سیستم اجازه ثبت شماره دانشجویی تکراری را بدهد.

در این حالت Test Case شماره 2 با شکست مواجه می‌شود.

مراحل وقوع شکست

1. کد برنامه به GitHub ارسال می‌شود.
2. مرحله Build با موفقیت انجام می‌شود.
3. تست‌های برنامه اجرا می‌شوند.
4. در Test Case شماره 2، سیستم نمی‌تواند شماره دانشجویی تکراری را تشخیص دهد.
5. تست با شکست مواجه می‌شود.
6. Pipeline متوقف می‌شود و مراحل بعدی اجرا نمی‌شوند.

نمودار مرحله شکست

       Code Push
           |
           v
       Build
           |
           v
     Test Execution
           |
           v
    Test Case 2 Failed
           |
           v
    Pipeline متوقف می‌شود
           |
           v
    رفع خطا و اجرای مجدد تست

نتیجه: در صورت شکست تست، Pipeline متوقف می‌شود و تا زمانی که مشکل برطرف نشود، مراحل بعدی مانند ساخت Docker Image و انتشار برنامه انجام نمی‌شوند.

---

4. توضیح ارتباط Pipeline با Docker

Docker ابزاری برای بسته‌بندی و اجرای نرم‌افزارها در محیطی به نام Container است.

این ابزار کمک می‌کند برنامه همراه با وابستگی‌ها و تنظیمات موردنیاز خود در محیط‌های مختلف به شکل یکسان اجرا شود.

ارتباط Docker با Pipeline

1. ابتدا برنامه‌نویس کدهای پروژه را می‌نویسد.
2. کدها به مخزن GitHub ارسال می‌شوند.
3. Pipeline به‌صورت خودکار مراحل ساخت و تست برنامه را اجرا می‌کند.
4. اگر تمام تست‌ها موفق باشند، Docker یک Image از برنامه ایجاد می‌کند.
5. این Image می‌تواند روی سرور یا محیط‌های دیگر اجرا شود.
6. در نهایت برنامه برای استفاده کاربران منتشر می‌شود.

مزایای استفاده از Docker در Pipeline

- اجرای یکسان برنامه در محیط‌های مختلف.
- ساده‌تر شدن انتقال نرم‌افزار به سرور.
- مدیریت بهتر وابستگی‌های برنامه.
- آسان‌تر شدن فرایند انتشار و استقرار نرم‌افزار.

---

