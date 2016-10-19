function Course(courseName, courseDescription, id, instructor, time) {
    this.courseName = courseName;
    this.courseDescription = courseDescription;
    this.id = id;
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
	this.getID = function(){
		return this.id;
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

function getAllCourses(callback) {
	/* call the php that has the php array which is json_encoded */
    console.log('Getting JSON');
 

    $.getJSON('getCourses.php', function(data) {
	   	console.log('loaded JSON');
	    var courses = []; // create array here
	    $.each(data, function(index, courseObject) {
	    	courses.push(new Course(courseObject.courseName, courseObject.courseDescription, courseObject.instructor, courseObject.time));
	    });
		callback.call(this,courses);
    });
    console.log("After function")
}

function decodeJson(){
    console.log("INSIDE OF FUNCTION");
    

}