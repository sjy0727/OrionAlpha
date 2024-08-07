/*
 * This file is part of OrionAlpha, a MapleStory Emulator Project.
 * Copyright (C) 2018 Eric Smith <notericsoft@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package util;

/**
 * Used for logging purposes within the JVM.
 *
 * @author Eric
 */
public class Logger {

    // ANSI color codes
    private static final String RESET = "\u001B[0m";
    private static final String BLACK = "\u001B[30m";
    private static final String RED = "\u001B[31m";
    private static final String GREEN = "\u001B[32m";
    private static final String YELLOW = "\u001B[33m";
    private static final String BLUE = "\u001B[34m";
    private static final String PURPLE = "\u001B[35m";
    private static final String CYAN = "\u001B[36m";
    private static final String WHITE = "\u001B[37m";

    public static void logReport(String format) {
        System.out.println(GREEN + "[INFO] " + RESET + format);
    }

    public static void logReport(String format, Object... args) {
        System.out.println(GREEN + "[INFO] " + RESET + String.format(format, args));
    }

    public static void logError(String format) {
        System.err.println(RED + "[ERROR] " + RESET + format);
    }

    public static void logError(String format, Object... args) {
        System.err.println(RED + "[ERROR] " + RESET + String.format(format, args));
    }
}
