from sier2 import Block
import param

class ExampleConfig(Block):
    """A block that provides an example config.

    Make sure that --config is used so the default config isnot overwritten.
    """

    in_arg = param.String(label='config arg', doc='An input to the config example')
    out_config = param.String(label='new config', doc='The contents of an ini file')

    def execute(self):
        ini = f'''
[block.sier2_blocks_config.blocks.DisplayExample]
arg = {self.in_arg}
'''
        self.out_config = ini
