# Sales Lead Agent

A sales lead management application built with Vue 3, TypeScript, and Python Flask backend.

## Features

- Lead management dashboard
- Customer management system
- AI-powered sales assistance (when deployed with backend)
- Responsive UI with Vue 3 and TypeScript

## Deployment

This project can be deployed using GitHub Pages as a static site:

1. Build the project:
   ```bash
   npm run build
   ```

2. Push the built files to the `gh-pages` branch:
   ```bash
   git add .
   git commit -m "Build for deployment"
   git subtree push --prefix dist origin gh-pages
   ```

3. In your GitHub repository:
   - Go to Settings
   - Click on "Pages" in the left sidebar
   - Select "Deploy from a branch"
   - Choose "gh-pages" branch and "/ (root)" folder
   - Click "Save"

4. Your app will be available at:
   ```
   https://zijun13.github.io/sales-lead-agent/
   ```

## Local Development

### Frontend Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Run the development server:
   ```bash
   npm run dev
   ```

3. Open `http://localhost:3000` in your browser.

### Backend Setup (Optional for local development)

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   python server.py
   ```

5. The backend will be running at `http://localhost:8000`.

## Architecture

- Frontend: Vue 3 with TypeScript, Vite, Vue Router
- Backend: Python Flask API
- AI Skills: Python modules implementing sales agent capabilities

## Notes

Since this is deployed as a static site on GitHub Pages, the backend API functionality is disabled. The frontend uses simulated data for demonstration purposes.