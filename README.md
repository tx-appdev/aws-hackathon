# VCT X AWS | Esports Manager Challenge

### Inspiration

Our inspiration for this project stems from our former founding and management of our high school Valorant Esports team, which went on to achieve a 3rd place ranking in the High School Esports League's Atlantic Region.

### What It Does

This LLM-Powered Digital Esports Assistant is a next-gen esports management app that leverages AI and Amazon Bedrock to analyze player performance, optimize team compositions, and provide personalized insights for professional Valorant teams.

### How We Built It

#### Designing Our App

To optimize performance through server sided rendering and static site generation, we opted to use Next.js for our web application. We chose to implement a Python backend for compatibility with Cloud AI services, allowing seamless integration with Amazon Bedrock.

#### LLM Training and Implementation

To train and use the LLM for our project, we implemented the following procedures:

- First, we used an Amazon IAM to set up our organization and to access Amazon Bedrock's Anthropic Claude model.
- We then accessed player statistics from https://www.vlr.gg/stats, converted the data into CSV files, and uploaded the data to Amazon Bedrock's Knowledge Bases.
- To implement Amazon Bedrock in our app, we used Boto3 to interact with AWS services and receive a text response.
- Finally, we used an Axios and Flask to fetch the responses from the backend whenever the user chat interface instantiated a new conversation.

### Challenges We Faced

One of the primary challenges we faced was a lack of experience developing with AWS products, as well as a lack of exposure to training LLM models in general. However, we turned this into a rich learning experience and gained critical skills working with Amazon Bedrock and Python backend environments in full-stack applications.

### Accomplishments We're Proud Of

Some accomplishments we are proud of include our implementation of a functional chat interface powered by Amazon Bedrock and our proactiveness in learning new skills under set time constraints. We are also proud of our versatility in developing a full-fledged application together as students based in multiple different universities.

### What We Learned

Through this project, we gained valuable experience implementing AWS services in full-stack web applications. We learned to navigate the AWS platform and work with elements of a Python backend, as well as training an LLM model with custom data.

### What's Next

To improve on this project further, we plan to use a larger data set to train the LLM model to improve accuracy of responses. We also plan to refactor our code base for the web application from having multiple CSS files to being fully Tailwind, in order to improve performance and increase maintainability. 
