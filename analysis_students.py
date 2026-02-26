import numpy as np
import pandas as pd


def generate_student_data(n_students=50, n_subjects=5):
    grade = np.random.randint(60, 101, size=(n_students, n_subjects))
    return grade


def create_dataframe(data, student_names, subjects):
    df = pd.DataFrame(data, columns=subjects, index=student_names)
    return df


def analyze_data(df):
    df['average'] = df.mean(axis=1)
    best_student = df['average'].idxmax()
    best_score = df['average'].max()
    worst_student = df['average'].idxmin()
    worst_score = df['average'].min()
    subject_avg = df[['Math', 'Physics', 'CS', 'English', 'History']].mean()
    hardest_subject = subject_avg.idxmin()

    stats = f"""
Best student: {best_student} with average {best_score:.2f}
Worst student: {worst_student} with average {worst_score:.2f}
Hardest subject: {hardest_subject}

Average by subject:
{subject_avg}
    """

    print(stats)
    return df, stats


def normalize_scores(scores):
    normalized = (scores - scores.min()) / (scores.max() - scores.min())
    return normalized


def generate_report(df, stats_text):
    df.to_csv('student_grades.csv')

    report = f"""
========================================
STUDENT GRADES ANALYSIS REPORT
========================================

{stats_text}

Total students: {len(df)}
========================================
    """

    with open('report.txt', 'w', encoding='utf-8') as f:
        f.write(report)

    print("\nFiles saved:")
    print("- student_grades.csv")
    print("- report.txt")

    return report


if __name__ == "__main__":
    grades = generate_student_data(n_students=50, n_subjects=5)

    student_names = [f"Student_{i + 1}" for i in range(50)]
    subjects = ['Math', 'Physics', 'CS', 'English', 'History']

    df = create_dataframe(grades, student_names, subjects)

    df, stats = analyze_data(df)

    df['Math_normalized'] = normalize_scores(df['Math'])
    print("\nNormalized Math scores (first 5):")
    print(df[['Math', 'Math_normalized']].head())

    generate_report(df, stats)