Copy this folder to tasks/<ID>_<name>/ and fill:
- page.jpg            photo of the handwritten note
- prompt.txt          natural Bengali question
- transcription.txt   exact Bengali text, crossed-out text as ~~text~~
- task.json           id, type (regular|complex), answer_type (number|yesno|text), answer, complexity: {"rules": n}
- rubric.json         reading + reasoning items in Bengali (only items that change the answer)
English translations (prompt, transcription, rubric, type, answer) go in human_review/<ID>/, never here.
ID prefix: R = regular (up to 3 rules), C = complex (more than 3 rules).
