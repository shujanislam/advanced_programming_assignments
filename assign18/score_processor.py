class ScoreProcessor:
    def process_score_file(self, file_path: str) -> int:
        """
        Reads an integer score from a file, multiplies it by 10,
        and returns the result.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file content is not a valid integer.
        """

        try:
            with open(file_path, "r") as file:
                data = file.read().strip()
                score = int(data)
                result = score * 10

        except FileNotFoundError:
            print(f"Error: File not found at path: {file_path}")
            raise

        except ValueError:
            print("Error: File contains invalid data. Expected a number.")
            raise

        else:
            print("Data processed successfully")
            return result

        finally:
            print("File cleanup completed")
