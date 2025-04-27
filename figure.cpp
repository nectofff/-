#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

using namespace std;
const double pi = 3.14159265;

class Figure {
public:
    virtual void read() = 0;
    virtual double area() = 0;
    virtual double perimeter() = 0;
    virtual string get_type() = 0;
    virtual void draw() = 0;
};

class Rectangle : public Figure{
private:
    int w;              
    int h;
    string type = "Rectangle";              
public:
    Rectangle(int w = 0, int h = 0) : w(w), h(h){}
 
    int get_width(){return w;}       
    int get_height(){return h;}    
 
    double area(){return h * w;}
    double perimeter(){return (h + w) * 2.0;} 
 
    void read(){cin >> w >> h;}
    void print();

    string get_type(){return type;}

    void draw(){
        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; i++){
                cout << "#";
            }
            cout << endl;
        }
    }

};

class Circle : public Figure{
private:
    int r;   
    string type = "Circle";           
public:
    Circle(int r = 0) : r(r){}
    int get_radius(){return r;}  

    double area(){return (r * r) * pi;}       
    double perimeter(){return (2 * pi) * r;}  
    
    void read(){cin >> r;}
    void print();

    string get_type(){return type;}

    void draw(){
        vector<vector<char>> arr((2 * r + 1) * (2 * r + 1));

        for(int y = 0; y < 2 * r + 1; y++){
            for(int x = 0; x <  2 * r + 1; x++){
                if(((x - r)*(x - r)) + ((y - r)*(y - r)) <= r * 2){arr[y][x] = '#';}
                else{arr[y][x] = '.';}
            }
        }
        for(int y = 0; y < 2 * r + 1; y++){
            for(int x = 0; x <  2 * r + 1; x++){
                cout << arr[y][x];
            }
            cout << endl;
        }
    }

};

class Triangle : public Figure{
private:
    int a, b, c;   
    string type = "Triangle";                
public:
    Triangle(int a = 0, int b = 0, int c = 0) : a(a), b(b), c(c){}
    int get_a(){return a;}                      
    int get_b(){return b;}                      
    int get_c(){return c;}                      
    
    double area(){
        double p = (a + b + c) / 2.0;
        double s = sqrt(p * (p - a) * (p - b) * (p - c));
        return s;
    }               
    double perimeter(){return a + b + c;}          
 
    void read(){cin >> a >> b >> c;}
    void print();

    string get_type(){return type;}

};

class Trapezoid : Figure{
private:
    int a, b;                       
    int c, d;                    
    int h;   
    string type = "Trapezoid";                    
 
public:
    Trapezoid(int a = 0, int b = 0, int c = 0, int d = 0, int h = 0) : a(a), b(b), c(c), d(d), h(h){}
    int get_a(){return a;}               
    int get_b(){return b;}                  
    int get_c(){return c;}               
    int get_d(){return d;}               
    int get_height(){return h;}  
    string get_type(){return type;}             
    
    double area(){return ((a + b) / 2.0) * h;}              
    double perimeter(){return a + b + c + d;}        
 
    void read(){cin >> a >> b >> c >> d >> h;}
    void print();
};


double array_area(vector<Figure*> array){
    double summ;
    for(int i = 0; i < array.size(); i++){
        summ += array[i]->area();
    }
    return summ;
}
double array_perimeter(vector<Figure*> array){
    double summ;
    for(int i = 0; i < array.size(); i++){
        summ += array[i]->perimeter();
    }
    return summ;
}


int count_rectangles(vector<Figure*> array){
    int count = 0;

    for(int i = 0; i < array.size(); i++){
        if(array[i]->get_type() == "Rectangle"){count++;}
    }
    return count;
}
int count_circles(vector<Figure*> array){
    int count = 0;
    
    for(int i = 0; i < array.size(); i++){
        if(array[i]->get_type() == "Circle"){count++;}
    }
    return count;
}
int count_triangles(vector<Figure*> array){
    int count = 0;
    
    for(int i = 0; i < array.size(); i++){
        if(array[i]->get_type() == "Triangle"){count++;}
    }
    return count;
}

int main() {
  Figure* f;
  string type;
  cin >> type;
  if (type == "Rectangle") {
    Rectangle* r = new Rectangle;
    r->read();
    f = r;
  } else {
    Circle* c = new Circle;
    c->read();
    f = c;
  }
  f->draw();
  return 0;  
}
