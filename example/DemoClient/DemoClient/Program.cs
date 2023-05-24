using NetMQ;
using NetMQ.Sockets;

namespace DemoClient
{
    internal class Program
    {
        static void Main(string[] args)
        {
            using (var client = new RequestSocket())
            {
                client.Connect("tcp://127.0.0.1:5555");

                while (true)
                {
                    string input = Console.ReadLine();
                    if (input == "exit")
                        break;

                    client.SendFrame(input);

                    var msg = client.ReceiveFrameString();
                    Console.WriteLine($"From Server: {msg}");
                }
            }
        }
    }
}