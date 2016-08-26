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

	courses.push(new Course("Robotics", "Build angry robots", "James Smith", "4:00-5:00am"));
	courses.push(new Course("Space", "sun stars and moon", "Tammy Porter", "6:00-7:00pm"));
	courses.push(new Course("Flowers", "smell good", "Sam Rhodes", "6:00-7:00pm"));
	courses.push(new Course("Rocks", "are hard", "The Rock", "6:00-7:00pm"));
	courses.push(new Course("Pants", "long", "Mr. Pants", "6:00-7:00pm"));
	courses.push(new Course("Shoes", "walking and running", "Dr. Socks", "6:00-7:00pm"));
	courses.push(new Course("Halo", "High altitude", "Dillan Ryans", "6:00-7:00pm"));

	return courses;
}