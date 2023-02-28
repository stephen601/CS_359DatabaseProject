CREATE TABLE Video(videoCode int, videoLength int, PRIMARY KEY (videoCode));

CREATE TABLE Model(modelNo char(10), width numeric(6,2), height numeric(6,2), weight numeric(6,2), depth numeric(6,2), screenSize numeric(6,2), PRIMARY KEY(modelNo));

CREATE TABLE Site (siteCode int, type varchar(16), address varchar(100), phone
varchar(16), PRIMARY KEY(siteCode));

CREATE TABLE DigitalDisplay(serialNo char(10), schedulerSystem char(10), modelNo char(10), PRIMARY KEY(serialNo), FOREIGN KEY (modelNo) REFERENCES Model(modelNo));

CREATE TABLE Client (clientId integer, name varchar(40), phone varchar(16), address varchar(100), PRIMARY KEY(clientId));

CREATE TABLE TechnicalSupport(empId integer, name varchar (40), gender char (1), PRIMARY KEY(empID));

CREATE TABLE Administrator(empId integer, name varchar(40), gender char(1), PRIMARY KEY(empId));

CREATE TABLE Salesman (empId integer, name varchar (40), gender char (1), PRIMARY KEY(empId));

CREATE TABLE AirtimePackage(packageId integer, class varchar (16), startDate date, lastDate date, frequency integer, videoCode integer, PRIMARY KEY(packageId));

CREATE TABLE AdmWorkHours(empId integer, day date, hours numeric(4,2), PRIMARY KEY(empId, day), FOREIGN KEY(empId) REFERENCES Administrator(empId));

CREATE TABLE Broadcasts(videoCode integer, siteCode integer, PRIMARY KEY(videoCode, siteCode), FOREIGN KEY(videoCode) REFERENCES Video(videoCode), FOREIGN KEY(siteCode) REFERENCES Site(siteCode));

CREATE TABLE Administers(empId integer, siteCode integer, PRIMARY KEY(empId, siteCode), FOREIGN KEY(empId) REFERENCES Administrator(empId), FOREIGN KEY(siteCode) REFERENCES Site(siteCode));

CREATE TABLE Specializes(empId integer, modelNo char(10), PRIMARY KEY(empId, modelNo), FOREIGN KEY(empId) REFERENCES TechnicalSupport(empId), FOREIGN KEY(modelNo) REFERENCES Model(modelNo));

CREATE TABLE Purchases(clientId integer, empId integer, packageId integer,
commissionRate numeric (4,2), PRIMARY KEY(clientId, empId, packageId), FOREIGN KEY(clientId) REFERENCES Client(clientId), FOREIGN KEY(empId) REFERENCES Salesman(empId), FOREIGN KEY(packageId) REFERENCES AirtimePackage(packageId));

CREATE TABLE Locates (serialNo char(10), siteCode integer, PRIMARY KEY(serialNo, siteCode), FOREIGN KEY(serialNo) REFERENCES DigitalDisplay(serialNo), FOREIGN KEY(siteCode) REFERENCES Site(siteCode));