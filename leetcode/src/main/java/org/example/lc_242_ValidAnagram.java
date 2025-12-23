package org.example;

import java.util.Arrays;

public class lc_242_ValidAnagram {
    public static boolean isAnagram(String s, String t){
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        Arrays.sort(sChars);
        Arrays.sort(tChars);

//        if (sChars.length != tChars.length){
//            return false;
//        }
//        for (int i = 0; i < sChars.length; i++){
//            if (sChars[i]!= tChars[i]){
//                return false;
//            }
//        }
//        return true;

        return Arrays.equals(sChars, tChars);
    }

    public static void main(String[] args) {
        String s1 = "car";
        String t1 = "rat";


        String s2 = "anagram";
        String t2 = "nagaram";

        System.out.println(isAnagram(s2,t2));

        char c = 'a';
        int[] freq = new int[256];
        freq[0]=1;
        //for (int f : freq) System.out.println(f);
        System.out.println(freq[c]);
    }



}
