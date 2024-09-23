// Displays a single flashcard
import { FlashCard } from "../../types/types";

export const FlashcardItem: React.FC<{ flashcard: FlashCard }> = ({
  flashcard,
}) => {
  return (
    <div
      style={{
        border: "1px solid #ccc",
        padding: "10px",
        marginBottom: "10px",
      }}
    >
      <p>
        <strong>Question:</strong> {flashcard.question}
      </p>
      <p>
        <strong>Answer:</strong> {flashcard.answer}
      </p>
      <p>
        <strong>Confidence:</strong> {flashcard.confidence}
      </p>
      <p>
        <strong>Subject ID:</strong> {flashcard.subject_id}
      </p>
    </div>
  );
};
