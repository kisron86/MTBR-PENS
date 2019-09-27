#include <ros/ros.h>
#include "opencv2/core/core.hpp"
#include "opencv2/calib3d/calib3d.hpp"
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
//#include <opencv2/contrib/contrib.hpp>
#include <stdio.h>

using namespace cv;
using namespace std;

int main(int argc, char **argv)
{
  ros::init(argc, argv, "calibration");
  ros::NodeHandle nh;

}
