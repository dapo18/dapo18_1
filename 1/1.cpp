#include <iostream>
#include <vector>
using namespace std;
struct Node{string v;Node*l,*r;Node(string x):v(x),l(0),r(0){}};

Node* buildTree(vector<string>& vals){
    if(vals.empty()) return 0;
    vector<Node*> nodes;
    for(auto &x: vals) nodes.push_back(new Node(x));
    int i=0;
    for(int j=1;j<vals.size();j+=2){
        if(j<vals.size()) nodes[i]->l=nodes[j];
        if(j+1<vals.size()) nodes[i]->r=nodes[j+1];
        i++;
    }
    return nodes[0];
}

void pre(Node*n){if(!n)return;cout<<n->v<<" ";pre(n->l);pre(n->r);}
void in(Node*n){if(!n)return;in(n->l);cout<<n->v<<" ";in(n->r);}
void post(Node*n){if(!n)return;post(n->l);post(n->r);cout<<n->v<<" ";}

int main(){
    vector<string> v; string x;
    cout<<"Введите узлы через пробел: ";
    while(cin>>x) v.push_back(x);
    Node* r = buildTree(v);
    cout<<"Preorder: ";pre(r);
    cout<<"\nInorder: ";in(r);
    cout<<"\nPostorder: ";post(r);
}
