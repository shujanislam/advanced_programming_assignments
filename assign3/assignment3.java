import java.util.List;
import java.util.Arrays;

public class BookSearch {
    public static void main(String[] args) {

        List<String> library = Arrays.asList(
                "Java Programming",
                "Data Structures",
                "Operating Systems",
                "Java Basics",
                "Computer Networks"
        );

        String key = "Java";

        System.out.println("Books containing \"" + key + "\":");

        for (int i = 0; i < library.size(); i++) {
            String title = library.get(i);
            if (title.indexOf(key) != -1) {
                System.out.println(title);
            }
        }
    }
}
