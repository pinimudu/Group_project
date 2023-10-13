# Sample list of candidates with their Z-Scores
candidates = [
    {"name": "Candidate 1", "z_score": 1.5},
    {"name": "Candidate 2", "z_score": -0.5},
    {"name": "Candidate 3", "z_score": 2.0},
    {"name": "Candidate 4", "z_score": -1.2},
    {"name": "Candidate 5", "z_score": 0.8}
]

# Define the Z-Score threshold for campus placement
z_score_threshold = 1.0

# Filter candidates based on the Z-Score threshold
selected_candidates = [candidate for candidate in candidates if candidate["z_score"] >= z_score_threshold]

# Print the selected candidates
print("Selected Candidates for Campus Placement:")
for candidate in selected_candidates:
    print(f"{candidate['name']} (Z-Score: {candidate['z_score']})")