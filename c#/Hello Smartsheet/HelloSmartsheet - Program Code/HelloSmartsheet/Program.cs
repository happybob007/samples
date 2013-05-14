//  Copyright 2013 Smartsheet.com

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

namespace ConsoleApplication3
{
    class Program
    {
        static void Main()
        {
            try
            {
                //Request Bearer Access Token
                Console.Write("\nEnter Smartsheet API access token\n");
                string token = Console.ReadLine();
                string baseURL = "https://api.smartsheet.com/1.1/sheet";

                //Create GET web request that will list available sheets
                WebRequest getRequest = WebRequest.Create(baseURL + "s");
                getRequest.ContentType = "application/json; charset=utf-8";
                getRequest.Method = "GET";
                getRequest.Headers.Add("Authorization: Bearer " + token);

                //Capture json web response using StreamReader
                Stream dataStream = getRequest.GetResponse().GetResponseStream();
                StreamReader objReader = new StreamReader(dataStream);

                //Deserialize data stream to dynamic object so we can work with the data
                JavaScriptSerializer js = new JavaScriptSerializer();
                var sheetList = js.Deserialize<dynamic>(objReader.ReadToEnd());
                Console.Write("\nFetching your list of sheets...\n");

                //If the dynamic object is empty, the user doesn't have any sheets 
                //They can either close the program or try again.
                if (sheetList.Length == 0)
                {
                    Console.Write("\nYou don't have any sheets.\nPress Esc to close or Enter to restart.");
                    Program.exitRestart();
                }

                //If the user has sheets, iterate through and display the first 5 available sheets
                else
                {
                    Console.WriteLine("\nTotal sheets: " + sheetList.Length + "\nShowing the first five sheets:\n");
                    for (int i=0; i<sheetList.Length&i<5;i++)
                    {
                        Console.Write((i + 1).ToString() + ": " + sheetList[i]["name"] + "\n");
                    }
                    Console.Write("\nEnter the number of the sheet you want to share:\n");
                }

                //Grab sheet ID based on user selection
                int id = int.Parse(Console.ReadLine()) - 1;

                //User inputs email address and access level of collaborator
                Console.Write("\nEnter an email address to share " + sheetList[id]["name"] + " to:\n");
                string email = Console.ReadLine();

                Console.Write("\nChoose an access level (ADMIN, EDITOR, EDITOR_SHARE or VIEWER) for " + email + "\n");
                string accessLevel = Console.ReadLine();

                Console.Write("\nSharing " + sheetList[id]["name"] + " to " + email + " as " + accessLevel + "...\n");

                //Create Collaborator object based on user input, convert to JSON string
                Collaborator collab = new Collaborator { email = email, accessLevel = accessLevel };
                string json = js.Serialize(collab);

                //Create POST webrequest that shares sheet
                WebRequest postRequest = WebRequest.Create(baseURL + "/" + sheetList[id]["id"].ToString() + "/shares?sendemail=false");
                postRequest.ContentType = "application/json; charset=utf-8";
                postRequest.Method = "POST";
                postRequest.Headers.Add("Authorization: Bearer " + token);

                using (var streamWriter = new StreamWriter(postRequest.GetRequestStream()))
                {
                    streamWriter.Write(json);
                }

                //Get response, display confirmation and share ID to user
                Stream responseStream = postRequest.GetResponse().GetResponseStream();
                StreamReader readStream = new StreamReader(responseStream);
                var jsonResponse = js.Deserialize<dynamic>(readStream.ReadToEnd());
                Console.Write("\nSheet shared successfully! Share ID " + jsonResponse["result"]["id"] + "\nPress Esc to close or Enter to restart\n");
                Program.exitRestart();
            }

            //Displays error message in console if request is not successful 
            catch (Exception e)
            {
                Console.Write("\n" + e.Message + "\n" + "Press Esc to close or Enter to resart\n");
                Program.exitRestart();
            }
        }

        //Method to exit or restart program
        static void exitRestart()
        {
            var key = Console.ReadKey();
            if (key.Key == ConsoleKey.Escape)
            {
                Environment.Exit(0);
            }
            else if (key.Key == ConsoleKey.Enter)
            {
                Console.Clear();
                Main();
            }
        }

        //Collaborator class sets an email address and access level for the person you're sharing with
        class Collaborator
        {
            public string email { get; set; }
            public string accessLevel { get; set; }
        }
    }
}