package utec.dbp.mychat;

import android.app.Activity;
import android.content.res.Resources;
import android.graphics.drawable.Drawable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.View;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.widget.ImageView;
import android.widget.LinearLayout;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.bumptech.glide.Glide;

import org.json.JSONException;
import org.json.JSONObject;

public class HomeActivity extends AppCompatActivity {

    public Activity getActivity() {
        return this;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        ImageView imageView = (ImageView) findViewById(R.id.imageView4);

        Resources res = getResources();
        Drawable drawable = res.getDrawable(R.drawable.image1);
        Drawable drawable2 = res.getDrawable(R.drawable.image2);
        Drawable drawable3 = res.getDrawable(R.drawable.image3);
        Glide.with(this).load("http://18.222.144.174:8080/static/F.gif").into(imageView);
/*
        WebView wb = (WebView) findViewById(R.id.webView1);

        wb.getSettings().setJavaScriptEnabled(true);
        wb.getSettings().setLoadWithOverviewMode(true);
        wb.getSettings().setUseWideViewPort(true);
        wb.setWebChromeClient(new WebChromeClient());
        wb.setLayerType(View.LAYER_TYPE_SOFTWARE, null);
        wb.loadUrl("http://13.58.202.142:8080/mobile_home");*/
    }
}

