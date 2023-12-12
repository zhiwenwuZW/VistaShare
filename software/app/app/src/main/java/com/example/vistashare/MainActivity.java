package com.example.vistashare;

import android.Manifest;
import android.content.pm.PackageManager;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.os.Environment;
import android.widget.MediaController;
import android.widget.Toast;
import android.widget.VideoView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import java.io.File;

public class MainActivity extends AppCompatActivity  {

    private VideoView videoView;

    @Override
    //对界面的按钮和显示位置实例化，并检查权限
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        videoView = (VideoView)findViewById(R.id.vdvwFilm);
        videoView.setMediaController(new MediaController(this));




        if(ContextCompat.checkSelfPermission(MainActivity.this, Manifest.permission.READ_MEDIA_VIDEO) != PackageManager.PERMISSION_GRANTED){
            ActivityCompat.requestPermissions(MainActivity.this, new String[]{Manifest.permission.READ_MEDIA_VIDEO}, 1);
        }else {
            initVideoPath();//初始化MediaPlayer
        }
    }


    //用一个单独的方法来实现视频播放初始化
    private void initVideoPath() {
        //本地的视频，需要在手机内存根目录添加一个名为 big_buck_bunny.mp4 的视频
        File file = new File(Environment.getExternalStorageDirectory(),"big_buck_bunny.mp4");//指定视频文件路径
        videoView.setVideoPath(file.getPath());//加载path文件代表的视频
        videoView.setOnPreparedListener(new MediaPlayer.OnPreparedListener() {
            @Override
            public void onPrepared(MediaPlayer mp) {
                mp.setLooping(true);//让视频循环播放
            }
        });
    }

    @Override
    //对权限的取得结果进行判断，并针对性操作。获得权限，执行初始化；如果没有获得权限，提示用户。
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        switch (requestCode) {
            case 1:
                if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                    initVideoPath();
                } else {
                    Toast.makeText(this, "拒绝权限，无法使用程序。", Toast.LENGTH_LONG).show();
                    finish();
                }
                break;
            default:
                break;
        }
    }



    @Override
    //执行完毕，释放所有资源
    protected void onDestroy() {
        super.onDestroy();
        if(videoView != null){
            videoView.suspend();
        }
    }
}
