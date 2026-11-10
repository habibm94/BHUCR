# C3_wedding_accounts

- **Type:** complex reasoning (4 rules)
- **Answer type:** number
- **Final answer:** 5700
- **Calculation:** 100000 - 131800 - 500 - 2000 + 45000 - 7000 + 2000 = 5700

## Prompt
- BN: ছেলের বিয়ের অনুষ্ঠান করলাম। দেখোতো কত টাকা বাচল?
- EN: I held my son's wedding. How much money is left?

## Transcription
- BN: `tasks/C3_wedding_accounts/transcription.txt`
- EN: `transcription_en.txt` (this folder)

## Reading rubric
| ID | Bengali | English |
|---|---|---|
| R01 | হাতে থাকা ১০০০০০ টাকা পড়েছে? | Read cash in hand 100000? |
| R02 | ডেকোরেশন ৩০০০০ টাকা পড়েছে? | Read decoration 30000? |
| R03 | অতিথি খাওয়ানো খরচ ২০০০০ টাকা পড়েছে? | Read guests' meal 20000? |
| R04 | কনে বাড়ির উপহার খরচ ১০০০০ টাকা পড়েছে? | Read gift to bride's home 10000? |
| R05 | ভ্যানওয়ালা ৫০০ টাকা পাবে পড়েছে? | Read the van driver will get 500? |
| R06 | সাউন্ড খরচ ৫০০০ টাকা পড়েছে? | Read sound 5000? |
| R07 | পান-সুপারি ২০০০ টাকা পড়েছে? | Read paan-supari 2000? |
| R08 | শেরওয়ানী ৫০০০ টাকা পড়েছে? | Read sherwani 5000? |
| R09 | গেট বানানো ৩০০০ টাকা পড়েছে? | Read gate making 3000? |
| R10 | চা মিষ্টি ১৫০০ টাকা পড়েছে? | Read tea and sweets 1500? |
| R11 | গয়না ৩০০০০ টাকা পড়েছে? | Read jewellery 30000? |
| R12 | গাড়ি ভাড়া ১৩০০০ টাকা পড়েছে? | Read car hire 13000? |
| R13 | ক্যাটারিং সার্ভিস চার্জ ১২৩০০ টাকা পড়েছে? | Read catering 12300? |
| R14 | ক্যাটারিং আরো ২০০০ টাকা পাবে পড়েছে? | Read catering will get 2000 more? |
| R15 | রুবিনার সাহায্য ৫০০০ টাকা পড়েছে? | Read Rubina's help 5000? |
| R16 | কালামের সাহায্য ২০০০০ পড়েছে? | Read Kalam's help 20000? |
| R17 | কালামকে ৭০০০ টাকা ফেরত দিতে হবে পড়েছে? | Read 7000 must be returned to Kalam? |
| R18 | আলমের সাহায্য ১০০০০ টাকা পড়েছে? | Read Alam's help 10000? |
| R19 | আলম আরো ২০০০ টাকা আগামীকাল দেবে পড়েছে? | Read Alam will give 2000 more tomorrow? |
| R20 | জুনায়েদের সাহায্য ১০০০০ টাকা পড়েছে? | Read Junayed's help 10000? |

## Reasoning rubric
| ID | Bengali | English |
|---|---|---|
| L01 | হাতে থাকা ১০০০০০ টাকাকে শুরু ধরেছে? | Used 100000 as the start? |
| L02 | সব ব্যয় ১৩১৮০০ টাকা বাদ দিয়েছে? | Subtracted all expenses, 131800? |
| L03 | ভ্যানওয়ালার ৫০০ টাকা ব্যয়ে ধরেছে? | Added the van driver's 500 to expenses? |
| L04 | ক্যাটারিংয়ের বাকি ২০০০ টাকা ব্যয়ে ধরেছে? | Added the catering's 2000 due to expenses? |
| L05 | সব সাহায্যের ৪৫০০০ টাকা যোগ করেছে? | Added all help, 45000? |
| L06 | কালামের ৭০০০ টাকা ফেরত বাদ দিয়েছে? | Subtracted Kalam's 7000 refund? |
| L07 | আলমের আগামীকালকের ২০০০ টাকা সাহায্যের হিসাবে যুক্ত করেছে? | Added Alam's 2000 coming tomorrow to the help? |
