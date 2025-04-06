#include <bits/stdc++.h>
using namespace std;

string findCandidateKeylosure(string att, vector<pair<string, string>> &vp) {
    set<char> st;
    for (auto it : att)
        st.insert(it);
    bool check = 0;
    set<char> prev;
    do {
        check = 0;
        prev = st;
        for (auto it : vp) {
            string l = it.first;
            vector<int> hash1(26, 0);
            for (auto it : st) {
                hash1[it - 'a']++;
            }
            bool f = 1;
            for (auto it1 : l) {
                if (hash1[it1 - 'a'] == 0) {
                    f = 0;
                    break;
                }
            }
            if (f == 1) {
                check = 1;
                for (auto it1 : it.second) {
                    st.insert(it1);
                }
            }
        }
    } while (check && prev != st);
    string res = "";
    for (auto it : st)
        res += it;
    return res;
}

bool isSubset(string &s1, string &s2) {
    bool f = 1;
    vector<int> hash(26, 0);
    for (auto it : s2)
        hash[it - 'a']++;
    for (auto it : s1) {
        if (hash[it - 'a'] == 0) {
            f = 0;
            break;
        }
    }
    return f;
}

vector<string> findCandidateKey(int n, vector<pair<string, string>> &vp) {
    set<string> res;
    for (int i = 1; i < pow(2, n); i++) {
        string f = "";
        int j = i;
        int pos = 0;
        while (j) {
            if (j & 1) {
                f += pos + 'a';
            }
            pos++;
            j = j >> 1;
        }
        if (findCandidateKeylosure(f, vp).size() == n) {
            set<string> newset;
            bool flag = 1;
            for (auto it : res) {
                if (isSubset(it, f)) {
                    flag = 0;
                    newset.insert(it);
                } else if (isSubset(f, it)) {
                    continue;
                } else {
                    newset.insert(it);
                }
            }
            if (flag) newset.insert(f);
            res = newset;
        }
    }
    return vector<string>(res.begin(), res.end());
}

int main() {
    int n;
    cout << "Enter Number of Atrributes: " << endl;
    cin >> n;
    unordered_map<char,char> mp1;
    unordered_map<char,char> mp2;
    cout << "Enter Atrributes:" << endl;
    int val = 0;
    for(int i =0;i < n;i++){
        char c;
        cin >> c;
        mp1[c] = val + 'a';
        mp2[val + 'a'] = c;
        val++;
    }
    cout << "Enter Number of functional dependencies:" << endl;
    int m;
    cin >> m;
    vector<pair<string, string>> vp;
    for (int i = 0; i < m; i++) {
        string l;
        string r;
        cout << "Enter first left hand attributes and then right hand attributes " << endl;
        cin >> l >> r;
        string left = "",right = "";
        for(auto it: l){
           left += mp1[it];
        }
        for(auto it:r){
            right += mp1[it];
        }
        vp.push_back({left, right});
    }

    vector<string> res = findCandidateKey(n, vp);
    cout<<"Candidate keys are:" << endl;
    for (auto it : res) {
        string ans = "";
        for(auto it1:it){
            ans += mp2[it1];
        }
        cout << ans << endl;
    }

    set<char> prime;
    for(auto it: res){
        for(auto it1:it){
            prime.insert(it1);
        }
    }
    set<pair<string,string>> partial;
    for(auto it: vp){
        string r = it.second;
        bool f = 1,f1 = 1,f2 = 1;
        for(auto it1:r){
            if(prime.find(it1) == prime.end()){
                for(auto it2:res){
                    if(isSubset(it.first,it2) && it.first != it2){
                        f = 0;
                    }
                }
            }
        }
        for(auto it1:it.first){
            if(prime.find(it1) == prime.end()){
                f1 = 0;
            }
        }
         for(auto it1:it.second){
            if(prime.find(it1) == prime.end()){
                f2 = 0;
            }
        }
        if(f == 0 || (f1 == 0 && f2 == 0)){
            partial.insert({it.first,it.second});
        }
    }
    set<char> attr;
    for(int i =0;i < n;i++) attr.insert(i + 'a');
    cout << "partial dependicies are : " << endl;
    for(auto it : partial){
        string ans = "",ans2 = "";
        for(auto it1:it.first) ans += mp2[it1];
          for(auto it1:it.second) ans2 += mp2[it1];
        cout << ans << " " << ans2 << endl;
    }
    cout << "Decomposed Tables are: " << endl;
    vector<string> closetab;
    for(auto it: partial){
        string close = findCandidateKeylosure(it.first,vp);
      bool f = 1;
      for(auto it1:closetab){
        if(isSubset(close,it1)){
            f = 0;
        }
      }
      if(f == 0) continue;
      closetab.push_back(close);
      string cclose = "";
      for(auto itt:close) cclose += mp2[itt];
        cout << cclose << endl;
        set<char> l,r;
        for(auto it1 : it.first) l.insert(it1);     
        for(auto it1: close){
            if(l.find(it1) == l.end()) r.insert(it1);
        }
        set<char> newattr;
        for(auto it:attr){
            if(r.find(it) == r.end()) newattr.insert(it);
        }
        attr = newattr;
    }
    string fin = "";
    for(auto it : attr) fin += mp2[it];
    cout << fin << endl;

    return 0;
}
