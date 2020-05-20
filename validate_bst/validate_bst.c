#include <stdio.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool validate(struct TreeNode *node, struct TreeNode **prev)
{
	if (!node)
		return true;
	if (!validate(node->left, prev))
		return false;
	if (*prev && (*prev)->val >= node->val)
		return false;
	*prev = node;
	return validate(node->right, prev);

}

bool isValidBST(struct TreeNode *root)
{
	struct TreeNode *prev = NULL;
	return validate(root, &prev);
}
