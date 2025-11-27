const fs = require('fs');
const path = require('path');
const { parse } = require('xml2js');
const { parseString } = require('xml2js');
const { promisify } = require('util');

const xml2js = promisify(parse);
const xml2jsAsync = promisify(xml2js.parse);

const parser = new xml2js.Parser({ explicitArray: true, explicitObject: true });

const parserAsync = async (xmlString) => {
  const parser = new xml2js.Parser({ explicitArray: true, explicitObject: true });
  const result = await parser.parseString(xmlString);
  return result;
};

const readXmlFile = async (filePath) => {
  const fileBuffer = await fs.promises.readFile(filePath);
  const xmlString = Buffer.from(fileBuffer);
  return xml2js.parseString(xmlString);
};

const parseXmlString = async (xmlString) => {
  const result = await parserAsync(xmlString);
  return result;
};

const parseXmlFile = async (filePath) => {
  const xmlString = await readXmlFile(filePath);
  return parseXmlString(xmlString);
};