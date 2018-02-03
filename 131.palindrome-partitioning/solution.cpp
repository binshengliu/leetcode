#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Result {
public:
	Result expand_to_new(string substring) const {
		Result new_one;
		new_one.result = this->result;
		if (new_one.result.empty()) {
			new_one.result.push_back(vector<string>());
		}

		for (size_t i = 0; i < new_one.result.size(); ++i) {
			new_one.result[i].push_back(substring);
		}

		return new_one;
	}

	void merge(Result &other) {
		this->result.reserve(this->result.size() + other.result.size());
		this->result.insert(this->result.begin(), other.result.begin(), other.result.end());
	}

	vector<vector<string> > raw() {
		return this->result;
	}

	void print() {
		for (size_t row = 0; row < this->result.size(); ++row) {
			for (size_t col = 0; col < this->result[row].size(); ++col) {
				cout << this->result[row][col] << " ";
		    }
		    cout << endl;
	    }
	}
private:
	vector<vector<string> > result;
};

class Solution {
public:
    vector<vector<string> > partition(string s) {
	    size_t size = s.size();
	    vector<vector<bool> > pal(size, vector<bool>(size, false));

	    vector<Result> result(size, Result());
	    for (size_t col = 0; col < size; ++col) {
		    for (size_t row = 0; row <= col; ++row) {
			    if (s[row] == s[col]) {
				    if (row == col || row + 1 == col) {
					    pal[row][col] = true;
				    } else  {
					    pal[row][col] = pal[row+1][col-1];
				    }
			    }
			    if (pal[row][col]) {
				    string sub = s.substr(row, col+1-row);
				    Result r;
				    if (row != 0) {
					    r = result[row-1].expand_to_new(sub);
				    } else {
					    r = r.expand_to_new(sub);
				    }

				    result[col].merge(r);
			    }
		    }
	    }

	    return result[size-1].raw();
    }
};

int main(int argc, char *argv[])
{
	Solution s;
	for (size_t i = 0; i < 10000; ++i) {
		vector<vector<string> > result = s.partition("aabsdfsdfasdreqwsadfsadf");
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
