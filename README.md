# Data Structures & Algorithms Library in Python

A high-performance, production-ready, object-oriented library of fundamental data structures implemented from scratch in Python. Each structure features comprehensive boundary-case management, dynamic iterator support, and optimal asymptotic time complexities.

---
# 🐍 Data Structures in Python

### 📝 About This Repository
The **`Data-structures-python`** folder is a comprehensive, structured collection of core Data Structures and Algorithms implemented from scratch using Python. It serves as a dedicated practice hub to master problem-solving, memory tracking, and software design principles. 

The implementations focus heavily on exploring different object-oriented design patterns, specifically comparing:
*   **Composition / Object Reference:** Building structures by linking distinct node objects together.
*   **Inheritance:** Extending existing structures or Python's built-in types to create specialized behavior.

---

## 📁 Repository Directory

This list reflects the exact folder structure of the repository.

### 🔹 Data-structures-python/ (Main Root Folder)

*   📂 **`data-structures/`** — Folder containing core linear data structures like linked lists.
    *   📂 `singly-linked-list/` — Folder containing various single-directional linked list setups.
        *   📄 `sll_head.py` — Singly linked list managed using only a head pointer.
        *   📄 `sll_head_tail.py` — Optimized singly linked list using both head and tail pointers.
    *   📄 `doubly-linked_list.py` — Standard doubly linked list implementation with forward and backward tracking.
*   📂 **`circular-lists/`** — Folder containing list structures where the last element links back to the first.
    *   📄 `cll.py` — Circular Singly Linked List implementation.
    *   📄 `cdll.py` — Circular Doubly Linked List implementation.
*   📂 **`Stack/`** — Folder containing Last-In-First-Out (LIFO) stack architectures.
    *   📄 `stack_sll_object.py` — Stack implemented using a Singly Linked List via composition (object creation).
    *   📄 `stack_sll_inheritance.py` — Stack implemented by inheriting from a Singly Linked List class.
    *   📄 `stack_list_inheritance.py` — Stack implemented by inheriting from Python's built-in `list`.
    *   📄 `stack_list.py` — Stack implemented using standard Python lists.
    *   📄 `stack_linked_list.py` — Custom linked-list-backed stack implementation.
*   📂 **`Queue/`** — Folder containing First-In-First-Out (FIFO) queue architectures.
    *   📄 `queue_sll_object.py` — Queue using standard Singly Linked List composition.
    *   📄 `queue_sll_inheritance.py` — Queue that inherits features from a Singly Linked List.
    *   📄 `queue_list_inheritance.py` — Queue inheriting directly from Python's built-in `list`.
    *   📄 `queue_list.py` — Standard Queue implementation using Python lists.
    *   📄 `queue_linked_list.py` — Custom linked-list-backed queue implementation.
*   📂 **`Deque/`** — Folder containing Double-Ended Queue (Deque) implementations allowing insertion and deletion from both ends.
    *   📄 `deque_list.py` — Double-ended queue using a Python list.
    *   📄 `deque_list_inheritance.py` — Deque inheriting from Python's built-in `list`.
    *   📄 `deque_dll.py` — Double-ended queue optimized using a Doubly Linked List.
