import QtQuick 2.15
import QtQuick.Controls 2.15
import QtMultimedia 5.15
import QtGraphicalEffects 1.15
import "../controls"
import "../../images/captured"



Item {
    //Custom properties
    property url btnIconSource: "../../images/svg_images/capture_icon.svg"
    property color btnColorDefault: "#1c1d20"
    property color btnColorMouseOver: "#23272E"
    property color btnColorClicked: "#00a1f1"
    property int iconWidth: 18
    property int iconHeight: 18
    property bool isActiveMenu: false
    property int n: 3

    id: item1
    Rectangle {
        id: rectangle
        color: "#2c313c"
        anchors.fill: parent

        Label {
            id: textAddFace
            color: "#ffffff"
            text: qsTr("Add a Face")
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 10
            font.pointSize: 16
        }

        Rectangle {
            id: cameraArea
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: textAddFace.bottom
            anchors.bottom: captureBtnArea.top
            anchors.bottomMargin: 100
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 49

            Rectangle {
                id: rectangle1
                x: 357
                width: cameraArea.height
                color: "#00000000"
                radius: 10
                border.width: 3
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.bottomMargin: 0
                anchors.topMargin: 0


                Rectangle {
                    id: cameraRectangle
                    color: "#00000000"
                    anchors.fill: parent

                    Camera {
                        id: camera

                    }

                    VideoOutput {
                        id: videoOutput
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.top: parent.top
                        source: camera
                        clip: false
                        anchors.horizontalCenter: parent.horizontalCenter
                        focus : visible // to receive focus and capture key events when visible
                    }


                }

            }


        }


        Rectangle {
            id: captureBtnArea
            y: 333
            height: 60
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.bottomMargin: 40

            Button{
                id: captureBtn
                text: qsTr("Capture")
                anchors.horizontalCenter: parent.horizontalCenter
                font.pointSize: 18

                width: 170

                QtObject{
                    id: internal

                    // Mouse Hover and Click Change Color
                    property var dynamicColor: if(captureBtn.down){
                                                   captureBtn.down ? btnColorClicked : btnColorDefault
                                               } else {
                                                   captureBtn.hovered ? btnColorMouseOver : btnColorDefault
                                               }
                }

                implicitWidth: 250
                implicitHeight: 60

                background: Rectangle{
                    id: bgBtn
                    color: internal.dynamicColor
                    radius: 10
                }

                contentItem: Item {
                    anchors.fill: parent
                    id: content
                    Image {
                        id: iconBtn
                        source: btnIconSource
                        anchors.leftMargin: 26
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        sourceSize.width: iconWidth
                        sourceSize.height: iconHeight
                        width: iconWidth
                        height: iconHeight
                        fillMode: Image.PreserveAspectFit
                        visible: false
                        antialiasing: true
                    }

                    ColorOverlay{
                        anchors.fill: iconBtn
                        source: iconBtn
                        color: "#7f5fac"
                        anchors.verticalCenter: parent.verticalCenter
                        antialiasing: true
                        width: iconWidth
                        height: iconHeight
                    }

                    Text{
                        color: "#7f5fac"
                        text: "Capture"
                        font: captureBtn.font
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        minimumPixelSize: 20
                        anchors.leftMargin: 75
                    }
                }

                onClicked: {

                        addFaceBackend.captureClicked()

                }

            }
        }



    }

    Connections {
        target: addFaceBackend;

    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:473;width:908}
}
##^##*/
