"""
Data models for the Library Management System.
Defines Book, Member, and Loan classes.
"""

from datetime import datetime
from typing import Optional


class Book:
    """Represents a book in the library."""
    
    def __init__(self, book_id: str, title: str, author: str):
        """
        Initialize a Book object.
        
        Args:
            book_id: Unique identifier for the book
            title: Title of the book
            author: Author of the book
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True  # Initially available
    
    def borrow(self) -> None:
        """Mark the book as borrowed."""
        self.available = False
    
    def return_book(self) -> None:
        """Mark the book as returned (available)."""
        self.available = True
    
    def __str__(self) -> str:
        return f"{self.book_id} - {self.title} by {self.author}"
    
    def __repr__(self) -> str:
        status = "Available" if self.available else "Borrowed"
        return f"Book({self.book_id}, {self.title}, {self.author}, {status})"


class Member:
    """Represents a library member."""
    
    def __init__(self, member_id: str, name: str, email: str):
        """
        Initialize a Member object.
        
        Args:
            member_id: Unique identifier for the member
            name: Full name of the member
            email: Email address of the member
        """
        self.member_id = member_id
        self.name = name
        self.email = email
    
    def __str__(self) -> str:
        return f"{self.member_id} - {self.name} ({self.email})"
    
    def __repr__(self) -> str:
        return f"Member({self.member_id}, {self.name}, {self.email})"


class Loan:
    """Represents a book loan record."""
    
    def __init__(self, loan_id: str, book: Book, member: Member):
        """
        Initialize a Loan object.
        
        Args:
            loan_id: Unique identifier for the loan
            book: Book object being borrowed
            member: Member object borrowing the book
        """
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.borrow_date = datetime.now()
        self.return_date: Optional[datetime] = None
        self.is_active = True
    
    def close_loan(self) -> None:
        """Close the loan and mark the return date."""
        self.return_date = datetime.now()
        self.is_active = False
    
    def __str__(self) -> str:
        status = "Active" if self.is_active else "Closed"
        return f"{self.loan_id} - {self.member.name} borrowed {self.book.title} [{status}]"
    
    def __repr__(self) -> str:
        return f"Loan({self.loan_id}, {self.book.book_id}, {self.member.member_id}, {self.is_active})"
