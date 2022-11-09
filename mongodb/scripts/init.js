db = db.getSiblingDB('admin');
db.createUser(
 {
   user: "flaskdb",
   pwd: "flaskdb",
   roles: [
    { role: "readWrite", db: "openings" },
   ]
 }
);
