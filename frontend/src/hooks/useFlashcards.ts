// Custom hook for handling flashcard data and logic
import { useState, useEffect } from "react";
import { FlashCard } from "../types/types";
import { fetchFlashcards } from "../services/flashcardService";

const useFlashcards = () => {
  const [flashcards, setFlashcards] = useState<FlashCard[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const getFlashcards = async () => {
      setLoading(true);
      try {
        const flashcardData = await fetchFlashcards();
        setFlashcards(flashcardData);
      } catch (error) {
        setError("Failed to fetch flashcards");
        console.error(error);
      } finally {
        setLoading(false);
      }
    };
    getFlashcards();
  }, []);

  return { flashcards, loading, error };
};

export default useFlashcards;
