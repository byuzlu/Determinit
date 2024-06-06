# Determinit
This project is designed to facilitate informed decision-making processes through the implementation of a weighted decision matrix calculation. The application provides users with a structured framework for evaluating candidates or options based on multiple criteria and their associated traits. By utilizing a weighted approach, users can assign relative importance to each criterion, reflecting their specific priorities and preferences.

Core Functionality
The core functionality of the application revolves around the creation and management of criteria and candidates. Users, whether they are administrators or candidates themselves, can create new criteria, defining the key attributes or characteristics that are relevant to the decision-making process. For each criterion, users can specify multiple traits or sub-factors, further refining the evaluation process. The related chart can be shown in Application_Chart.JPG file.

Database Integration
To ensure seamless data management and accessibility, the application integrates with an SQL database. This allows for the systematic storage of criteria, traits, candidate information, and evaluation results. By leveraging the capabilities of the SQL database, users can easily retrieve and update information as needed, ensuring data integrity and reliability throughout the decision-making process. The related chart can be shown in Database_Chart.JPG file.

Candidate Evaluation
Once criteria and candidates are defined and stored in the database, users can initiate the evaluation process. The application calculates a weighted score for each candidate based on their performance across the defined criteria and traits. This weighted score provides a quantitative measure of each candidate's suitability or alignment with the desired criteria, aiding in the decision-making process.

Sensitivity Analysis (Future Development)
In future developments, the application could be enhanced to incorporate sensitivity analysis capabilities. Sensitivity analysis allows users to assess the impact of changes in criteria weights on the overall evaluation outcome. By adjusting the relative importance of criteria and observing the corresponding changes in candidate rankings, users can gain insights into the robustness of their decision-making model and identify potential areas of focus or improvement.

Libraries Used
The project utilizes several libraries to support its functionality:

sqlite3: for database management and integration.
PySimpleGUI: for building a user-friendly graphical interface.
numpy: for numerical calculations and data manipulation.

Installation and Usage
To set up the project environment, users should install the required libraries and ensure access to an SQL database. The application can then be executed using the provided scripts, allowing users to create criteria, add candidates, and initiate evaluations through the intuitive interface.

Future Enhancements
In addition to sensitivity analysis, future enhancements could include advanced reporting and visualization capabilities, allowing users to explore evaluation results in greater detail. Integration with external data sources or APIs could also enrich the decision-making process by providing additional context or insights.

Contributors and Contact
For any questions, contributions, or support, please reach out to baha.yuzlu@gmail.com. Your feedback and contributions are highly valued and appreciated as I continue to evolve and improve the application.
