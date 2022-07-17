/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *a = headA;
        ListNode *b = headB;
        int a_cnt = 0;
        int b_cnt = 0;
        while (a) {
            a_cnt++;
            a = a->next;
        }
        while (b) {
            b_cnt++;
            b = b->next;
        }
        a = headA;
        b = headB;
        while (a && a_cnt > b_cnt) {
            a = a->next;
            a_cnt--;
        }
        while (b && a_cnt < b_cnt) {
            b = b->next;
            b_cnt--;
        }
        while (a && b) {
            if (a == b) return a;
            else {
                a = a->next;
                b = b->next;
            }
        }
        return nullptr;
    }
};
