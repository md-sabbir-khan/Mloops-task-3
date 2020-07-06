# Mloops-task-3 Machine Learning with DevOps

1  Create container image that’s has Python 3 and Keras or numpy installed using docker file.
   When we launch this image, it should automatically starts train the model in the container.
2. Create a job chain of job 1, job 2, job 3, job 4 and job 5 using build pipeline plugin in Jenkins.

3. Job 1 : Pull the GitHub repository automatically when some developers push repo to GitHub.

4. Job 2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to    deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the software required for the CNN processing).

5. Job 3 : if metrics accuracy is less than 90% then tweak the machine learning model architecture.

6. Job 4 :After model train successfully it send a Email notification to the Developer.

7. Job 5 : for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left.
