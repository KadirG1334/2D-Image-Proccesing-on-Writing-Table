from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line #drawing line
import time
import matplotlib.pyplot as plt




X2_noktaları = []
Y2_noktaları=  []


Slopex = []
Slopey = []
SLOPE =  []

class DrawInput(Widget):
    

    
    def on_touch_down(self, touch):
        
        """BAŞLANGIÇ POZİSYONU"""
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))
           
        
    def on_touch_move(self, touch):
        
        X2_noktaları.append(int(touch.x))
        Y2_noktaları.append(int(touch.y))
      
        touch.ud["line"].points += (touch.x, touch.y)
		
            
        
    def on_touch_up(self, touch):
        print("RELEASED!",touch)
        
     
                  
       
        time.sleep(1)
        
        plt.xlim([0, 800])
        plt.ylim([0,600])
        length = len(X2_noktaları)
       
        
        
          
        def MarkerDefine():
            Tolerable = input("Enter fault distance: ")
            TolerableInt =int(Tolerable)
            for i in range(0,length-1):
                
                x1 = X2_noktaları[i]
                x2 = X2_noktaları[i+1]
                y1= Y2_noktaları[i]
                y2 = Y2_noktaları[i+1]
                
                if  x2-x1 ==0:
                   continue
                    
                    
                if x2-x1 !=0:
              
                    m = (y2-y1)/(x2-x1)
                    
                    SLOPE.append(m)     
                    
                    if SLOPE[i] != SLOPE[i-1] and (Y2_noktaları[i+1]+TolerableInt >= Y2_noktaları[i] or Y2_noktaları[i+1]-TolerableInt >= Y2_noktaları[i]) and (X2_noktaları[i+1]+TolerableInt >= X2_noktaları[i] or X2_noktaları[i+1]-TolerableInt >= X2_noktaları[i]):
                        Slopex.append(X2_noktaları[i])
                        Slopey.append(Y2_noktaları[i])
             
                
        
        MarkerDefine()
        
        
        plt.scatter(X2_noktaları[0],Y2_noktaları[0],marker='*',color='#cf0606',s=15)
        plt.scatter(Slopex,Slopey, marker='*',color='#cf0606',s=15)
        plt.plot(X2_noktaları,Y2_noktaları)
   
        plt.show()
        
        
        
    
 
        
class SimpleKivy4(App):
    
    def build(self):
        return DrawInput()

if __name__ == "__main__":
    SimpleKivy4().run()


    

        
        
        
        