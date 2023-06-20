CREATE OR REPLACE PROCEDURE update_subject
(
	subj_id_old INT,
	subj_id_new INT,
	subj_title TEXT,
	subj_type TEXT
)
LANGUAGE plpgsql AS $$
DECLARE
	temp_teach_id INT;
	temp_teach_name TEXT;
	temp_week INT;
	temp_day INT;
	temp_time_id INT;
	temp_room TEXT;
	temp_num INT;
BEGIN
	SELECT id INTO temp_teach_id FROM timetable WHERE subject_id_fk=subj_id_old;
	SELECT name INTO temp_teach_name FROM preps WHERE subject_id_fk=subj_id_old;
	DELETE FROM preps WHERE subject_id_fk = subj_id_old;
	
	SELECT id INTO temp_time_id FROM timetable WHERE subject_id_fk = subj_id_old;
	SELECT num_of_week INTO temp_week FROM timetable WHERE subject_id_fk = subj_id_old;
	SELECT day INTO temp_day FROM timetable WHERE subject_id_fk = subj_id_old;
	SELECT room_numb INTO temp_room FROM timetable WHERE subject_id_fk = subj_id_old;
	SELECT num_of_pair INTO temp_num FROM timetable WHERE subject_id_fk = subj_id_old;
	DELETE FROM timetable WHERE subject_id_fk =subj_id_old;
	
	UPDATE subject SET id = subj_id_new, title = subj_title, lec_lab_prac = subj_type WHERE id = subj_id_old;
	INSERT INTO preps VALUES(temp_teach_id, temp_teach_name, subj_id_new);
	INSERT INTO timetable VALUES(temp_time_id, temp_day,subj_id_new, temp_room,temp_num,temp_week);
END;
$$;

