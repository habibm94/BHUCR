# C2_tour_accounts

- **Type:** complex reasoning (5 rules)
- **Answer type:** yesno
- **Final answer:** Yes
- **Calculation:** 10000 - (10000 + 200 - 250) = 50 > 0 → yes

## Prompt
- BN: ট্যুর থেকে ফিরলাম। আমি ছিলাম হিসাবের দায়িত্বে। দেখোতো হিসাব থেকে কোন টাকা বেচেছে কীনা?
- EN: We are back from the trip. I was in charge of the accounts. Is any money left over?

## Transcription
- BN: `tasks/C2_tour_accounts/transcription.txt`
- EN: `transcription_en.txt` (this folder)

## Reading rubric
| ID | Bengali | English |
|---|---|---|
| R01 | আশিষ ২৩০০ টাকা দিয়েছে পড়েছে? | Read Ashish paid 2300? |
| R02 | জাহেদ ৩৩০০ টাকা দিয়েছে পড়েছে? | Read Jahed paid 3300? |
| R03 | কেয়া মোট ৩০০০ টাকা দিয়েছে, ক্যাশে ২০০০ আর চেকে ১০০০, পড়েছে? | Read Keya paid 3000 in total, 2000 cash and 1000 by cheque? |
| R04 | আমি ১০০০ টাকা দিয়েছি পড়েছে? | Read I paid 1000? |
| R05 | রুবেল ৪০০ টাকা দিয়েছে পড়েছে? | Read Rubel paid 400? |
| R06 | রুবেল আরো ৫০০ টাকা দেবে বলেও দেয়নি পড়েছে? | Read Rubel promised 500 more but did not pay? |
| R07 | বাস ভাড়া ৩৪০০ টাকা পড়েছে? | Read bus fare 3400? |
| R08 | টোল ৩০০ টাকা পড়েছে? | Read toll 300? |
| R09 | হোটেল ভাড়া ৫০০০ টাকা পড়েছে? | Read hotel 5000? |
| R10 | ইন্স্যুরেন্স ৫০০ টাকা, ৫০% ফেরত পাবে পড়েছে? | Read insurance 500 with 50% refund? |
| R11 | লোকাল বাইক ৩০০ টাকা, আরো ২০০ টাকা পাবে পড়েছে? | Read local bike 300 with 200 more due? |
| R12 | খাবার ৫০০ টাকা পড়েছে? | Read food 500? |

## Reasoning rubric
| ID | Bengali | English |
|---|---|---|
| L01 | সবার দেয়া মোট ১০০০০ টাকা জমা ধরেছে? | Counted total collected as 10000? |
| L02 | রুবেলের না দেয়া ৫০০ টাকা জমায় ধরেনি? | Did not count Rubel's unpaid 500? |
| L03 | সব খরচ ১০০০০ টাকা জমা থেকে বাদ দিয়েছে? | Subtracted all expenses, 10000? |
| L04 | লোকাল বাইকের বাকি ২০০ টাকা দেনা খরচে ধরেছে? | Added the bike's 200 due to expenses? |
| L05 | ইন্স্যুরেন্স এর ফেরত আসা ৫০%, মানে ২৫০ টাকা খরচ থেকে বাদ দিয়েছে? | Subtracted the 50% insurance refund, 250, from expenses? |
