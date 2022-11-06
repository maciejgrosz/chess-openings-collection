conn = new Mongo();
db = conn.getDB("openings");
db.createUser(
    {
        user: "flaskdb",
        pwd: "flaskdb",
        roles: [
            {
                role: "readWrite",
                db: "openings"
            }
        ]
    }
    );
    