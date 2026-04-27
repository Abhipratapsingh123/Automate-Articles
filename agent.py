from langgraph.graph import StateGraph,START,END
from nodes import evaluate_language,evaluate_format,evaluate_grammar
from state import EvalState

# defining workflow
graph = StateGraph(EvalState)

graph.add_node("language", evaluate_language)
graph.add_node("format", evaluate_format)
graph.add_node("grammar", evaluate_grammar)


# definging edges
graph.add_edge(START,"language")
graph.add_edge("language","format")
graph.add_edge("format","grammar")
graph.add_edge("grammar",END)


workflow = graph.compile()


result = workflow.invoke(
{
"article": """ Supervised Machine Learning
Last Updated : 14 Apr, 2026
Supervised learning is a type of machine learning where a model learns from labelled data, meaning each input has a correct output. The model compares its predictions with actual results and improves over time to increase accuracy.

supervised-machine-learning
Supervised Machine Learning
Its main features are:

Labelled Data: Each input has a known output
Learning from Errors: Adjusts itself to reduce prediction errors
Goal: Make accurate predictions on new data
Example: Recognizing handwritten digits from trained data
Types of Supervised Learning
Now, Supervised learning can be applied to two main types of problems:



Classification: Where the output is a categorical variable (e.g., spam vs. non-spam emails, yes vs. no).
Regression: Where the output is a continuous variable (e.g., predicting house prices, stock prices).
difff
Types of Supervised Learning
Let's first understand the classification and regression data through the table below:

supervised-data
Sample
Both the above figures have labelled data set as follows:

Figure A: It is a dataset of a shopping store that is useful in predicting whether a customer will purchase a particular product under consideration or not based on his/her gender, age and salary.

Input: Gender, Age, Salary
Output: Purchased i.e. 0 or 1; 1 means yes the customer will purchase and 0 means that the customer won't purchase it.
Figure B: It is a Meteorological dataset that serves the purpose of predicting wind speed based on different parameters.

Input: Dew Point, Temperature, Pressure, Relative Humidity, Wind Direction
Output: Wind Speed
Working of Supervised Machine Learning
The working of supervised machine learning follows these key steps:

1. Collect Labeled Data
Gather a dataset where each input has a known correct output (label).
Example: Images of handwritten digits with their actual numbers as labels.
2. Split the Dataset
Divide the data into training data (about 80%) and testing data (about 20%).
The model will learn from the training data and be evaluated on the testing data.
3. Train the Model
Feed the training data (inputs and their labels) to a suitable supervised learning algorithm (like Decision Trees, SVM or Linear Regression).
The model tries to find patterns that map inputs to correct outputs.
4. Validate and Test the Model
Evaluate the model using testing data it has never seen before.
The model predicts outputs and these predictions are compared with the actual labels to calculate accuracy or error.
5. Deploy and Predict on New Data
Once the model performs well, it can be used to predict outputs for completely new, unseen data.
Supervised Machine Learning Algorithms
Supervised learning can be further divided into several different types, each with its own unique characteristics and applications. Here are some of the most common types of supervised learning algorithms:

Linear Regression: Linear regression is a type of supervised learning regression algorithm that is used to predict a continuous output value. It is one of the simplest and most widely used algorithms in supervised learning.
Logistic Regression: Logistic regression is a type of supervised learning classification algorithm that is used to predict a binary output variable.
Decision Trees : Decision tree is a tree-like structure that is used to model decisions and their possible consequences. Each internal node in the tree represents a decision, while each leaf node represents a possible outcome.
Random Forests: Random forests again are made up of multiple decision trees that work together to make predictions. Each tree in the forest is trained on a different subset of the input features and data. The final prediction is made by aggregating the predictions of all the trees in the forest.
Support Vector Machine(SVM): The SVM algorithm creates a hyperplane to segregate n-dimensional space into classes and identify the correct category of new data points. The extreme cases that help create the hyperplane are called support vectors, hence the name Support Vector Machine.
K-Nearest Neighbors: KNN works by finding k training examples closest to a given input and then predicts the class or value based on the majority class or average value of these neighbors. The performance of KNN can be influenced by the choice of k and the distance metric used to measure proximity.
Gradient Boosting: Gradient Boosting combines weak learners, like decision trees, to create a strong model. It iteratively builds new models that correct errors made by previous ones.
Naive Bayes Algorithm: The Naive Bayes algorithm is a supervised machine learning algorithm based on applying Bayes' Theorem with the “naive” assumption that features are independent of each other given the class label.
Algorithm	Regression,
Classification	Purpose	Method	Use Cases
Linear Regression	Regression	Predict continuous output values	Linear equation minimizing sum of squares of residuals	Predicting continuous values
Logistic Regression	Classification	Predict binary output variable	Logistic function transforming linear relationship	Binary classification tasks
Decision Trees	Both	Model decisions and outcomes	Tree-like structure with decisions and outcomes	Classification and Regression tasks
Random Forests	Both	Improve classification and regression accuracy	Combining multiple decision trees	Reducing overfitting, improving prediction accuracy
SVM	Both	Create hyperplane for classification or predict continuous values	Maximizing margin between classes or predicting continuous values	Classification and Regression tasks
KNN	Both	Predict class or value based on k closest neighbors	Finding k closest neighbors and predicting based on majority or average	Classification and Regression tasks, sensitive to noisy data
Gradient Boosting	Both	Combine weak learners to create strong model	Iteratively correcting errors with new models	Classification and Regression tasks to improve prediction accuracy
Naive Bayes	Classification	Predict class based on feature independence assumption	Bayes' theorem with feature independence assumption	Text classification, spam filtering, sentiment analysis, medical
These types of supervised learning in machine learning vary based on the problem we're trying to solve and the dataset we're working with. In classification problems, the task is to assign inputs to predefined classes, while regression problems involve predicting numerical outcomes.

Practical Examples of Supervised learning
Fraud Detection in Banking: Uses labeled transaction data to identify and predict fraudulent activities.
Parkinson Disease Prediction: Analyzes medical data to detect and predict the presence of the disease.
Customer Churn Prediction: Uses historical customer data to predict whether a customer will leave a service.
Cancer cell classification: Implements supervised learning for cancer cells based on their features and identifying them if they are ‘malignant’ or ‘benign.
Stock Price Prediction: Uses past data to predict stock trends and support investment decisions.
Advantages
Easy to understand and implement as it learns from labeled data.
Provides high accuracy when sufficient labeled data is available.
Works for both classification (spam detection, disease prediction) and regression (price forecasting).
Can generalize well to unseen data with proper training and diverse datasets.
Widely used in applications like speech recognition, medical diagnosis, sentiment analysis and fraud detection.
Disadvantages
Requires large amounts of labeled data, which is expensive and time-consuming to prepare.
Can be biased if the training data is unbalanced, leading to unfair or inaccurate predictions.
May overfit the training data instead of learning general patterns, especially with small datasets.
Performance can drop when applied to data that is very different from the training data.
Not easily scalable for problems with a very large number of labels, such as in natural language tasks.
̉̉"""}

)


print(result["language_feedback"])
print(result["format_feedback"])
print(result["grammar_feedback"])
print(result["individual_scores"])













   