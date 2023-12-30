# Task Manager Demo

## Description

This is a assigment demo for a simple task manager django application using DjangoRESTFramework.
This app adds, updates and deletes tasks along with showing all tasks and task status.

## Table of Contents

- [Task Manager Demo](#task-manager-demo)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
    - [Activate the virtual environment:](#activate-the-virtual-environment)
    - [3. Install Dependencies](#3-install-dependencies)
    - [4. Apply Migrations](#4-apply-migrations)
    - [5. Run the Development Server](#5-run-the-development-server)
    - [6. Run the test cases](#6-run-the-test-cases)

## Prerequisites

- Python 3.x (Developed using 3.8.6)

## Getting Started

Follow these instructions to set up and run your project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/RahilV/Arcitech_task_manager.git
cd Arcitech_task_manager
```

### 2. Create a Virtual Environment

- For Windows
    ```bash
        python -m venv venv
    ```
- For macOS/Linux:
    ```bash
        python3 -m venv venv
    ```

### Activate the virtual environment:

- For Windows
    ```bash
        .\venv\Scripts\activate
    ```
- For macOS/Linux:
    ```bash
        source venv/bin/activate
    ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```
(note if "python" command doesn't work use "python3")

### 5. Run the Development Server
```bash
python manage.py runserver
```
(note if "python" command doesn't work use "python3")

### 6. Run the test cases
```bash
python manage.py test
```
(note if "python" command doesn't work use "python3")