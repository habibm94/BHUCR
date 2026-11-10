# R3_house_repair

- **Type:** regular reasoning (2 rules)
- **Answer type:** yesno
- **Final answer:** Yes
- **Calculation:** 68500 - 51870 = 16630 >= 8000 → yes

## Prompt
- BN: বাসায় মেরামতের কাজ করি। মিস্ত্রী বলল আরো ৮০০০ টাকা লাগবে রং কিনতে। দেখোতো রং কেনার টাকা আছে কীনা ক্যাশে
- EN: I'm doing repair work at home. The mason said 8000 taka more is needed to buy paint. Is there enough cash to buy the paint?

## Transcription
- BN: `tasks/R3_house_repair/transcription.txt`
- EN: `transcription_en.txt` (this folder)

## Reading rubric
| ID | Bengali | English |
|---|---|---|
| R01 | শুরুর ক্যাশ ৬৩৫০০ টাকা পড়েছে? | Read starting cash 63500? |
| R02 | পরে যোগ ৫০০০ টাকা পড়েছে? | Read added later 5000? |
| R03 | ইট ১০০০০ টাকা পড়েছে? | Read bricks 10000? |
| R04 | বালু ৩০০০ টাকা পড়েছে? | Read sand 3000? |
| R05 | সিমেন্ট ১৩৭০০ টাকা পড়েছে? | Read cement 13700? |
| R06 | পরিবহণ ১৭০০ টাকা পড়েছে? | Read transport 1700? |
| R07 | রড ৮০০০ টাকা, পরে আরো ২২০০ টাকা পড়েছে? | Read rod 8000, 2200 more later? |
| R08 | কাঠ ২৩৭০ টাকা পড়েছে? | Read wood 2370? |
| R09 | বাঁশ পরিবহণ ৫০০ টাকা পড়েছে? | Read bamboo transport 500? |
| R10 | বাঁশ ১২০০ টাকা পড়েছে? | Read bamboo 1200? |
| R11 | মিস্ত্রী খরচ ৭০০০ টাকা পড়েছে? | Read mason's fee 7000? |
| R12 | মিস্ত্রীর দুপুরের খাবার ২২০০ টাকা পড়েছে? | Read mason's lunch 2200? |

## Reasoning rubric
| ID | Bengali | English |
|---|---|---|
| L01 | শুরুর ক্যাশ ৬৩৫০০ আর পরে যোগ ৫০০০ মিলিয়ে মোট ৬৮৫০০ টাকা ধরেছে? | Added starting cash 63500 and 5000 to 68500? |
| L02 | রডের পরের ২২০০ টাকাও খরচে ধরেছে? | Added the rod's later 2200 to expenses? |
| L03 | সব খরচ ৫১৮৭০ টাকা বাদ দিয়েছে? | Subtracted all expenses, 51870? |
| L04 | ক্যাশ ৬৮৫০০ টাকা থেকে খরচ ৫১৮৭০ টাকা বাদ দিয়েছে? | Subtracted expenses 51870 from cash 68500? |
| L05 | বাকি থাকা ১৬৬৩০ টাকা রঙ কেনার ৮০০০ টাকার সাথে তুলনা করেছে? | Compared the remaining 16630 with the 8000 for paint? |
