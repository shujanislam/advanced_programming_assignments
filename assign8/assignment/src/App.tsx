import React, { useMemo, useState } from "react";

export default function App() {
  const [studentsMap, setStudentsMap] = useState(
    new Map([
      [
        1,
        {
          id: 1,
          name: "Ayan",
          enrolledCourses: new Set([
            "Advanced Programming",
            "Algorithms",
          ]),
          gpa: 8.7,
        },
      ],
      [
        2,
        {
          id: 2,
          name: "Riya",
          enrolledCourses: new Set([
            "Algorithms",
            "Computer Architecture",
          ]),
          gpa: 9.1,
        },
      ],
      [
        3,
        {
          id: 3,
          name: "Shujan",
          enrolledCourses: new Set([
            "Advanced Programming",
            "Computer Architecture",
          ]),
          gpa: 8.3,
        },
      ],
    ])
  );

  const [name, setName] = useState("");
  const [gpa, setGpa] = useState("");
  const [courses, setCourses] = useState("");
  const [filterCourse, setFilterCourse] = useState("");

  const addStudent = () => {
    if (!name.trim() || !gpa.trim() || !courses.trim()) return;

    const ids = Array.from(studentsMap.keys());
    const newId = ids.length ? Math.max(...ids) + 1 : 1;

    const newStudent = {
      id: newId,
      name: name.trim(),
      enrolledCourses: new Set(
        courses
          .split(",")
          .map((c) => c.trim())
          .filter(Boolean)
      ),
      gpa: parseFloat(gpa),
    };

    const updated = new Map(studentsMap);
    updated.set(newId, newStudent);
    setStudentsMap(updated);

    setName("");
    setGpa("");
    setCourses("");
  };

  const removeStudent = (id) => {
    const updated = new Map(studentsMap);
    updated.delete(id);
    setStudentsMap(updated);
  };

  const studentsArray = useMemo(
    () => Array.from(studentsMap.values()),
    [studentsMap]
  );

  const sortedStudents = useMemo(
    () => [...studentsArray].sort((a, b) => b.gpa - a.gpa),
    [studentsArray]
  );

  const uniqueCourses = useMemo(() => {
    return Array.from(
      studentsArray.reduce((acc, student) => {
        student.enrolledCourses.forEach((course) => acc.add(course));
        return acc;
      }, new Set())
    ).sort();
  }, [studentsArray]);

  const filteredStudents = useMemo(() => {
    if (!filterCourse.trim()) return sortedStudents;
    return sortedStudents.filter((student) =>
      student.enrolledCourses.has(filterCourse.trim())
    );
  }, [sortedStudents, filterCourse]);

  return (
    <div style={styles.page}>
      <div style={styles.container}>
        <div style={styles.hero}>
          <div>
            <p style={styles.eyebrow}>Enrollment System</p>
            <h1 style={styles.title}>Course Enrollment Dashboard</h1>
            <p style={styles.subtitle}>
              Manage students, sort by GPA, view enrolled courses, and filter by subject.
            </p>
          </div>
        </div>

        <div style={styles.topGrid}>
          <div style={styles.card}>
            <h3 style={styles.cardTitle}>Add Student</h3>
            <div style={styles.formGrid}>
              <input
                type="text"
                placeholder="Student name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                style={styles.input}
              />
              <input
                type="number"
                step="0.01"
                placeholder="GPA"
                value={gpa}
                onChange={(e) => setGpa(e.target.value)}
                style={styles.input}
              />
              <input
                type="text"
                placeholder="Advanced Programming, Algorithms"
                value={courses}
                onChange={(e) => setCourses(e.target.value)}
                style={styles.input}
              />
              <button onClick={addStudent} style={styles.primaryButton}>
                Add Student
              </button>
            </div>
          </div>

          <div style={styles.card}>
            <h3 style={styles.cardTitle}>Filter by Course</h3>
            <input
              type="text"
              placeholder="Advanced Programming"
              value={filterCourse}
              onChange={(e) => setFilterCourse(e.target.value)}
              style={{ ...styles.input, marginBottom: "18px" }}
            />

            <h3 style={styles.cardTitle}>Unique Courses</h3>
            <div style={styles.tagsWrap}>
              {uniqueCourses.map((course, index) => (
                <span key={index} style={styles.tag}>
                  {course}
                </span>
              ))}
            </div>
          </div>
        </div>

        <div style={styles.card}>
          <div style={styles.sectionHeader}>
            <div>
              <h3 style={styles.cardTitle}>Students Sorted by GPA</h3>
              <p style={styles.muted}>
                Filtering students by course takes <strong>O(n)</strong> time.
              </p>
            </div>
          </div>

          <div style={styles.studentsGrid}>
            {filteredStudents.map((student) => (
              <div key={student.id} style={styles.studentCard}>
                <div style={styles.studentTop}>
                  <div>
                    <h4 style={styles.studentName}>{student.name}</h4>
                    <p style={styles.studentMeta}>ID: {student.id}</p>
                  </div>
                  <div style={styles.gpaBox}>
                    <span style={styles.gpaValue}>{student.gpa.toFixed(2)}</span>
                    <span style={styles.gpaLabel}>GPA</span>
                  </div>
                </div>

                <div style={styles.tagsWrap}>
                  {Array.from(student.enrolledCourses).map((course, idx) => (
                    <span key={idx} style={styles.softTag}>
                      {course}
                    </span>
                  ))}
                </div>

                <button
                  onClick={() => removeStudent(student.id)}
                  style={styles.secondaryButton}
                >
                  Remove Student
                </button>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    width: "100%",
    background: "#fafafa",
    color: "#111",
    fontFamily:
      'Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
    padding: "32px",
    boxSizing: "border-box",
  },
  container: {
    width: "100%",
    maxWidth: "100%",
    margin: "0 auto",
  },
  hero: {
    marginBottom: "24px",
  },
  eyebrow: {
    margin: 0,
    fontSize: "12px",
    color: "#666",
    textTransform: "uppercase",
    letterSpacing: "0.08em",
  },
  title: {
    margin: "8px 0 8px 0",
    fontSize: "42px",
    fontWeight: 700,
    letterSpacing: "-0.04em",
  },
  subtitle: {
    margin: 0,
    fontSize: "16px",
    color: "#666",
    maxWidth: "700px",
    lineHeight: 1.6,
  },
  topGrid: {
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    gap: "20px",
    marginBottom: "20px",
    width: "100%",
  },
  card: {
    background: "#fff",
    border: "1px solid #eaeaea",
    borderRadius: "20px",
    padding: "24px",
    boxShadow: "0 1px 2px rgba(0,0,0,0.04)",
  },
  cardTitle: {
    margin: "0 0 14px 0",
    fontSize: "18px",
    fontWeight: 600,
  },
  formGrid: {
    display: "grid",
    gap: "12px",
  },
  input: {
    width: "100%",
    padding: "13px 14px",
    border: "1px solid #e5e5e5",
    borderRadius: "12px",
    fontSize: "14px",
    outline: "none",
    boxSizing: "border-box",
    background: "#fff",
  },
  primaryButton: {
    border: "none",
    background: "#111",
    color: "#fff",
    padding: "13px 16px",
    borderRadius: "12px",
    cursor: "pointer",
    fontSize: "14px",
    fontWeight: 500,
  },
  secondaryButton: {
    marginTop: "18px",
    width: "100%",
    border: "1px solid #e5e5e5",
    background: "#fff",
    color: "#111",
    padding: "12px 14px",
    borderRadius: "12px",
    cursor: "pointer",
    fontSize: "14px",
    fontWeight: 500,
  },
  tagsWrap: {
    display: "flex",
    flexWrap: "wrap",
    gap: "8px",
  },
  tag: {
    padding: "8px 12px",
    borderRadius: "999px",
    background: "#f7f7f7",
    border: "1px solid #ececec",
    fontSize: "13px",
  },
  softTag: {
    padding: "7px 10px",
    borderRadius: "999px",
    background: "#f5f5f5",
    fontSize: "13px",
    color: "#333",
  },
  sectionHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "18px",
  },
  muted: {
    margin: 0,
    color: "#666",
    fontSize: "14px",
  },
  studentsGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))",
    gap: "16px",
    width: "100%",
  },
  studentCard: {
    border: "1px solid #ededed",
    borderRadius: "18px",
    padding: "18px",
    background: "#fff",
  },
  studentTop: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    gap: "16px",
    marginBottom: "14px",
  },
  studentName: {
    margin: 0,
    fontSize: "18px",
    fontWeight: 600,
  },
  studentMeta: {
    margin: "6px 0 0 0",
    fontSize: "13px",
    color: "#666",
  },
  gpaBox: {
    display: "flex",
    flexDirection: "column",
    alignItems: "flex-end",
  },
  gpaValue: {
    fontSize: "24px",
    fontWeight: 700,
    letterSpacing: "-0.03em",
  },
  gpaLabel: {
    fontSize: "12px",
    color: "#666",
    textTransform: "uppercase",
    letterSpacing: "0.08em",
  },
};
