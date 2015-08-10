/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* InsertNth(Node *head, int data, int position)
{
    Node* node = NULL;
  // Complete this method only
  // Do not write main function. 
    if (position != 0){
        if (head->next != NULL){
            Node* next = InsertNth(head->next, data, position - 1);
            head->next = next;
        }
        else{
            head->next = (Node*)malloc(sizeof(Node*));
            head->next->data = data;
        }
    }else{
        node = (Node*)malloc(sizeof(Node));
        node->data = data;
        node->next = head;
    }
    
    return node != NULL ? node : head;
}