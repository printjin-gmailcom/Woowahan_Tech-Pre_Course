package convenience.utils;

import camp.nextstep.edu.missionutils.Console;

public class ConsoleUtils {
    public static String readInput() {
        return Console.readLine();
    }

    public static void printMessage(String message) {
        System.out.println(message);
    }

    public static void printError(String message) {
        System.out.println("[ERROR] " + message);
    }
}
