// Displays a list of flashcards
import React, { useEffect, useState } from "react";
import { fetchFlashcards } from "../../services/flashcardService";
import { FlashCard } from "../../types/types";

const FlashcardsDisplay: React.FC = () => {
  const [flashcards, setFlashcards] = useState<FlashCard[]>([]);

  useEffect(() => {
    const getFlashcards = async () => {
      try {
        const flashcardData = await fetchFlashcards();
        setFlashcards(flashcardData);
      } catch (error) {
        console.error(error);
      }
    };
    getFlashcards();
  }, []);
  return (
    <div>
      <h1>Flashcards</h1>
      <ul>
        {flashcards.map((flashcard) => (
          <li key={flashcard.id}>
            {flashcard.question} - {flashcard.answer} - {flashcard.confidence} -{" "}
            {flashcard.subject_id}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FlashcardsDisplay;
