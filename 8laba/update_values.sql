CREATE OR REPLACE PROCEDURE update_values
(
  timetable_week INT, 
  timetable_day INT,
  timetable_num INT,
  timetable_room_numb TEXT,
  subject_type TEXT,
  teacher_fullname TEXT,
  subject_title TEXT
)
LANGUAGE plpgsql AS $$
DECLARE
  my_subject_id INT;
BEGIN
  SELECT subject_id_fk INTO my_subject_id FROM timetable
  WHERE day = timetable_day AND num_of_week = timetable_week AND num_of_pair = timetable_num;

  
  UPDATE subject SET lec_lab_prac = subject_type, title=subject_title WHERE id = my_subject_id;
  UPDATE preps SET name = teacher_fullname WHERE id = my_subject_id;
  UPDATE timetable SET room_numb = timetable_room_numb WHERE id = my_subject_id;
END;
$$; 


CALL update_values(1,1,4,'Н-333','лекция','Шаймарданова Л. К.', 'Высшая математика');