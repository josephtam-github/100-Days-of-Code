#!/usr/bin/env python3
"""
This script reads student grades from a CSV file, calculates averages,
and writes the results to a new file.
"""

import csv
from typing import List, Tuple


def read_grades(filename: str) -> List[Tuple[str, List[float]]]:
    """
    Read student grades from a CSV file.

    Args:
        filename (str): Name of the CSV file to read.

    Returns:
        List[Tuple[str, List[float]]]: List of tuples containing student name
        and their grades.
    """
    students = []
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                name = row[0]
                grades = [float(grade) for grade in row[1:] if grade]
                students.append((name, grades))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
    return students


def calculate_average(grades: List[float]) -> float:
    """
    Calculate the average of a list of grades.

    Args:
        grades (List[float]): List of numerical grades.

    Returns:
        float: The average of the grades, rounded to 2 decimal places.
    """
    return round(sum(grades) / len(grades), 2) if grades else 0


def write_results(filename: str, results: List[Tuple[str, float]]) -> None:
    """
    Write student names and their average grades to a file.

    Args:
        filename (str): Name of the file to write results to.
        results (List[Tuple[str, float]]): List of tuples containing student
        name and average grade.
    """
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Student', 'Average Grade'])
            for name, average in results:
                writer.writerow([name, average])
        print(f"Results written to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")


def main():
    """Main function to orchestrate the grade analysis process."""
    input_file = 'student_grades.csv'
    output_file = 'student_averages.csv'

    students = read_grades(input_file)
    if not students:
        return

    results = [(name, calculate_average(grades)) for name, grades in students]
    write_results(output_file, results)


if __name__ == "__main__":
    main()
