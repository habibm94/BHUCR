# C1_shop_ledger

- **Type:** complex reasoning (12 rules)
- **Answer type:** number
- **Final answer:** 22890
- **Calculation:** (2320 - 230) + 24600 + 300 - 4100 = 22890

## Prompt
- BN: দেখোতো আজ রাতে দোকান বন্ধ করার সময় ক্যাশে কত টাকা থাকবে?
- EN: Can you check how much cash will be in the drawer when I close the shop tonight?

## Transcription
- BN: `tasks/C1_shop_ledger/transcription.txt`
- EN: `transcription_en.txt` (this folder)

## Reading rubric
| ID | Bengali | English |
|---|---|---|
| R01 | ক্যাশে আগে থেকে থাকা ২৩২০ টাকা পড়েছে? | Read opening cash 2320? |
| R02 | চা খাওয়া বাবদ খরচ ২৩০ টাকা পড়েছে? | Read tea expense 230? |
| R03 | জসিমের নগদ বিক্রি ৫০০ টাকা পড়েছে? | Read Jashim's cash sale 500? |
| R04 | আব্দুল্লাহর নগদ বিক্রি ৫০০ টাকা পড়েছে? | Read Abdullah's cash sale 500? |
| R05 | আব্দুল্লাহর বিকেলে দেয়া পাওনা ২০০ টাকা পড়েছে? | Read Abdullah paid the 200 due in the afternoon? |
| R06 | কবিরের নগদ বিক্রি ৮০০ টাকা পড়েছে? | Read Kabir's cash sale 800? |
| R07 | কবিরকে রাতে ৩০০ টাকা ফেরত দিতে হবে পড়েছে? | Read Kabir must get a 300 refund tonight? |
| R08 | জলিলের নগদ বিক্রি ১৭০০০ টাকা পড়েছে? | Read Jalil's cash sale 17000? |
| R09 | রুবায়েতের নগদ বিক্রি ২৭০০ টাকা পড়েছে? | Read Rubayet's cash sale 2700? |
| R10 | কাকনের নগদ বিক্রি ৩০০ টাকা পড়েছে? | Read Kakon's cash sale 300? |
| R11 | ওসমানের নগদ বিক্রি ১৩০০ টাকা পড়েছে? | Read Osman's cash sale 1300? |
| R12 | জামিলের নগদ বিক্রি ১৫০০ টাকা পড়েছে? | Read Jamil's cash sale 1500? |
| R13 | জামিল বাকি ১০০ টাকা রাতে দিয়ে যাবে পড়েছে? | Read Jamil will pay the remaining 100 tonight? |
| R14 | চৈতি রাতে ৩০০০ টাকা নিতে আসবে পড়েছে? | Read Chaiti will come to take 3000 tonight? |
| R15 | ওবায়েদ রাতে ৮০০ টাকা নিতে আসবে পড়েছে? | Read Obayed will come to take 800 tonight? |

## Reasoning rubric
| ID | Bengali | English |
|---|---|---|
| L01 | ক্যাশে আগে থেকে থাকা ২৩২০ টাকাকে শুরুর ক্যাশ ধরেছে? | Used opening cash 2320 as the starting balance? |
| L02 | চা খাওয়ার খরচ ২৩০ টাকা আজকের ব্যয় হিসেবে বাদ দিয়েছে? | Subtracted tea 230 as today's expense? |
| L03 | সব নগদ বিক্রির ২৪৬০০ টাকা আজকের হিসাবে যোগ করেছে? | Added all cash sales 24600 to today? |
| L04 | সব মিলিয়ে পাওনার ৩০০ টাকা আজকের হিসাবে যোগ করেছে? | Added all receivables collected today, 300? |
| L05 | সব মিলিয়ে ফেরত দেয়া ৪১০০ টাকা আজকের দেনা হিসেবে বাদ দিয়েছে? | Subtracted all payouts tonight, 4100? |
