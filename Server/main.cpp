#include "Engine.h"
#include <iostream>
#include "Reactor.h"

using namespace std;
using namespace ServWork;

class MyReactor : public Reactor
{
public:
	void OnReceive(const ClientSocket& socket, uint8 id, Buffer buf) override
	{
		buf >>= 16 * sizeof(char_t);
		buf.Set(0, socket.GetData().GetIp());

		for (const auto& client : GetServer().GetClients())
			client.Send(id, buf);
	}

	void OnAccept(const ClientSocket& socket) override
	{
		auto msg = Name{ STR("enter") }.Get();
		msg = socket.GetData().GetIp() + msg;
		Buffer buffer{ msg.length() };
		buffer = msg.c_str();

		for (const auto& client : GetServer().GetClients())
				client.Send(0, buffer);
	}

	void OnClose(const ClientSocket& socket) override
	{
		static auto msg = Name{ STR("exit") }.Get();
		msg = socket.GetData().GetIp() + msg;
		Buffer buffer{ msg.length() };
		buffer = msg.c_str();

		for (const auto& client : GetServer().GetClients())
			client.Send(0, buffer);
	}

	void OnLimitError(const char_t* ip) override
	{
		cout << Name{ STR("room_full") }.Get() << ip << endl;
	}
};

int main()
{
	return ServWork::Engine<MyReactor>{}.Run();
}