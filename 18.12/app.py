class Server:
    def __init__(self, hostname, ip, status, cpu, memory):
        self.hostname = hostname
        self.ip = ip
        self.status = status
        self.cpu = cpu
        self.memory = memory


class ServerMonitor:
    def __init__(self):
        self.servers = {}

    def add_server(self, server):
        self.servers[server.hostname] = server

    def get_critical_servers(self):
        return [
            s for s in self.servers.values()
            if s.status == "offline" or s.cpu > 90
        ]

    def generate_report(self):
        total = len(self.servers)

        online = sum(s.status == "online" for s in self.servers.values())
        offline = sum(s.status == "offline" for s in self.servers.values())
        degraded = sum(s.status == "degraded" for s in self.servers.values())

        report = (
            "Отчет о состоянии серверов\n"
            "=======================\n"
            f"Всего серверов: {total}\n"
            f"Online: {online} | Offline: {offline} | Degraded: {degraded}\n\n"
            "Проблемные серверы:\n"
        )

        critical = self.get_critical_servers()
        if not critical:
            report += "Нет проблемных серверов"
        else:
            for s in critical:
                if s.status == "offline":
                    report += f"- {s.hostname} ({s.ip}): Status: offline\n"
                else:
                    report += f"- {s.hostname} ({s.ip}): CPU {s.cpu}%\n"

        return report

m = ServerMonitor()
m.add_server(Server("web-prod-01", "192.168.1.10", "online", 95, 70))
m.add_server(Server("db-backup-02", "192.168.1.30", "offline", 0, 0))

print(m.generate_report())
