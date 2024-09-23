// Custom hook for handling subject data and logic
import { useState, useEffect } from "react";
import { Subject } from "../types/types";
import { fetchSubjects } from "../services/subjectService";

const useSubjects = () => {
  const [subjects, setSubjects] = useState<Subject[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const getSubjects = async () => {
      try {
        const flashcardData = await fetchSubjects();
        setSubjects(flashcardData);
      } catch (error) {
        setError("Failed to fetch subjects");
        console.error(error);
      }
    };
    getSubjects();
  }, []);

  return { subjects, error };
};

export default useSubjects;
