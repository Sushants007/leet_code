/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root)
    {
        queue<TreeNode*> qu;
        vector<vector<int>> ans;
        if(root == nullptr)
        {
            return ans;
        }
        qu.push(root);
        while(!qu.empty())
        {
            int size = qu.size();
            vector<int> temp;
            for(int i = 0 ; i < size ; ++i)
            {
                temp.push_back(qu.front()->val);
                if(qu.front()->left)
                {
                    qu.push(qu.front()->left);
                }
                if(qu.front()->right)
                {
                    qu.push(qu.front()->right);
                }
                qu.pop();
            }
            ans.push_back(temp);
        }
        return ans;
    }
};