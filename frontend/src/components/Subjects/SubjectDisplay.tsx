// Displays a list of subjects
import useSubjects from "../../hooks/useSubjects";
import SubjectList from "./SubjectList";
import SubjectForm from "./SubjectForm";
import React, { useState } from "react";

const SubjectsDisplay: React.FC = () => {
  const [showForm, setShowForm] = useState<boolean>(false);
  const { subjects, loading, error } = useSubjects();

  const toggleSubjectForm = () => {
    setShowForm((cur: boolean) => !cur);
  };

  return (
    <div>
      <h1>Subjects</h1>
      <button onClick={toggleSubjectForm}>
        {showForm ? "Cancel" : "Create Subject"}
      </button>
      {showForm && <SubjectForm />}
      {loading && <p>Loading subjects...</p>}
      {error && <p>{error}</p>}
      {subjects.length > 0 ? (
        <SubjectList subjects={subjects} />
      ) : (
        !loading && <p>No subjects available</p>
      )}
    </div>
  );
};

export default SubjectsDisplay;
