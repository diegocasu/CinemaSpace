package cinemaspace.model;


import javax.xml.*;
import javax.xml.parsers.*;
import org.w3c.dom.*;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

import org.xml.sax.*;
import javax.xml.validation.*;
import javax.xml.transform.dom.*;


public class LocalConfigurationParameters {
    private static final String XMLConfigurationFilePath = "./configuration.xml";
    private static final String XSDConfigurationFilePath = "./configuration.xsd";
    
    public static String connectionString = "";
    
    private static Document validateXMLConfiguration(){
        Document configurationDocument;
        
        try{
           DocumentBuilder documentBuilder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
           SchemaFactory schemaFactory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
           
           configurationDocument = documentBuilder.parse(new File(XMLConfigurationFilePath));
           Schema validationSchema = schemaFactory.newSchema(new File(XSDConfigurationFilePath));
           
           validationSchema.newValidator().validate(new DOMSource(configurationDocument));
           
        } catch(Exception exception) {
           if ( exception instanceof SAXException)
                System.out.println("Validation error: " + exception.getMessage());
           else
                System.out.println(exception.getMessage());
           configurationDocument = null;
        }
        
        return configurationDocument;
    }
    
    
    public static boolean retrieveLocalConfiguration() {
    	Document configurationDocument = validateXMLConfiguration();
    	
        if (configurationDocument == null)
            return false;
        
        String addressDBMS = configurationDocument.getElementsByTagName("addressDBMS").item(0).getTextContent();
        String portDBMS = configurationDocument.getElementsByTagName("portDBMS").item(0).getTextContent();
        
        connectionString += addressDBMS + ":" + portDBMS;
     
        return true;
    }
    
}
