'''
Main entry point
'''

from core.reaction import Reaction

from ui.tkinter.main import start_gui


if __name__ == '__main__':
    # start_gui()
    r = Reaction('Fe(OH)3 + H2SO4 = Fe2(SO4)3 + H2O', ['4in3','','','18g'])

    print(r)
    # if ui.args.args['gui']:
    #     ui.gui.run()
    # else:
    #     ui.console.run(ui.args)
    
