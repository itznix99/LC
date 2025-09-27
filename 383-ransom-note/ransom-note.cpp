class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int check1[26]={0};
        int check2[26]={0};
        for (int i=0;i<ransomNote.length();i++){
            check1[ransomNote[i]-'a']++;
        }
        for (int i=0;i<magazine.length();i++){
            check2[magazine[i]-'a']++;
        }
        for (int i=0;i<26;i++){
            if (check1[i]>check2[i]){
                return false;
            }
        }
        return true;
        /*for (int i=0;i<26;i++){
            printf("%d %d\n",check1[i],check2[i]);
        }
        return false;*/
    }
};