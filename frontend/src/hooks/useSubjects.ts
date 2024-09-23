// Custom hook for handling subject data and logic
import { useState, useEffect } from "react";
import { Subject } from "../types/types";
import { fetchSubjects } from "../services/subjectService";

const useSubjects = () => {
  const [subjects, setSubjects] = useState<Subject[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const getSubjects = async () => {
      setLoading(true);
      try {
        const flashcardData = await fetchSubjects();
        setSubjects(flashcardData);
      } catch (error) {
        setError("Failed to fetch subjects");
        console.error(error);
      } finally {
        setLoading(false);
      }
    };
    getSubjects();
  }, []);

  return { subjects, loading, error };
};

export default useSubjects;
