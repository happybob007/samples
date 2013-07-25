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

namespace SheetStructure
{
    class SheetStructure
    {
        static void Main(string[] args)
        {
            //Create variables that will be passed as arguments to the MakePostRequest method
            string newSheetName = "Betty's Bake Sale";
            string newSheetData = "{\"name\":\"" + newSheetName + "\",\"columns\":[{\"title\":\"Baked Good\",\"primary\":true, \"type\":\"TEXT_NUMBER\"},{\"title\":\"Baker\",\"type\":\"CONTACT_LIST\"},{\"title\":\"Price Per Item\", \"type\":\"TEXT_NUMBER\"}, {\"title\":\"Gluten Free?\", \"type\":\"CHECKBOX\", \"symbol\":\"FLAG\"}, {\"title\":\"Status\", \"type\":\"PICKLIST\", \"options\":[\"Started\",\"Finished\",\"Delivered\"]}]}";

            //Run the MakePostRequest method to create a new sheet, store the sheet id from the json response to a string variable
            SmartsheetRequest createNewSheet = new SmartsheetRequest { callURL = "/sheets", method = "POST" };
            var createSheetResponse = createNewSheet.MakeRequest(newSheetData);

            //Extract the sheet ID from the JSON response to use in future calls
            string sheetId = createSheetResponse["result"]["id"].ToString();

            //Run the MakePostRequest method with different arguments to create a new column in the sheet
            string newColumn = "{\"title\":\"Delivery Date\", \"type\":\"DATE\", \"index\":5}";
            SmartsheetRequest addNewColumn = new SmartsheetRequest { callURL = "/sheet/" + sheetId + "/columns", method = "POST" };
            addNewColumn.MakeRequest(newColumn);

            //Run the MakeGetRequest method to get a list of column id's from the sheet; the json response is saved to a var
            SmartsheetRequest getColumnIds = new SmartsheetRequest { callURL = "/sheet/" + sheetId + "/columns", method = "GET" };
            var jsonColumnIds = getColumnIds.MakeRequest("null");

            //Run the MakePostRequest method to insert 6 new rows with values into the sheet
            string addSixRows = "{\"toTop\":true, \"rows\": [{ \"cells\": [{\"columnId\":" + jsonColumnIds[0]["id"] + ", \"value\":\"Brownies\"}, {\"columnId\":" + jsonColumnIds[1]["id"] + ",\"value\":\"julieanne@smartsheet.com\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[2]["id"] + ", \"value\": \"$1\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[3]["id"] + ",\"value\":true}, {\"columnId\":" + jsonColumnIds[4]["id"] + ",\"value\":\"Finished\"}, {\"columnId\":" + jsonColumnIds[5]["id"] + ",\"value\":\"None\", \"strict\":false}]}, {\"cells\":[{\"columnId\":" + jsonColumnIds[0]["id"] + ",\"value\": \"Snickerdoodles\"}, {\"columnId\":" + jsonColumnIds[1]["id"] + ", \"value\": \"stevenelson@smartsheet.com\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[2]["id"] + ",\"value\":\"$2\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[3]["id"] + ",\"value\": false}, {\"columnId\":" + jsonColumnIds[4]["id"] + ",\"value\": \"Delivered\"}, {\"columnId\":" + jsonColumnIds[5]["id"] + ",\"value\":\"2013-09-04\", \"strict\":false}]}, {\"cells\": [{\"columnId\":" + jsonColumnIds[0]["id"] + ",\"value\": \"Rice Krispy Treats\"}, {\"columnId\":" + jsonColumnIds[1]["id"] + ", \"value\": \"rickthames@smartsheet.com\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[2]["id"] + ",\"value\": \"$.50\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[3]["id"] + ",\"value\":false}, {\"columnId\":" + jsonColumnIds[4]["id"] + ", \"value\": \"Started\"}, {\"columnId\":" + jsonColumnIds[5]["id"] + ", \"value\":\"None\", \"strict\":false}]}, {\"cells\": [{\"columnId\":" + jsonColumnIds[0]["id"] + ", \"value\": \"Muffins\"}, {\"columnId\":" + jsonColumnIds[1]["id"] + ", \"value\": \"sandrasmart@smartsheet.com\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[2]["id"] + ",\"value\": \"$1.50\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[3]["id"] + ", \"value\": false}, {\"columnId\":" + jsonColumnIds[4]["id"] + ", \"value\": \"Finished\"}, {\"columnId\":" + jsonColumnIds[5]["id"] + ",\"value\": \"None\", \"strict\":false}]}, {\"cells\": [{\"columnId\":" + jsonColumnIds[0]["id"] + ",\"value\": \"Chocolate Chip Cookies\"}, {\"columnId\":" + jsonColumnIds[1]["id"] + ",\"value\": \"janedaniels@smartsheet.com\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[2]["id"] + ",\"value\": \"$1\", \"strict\": false}, {\"columnId\":" + jsonColumnIds[3]["id"] + ",\"value\":false}, {\"columnId\":" + jsonColumnIds[4]["id"] + ",\"value\":\"Delivered\"}, {\"columnId\":" + jsonColumnIds[5]["id"] + ",\"value\": \"2013-09-05\"}]}, {\"cells\": [{\"columnId\":" + jsonColumnIds[0]["id"] + ",\"value\": \"Ginger Snaps\"}, {\"columnId\":" + jsonColumnIds[1]["id"] + ",\"value\":\"nedbarnes@smartsheet.com\", \"strict\":false},{\"columnId\":" + jsonColumnIds[2]["id"] + ",\"value\":\"$0.50\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[3]["id"] + ",\"value\": true}, {\"columnId\":" + jsonColumnIds[4]["id"] + ",\"value\":\"Unknown\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[5]["id"] + ",\"value\":\"None\", \"strict\":false}]}]}";
            SmartsheetRequest addNewRows = new SmartsheetRequest { callURL = "/sheet/" + sheetId + "/rows", method = "POST" };
            var jsonRowIds = addNewRows.MakeRequest(addSixRows);

            //Move row 6 to the top to keep an eye on it
            SmartsheetRequest moveRowSix = new SmartsheetRequest { callURL = "/row/" + jsonRowIds["result"][5]["id"], method = "PUT" };
            moveRowSix.MakeRequest("{\"toTop\":true}");

            //Insert a row containing the value "Delivered" in the primary column 
            string parentRow = "{\"toBottom\":true, \"rows\": [{\"cells\": [{\"columnId\":" + jsonColumnIds[0]["id"] + ", \"value\": \"Delivered\"}]}]}";
            var insertParentResponse = addNewRows.MakeRequest(parentRow);
            string parentRowId = insertParentResponse["result"][0]["id"].ToString();

            //Find rows of baked good that have been have been "Delivered", and indent them underneath the new row
            for (int i = 0; i < 6; i++)
            {
                for (int x = 0; x < 6; x++)
                {
                    if (jsonRowIds["result"][i]["cells"][x]["columnId"] == jsonColumnIds[4]["id"] && jsonRowIds["result"][i]["cells"][x]["value"] == "Delivered")
                    {
                        SmartsheetRequest moveDeliveredRows = new SmartsheetRequest { callURL = "/row/" + jsonRowIds["result"][i]["id"], method = "PUT" };
                        moveDeliveredRows.MakeRequest("{\"parentId\":" + parentRowId + "}");
                    }
                }
            }

            //Add two new rows to the sheet, at the same level as the row of muffins
            string addScones = "{\"siblingId\":" + jsonRowIds["result"][3]["id"] + ", \"rows\": [{ \"cells\": [{\"columnId\":" + jsonColumnIds[0]["id"] + ", \"value\":\"Scones\"}, {\"columnId\":" + jsonColumnIds[1]["id"] + ",\"value\":\"thomaslively@smartsheet.com\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[2]["id"] + ", \"value\": \"$1.50\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[3]["id"] + ",\"value\":true}, {\"columnId\":" + jsonColumnIds[4]["id"] + ",\"value\":\"Finished\"}, {\"columnId\":" + jsonColumnIds[5]["id"] + ",\"value\":\"None\", \"strict\":false}]}]}]";
            addNewRows.MakeRequest(addScones);

            string addLemonBars = "{\"siblingId\":" + jsonRowIds["result"][3]["id"] + ", \"rows\": [{ \"cells\": [{\"columnId\":" + jsonColumnIds[0]["id"] + ", \"value\":\"Lemon Bars\"}, {\"columnId\":" + jsonColumnIds[1]["id"] + ",\"value\":\"rickthames@smartsheet.com\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[2]["id"] + ", \"value\": \"$1.00\", \"strict\":false}, {\"columnId\":" + jsonColumnIds[3]["id"] + ",\"value\":false}, {\"columnId\":" + jsonColumnIds[4]["id"] + ",\"value\":\"Started\"}, {\"columnId\":" + jsonColumnIds[5]["id"] + ",\"value\":\"None\", \"strict\":false}]}]}]";
            addNewRows.MakeRequest(addLemonBars);

            //Move 'Status' column next to the first column  (index 1) to keep an eye on it
            //Move 'Delivery Date' column next to 'Status' (index 2) for better visibility
            string statusColumn = "{\"title\":\"Status\",\"index\":1, \"sheetId\":" + sheetId + "}";
            string deliveryColumn = "{\"title\":\"Delivery Date\",\"index\":2, \"sheetId\":" + sheetId + "}";

            for (int i = 0; i < jsonColumnIds.Length; i++)
            {
                SmartsheetRequest moveStatusColumn = new SmartsheetRequest { callURL = "/column/" + jsonColumnIds[i]["id"], method = "PUT" };
                if (jsonColumnIds[i]["title"] == "Status")
                {
                    var moveResponse = moveStatusColumn.MakeRequest(statusColumn);
                }

                else if (jsonColumnIds[i]["title"] == "Delivery Date")
                {
                    var moveResponse = moveStatusColumn.MakeRequest(deliveryColumn);
                    //Display JSON response message to console, to confirm program has completed
                    Console.Write(moveResponse["message"]);
                }
            }

            Console.Read();
        }
    }

   //Class contains the Make Request method that is used to process all API requests
    class SmartsheetRequest
    {
        public string method { get; set; }
        public string callURL { get; set; }

        JavaScriptSerializer js = new JavaScriptSerializer();

        //Replace the text with your Smartsheet API token, generated in-app
        string token = "insert your token here";
        string baseURL = "https://api.smartsheet.com/1.1";

        public dynamic MakeRequest(string json)
        {
            WebRequest postRequest = WebRequest.Create(baseURL + callURL);
            postRequest.ContentType = "application/json; charset=utf-8";
            postRequest.Method = method;
            postRequest.Headers.Add("Authorization: Bearer " + token);

            if (json != "null")
            {

                using (var streamWriter = new StreamWriter(postRequest.GetRequestStream()))
                {
                    streamWriter.Write(json);
                }
            }
            Stream responseStream = postRequest.GetResponse().GetResponseStream();
            StreamReader readStream = new StreamReader(responseStream);
            var jsonResponse = js.Deserialize<dynamic>(readStream.ReadToEnd());

            return jsonResponse;
        }
    }
}
