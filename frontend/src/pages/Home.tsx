import React from "react";
import { Link } from "react-router-dom";

const Home: React.FC = () => {
  return (
    <div>
      <h1>Welcome to the Study App</h1>
      <nav>
        <ul>
          <li>
            <Link to="/flashcards">View Flashcards</Link>
          </li>
          <li>
            <Link to="/subjects">View Subjects</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Home;
