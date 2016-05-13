import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class PageRank {

    static String path="pkumirror";
    static String domainname=".pku.edu.cn";

    static void scanFile(File file,String fromPage,double coe) {
        // read file
        StringBuilder text=new StringBuilder();
        try {
            BufferedReader fin=new BufferedReader(new FileReader(file));
            String s;
            s=fin.readLine();
            while (s!=null) {
                text.append(s+"\n");
                s=fin.readLine();
            }
        } catch (Exception e) {
            return;
        }
        // find links
        String pattern="(http|https)://[^/>]*\\.pku\\.edu\\.cn";
        Pattern p=Pattern.compile(pattern,Pattern.CASE_INSENSITIVE);
        Matcher m=p.matcher(text);
        while (m.find()) {
            String s=m.group();
            Mat.addEdge(fromPage,s.substring(s.indexOf("//")+2),coe);
        }
    }

    static void listFiles(File dir,String fromPage,double coe){
        // dfs all html files
        if (!dir.isDirectory()) return;
        String[] files=dir.list();
        for (int i=0;i<files.length;i++) {
            File file=new File(dir,files[i]);
            if (file.isDirectory()) listFiles(file,fromPage,coe/files.length);
            if (file.isFile()) {
                if(files[i].contains(".html")||files[i].contains(".htm")){
                    scanFile(file,fromPage,coe);
                }
            }
        }
    }

    static void createMat(String path) {
        File dir=new File(path);
        if (!dir.isDirectory()) return;

        String[] files=dir.list();
        //System.out.println(files.length);
        for (int i=0;i<files.length;i++)
            Mat.addNode(files[i]);
        for (int i=0;i<files.length;i++) {
            File file=new File(dir,files[i]);
            if (file.isDirectory()) {
                listFiles(file,files[i],1);
            }
        }
    }

    public static void main(String[] args) {
        Mat.reset();
        createMat(path);
        Mat.calc();
    }

}
