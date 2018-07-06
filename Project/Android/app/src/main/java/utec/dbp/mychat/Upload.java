package utec.dbp.mychat;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
/*
public static final String UPLOAD_URL = "http://animotradings.000webhostapp.com/upload.php";
public static final String UPLOAD_KEY = "image";

//Categories Spinner
        Spinner spinner;
        ArrayAdapter<CharSequence> adapter;

//Meet-up Spinner
        Spinner spinner2;
        ArrayAdapter<CharSequence> adapter2;

@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sell_activityy);

        //PhotoUpload
        buttonChoose = (Button) findViewById(R.id.buttonChoose);
        buttonUpload = (Button) findViewById(R.id.buttonUpload);

        imageView = (ImageView) findViewById(R.id.imageView);

        buttonChoose.setOnClickListener(this);
        buttonUpload.setOnClickListener(this);

        // Categories Spinner
        spinner = (Spinner)findViewById(sCategories);
        adapter = ArrayAdapter.createFromResource(this, R.array.category_types, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);
        spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
@Override
public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        Toast.makeText(getBaseContext(), parent.getItemAtPosition(position)+" selected", Toast.LENGTH_LONG).show();
        }

@Override
public void onNothingSelected(AdapterView<?> parent) {

        }
        });

        // Meet-up Spinner
        spinner2 = (Spinner)findViewById(smeetup);
        adapter2 = ArrayAdapter.createFromResource(this, R.array.meetup_location, android.R.layout.simple_spinner_item);
        adapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner2.setAdapter(adapter2);
        spinner2.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
@Override
public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        Toast.makeText(getBaseContext(), parent.getItemAtPosition(position)+" selected", Toast.LENGTH_LONG).show();
        }

@Override
public void onNothingSelected(AdapterView<?> parent) {
        }
        });

final EditText etItemName = (EditText) findViewById(R.id.etItemName);
final EditText etCondition = (EditText) findViewById(R.id.etCondition);
final EditText etDescription = (EditText) findViewById(R.id.etDescription);
final EditText etPrice = (EditText) findViewById(R.id.etPrice);
final EditText etContact = (EditText) findViewById(R.id.etContact);
final Spinner sCategories  = (Spinner) findViewById (R.id.sCategories);
final Spinner smeetup = (Spinner) findViewById (R.id.smeetup);
final Button bSubmit = (Button) findViewById(R.id.bSubmit);

        bSubmit.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View v) {
final String item_name = etItemName.getText().toString();
final String conditionn = etCondition.getText().toString();
final String description = etDescription.getText().toString();
final int price = Integer.parseInt(etPrice.getText().toString());
final double contact = Double.parseDouble(etContact.getText().toString());
final String categories = sCategories.getSelectedItem().toString();
final String meetup = smeetup.getSelectedItem().toString();


        // Data Upload...
        Response.Listener<String> responseListener= new Response.Listener<String>(){

@Override
public void onResponse(String response) {
        try {
        JSONObject jsonResponse = new JSONObject(response);
        boolean success = jsonResponse.getBoolean("success");

        if (success){
        Intent intent =  new Intent(SellActivityy.this, NavigationDrawer.class);
        SellActivityy.this.startActivity(intent);
        } else{
        AlertDialog.Builder builder = new AlertDialog.Builder(SellActivityy.this);
        builder.setMessage("Ad posting failed!")
        .setNegativeButton("Retry", null)
        .create()
        .show();
        }
        } catch (JSONException e) {
        e.printStackTrace();
        }
        }
        };

        SellRequest sellRequest = new SellRequest(item_name, conditionn, description, price, contact, categories, meetup, responseListener);
        RequestQueue queue = Volley.newRequestQueue(SellActivityy.this);
        queue.add(sellRequest);
        }
        });
        }

//PhotoUpload

private void showFileChooser() {
        Intent intent = new Intent();
        intent.setType("image/*");
        intent.setAction(Intent.ACTION_GET_CONTENT);
        startActivityForResult(Intent.createChooser(intent, "Select Picture"), PICK_IMAGE_REQUEST);
        }

private int PICK_IMAGE_REQUEST = 1;

private Button buttonChoose;
private Button buttonUpload;
private Button buttonView;

private ImageView imageView;

private Bitmap bitmap;

private Uri filePath;
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == PICK_IMAGE_REQUEST && resultCode == RESULT_OK && data != null && data.getData() != null) {

        filePath = data.getData();
        try {
        bitmap = MediaStore.Images.Media.getBitmap(getContentResolver(), filePath);
        imageView.setImageBitmap(bitmap);
        } catch (IOException e) {
        e.printStackTrace();
        }
        }
        }

public String getStringImage(Bitmap bmp){
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        bmp.compress(Bitmap.CompressFormat.JPEG, 100, baos);
        byte[] imageBytes = baos.toByteArray();
        String encodedImage = Base64.encodeToString(imageBytes, Base64.DEFAULT);
        return encodedImage;
        }
private void uploadImage(){
// Picture Upload...
class UploadImage extends AsyncTask<Bitmap,Void,String> {

    ProgressDialog loading;
    RequestHandler rh = new RequestHandler();

    @Override
    protected void onPreExecute() {
        super.onPreExecute();
        loading = ProgressDialog.show(SellActivityy.this, "Uploading...", null,true,true);
    }

    @Override
    protected void onPostExecute(String s) {
        super.onPostExecute(s);
        loading.dismiss();
        Toast.makeText(getApplicationContext(),s,Toast.LENGTH_LONG).show();
    }

    @Override
    protected String doInBackground(Bitmap... params) {
        Bitmap bitmap = params[0];
        String uploadImage = getStringImage(bitmap);

        HashMap<String,String> data = new HashMap<>();

        data.put(UPLOAD_KEY, uploadImage);
        String result = rh.sendPostRequest(UPLOAD_URL,data);

        return result;
    }
}

    UploadImage ui = new UploadImage();
    ui.execute(bitmap);

            }

@Override
public void onClick(View v) {
        if (v == buttonChoose) {
        showFileChooser();
        }

        if(v == buttonUpload){
        uploadImage();
        }



private void viewImage() {
        startActivity(new Intent(this, ImageListView.class)); }}

        */