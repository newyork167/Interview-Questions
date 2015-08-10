/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Insert(Node *head,int data)
{
  // Complete this method
    if(head == NULL){
        head = (Node*)malloc(sizeof(Node));
        head->data = data;
        return head;
    }
    
    if (head->next != NULL){
        Insert(head->next, data);
    }
    else{
        head->next = (Node*)malloc(sizeof(Node));
        head->next->data = data;
    }
    
    return head;
}