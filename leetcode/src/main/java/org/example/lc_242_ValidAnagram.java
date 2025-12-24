package org.example;

import java.util.Arrays;

public class lc_242_ValidAnagram {
    public static boolean isAnagram(String s, String t){
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        Arrays.sort(sChars);
        Arrays.sort(tChars);
        return Arrays.equals(sChars, tChars);
    }

    public static boolean isAnagramFrequencyMethod(String s, String t){
        int[] freq = new int[26];
        for (char c : s.toCharArray()){
            freq[c-'a']++;
        }
        for (char c : t.toCharArray()){
            freq[c-'a']--;
        }
        for (int f : freq){
            if (f!=0){
                return false;
            }
        }
        return true;
    }

    public static boolean isAnagramFrequencyMethodTwo(String s, String t){
        int[] freq = new int[256];
        for (char c : s.toCharArray()){
            freq[c]++;
        }
        for (char c : t.toCharArray()){
            freq[c]--;
        }
        for (int f : freq){
            if (f!=0){
                return false;
            }
        }
        return true;
    }


    public static void main(String[] args) {
        String s1 = "car";
        String t1 = "rat";

        String s2 = "anagram";
        String t2 = "nagaram";

        System.out.println(isAnagram(s1,t1));
        System.out.println(isAnagram(s2,t2));
        System.out.println(isAnagramFrequencyMethod(s1,t1));
        System.out.println(isAnagramFrequencyMethod(s2,t2));
    }



}
