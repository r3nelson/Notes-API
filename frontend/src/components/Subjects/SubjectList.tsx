import React from "react";
import SubjectItem from "./SubjectItem";
import { Subject } from "../../types/types"; // Adjust the import based on your types

interface SubjectListProps {
  subjects: Subject[];
}

const SubjectList: React.FC<SubjectListProps> = ({ subjects }) => {
  return (
    <ul>
      {subjects.map((subject) => (
        <li key={subject.id}>
          <SubjectItem subject={subject} />
        </li>
      ))}
    </ul>
  );
};

export default SubjectList;
