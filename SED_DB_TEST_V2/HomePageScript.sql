CREATE TABLE SED_Database.sedUI_homepage(
	homepage_id INT(10) ZEROFILL NOT NULL AUTO_INCREMENT PRIMARY KEY,
    homepage_description VARCHAR(5000),
    homepage_news_event VARCHAR(5000)
);
INSERT INTO SED_Database.sedUI_homepage
	(homepage_description, homepage_news_event)
VALUES
	("MITRE Scout Engineering Day was pioneered in 2012 at the headquarters of The MITRE Corporation in the Washington, DC area. Each year since its inception, Scout Engineering Day has hosted between 300 to 400 Scouts and 70 to 100 Scouters, Merit Badge Counselors and volunteers for an exciting day of STEM activities. We look forward to welcoming your Scout to this year's event!", "The Boy Scouts of America is one of the nation's largest and most prominent values-based youth development organizations. The BSA provides a program for young people that builds character, trains them in the responsibilities of participating citizenship, and develops personal fitness.");
