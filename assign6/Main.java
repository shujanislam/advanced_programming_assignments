import java.util.*;
import java.util.stream.Collectors;

class Student {
    private int id;
    private String name;
    private List<String> courses;
    private Map<String, Integer> scores;

    public Student(int id, String name, List<String> courses, Map<String, Integer> scores) {
        this.id = id;
        this.name = name;
        this.courses = new ArrayList<>(courses);
        this.scores = new HashMap<>(scores);
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public List<String> getCourses() {
        return courses;
    }

    public Map<String, Integer> getScores() {
        return scores;
    }

    public double getAverageScore() {
        if (courses == null || courses.isEmpty()) {
            return 0.0;
        }

        double total = courses.stream()
                .mapToInt(course -> scores.getOrDefault(course, 0))
                .sum();

        return total / courses.size();
    }

    @Override
    public String toString() {
        return "Student{id=" + id +
                ", name='" + name + '\'' +
                ", courses=" + courses +
                ", scores=" + scores +
                ", avg=" + String.format("%.2f", getAverageScore()) +
                '}';
    }
}

class StudentPerformanceAnalyzer {

    public static List<Student> getTopNStudents(List<Student> students, int n) {
        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getAverageScore).reversed())
                .limit(n)
                .collect(Collectors.toList());
    }

    public static Map<String, Double> getAverageScorePerCourse(List<Student> students) {
        Set<String> allCourses = getAllUniqueCourses(students);

        return allCourses.stream()
                .collect(Collectors.toMap(
                        course -> course,
                        course -> students.stream()
                                .mapToInt(student -> student.getScores().getOrDefault(course, 0))
                                .average()
                                .orElse(0.0)
                ));
    }

    public static Set<String> getAllUniqueCourses(List<Student> students) {
        return students.stream()
                .flatMap(student -> student.getCourses().stream())
                .collect(Collectors.toCollection(HashSet::new));
    }
}

public class Main {

    public static int readInt(Scanner sc, String prompt) {
        while (true) {
            System.out.print(prompt);
            if (sc.hasNextInt()) {
                int value = sc.nextInt();
                sc.nextLine();
                return value;
            } else {
                System.out.println("Invalid input. Please enter an integer.");
                sc.nextLine();
            }
        }
    }

    public static String readChoice(Scanner sc, String prompt) {
        System.out.print(prompt);
        return sc.nextLine().trim().toLowerCase();
    }

    public static void printComplexity(String operation, String timeComplexity, String spaceComplexity) {
        System.out.println("Complexity of " + operation + ":");
        System.out.println("Time Complexity: " + timeComplexity);
        System.out.println("Space Complexity: " + spaceComplexity);
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Student> students = new ArrayList<>();

        List<String> fixedCourses = new ArrayList<>(
                Arrays.asList("Advanced Programming", "Algorithms", "Computer Architecture")
        );

        System.out.println("=== Student Performance Analyzer ===");

        while (true) {
            System.out.println("\nEnter details for a student:");

            int id = readInt(sc, "Enter student ID: ");

            System.out.print("Enter student name: ");
            String name = sc.nextLine();

            Map<String, Integer> scores = new HashMap<>();

            for (String course : fixedCourses) {
                int marks = readInt(sc, "Enter marks for " + course + ": ");
                scores.put(course, marks);
            }

            students.add(new Student(id, name, fixedCourses, scores));

            String choice = readChoice(sc, "Do you want to add another student? (yes/no): ");
            if (!choice.equals("yes")) {
                break;
            }
        }

        System.out.println("\nAll Students:");
        students.forEach(System.out::println);
        printComplexity("displaying all students", "O(n)", "O(1) auxiliary");

        int n = readInt(sc, "\nEnter N for Top N Students: ");

        System.out.println("\nTop " + n + " Students:");
        List<Student> topStudents = StudentPerformanceAnalyzer.getTopNStudents(students, n);
        topStudents.forEach(System.out::println);
        printComplexity("getTopNStudents", "O(n log n * c)", "O(n)");

        System.out.println("Average Score Per Course:");
        Map<String, Double> avgPerCourse = StudentPerformanceAnalyzer.getAverageScorePerCourse(students);
        avgPerCourse.forEach((course, avg) ->
                System.out.println(course + " -> " + String.format("%.2f", avg)));
        printComplexity("getAverageScorePerCourse", "O(m * n)", "O(m)");

        System.out.println("All Unique Courses:");
        Set<String> uniqueCourses = StudentPerformanceAnalyzer.getAllUniqueCourses(students);
        uniqueCourses.forEach(System.out::println);
        printComplexity("getAllUniqueCourses", "O(n * c)", "O(m)");

        sc.close();
    }
}
