# VCT Hackathon 2024

Temporary README.md file with directions for the project.

## Downloads

- **Git:** https://git-scm.com/downloads (select VSCode as default code editor)
- **Node.js:** https://nodejs.org/en (local node environment)
- **NVM:** https://github.com/nvm-sh/nvm (optional, but good to have in case of different node versions)
- **Python:** https://www.python.org/downloads/

## Development Guide

### Next.js
1. Install yarn (Windows tutorial: https://youtu.be/HyJ89KCB7x8?si=GDqsvi3ZUBw1Jnc-)
2. Sign in to VSCode with your GitHub account and clone the repository. Instructions can be found here: https://code.visualstudio.com/docs/sourcecontrol/github
3. Open the VSCode terminal and navigate to the client-next folder with `cd client-next`.
4. Run `yarn install` to install all the needed dependencies for the project.
5. Run `yarn dev` to start the project on localhost:3000.

### Python
1. In your terminal, run: `ssh user@your-production-server`
2. Navigate to your project directory on the server: `cd /path/to/your/project`
3. Create a virtual environment (Python 3.x): `python3 -m venv venv`
4. On Linux/MacOS: `source venv/bin/activate`
5. On Windows (if applicable): `.\venv\Scripts\activate`
6. Install requirements: `pip install -r requirements.txt`

Amazon Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html
