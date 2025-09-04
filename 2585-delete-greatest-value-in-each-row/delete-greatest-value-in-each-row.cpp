class Solution {
public:
    int max(vector<int> v, int c=1){
        int res=0,ind=0;
        for (int i=0;i<v.size();i++){
            if (v[i]>res){
                res=v[i];
                ind=i;
            }
        }
        if (c==0){
            return ind;
        }
        return res;
    }
    int deleteGreatestValue(vector<vector<int>>& grid) {
        int m=grid.size(),n=grid[0].size(),res=0;
        vector<int> store;
        while (grid[0].size()>0){
            store.clear();
            for (int i=0;i<m;i++){
                int found=max(grid[i],0);
                store.push_back(grid[i][found]);
                grid[i].erase(grid[i].begin()+found);
            }
            res+=max(store);
        }
        //cout<<m<<n;
        return res;
    }
};