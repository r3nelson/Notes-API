import FlashcardItem from "./FlashcardItem";
import { FlashCard } from "../../types/types";

interface FlascardListProps {
  flashcards: FlashCard[];
}

const FlashcardList: React.FC<FlascardListProps> = ({ flashcards }) => {
  return (
    <ul>
      {flashcards.map((flashcard) => (
        <li key={flashcard.id}>
          <FlashcardItem flashcard={flashcard} />
        </li>
      ))}
    </ul>
  );
};

export default FlashcardList;
