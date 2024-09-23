// Displays a list of flashcards
import FlashcardItem from "./FlashCardItem";
import useFlashcards from "../../hooks/useFlashcards";

const FlashcardsDisplay: React.FC = () => {
  const { flashcards, error } = useFlashcards();

  return (
    <div>
      <h1>Flashcards</h1>
      {error && <p>{error}</p>}
      {flashcards.length > 0 ? (
        <ul>
          {flashcards.map((flashcard) => (
            <li key={flashcard.id}>
              <FlashcardItem flashcard={flashcard} />
            </li>
          ))}
        </ul>
      ) : (
        <p> No flashcards available</p>
      )}
    </div>
  );
};

export default FlashcardsDisplay;
