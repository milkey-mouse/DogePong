import Zero
import Events
import Property
import VectorMath

Vec3 = VectorMath.Vector3

class EnemyAI:
    def DefineProperties(self):
        self.PaddleSpeed = Property.Float(0.15)
        pass

    def Initialize(self, initializer):
        self.Ball = self.Space.FindObjectByName("Ball")
        Zero.Connect(self.Space, Events.LogicUpdate, self.OnLogicUpdate)
        pass

    def OnLogicUpdate(self, UpdateEvent):
        if(not self.Ball):
            #print("No Ball")
            return
        
        #print("in Update")
        if(self.Ball.Transform.Translation.y < self.Owner.Transform.Translation.y - self.PaddleSpeed):
           #print("MOVE")
            self.Owner.Transform.Translation += Vec3(0, -self.PaddleSpeed, 0)
        
        if(self.Ball.Transform.Translation.y > self.Owner.Transform.Translation.y + self.PaddleSpeed):
            #print("MOVE")
            self.Owner.Transform.Translation += Vec3(0, self.PaddleSpeed, 0)
        
        

Zero.RegisterComponent("EnemyAI", EnemyAI)