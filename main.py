# GlobalDict
# Just a basic calculator, nothing interesting here !

from Range import *

class Calculator(types.KX_PythonComponent):
    args = {}
    
    def awake(self, args):
        self.obj = self.object.scene.objects
        self.input = self.obj["input"]
        self.output = self.obj["output"]
        self.input.text = ""; self.output.text = ""
        
        # A list of excluded objects
        self.ommited = [self.obj["Camera"], self.obj["screen"],self.obj["clear"], self.obj["="]]
        self.l = logic.mouse.inputs[events.LEFTMOUSE] # Left click
        
    def start(self, args):
        pass
    
    def update(self):
        p = logic.mouse.position # Get mouse cursor position on the screen
        o = self.object.getScreenRay(p[0], p[1], 10) # Get the button pointed by the cursor
        
        if len(self.input.text) > 13:
            self.input.text = self.input.text[:-1] # Delete the last character if the length exceeds 13
            self.output.color = (1,0,0,1) # Set the output text's color to red
            self.output.text = "Field full !" # Print
            
        if len(self.output.text) >= 13: # Delete all characters from index 13 onwards if the length exceeds 13
            self.output.text = self.output.text[:13]
            
        if o is not None:
            if o not in self.ommited: # Target buttons not in our ommited list
                if self.l.activated:
                    self.input.text = str(self.input.text + str(o.name)) # Add button name to the input
                    
            if o == self.ommited[2]:
                if self.l.activated:
                    self.input.text = self.input.text[:-1] # Delete the last character from the input if clear is pressed
                    self.output.text = "" # Clear the output text
                    
            if o == self.ommited[3]:
                if self.l.activated:
                    try: 
                        self.output.color = (0,1,0,1) # Change output color to blue
                        self.output.text = "= " + str(eval(self.input.text)) # Return an evaluation of the input
                        
                    except:
                        self.output.color = (1,0,0,1) # Change output text color to red
                        self.output.text = "Math error !" # Print math error if calculations are invalid e.g Zero division
        