class Solution {
public:

    vector<vector<string>> og;

    string encode(vector<string>& strs) {
        og.push_back(strs);
        int encoded = og.size()-1;
        return to_string(encoded);
    }

    vector<string> decode(string s) {
        return og[stoi(s)];
    }
};
