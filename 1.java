import java.util.*;
class N{String v;N l,r;N(String x){v=x;}}
public class Main{
 static N build(List<String> v){
  if(v.isEmpty())return null;
  List<N> n=new ArrayList<>();
  for(String s:v)n.add(new N(s));
  int i=0;
  for(int j=1;j<v.size();j+=2){
    if(j<v.size())n.get(i).l=n.get(j);
    if(j+1<v.size())n.get(i).r=n.get(j+1);
    i++;
  }
  return n.get(0);
 }
 static void pre(N n){if(n==null)return;System.out.print(n.v+" ");pre(n.l);pre(n.r);}
 static void in(N n){if(n==null)return;in(n.l);System.out.print(n.v+" ");in(n.r);}
 static void post(N n){if(n==null)return;post(n.l);post(n.r);System.out.print(n.v+" ");}
 public static void main(String[]a){
  Scanner sc=new Scanner(System.in);
  System.out.print("Введите узлы через пробел: ");
  List<String> vals=new ArrayList<>();
  while(sc.hasNext()) vals.add(sc.next());
  N r=build(vals);
  System.out.print("Preorder: ");pre(r);
  System.out.print("\nInorder: ");in(r);
  System.out.print("\nPostorder: ");post(r);
 }
}
