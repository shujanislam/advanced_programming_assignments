import pytest

from score_processor import ScoreProcessor


def test_process_score_file_success(tmp_path, capsys):
    processor = ScoreProcessor()

    score_file = tmp_path / "score.txt"
    score_file.write_text("8")

    result = processor.process_score_file(str(score_file))

    captured = capsys.readouterr()

    assert result == 80
    assert "Data processed successfully" in captured.out
    assert "File cleanup completed" in captured.out


def test_process_score_file_missing_file(capsys):
    processor = ScoreProcessor()

    with pytest.raises(FileNotFoundError):
        processor.process_score_file("missing_score.txt")

    captured = capsys.readouterr()

    assert "Error: File not found at path: missing_score.txt" in captured.out
    assert "File cleanup completed" in captured.out


def test_process_score_file_invalid_data(tmp_path, capsys):
    processor = ScoreProcessor()

    score_file = tmp_path / "bad_score.txt"
    score_file.write_text("abc")

    with pytest.raises(ValueError):
        processor.process_score_file(str(score_file))

    captured = capsys.readouterr()

    assert "Error: File contains invalid data. Expected a number." in captured.out
    assert "File cleanup completed" in captured.out
