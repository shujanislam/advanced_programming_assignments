from score_processor import ScoreProcessor

processor = ScoreProcessor()

try:
    result = processor.process_score_file("score.txt")
    print("Final result:", result)
except FileNotFoundError:
    print("Could not process score because the file is missing.")
except ValueError:
    print("Could not process score because the file contains invalid data.")
