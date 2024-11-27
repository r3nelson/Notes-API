// Displays a list of flashcards
import FlashcardList from "./FlashcardList";
import FlashcardForm from "./FlashcardForm";
import useFlashcards from "../../hooks/useFlashcards";
import { useState } from "react";

const FlashcardsDisplay: React.FC = () => {
  const [showCreateFlashcardForm, setShowCreateFlashcardForm] =
    useState<boolean>(false);
  //   const [showSelectSubjectForm, setShowSelectSubjectForm] =
  //     useState<boolean>(false);
  const { flashcards, loading, error } = useFlashcards();

  const toggleFlashcardForm = () => {
    setShowCreateFlashcardForm((cur) => !cur);
  };

  //   const toggleSelectSubjectForm = () => {
  //     setShowSelectSubjectForm((cur) => !cur);
  //   };

  return (
    <div>
      <h1>Flashcards</h1>
      <button onClick={toggleFlashcardForm}>
        {showCreateFlashcardForm ? "Cancel" : "Create Flashcard"}
      </button>
      {/* <button onClick={toggleSelectSubjectForm}>Show Flashcards</button> */}

      {showCreateFlashcardForm && <FlashcardForm />}
      {/* {showSelectSubjectForm && <SelectSubjectForm />} */}

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
