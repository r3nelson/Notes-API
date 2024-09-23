// Displays a list of subjects
import useSubjects from "../../hooks/useSubjects";
import SubjectList from "./SubjectList";

const SubjectsDisplay: React.FC = () => {
  const { subjects, loading, error } = useSubjects();

  return (
    <div>
      <h1>Subjects</h1>
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
