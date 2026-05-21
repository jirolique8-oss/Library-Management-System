# Library Management System

A comprehensive Python-based Library Management System that allows users to manage books, members, and loans in a library.

## Features

### 1. **Add Book** (Flowchart: _01_add_book.svg)
- Add new books to the library
- Store book information: ID, Title, Author
- Books are automatically marked as available

### 2. **Register Member** (Flowchart: _02_register_member.svg)
- Register new library members
- Store member information: ID, Name, Email

### 3. **Borrow Book** (Flowchart: _03_borrow_book.svg)
- Members can borrow available books
- Validates both book and member existence
- Marks book as unavailable when borrowed
- Creates loan records with unique loan IDs
- Error handling for:
  - Book not found
  - Member not found
  - Book already borrowed

### 4. **Return Book** (Flowchart: _04_return_book.svg)
- Members can return borrowed books
- Marks book as available again
- Closes the loan record
- Validates book, member, and active loan

### 5. **View Books** (Flowchart: _05_view_book.svg)
- Display all books in the library
- Shows status: Available or Borrowed
- Empty state handling

### 6. **View Members** (Flowchart: _06_view_member.svg)
- Display all registered members
- Shows member ID, Name, and Email
- Empty state handling

### 7. **View Loans** (Flowchart: _07_view_loan.svg)
- Display all loans (active and closed)
- Shows loan status: Active or Closed
- Includes member name and book title

### 8. **Exit** (Flowchart: _08_exit.svg)
- Gracefully exit the application

## Project Structure

```
Library-Management-System/
├── book.py              # Book class definition
├── member.py            # Member class definition
├── loan.py              # Loan class definition
├── exceptions.py        # Custom exceptions
├── library_service.py   # Core service class
├── main.py              # Application entry point
├── README.md            # This file
└── flowcharts/          # Visual flowcharts for each feature
    ├── _01_add_book.svg
    ├── _02_register_member.svg
    ├── _03_borrow_book.svg
    ├── _04_return_book.svg
    ├── _05_view_book.svg
    ├── _06_view_member.svg
    ├── _07_view_loan.svg
    └── _08_exit.svg
```

## Class Descriptions

### Book
Represents a book in the library with methods to track borrowing status.

**Attributes:**
- `book_id`: Unique identifier
- `title`: Book title
- `author`: Author name
- `available`: Boolean flag (True = available, False = borrowed)

**Methods:**
- `borrow()`: Mark book as borrowed
- `return_book()`: Mark book as available

### Member
Represents a library member.

**Attributes:**
- `member_id`: Unique identifier
- `name`: Member name
- `email`: Email address

### Loan
Represents a book loan transaction.

**Attributes:**
- `loan_id`: Unique loan identifier (format: L001, L002, etc.)
- `book`: Book object
- `member`: Member object
- `is_active`: Boolean (True = active loan, False = returned)
- `borrow_date`: Timestamp of borrowing
- `return_date`: Timestamp of return (None if active)

**Methods:**
- `close_loan()`: Mark loan as returned and set return date

### LibraryService
Core service class managing all library operations.

**Methods:**
- `add_book(book_id, title, author)`: Add a new book
- `register_member(member_id, name, email)`: Register a member
- `borrow_book(book_id, member_id)`: Borrow a book
- `return_book(book_id, member_id)`: Return a book
- `view_books()`: Get all books
- `view_members()`: Get all members
- `view_loans()`: Get all loans

## Custom Exceptions

- `BookNotFoundError`: Raised when a book ID doesn't exist
- `MemberNotFoundError`: Raised when a member ID doesn't exist
- `BookUnavailableError`: Raised when attempting to borrow an already borrowed book
- `LoanNotFoundError`: Raised when no active loan is found for return

## Usage

### Running the Application

```bash
python main.py
```

### Example Workflow

1. **Add a Book:**
   - Select option 1
   - Enter Book ID: `B001`
   - Enter Title: `Python Programming`
   - Enter Author: `John Doe`

2. **Register a Member:**
   - Select option 2
   - Enter Member ID: `M001`
   - Enter Name: `Alice Smith`
   - Enter Email: `alice@example.com`

3. **Borrow a Book:**
   - Select option 3
   - Enter Book ID: `B001`
   - Enter Member ID: `M001`

4. **View Books:**
   - Select option 5
   - See all books with their status

5. **Return a Book:**
   - Select option 4
   - Enter Book ID: `B001`
   - Enter Member ID: `M001`

6. **View Loans:**
   - Select option 7
   - See all loans and their status

## Error Handling

The system includes comprehensive error handling:
- Validation of required fields
- Detection of non-existent books/members
- Prevention of borrowing unavailable books
- Tracking of loan status for returns
- User-friendly error messages

## Design Patterns

- **Service Layer Pattern**: LibraryService encapsulates business logic
- **Entity Pattern**: Book, Member, and Loan are domain entities
- **Exception Handling**: Custom exceptions for specific error cases
- **Data Structure**: Dictionaries for O(1) lookups, lists for ordered data

## Future Enhancements

- Database integration (SQLite, PostgreSQL)
- Due dates and late fees
- Book search and filtering
- Member transaction history
- Authentication and authorization
- Data persistence
- Graphical user interface (GUI)
- API endpoints (REST/GraphQL)

## Author

Created as a Library Management System project with comprehensive flowcharts and object-oriented design.

## License

Open source - feel free to use and modify!
