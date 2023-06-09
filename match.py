from matching import process
from pathlib import Path
from matching.rules.rule import Generic

data_folder = Path("./mentoring-data")
mentors, mentees = process.conduct_matching_from_file(
    path_to_data=data_folder,
    rules=[[Generic({True: 3, False: 0}, lambda match: match.mentee.organisation != match.mentor.organisation and match.mentee.role == match.mentor.role)]]
)

output_folder = data_folder / "output"
process.create_mailing_list(mentors, output_folder)
process.create_mailing_list(mentees, output_folder)