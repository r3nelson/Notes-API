// Custom hook for handling flashcard data and logic
import { useState, useEffect } from "react";
import { FlashCard } from "../types/types";
import { fetchFlashcards } from "../services/flashcardService";

const useFlashcards = () => {
  const [flashcards, setFlashcards] = useState<FlashCard[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const getFlashcards = async () => {
      try {
        const flashcardData = await fetchFlashcards();
        setFlashcards(flashcardData);
      } catch (error) {
        setError("Failed to fetch flashcards");
        console.error(error);
      }
    };
    getFlashcards();
  }, []);

  return { flashcards, error };
};

export default useFlashcards;
