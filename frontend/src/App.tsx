import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import FlashcardsPage from "./pages/FlashcardsPage";
import SubjectsPage from "./pages/SubjectsPage";

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/flashcards" element={<FlashcardsPage />} />
        <Route path="/subjects" element={<SubjectsPage />} />
      </Routes>
    </Router>
  );
};

export default App;
