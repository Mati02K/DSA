package com.mathesh.dsa;


class Node<T> {
    private T data;
    private Node<T> next; // Next Node

    public Node(T data) {
        this.data = data;
        this.next = null;
    }

    public T getData() {
        return data;
    }
//    Set data Setter is not needed as we set the value through Constructor

    public Node<T> getNext() {
        return next;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }
}

public class LinkedList<T> {
    private Node<T> head;

    public void insertAtHead (T data){
        Node<T> newNode = new Node<>(data);
        this.head = newNode;
    }

    public void insertAtEnd (T data) {
        if(this.head == null) {
            this.insertAtHead(data);
        }
        Node<T> itr = this.head;

        while(itr.getNext() != null)
        {
            itr = itr.getNext();
        }
        itr.setNext(new Node<T>(data));
    }

    @Override
    public String toString() {
        if(this.head == null){
            System.out.println("Linked List is Empty");
        }
        Node<T> itr = this.head;
        String llist = "";
        while(itr != null){
            if(itr.getNext() != null){
                llist = llist + String.valueOf(itr.getData()) + " ---> ";
            }
            else{
                llist += String.valueOf(itr.getData());
            }
            itr = itr.getNext();
        }
        return llist;
    }

    public int getLength(){
        int length = 0;
        Node<T> itr = this.head;
        while(itr != null){
            length += 1;
            itr = itr.getNext();
        }
        return length;
    }

    public boolean removeByValue(T data){
        if(this.head == null){
            System.out.println("Linked List Is Empty");
            return false;
        }
        try{
            if(this.head.getData() == data){
                this.head = this.head.getNext();
                return true;
            }
        }
        catch (Exception e){
            System.out.println("Invalid Datatypes");
        }

        Node<T> itr = this.head;
        while(itr.getNext() != null){
            try{
                if(itr.getNext().getData() == data){
                    itr.setNext(itr.getNext().getNext());
                    System.out.println("Node " + data + " has been deleted");
                    return true;
                }
            }
            catch (Exception e){
                System.out.println("Invalid Datatypes");
                return false;
            }
            finally {
                itr = itr.getNext();
            }
        }
        return false;
    }

    public Node<T> reverseLinkedList(Node<T> head){
        if(head == null){
            return head;
        }
        Node<T>  curr = head;
        Node<T> prev = null;
        Node<T> next = null;
        while(curr != null){
            next = curr.getNext();
            curr.setNext(prev);
            prev = curr;
            curr = next;
        }
        return prev;
    }

    public static void main(String[] args) {
        LinkedList<Integer> ll = new LinkedList<>();
        ll.insertAtHead(20);
        ll.insertAtEnd(23);
        ll.insertAtEnd(34);
        ll.insertAtEnd(2);
        ll.insertAtEnd(97);
        System.out.println(ll);
        System.out.println(ll.getLength());
        ll.removeByValue(97);
        System.out.println(ll);
        ll.head = ll.reverseLinkedList(ll.head);
        System.out.println(ll);
    }
}
