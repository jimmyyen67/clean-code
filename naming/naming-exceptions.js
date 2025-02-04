var Database = /** @class */ (function () {
    function Database() {
    }
    Object.defineProperty(Database.prototype, "connectedClient", {
        get: function () {
            if (!this.client) {
                throw new Error('Database not connected!');
            }
            return this.client;
        },
        enumerable: false,
        configurable: true
    });
    Database.prototype.connect = function () {
        this.client = {};
    };
    return Database;
}());
var db = new Database();
db.connectedClient.query();
