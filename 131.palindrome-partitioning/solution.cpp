#include <vector>
#include <string>
#include <iostream>
using namespace std;

bool is_palindrome(string &s) {
	size_t begin = 0;
	size_t end = s.size() - 1;
	while (begin < end) {
		if (s[begin] != s[end]) {
			return false;
		}
		++begin;
		--end;
	}

	return true;
}

void find_palindrome_recursively(const string &s, vector<string> &path, vector<vector<string> > &result) {
	if (s.empty()) {
		result.push_back(path);
		return;
	}

	for (size_t i = 0; i < s.size(); ++i) {
		string prefix = s.substr(0, i + 1);
		string suffix = s.substr(i + 1);
		if (is_palindrome(prefix)) {
			path.push_back(prefix);
			find_palindrome_recursively(suffix, path, result);
			path.pop_back();
		}
	}
}

class Solution {
public:
    vector<vector<string> > partition(string s) {
	    vector<vector<string> > result;
	    vector<string> path;
	    find_palindrome_recursively(s, path, result);
	    return result;
    }
};

int main(int argc, char *argv[])
{
	Solution s;
	for (size_t i = 0; i < 1; ++i) {
		vector<vector<string> > result = s.partition("aab");
	for (size_t i = 0; i < result.size(); ++i) {
		for (size_t j = 0; j < result[i].size(); ++j) {
			cout << result[i][j] << " ";
		}
		cout << endl;
	}
	}
	// cout << "Result: " << endl;
	// for (size_t i = 0; i < result.size(); ++i) {
	// 	for (size_t j = 0; j < result[i].size(); ++j) {
	// 		cout << result[i][j] << " ";
	// 	}
	// 	cout << endl;
	// }
	return 0;
}
