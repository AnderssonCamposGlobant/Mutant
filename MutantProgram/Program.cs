using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Web;

namespace MutantProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bienvenido, soy Magneto! Necesito saber si eres un mutante.", Console.ForegroundColor);
            Console.WriteLine("A continuación debes ingresar 6 datos y cada uno de 6 digitos.", Console.ForegroundColor);

            string horizontal1 = ValidarSecuencia("Ingresa la primera secuencia de datos:");
            string horizontal2 = ValidarSecuencia("Ingresa la segunda secuencia de datos:");
            string horizontal3 = ValidarSecuencia("Ingresa la tercera secuencia de datos:");
            string horizontal4 = ValidarSecuencia("Ingresa la cuarta secuencia de datos:");
            string horizontal5 = ValidarSecuencia("Ingresa la quinta secuencia de datos:");
            string horizontal6 = ValidarSecuencia("Ingresa la sexta secuencia de datos:");

            bool mutante = EsMutante(horizontal1, horizontal2, horizontal3, horizontal4, horizontal5, horizontal6);
            Console.ReadLine();
        }

        private static string ValidarSecuencia(string textoSecuencia)
        {
            string resultado = string.Empty;
            Console.WriteLine(textoSecuencia, Console.ForegroundColor);
            Console.ForegroundColor = ConsoleColor.Green;
            string valor = Console.ReadLine();
            if (valor.Length != 6)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Debes ingresar una secuencia de datos de 6 caracteres. Ingresaste " + valor.Length + " caracteres. Inténtalo de nuevo.", Console.ForegroundColor);
                ValidarSecuencia(textoSecuencia);
            }

            resultado = valor;
            return resultado;
        }



        private static bool EsMutante(string horizontal1, string horizontal2, string horizontal3, string horizontal4, string horizontal5, string horizontal6)
        {
            bool mutante = false;
            Console.WriteLine("Conectando con servicio web AWS...", Console.ForegroundColor);

            var json = new Root();
            json.Dna = new List<string>();
            json.Dna.Add(horizontal1);
            json.Dna.Add(horizontal2);
            json.Dna.Add(horizontal3);
            json.Dna.Add(horizontal4);
            json.Dna.Add(horizontal5);
            json.Dna.Add(horizontal6);

            var mutantResponse = CallServiceAWS("https://f8fciea5if.execute-api.us-east-2.amazonaws.com/mutant", json);
            Object jsonBody = JObject.Parse(mutantResponse.Body);
            var mensaje = ((Newtonsoft.Json.Linq.JContainer)jsonBody).First;
            var mensajeAWS = ((Newtonsoft.Json.Linq.JValue)((Newtonsoft.Json.Linq.JContainer)mensaje).First).Value;
            Console.WriteLine("statusCode: " + mutantResponse.StatusCode + ", Respuesta: " + mensajeAWS, Console.ForegroundColor);

            Console.WriteLine("Conectando con servicio Dynamodb en AWS...", Console.ForegroundColor);
            var insertDynamodb = CallServiceAWS("https://m6ns7kukna.execute-api.us-east-2.amazonaws.com/dynamodb", json);
            Object jsonBodyDynamo = JObject.Parse(insertDynamodb.Body);
            var mensajeDynamo = ((Newtonsoft.Json.Linq.JContainer)jsonBodyDynamo).First;
            var mensajeAWSDynamo = ((Newtonsoft.Json.Linq.JValue)((Newtonsoft.Json.Linq.JContainer)mensajeDynamo).First).Value;
            Console.WriteLine("Respuesta Dynamodb" + mensajeAWSDynamo, Console.ForegroundColor);

            return mutantResponse.StatusCode==200 ? true : false;
        }

        public static RootResponse CallServiceAWS(string serviceUrl, object jsonRequest)
        {
            var serviceResponse = new RootResponse();
            Uri serviceUri = new Uri(serviceUrl);
            try
            {
                ServicePointManager.Expect100Continue = true;
                ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
                Uri myUri = new Uri(serviceUrl, UriKind.Absolute);
                HttpWebRequest httpWebRequest = (HttpWebRequest)HttpWebRequest.Create(myUri);
                httpWebRequest.ContentType = "application/json";
                httpWebRequest.Method = "POST";

                using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
                {
                    var bodyJson = JsonConvert.SerializeObject(jsonRequest);
                    streamWriter.Write(bodyJson);
                }

                var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
                using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
                {
                    var result = streamReader.ReadToEnd();
                    serviceResponse = JsonConvert.DeserializeObject<RootResponse>(result);
                }
            }
            catch (WebException ex)
            {
                var webResponse = ex.Response as System.Net.HttpWebResponse;
                if (webResponse != null)
                {
                    switch (webResponse.StatusCode)
                    {
                        case System.Net.HttpStatusCode.InternalServerError:
                            break;

                        case System.Net.HttpStatusCode.NotFound:
                            break;

                        case System.Net.HttpStatusCode.BadRequest:
                            break;

                        case System.Net.HttpStatusCode.Unauthorized:
                            break;

                        case System.Net.HttpStatusCode.MethodNotAllowed:
                            break;

                        default:
                            break;
                    }
                }
            }
            catch (Exception ex)
            {
                throw ex;
            }

            return serviceResponse;
        }


        public class Root
        {
            [JsonProperty("dna")]
            public List<string> Dna { get; set; }
        }

        public class Headers
        {
            [JsonProperty("Content-Type")]
            public string ContentType { get; set; }
        }

        public class RootResponse
        {
            [JsonProperty("headers")]
            public Headers Headers { get; set; }

            [JsonProperty("statusCode")]
            public int StatusCode { get; set; }

            [JsonProperty("body")]
            public string Body { get; set; }
        }

    }
}
