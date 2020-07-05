'''
Main entry point
'''

import ui

if __name__ == '__main__':
    if ui.args.args['gui']:
        ui.gui.run()
    else:
        ui.console.run(ui.args)
