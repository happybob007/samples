//  Copyright 2013 Smartsheet, Inc.

//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at

//       http://www.apache.org/licenses/LICENSE-2.0

//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Net;
using System.Web.Script.Serialization;

namespace SmartsheetAttachment
{
    class SmartsheetAttachment
    {
        static void Main(string[] args)
        {
            try
            {
                //Run the MakeRequest method to create a new sheet
                string newSheetName = "Smartsheet Attachment Test";
                string newSheetData = "{\"name\":\"" + newSheetName + "\",\"columns\":[{\"title\":\"Attachment Name\",\"primary\":true, \"type\":\"TEXT_NUMBER\"}]}]}";
                SmartsheetRequest createNewSheet = new SmartsheetRequest { callURL = "/sheets", method = "POST", contentType = "application/json" };
                var createSheetResponse = createNewSheet.MakeRequest(newSheetData);

                //Extract the sheet ID from the JSON response to use in future calls
                string sheetId = createSheetResponse["result"]["id"].ToString();
                Console.Write("Sheet Created with ID: " + sheetId + "\n");

                //Extract the column ID from the JSON response to use in future calls
                long primaryColumnId = createSheetResponse["result"]["columns"][0]["id"];

                //Save the path to each file to a string array
                //Replace the sample paths with your own
                string[] paths = new string[] { @"C:\MyAttachment.jpg", @"C:\MyAttachment2.jpg" };

                //Create an array where you will store the attachment Ids from Smartsheet.
                //The size of the array is equal to the size of the paths array.
                string[] fileAttachmentIds = new string[paths.Length];

                //Post each attachment in the array to a new row in the sheet using the insertRow object
                SmartsheetRequest insertRow = new SmartsheetRequest { callURL = "/sheet/" + sheetId + "/rows", method = "POST", contentType = "application/json" };

                for (int x = 0; x < paths.Length; x++)
                {
                    //FileInfo class defines properties of the file such as name, size, etc
                    FileInfo file = new FileInfo(paths[x]);

                    //Run the MakePostRequest method to insert a new row with values into the sheet
                    string addRow = "{\"toTop\":true, \"rows\": [{ \"cells\": [{\"columnId\":" + primaryColumnId + ", \"value\":\"" + file.Name + "\"}]}]}";
                    var jsonRowIds = insertRow.MakeRequest(addRow);

                    //Capture the Row Id to a string to use in your next call
                    string rowId = jsonRowIds["result"][0]["id"].ToString();

                    //Pass the rowId to the CallURL when posting the attachment
                    //In the callURL below, replace /row/ with /sheet/, and rowId with sheetId to post a sheet-level attachment
                    SmartsheetRequest uploadFile = new SmartsheetRequest { callURL = "/row/" + rowId + "/attachments", contentType = "application/jpg" };
                    var jsonUploadResponse = uploadFile.PostAttachment(paths[x], file);

                    //Save the attachment Id to a string in your array
                    fileAttachmentIds[x] = jsonUploadResponse["result"]["id"].ToString();
                    Console.Write(jsonUploadResponse["message"] + "; Attachment was uploaded with ID " + fileAttachmentIds[x] + "\n");
                }

                //Create a new row, Upload a URL as an attachment to the row
                string URLname = "Cupcake Heaven";
                string newRowForURL = "{\"toTop\":true, \"rows\": [{ \"cells\": [{\"columnId\":" + primaryColumnId + ", \"value\":\"" + URLname + "\"}]}]}";
                var newRowForURLReponse = insertRow.MakeRequest(newRowForURL);

                string urlRowId = newRowForURLReponse["result"][0]["id"].ToString();
                string urlInfo = "{\"name\":\"" + URLname + "\", \"description\":\"A great distraction from coding\", \"attachmentType\":\"LINK\", \"url\":\"http://pinterest.com/julilj/pictures-of-cupcakes\"}";
                SmartsheetRequest uploadURL = new SmartsheetRequest { callURL = "/row/" + urlRowId + "/attachments/", method = "POST", contentType = "" };
                var urlUploadResponse = uploadURL.MakeRequest(urlInfo);
                string URLattachmentId = urlUploadResponse["result"]["id"].ToString();
                Console.Write(urlUploadResponse["message"] + "; URL Attachment was uploaded with ID " + URLattachmentId + "\n");

                //Gets attachment info for all file attachments, including temporary download URL, and downloads the file to your computer
                for (int x = 0; x < fileAttachmentIds.Length; x++)
                {
                    SmartsheetRequest getAttachment = new SmartsheetRequest { callURL = "/attachment/" + fileAttachmentIds[x], method = "GET" };
                    var jsonGetAttachment = getAttachment.MakeRequest("null");

                    //Runs the downloadAttachment method which saves the file to your computer's temporary file
                    SmartsheetRequest downloadAttachment = new SmartsheetRequest { };
                    downloadAttachment.DownloadAttachment(jsonGetAttachment["url"], jsonGetAttachment["sizeInKb"], jsonGetAttachment["name"]);
                    Console.Write(jsonGetAttachment["name"] + " was successfully downloaded to your computer\n");
                }

                //Deletes an attachment from Smartsheet
                //Set idToDelete equal to an index from your fileAttachmentIds array, or URLattachmentId
                string idToDelete = fileAttachmentIds[0];
                SmartsheetRequest deleteAttachment = new SmartsheetRequest { callURL = "/attachment/" + idToDelete, method = "DELETE" };
                var jsonDeleteResponse = deleteAttachment.MakeRequest("null");

                Console.Write(jsonDeleteResponse["message"] + "; Attachment " + idToDelete + " was deleted from Sheet " + sheetId + "\n");
                Console.Write("Program Complete.");
                Console.Read();
            }
            catch (WebException e)
            {
                Console.Write(e.Message);
                Console.Read();
            }
        }
    }

    class SmartsheetRequest
    {
        public string method { get; set; }
        public string callURL { get; set; }
        public string contentType { get; set; }

        JavaScriptSerializer js = new JavaScriptSerializer();

        //Replace the text with your Smartsheet API token, generated in-app
        string token = "insert token here";
        string baseURL = "https://api.smartsheet.com/1.1";

        public dynamic MakeRequest(string json)
        {
            WebRequest request = WebRequest.Create(baseURL + callURL);
            request.ContentType = contentType;
            request.Method = method;
            request.Headers.Add("Authorization: Bearer " + token);

            if (json != "null")
            {
                using (var streamWriter = new StreamWriter(request.GetRequestStream()))
                {
                    streamWriter.Write(json);
                }
            }
            Stream responseStream = request.GetResponse().GetResponseStream();
            StreamReader readStream = new StreamReader(responseStream);
            var jsonResponse = js.Deserialize<dynamic>(readStream.ReadToEnd());

            return jsonResponse;
        }

        public dynamic PostAttachment(string path, FileInfo file)
        {
            //File is read to a byte array, which stores binary data, and can represent a number of different file types
            byte[] data = File.ReadAllBytes(path);

            WebRequest postRequest = WebRequest.Create(baseURL + callURL);
            postRequest.ContentType = contentType;
            postRequest.Method = "POST";
            postRequest.ContentLength = file.Length;
            //Timeout property is set to infinite, to accomodate larger files
            postRequest.Timeout = System.Threading.Timeout.Infinite;
            postRequest.Headers.Add("Authorization: Bearer " + token);
            postRequest.Headers.Add("Content-Disposition: attachment; filename=\"" + file.Name + "\"");

            //Write the binary file starting at position 0 to the Request Stream to send it to Smartsheet
            Stream stream = postRequest.GetRequestStream();
            stream.Write(data, 0, data.Length);
            stream.Close();

            Stream responseStream = postRequest.GetResponse().GetResponseStream();
            StreamReader readStream = new StreamReader(responseStream);
            var jsonResponse = js.Deserialize<dynamic>(readStream.ReadToEnd());
            return jsonResponse;
        }

        public void DownloadAttachment(string attachURL, int size, string name)
        {
            string attachName = new FileInfo(name).Name;
            WebRequest getAttachRequest = WebRequest.Create(attachURL);
            getAttachRequest.Method = WebRequestMethods.File.DownloadFile;

            //Open the Response stream containing the file, write it to a byte array
            Stream responseStream = getAttachRequest.GetResponse().GetResponseStream();

            byte[] data = new byte[size];

            FileStream fs = new FileStream(attachName, FileMode.Create);
            int readCount = responseStream.Read(data, 0, data.Length);
            while (readCount > 0)
            {
                fs.Write(data, 0, readCount);
                readCount = responseStream.Read(data, 0, data.Length);
            }

            fs.Close();
            responseStream.Close();
        }
    }
}