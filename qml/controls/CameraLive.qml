import QtQuick 2.0
import QtMultimedia 5.15
Rectangle {
    id: cameraRectangle
    color: "#00000000"
    radius: 10
    border.width: 6

    Camera {
        id: camera

        imageProcessing.whiteBalanceMode: CameraImageProcessing.WhiteBalanceFlash

        exposure {
            exposureCompensation: -1.0
            exposureMode: Camera.ExposurePortrait
        }

        flash.mode: Camera.FlashRedEyeReduction

        imageCapture {
            onImageCaptured: {
                photoPreview.source = preview  // Show the preview in an Image
            }
        }
    }

    VideoOutput {
        anchors.verticalCenter: parent.verticalCenter
        anchors.top: parent.top
        source: camera
        anchors.horizontalCenter: parent.horizontalCenter
        focus : visible // to receive focus and capture key events when visible
    }

    Image {
        id: photoPreview
        anchors.verticalCenter: parent.verticalCenter
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
