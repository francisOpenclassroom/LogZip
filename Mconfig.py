class ModuleConfig:
    """ Module de configuration """
    def __init__(self,path_in,path_out,execution,taille):
        self.path_in = path_in
        self.path_out = path_out
        self.config = execution
        self.size = taille

    def ConfigIni(self):


c1 = ModuleConfig("a","b","c",3)

