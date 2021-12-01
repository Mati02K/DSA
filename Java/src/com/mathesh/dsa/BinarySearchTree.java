package com.mathesh.dsa;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;


public class BinarySearchTree {
    private int data;
    private BinarySearchTree left;
    private BinarySearchTree right;

    public BinarySearchTree(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }

    public int getData() {
        return data;
    }

    public void setData(int data) {
        this.data = data;
    }

    public BinarySearchTree getLeft() {
        return left;
    }

    public void setLeft(BinarySearchTree left) {
        this.left = left;
    }

    public BinarySearchTree getRight() {
        return right;
    }

    public void setRight(BinarySearchTree right) {
        this.right = right;
    }

    public void add_child(int data){
        if(data == this.getData()){
            System.out.println("Number Already Exists in the Tree");
        }

        if(data < this.getData()){
            if(this.getLeft() != null){
                this.getLeft().add_child(data);
            }
            else{
                this.setLeft(new BinarySearchTree(data));
            }
        }

        if(data > this.getData()){
            if(this.getRight() != null){
                this.getRight().add_child(data);
            }
            else{
                this.setRight(new BinarySearchTree(data));
            }
        }
    }

    public void in_order_traversal(){
        if(this == null){
            System.out.println("Tree is Empty");
        }
//        Left
        if(this.getLeft() != null){this.getLeft().in_order_traversal();}

//        Data
        System.out.println(this.getData() + " ");

//        Right
        if(this.getRight() != null){this.getRight().in_order_traversal();}
    }

    public void pre_order_traversal(){
        if(this == null){
            System.out.println("Tree is Empty");
        }
        // Data
        System.out.println(this.getData() + " ");

//        Left
        if(this.getLeft() != null){this.getLeft().pre_order_traversal();}

//        Right
        if(this.getRight() != null){this.getRight().pre_order_traversal();}
    }

    public void post_order_traversal(){
        if(this == null){
            System.out.println("Tree is Empty");
        }

//        Left
        if(this.getLeft() != null){this.getLeft().pre_order_traversal();}

//        Right
        if(this.getRight() != null){this.getRight().pre_order_traversal();}

        // Data
        System.out.println(this.getData() + " ");
    }

    public BinarySearchTree deleteNode(BinarySearchTree Tree, int data){

//      To be Done
        if(Tree == null){
            return Tree;
        }
        //        Checking for leaf node
        if(Tree.getLeft() != null
                && Tree.getLeft().getData() == data
                && Tree.getLeft().getLeft() == null
                && Tree.getLeft().getRight() == null) {
            Tree.setLeft(null);
        }
        if(Tree.getRight() != null
                && Tree.getRight().getData() == data
                && Tree.getRight().getLeft() == null
                && Tree.getRight().getRight() == null) {
            Tree.setRight(null);
        }

        if(Tree.getData() > data){
            deleteNode(Tree.getLeft(),data);
        }
        else if(Tree.getData() < data){
            deleteNode(Tree.getRight(),data);
        }

        else{
            if(Tree.getLeft() == null){
                return Tree.getRight();
            }
            else if(Tree.getRight() == null){
                return Tree.getLeft();
            }
            Tree.setData(findMin(Tree.getRight()));

            Tree.setRight(deleteNode(Tree.getRight(), Tree.getData()));
        }
        return Tree;
    }

    public int findMin(BinarySearchTree Tree){

        if(Tree == null){
            System.out.println("Tree is Empty");
            return -1;
        }
        while(Tree.getLeft() != null){
            Tree = Tree.getLeft();
        }
        return Tree.getData();
    }

    //    Inverting  a Binary Tree is simply getting a symmetric image if a tree, however Binary Search Properties will be gone
    public BinarySearchTree invertBinaryTree(BinarySearchTree tree){
        if(tree == null){
            return null;
        }
//        Swapping of left and right
        BinarySearchTree temp = tree.getLeft();
        tree.setLeft(tree.getRight());
        tree.setRight(temp);

//        Calling on left and right childs to continue the same property
        invertBinaryTree(tree.getLeft());
        invertBinaryTree(tree.getRight());

        return tree;
    }


    //    Level Order Traversal of a Binary tree
    public List<List<Integer>> levelOrderTraversal(BinarySearchTree tree){
        List<List<Integer>> traversal = new ArrayList<>();
        Queue<BinarySearchTree> queue = new LinkedList<>();
        BinarySearchTree curr = null;
        queue.add(tree);
        while(!queue.isEmpty()){
            List<Integer> tmplist = new ArrayList<>();
            int n = queue.size();
            for(int i = 0; i < n; i++) {
                curr = queue.remove();
                if (curr != null) {
                    tmplist.add(curr.getData());
                    queue.add(curr.getLeft());
                    queue.add(curr.getRight());
                }
            }
            if(tmplist.size() > 0){
                traversal.add(tmplist);
            }
        }
        return traversal;
    }


    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree(25);
        tree.add_child(45);
        tree.add_child(32);
        tree.add_child(2);
        tree.add_child(23);
        tree.add_child(90);

        tree.in_order_traversal();
        System.out.println("------------------");
        tree.pre_order_traversal();
        System.out.println("------------------");
        tree.post_order_traversal();
        System.out.println(tree.findMin(tree));
        //tree = tree.deleteNode(tree,32);
        //tree = tree.invertBinaryTree(tree);
        tree.in_order_traversal();
        System.out.println(tree.levelOrderTraversal(tree));


    }
}

