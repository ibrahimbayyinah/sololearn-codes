function Person(name, age){
    this.name = name;
    this.age = age;
    this.changeName = function(name){
        this.name = name;
    }
}

var John = new Person("John", 24);
document.write(John.name + "<br>");
John.changeName("Derek");
document.write(John.name);
