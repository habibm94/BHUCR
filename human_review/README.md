# Human review only

English translations of every task: prompt, transcription, rubric, type and final answer.

**For human judges only.** The harness never reads this folder: `run_eval.py` loads only `tasks/<id>/` and `shared/`, and refuses any path under `human_review/`. Neither the tested models nor the LLM judge ever see these files. This keeps answers and translations out of every model call, so models cannot copy them and the judge grades only against the Bengali source.

Each task folder has `task_en.md` (type, answer, calculation, prompt, rubric in Bengali and English) and `transcription_en.txt`.
