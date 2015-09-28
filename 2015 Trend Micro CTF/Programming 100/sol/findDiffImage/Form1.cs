using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Net;
using System.Text.RegularExpressions;
namespace findDiffImage
{
    public partial class Form1 : Form
    {

        string hostUrl = "http://ctfquest.trendmicro.co.jp:43210";
        string url = "http://ctfquest.trendmicro.co.jp:43210/abd4275f273f68080361a8e9ec166e6c1befadd95bb9?x=323&y=251";
        public Form1()
        {
            InitializeComponent();
        }

        private Bitmap getImageByUrl(string url)
        {
            WebClient wc = new WebClient();
            byte[] bytes = wc.DownloadData(url);
            Bitmap b = new Bitmap(new MemoryStream(bytes));
            return b;
        }
        private string getNextImageUrl(string url)
        {
            WebClient wc = new WebClient();
            string html = wc.DownloadString(url);
            string pattern = @"/img/[a-zA-Z0-9]+.png";
            Regex regex = new Regex(pattern, RegexOptions.IgnoreCase);
            MatchCollection matches = regex.Matches(html);
            int index = 0;
            foreach (Match match in matches) // 一一取出 MatchCollection 內容
            {
                return "http://ctfquest.trendmicro.co.jp:43210" + match.Value;
            }

            return "";
        }
        private Point getDiffColorPoint(Bitmap image)
        {
            Color mycolor = Color.White;
            Color backgroundColor = image.GetPixel(1, 1);
            for (int x = 0; x < image.Width; x++)
            {
                for (int y = 0; y < image.Height; y++)
                {

                    if (image.GetPixel(x, y) != backgroundColor && mycolor == Color.White)
                    {
                        mycolor = image.GetPixel(x, y);
                    }
                    if (image.GetPixel(x, y) != backgroundColor && image.GetPixel(x, y) != mycolor)
                    {
                        return new Point(x, y );
                    }
                }
            }
            GC.Collect();
            return new Point(0, 0);
        }
        private void buttonNextImage_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate(url);
            string imageUrl = getNextImageUrl(url);
            if(imageUrl != ""){
                // getImage and find the diffpoint
                Point aim = getDiffColorPoint(getImageByUrl(imageUrl));

                // next url
                string[] filepath = imageUrl.Split('/');
                string filename = filepath[filepath.Length - 1].Replace(".png", "");
                url = string.Format("{0}?x={1}&y={2}", hostUrl + "/" + filename, aim.X, aim.Y);
                Console.WriteLine(url);
            }
            
        }
    }
}
