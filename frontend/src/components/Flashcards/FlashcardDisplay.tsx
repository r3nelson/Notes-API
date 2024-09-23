// Displays a list of flashcards
import FlashcardList from "./FlashcardList";
import useFlashcards from "../../hooks/useFlashcards";

const FlashcardsDisplay: React.FC = () => {
  const { flashcards, loading, error } = useFlashcards();

  return (
    <div>
      <h1>Flashcards</h1>
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
