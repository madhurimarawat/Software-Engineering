# Software-Engineering
This repository provides exercises for practicing software engineering techniques, including version control, code review, unit testing with Python, continuous integration, and agile methodologies.

<img src = "https://static.vecteezy.com/system/resources/previews/000/180/409/original/software-engineers-vector.png" height = "500px" width = "100%">

## Tools and Technologies ⚙️💻

### 1. [Python](https://docs.python.org/3/)
Python is a high-level, interpreted programming language known for its simplicity and versatility. It is widely used in software engineering for tasks such as unit testing, code analysis, and automation. The `pytest` framework, used in this repository, is a popular testing tool in the Python ecosystem for writing simple and scalable test cases.

- **[pytest Documentation](https://docs.pytest.org/en/latest/)**
  
    `pytest` is a Python-based testing framework that simplifies writing small to complex test cases. It supports the development of unit tests by providing mechanisms for writing assertions, handling test fixtures, and generating test reports. Its ability to scale from simple functions to complex applications makes it ideal for ensuring code reliability and correctness.

### 2. [Git](https://madhurimarawat.github.io/Semester-Notes/Git-Commands.html)
Git is a distributed version control system that tracks changes to files and allows multiple people to collaborate on a project. It enables users to manage and coordinate changes to the source code, ensuring that different versions of the code are maintained efficiently. Key operations include creating repositories, committing changes, and pushing to remote repositories.

### 3. [Sphinx](https://www.sphinx-doc.org/en/master/)
Sphinx is a documentation generation tool designed to convert Python code comments (docstrings) into rich, accessible HTML documentation. It supports automatic API documentation and extensive formatting features, making it ideal for creating comprehensive documentation for software projects.

### 4. [MkDocs](https://www.mkdocs.org/)
MkDocs is a static site generator specifically for project documentation. It emphasizes simplicity and markdown-based writing, making it easy to create well-structured documentation with minimal configuration. MkDocs is known for its clean, readable layouts and is used in various development environments to create professional documentation.

### 5. [Unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
The `unittest.mock` module in Python allows for replacing parts of a system under test with mock objects to simulate real-world behaviors. This technique is useful in unit testing when isolating the function under test by removing dependencies on external components or systems, ensuring that tests remain focused and independent.

### 6. [Dependency-Injector](https://python-dependency-injector.ets-labs.org/)
`dependency-injector` is a Python framework for implementing dependency injection, a design pattern that decouples the creation of dependencies from their usage. By injecting dependencies into objects rather than hard-coding them, this technique promotes flexibility, testability, and modularity in software design.

### 7. [GitHub Actions And Travis CI](https://docs.github.com/en/actions) | [Travis CI Documentation](https://docs.travis-ci.com/)
GitHub Actions and Travis CI are continuous integration (CI) tools that automate the building and testing of code whenever changes are pushed to a repository. CI pipelines ensure that code quality is maintained by running tests automatically after each commit, allowing teams to detect and fix errors early in the development process.

### 8. [Codacy](https://docs.codacy.com/)
Codacy is an automated code review tool that helps ensure code quality and maintainability by analyzing code for potential issues, code style violations, and complexity. It integrates with various version control systems and provides feedback on each commit or pull request to promote cleaner, more efficient code.

### 9. [CodeFactor](https://docs.codefactor.io/)
CodeFactor is a code analysis tool that provides automated feedback on code quality by identifying style issues, potential bugs, and code complexity. It helps teams maintain high-quality code by integrating with GitHub repositories and providing real-time feedback on code changes. CodeFactor also supports code metrics and reporting for ongoing improvements.

---

## Directory Structure 📂

This repository **Software-Engineering** organizes various experiments related to software engineering practices, each identified by its experiment number. 

- **Experiment Structure**: Each experiment contains subfolders for:
  - Source code
  - Documentation
  - Output files
- **Experiment Examples**:
  - **Experiment 1**: Includes Python source and test code using `pytest`, documentation explaining the testing methodology, and a summary of the output.
  - **Experiment 2**: Focuses on Git operations, featuring relevant text files and output documentation.
- **Further Topics (Experiments 3 to 11)**:
  - **Documentation Generation**: Using Sphinx and MkDocs.
  - **Practical Exercises**: Including mocking, dependency injection, and code refactoring.
  - **Hands-on Learning**: Jupyter notebooks for interactive learning.
- **Continuous Integration**: Experiment 7 addresses CI processes, with documentation related to GitHub Actions and Travis CI.
- **Markdown Conversion**: Markdown files have been converted to PDF format using [md2pdf](https://md2pdf.netlify.app/).
- **Navigation**: The structured approach facilitates easy navigation and understanding of the resources and outcomes related to each experiment.

```
Software-Engineering/
│
├── Experiment 1/
│   ├── Source Code/ 💻             # Contains Python source code related to unit testing using pytest.
|   ├── Test/ 💻                    # Contains Python test code related to unit testing using pytest
│   ├── Documentation/ 📝      # Includes word documentation explaining test cases and methodology.
│   │   └── Pytest Unit Testing.docx
│   ├── Output/ 📊                  # Holds Word document with output for Experiment 1.
│   │   └── Experiment 1 Output.docx
│
├── Experiment 2/
│   ├── Documentation/ 📝           # Contains text files related to Git operations and learning.
│   │   ├── Git Setup And Commands.txt
│   ├── Output/ 📊                  # Holds Word document with output for Experiment 2.
│   │   └── Experiment 2 Output.docx
│   ├── Learning-Git Repo Content/  # Stores content from the associated Learning Git repository.
│   │   └── repo_files/
│
├── Experiment 3/
│   ├── Documentation/ 📝                     # Example projects demonstrating Sphinx and MkDocs usage.
│   │   ├── Experiment 3 Commands.docx        # Contains commands and procedures used in Experiment 3.
│   ├── Experiment Output/ 📊                   # Holds Word document with output for Experiment 3.
│   │   └── Experiment 3 Output.docx            # Output from Experiment 3.
│   ├── Example Documentation/                   # Contains simple examples of output files.
│   ├── MkDocs Pdoc Documentation/              # Documentation generated using MkDocs and Pdoc.
│   ├── Sphinx Docstring Documentation/          # Documentation generated automatically using Sphinx.
│   ├── Docstring Documentation/ 📝              # Contains docstring documentation in markdown format.
│   │   └── docstrings.md                        # Markdown file containing docstrings.
│   ├── Output/ 📊                              # Word file containing the output from MkDocs and Pdoc tools.
│   │   └── Experiment 3 Output.docx            # Consolidated output for Experiment 3.
│   ├── Reference Documents/ 📚                  # Additional reference materials or readings related to Sphinx and MkDocs.
│   │   └── additional_readings.md               # Contains further documentation regarding Sphinx and MkDocs.
│   ├── Experiment Output Docstring Documentation # Contains the output and generated documentation for Experiment 3.
│   ├── README.md 📝    #  Contains the Documentation for this folder
│
├── Experiment 4/ 💻
│   └── Mocking.ipynb                    # Jupyter notebook for mocking exercises.
│
├── Experiment 5/ 💻
│   └── Dependency Injection.ipynb       # Jupyter notebook for dependency injection exercises.
│
├── Experiment 6/ 💻
│   └── Code Refactoring.ipynb           # Jupyter notebook for code refactoring exercises.
│
└── Experiment 7/
    ├── Output/ 📊                  # Single Word document with output for CI processes.
    │   └── Experiment 7 Output.docx
    ├── GitHub Actions/             # Contains markdown and PDF documentation related to GitHub Actions CI.
    │   ├── Documentation/ 📝
    │   │   ├── GitHub Actions Description.md
    │   │   └── GitHub Actions Description.pdf
    ├── Travis CI/                  # Contains markdown and PDF documentation related to Travis CI.
    │   ├── Documentation/ 📝
    │   │   ├── Travis CI Description.md
    │   │   └── Travis CI Description.pdf
```

---

## Table Of Contents 📔 🔖 📑

### 1. [Unit Testing with pytest](https://github.com/madhurimarawat/Software-Engineering/tree/main/Experiment%201)

This experiment focuses on writing and executing unit tests for Python functions using the pytest framework. You will cover various test cases and assertions to ensure the correctness and reliability of your code.

### 2. [Version Control with Git](https://github.com/madhurimarawat/Software-Engineering/tree/main/Experiment%202)

This experiment involves practicing basic Git operations such as repository creation, file addition, committing changes, and pushing to a remote repository. You can find additional practice and details in the [Learning Git Repository](https://github.com/madhurimarawat/Learning-Git).

### 3. [Code Documentation Practice](https://github.com/madhurimarawat/Software-Engineering/tree/main/Experiment%203)

Write Python function and class docstrings to document code functionality. Students will then generate HTML documentation using tools like Sphinx or MkDocs. This exercise stresses the importance of maintaining clear and accessible code documentation.

### 4. [Mocking](https://github.com/madhurimarawat/Software-Engineering/tree/main/Experiment%204)

Practice the technique of mocking in Python using libraries such as `unittest.mock`. Students will isolate and test individual components of a software system by replacing dependencies with mock objects, simulating real components in a controlled environment.

### 5. [Dependency Injection](https://github.com/madhurimarawat/Software-Engineering/tree/main/Experiment%205)

Explore the concept of dependency injection using libraries like `dependency-injector`. This technique enables students to write flexible and testable code by decoupling the components from their dependencies, allowing easier integration and testing.

### 6. [Code Refactoring Exercise](https://github.com/madhurimarawat/Software-Engineering/tree/main/Experiment%206)

Identify and refactor code snippets to improve code quality, readability, and performance. Focus on techniques such as extracting methods, removing duplication, and improving naming conventions. This exercise aims to enhance the maintainability and efficiency of the code while adhering to best practices in software development.

### 7. [Continuous Integration Setup](https://github.com/madhurimarawat/Software-Engineering/tree/main/Experiment%206)

Set up a basic continuous integration (CI) pipeline using tools like Travis CI or GitHub Actions. You can refer to additional resources in the [Learning Travis CI Repository](https://github.com/madhurimarawat/Learning-Travis-CI) and [Learning GitHub Actions Repository](https://github.com/madhurimarawat/Learning-GitHub-Actions-CI).

### 8. [Agile Sprint Planning](https://github.com/madhurimarawat/Software-Engineering/tree/main/Experiment%208)
 
Conduct a simulated sprint planning session following agile principles, where students break down user stories into tasks, estimate their effort, and allocate them for a sprint. This exercise emphasizes collaboration, clear task definitions, and effective time management, preparing participants for real-world agile practices in software development.

**Related Repositories:**  
- [Agile-Sprint-and-Iris-Data-Explorer](https://github.com/madhurimarawat/Agile-Sprint-and-Iris-Data-Explorer)

### 9. [Code Review Automation](https://github.com/madhurimarawat/Software-Engineering/tree/main/Experiment%209)

Integrate a code quality analysis tool like CodeFactor or Codacy with GitHub to automatically analyze code changes and provide feedback on code style, complexity, and potential issues. This exercise helps students understand the importance of automated code reviews for maintaining code quality and streamlining the development workflow.

**Related Repositories:**  
- [Learning-Codacy](https://github.com/madhurimarawat/Learning-Codacy)
- [Learning-CodeFactor](https://github.com/madhurimarawat/Learning-CodeFactor)

### 10. [Code Review Simulation](https://github.com/madhurimarawat/Software-Engineering/tree/main/Experiment%2010)

Conduct a simulated code review session where students provide feedback on each other's code, focusing on readability, maintainability, and adherence to coding standards. This exercise aims to cultivate constructive feedback skills, promote code quality, and reinforce best practices for collaboration among developers.

### 11. [Pair Programming Activity](https://github.com/madhurimarawat/Software-Engineering/tree/main/Experiment%2011)
 
Pair up students to work on a programming task collaboratively, taking turns as the driver and navigator, and switching roles periodically to promote teamwork and knowledge sharing. This activity fosters communication, enhances problem-solving skills, and helps students learn from each other while improving code quality and development efficiency.

---

## Thanks for Visiting 😄

- Drop a 🌟 if you find this repository useful.<br><br>
- If you have any doubts or suggestions, feel free to reach me.<br><br>
📫 How to reach me:  &nbsp; [![Linkedin Badge](https://img.shields.io/badge/-madhurima-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/madhurima-rawat/) &nbsp; &nbsp;
<a href ="mailto:rawatmadhurima@gmail.com"><img src="https://github.com/madhurimarawat/Machine-Learning-Using-Python/assets/105432776/b6a0873a-e961-42c0-8fbf-ab65828c961a" height=35 width=30 title="Mail Illustration" alt="Mail Illustration📫" > </a><br><br>
- **Contribute and Discuss:** Feel free to open <a href= "https://github.com/madhurimarawat/Software-Engineering/issues">issues 🐛</a>, submit <a href = "https://github.com/madhurimarawat/Software-Engineering/pulls">pull requests 🛠️</a>, or start <a href = "https://github.com/madhurimarawat/Software-Engineering/discussions">discussions 💬</a> to help improve this repository!
