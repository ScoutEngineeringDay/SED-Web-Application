function Course(courseName, courseDescription, instructor, time) {
    this.courseName = courseName;
    this.courseDescription = courseDescription;
    this.instructor = instructor;
    this.time = time;

	this.setCourseName = function(newName){
		this.courseName = newName;
	}
	this.getCourseName = function(){
		return this.courseName;
	}
	this.setCourseDescription = function(newDescription){
		this.courseDescription = newDescription;
	}
	this.getCourseDescription = function(){
		return this.courseDescription;
	}
	this.setInstructor = function(newInstructor){
		this.instructor = newInstructor;
	}
	this.getInstructor = function(){
		return this.instructor;
	}
	this.setTime = function(newTime){
		this.time = newTime;
	}
	this.getTime = function(){
		return this.time;
	}

	this.commitToDatabase = function(){
		//To be implemented
	}
}

function getAllCourses(){
	var courses = new Array();

	courses.push(new Course("Robotics", "Earning the Robotics merit badge requires a Scout to understand how robots move (actuators), sense the environment (sensors), and understand what to do (programming); he should demonstrate robot design in building a robot. You should help ensure that the Scout has sufficiently explored the field of robotics to understand what it is about, and to discover whether this may be a field of interest for him as a career.", "James Smith", "4:00-5:00am"));
	courses.push(new Course("Space Exploration", "Space is mysterious. We explore space for many reasons, not least because we don't know what is out there, it is vast, and humans are full of curiosity. Each time we send explorers into space, we learn something we didn't know before. We discover a little more of what is there.", "Tammy Porter", "6:00-7:00pm"));
	courses.push(new Course("Engineering", "Engineers use both science and technology to turn ideas into reality, devising all sorts of things, ranging from a tiny, low-cost battery for your cell phone to a gigantic dam across the mighty Yangtze River in China.", "6:00-7:00pm"));
	courses.push(new Course("Electronics", "Electronics is the science that controls the behavior of electrons so that some type of useful function is performed. Today, electronics is a fast-changing and exciting field.", "The Rock", "6:00-7:00pm"));
	courses.push(new Course("Chemistry", "Chemistry explores how substances react with each other, how they change, how certain forces connect molecules, and how molecules are made are all parts of chemistry. Stretch your imagination to envision molecules that cannot be seen—but can be proven to exist—and you become a chemist.", "Mr. Pants", "6:00-7:00pm"));
	courses.push(new Course("Oceanography", "The oceans cover more than 70 percent of our planet and are the dominant feature of Earth. Wherever you live, the oceans influence the weather, the soil, the air, and the geography of your community. To study the oceans is to study Earth itself.", "Dr. Socks", "6:00-7:00pm"));
	courses.push(new Course("Geology", "Geology is the study of Earth. It includes the study of materials that make up Earth, the processes that change it, and the history of how things happened, including human civilization, which depends on natural materials for existence.", "Dillan Ryans", "6:00-7:00pm"));

	return courses;
}

function findCourse(){
	//To be implemented
}