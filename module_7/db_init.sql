
DROP USER IF EXISTS 'pysports_user'@'localhost';

CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Grace@9812T';

GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';


DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;


CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);


-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Team Gandalf', 'White Wizards');

INSERT INTO team(team_name, mascot)
    VALUES('Team Sauron', 'Orcs');


-- insert player records 
INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Daniel', 'Luo', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Erik', 'Tuazama', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Amber', 'Jones', (SELECT team_id FROM team WHERE team_name = 'Team Gandalf'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Prince', 'Zama', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Grace', 'Tua', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('PaaTay', 'Gono', (SELECT team_id FROM team WHERE team_name = 'Team Sauron'));