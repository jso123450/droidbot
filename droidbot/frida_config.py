class FridaConfig:

    def __init__(self):
        self.enabled = False
        self.scripts = []

    
    def enable(self, scripts):
        self.enabled = True
        self.scripts = scripts

    
    def get_start_command(self, device, pkg):
        cmd = f"frida --device {device} "
        for script in self.scripts:
            cmd += f"-l {script} "
        cmd += f"-f {pkg}"
        return cmd

    def get_start_command_prefix(self, device):
        return f"frida --device {device}"
        

FRIDA_CONFIG = FridaConfig()