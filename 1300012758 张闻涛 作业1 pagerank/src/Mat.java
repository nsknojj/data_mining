import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

/**
 * Created by IBM on 2015/10/13.
 */
public class Mat {

    static final int MAXN=1000;
    static String[] pagename=new String[MAXN];
    static HashMap<String,Integer> map=new HashMap<>();
    static int ct=0;
    static double[][] mat=new double[MAXN][MAXN];
    static double[][] m=new double[MAXN][MAXN];
    static double[][] x=new double[2][MAXN],y=new double[2][MAXN];
    // matrix multiplication
    static void mul(double[][] a,double[][] b,double[][] c,int n,int m,int l) {
        for (int i=1;i<=n;i++)
            for (int j=1;j<=l;j++)
                c[i][j]=0;
        for (int k=1;k<=m;k++)
            for (int i=1;i<=n;i++)
                for (int j=1;j<=l;j++)
                    c[i][j]+=a[i][k]*b[k][j];
    }

    static void output() {
        for (int i=0;i<map.size();i++) {
            for (int j = 0; j < map.size(); j++)
                System.out.printf("%d ", mat[i][j]);
            System.out.println();
        }
    }
    // add a node of web page
    static void addNode(String name) {
        map.put(name,++ct);
        pagename[ct]=name;
        //System.out.println(name);
    }

    static void reset() {
        for (int i=0;i<MAXN;i++)
            for (int j=0;j<MAXN;j++)
                mat[i][j]=0.0;
    }
    // add two pages' relationship
    static void addEdge(String from,String to,double coe) {
        from=from.toLowerCase().trim();
        to=to.toLowerCase().trim();
        if (!from.equals(to)) {
            if (map.containsKey(to)) {
                mat[map.get(from)][map.get(to)]+=coe;
                //System.out.println(from + " " + to);
            }
            else {
                //System.out.println(to);
                //map.put(to,++ct);
            }
        }
    }

    static void quickSort(int[] numbers, int start, int end) {
        if (start < end) {
            double base = x[1][numbers[start]]; // 选定的基准值（第一个数值作为基准值）
            int temp; // 记录临时中间值
            int i = start, j = end;
            do {
                while ((x[1][numbers[i]] < base) && (i < end))
                    i++;
                while ((x[1][numbers[j]] > base) && (j > start))
                    j--;
                if (i <= j) {
                    temp = numbers[i];
                    numbers[i] = numbers[j];
                    numbers[j] = temp;
                    i++;
                    j--;
                }
            } while (i <= j);
            if (start < j)
                quickSort(numbers, start, j);
            if (end > i)
                quickSort(numbers, i, end);
        }
    }

    static void calc() {
        //output();
        int n=map.size();
        double p=0.95,delta=(1.0-p)/n;
        double sum=0;

        // calc the matrix of iteration
        for (int i=1;i<=n;i++) {
            sum=0;
            x[1][i]=1.0/(double)(n);
            for (int j=1;j<=n;j++)
                sum+=mat[i][j];
            for (int j=1;j<=n;j++)
                if (sum>0.001) m[i][j]=(double)mat[i][j]/(double)sum;
                else m[i][j]=0.0;
        }
        // iterate, calc PageRank
        //System.out.println(n);
        while (true) {
            mul(x,m,y,1,n,n);
            boolean flag=false;
            for (int i=1;i<=n;i++) {
                y[1][i] = y[1][i] * p + delta;
                if (Math.abs(y[1][i]-x[1][i])>0.001) flag=true;
            }
            if (!flag) break;
            for (int i=1;i<=n;i++) x[1][i]=y[1][i];
        }
        // sort and output
        int[] no=new int[MAXN];
        for (int i=1;i<=n;i++) no[i]=i;
        quickSort(no,1,n);
//        TreeMap<Double,Integer> sm=new TreeMap<>();
//        for (int i=1;i<=n;i++) sm.put(x[1][i],i);
//        System.out.println(sm.size());
        for (int i=n;i>=1;i--) {
            System.out.printf("%s",pagename[no[i]]);
            for (int j=30-pagename[no[i]].length();j>0;j--)System.out.printf(" ");
            System.out.printf("%.8f\n",x[1][no[i]]);
        }
    }

}
