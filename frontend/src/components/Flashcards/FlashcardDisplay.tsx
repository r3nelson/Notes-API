// Displays a list of flashcards
import FlashcardList from "./FlashcardList";
import FlashcardForm from "./FlashcardForm";
import useFlashcards from "../../hooks/useFlashcards";
import { useState } from "react";

const FlashcardsDisplay: React.FC = () => {
  const [showForm, setShowForm] = useState<boolean>(false);
  const { flashcards, loading, error } = useFlashcards();

  const toggleFlashcardForm = () => {
    setShowForm((cur) => !cur);
  };

  return (
    <div>
      <h1>Flashcards</h1>
      <button onClick={toggleFlashcardForm}>
        {showForm ? "Cancel" : "Create Flashcard"}
      </button>

      {showForm && <FlashcardForm />}

      {loading && <p>Loading flashcards</p>}
      {error && <p>{error}</p>}
      {flashcards.length > 0 ? (
        <FlashcardList flashcards={flashcards} />
      ) : (
        !loading && <p>No flashcards available</p>
      )}
    </div>
  );
};

export default FlashcardsDisplay;
